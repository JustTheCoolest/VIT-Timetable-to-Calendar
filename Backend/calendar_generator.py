import icalendar
import datetime
from dateutil import rrule as dateutil_rrule
import re


days = ("MO", "TU", "WE", "TH", "FR", "SA", "SU")
RECORD_SIZE = 32


def get_courses(text: str) -> dict[str, dict]:
    """
    Converts the text copied from the course list in, VTopCC >> Academics >> Time Table, to a list of courses with the
    relevant data.
    """
    data = text.splitlines()
    start_index = data.index('1')
    courses = {}
    for line_index in range(start_index, len(data), RECORD_SIZE):
        slot = data[line_index + 15][:-2]
        header = (data[line_index + 4].split(' - '))
        course_code = header[0]
        courses[course_code] = {
            'title': header[1],
            'LTPJC': tuple(map(float, data[line_index + 8].split())),
            'class_code': data[line_index + 13],
            'slot': slot,
            'venue': data[line_index + 18],
            'professor': data[line_index + 20][:-2]
        }
    return courses


def get_slot_times(start_times: list[str], end_times: list[str]) -> list[(datetime.time, datetime.time)]:
    """
    Slots times from first two lines of timetable text becomes,
     list(tuple(start_time, end_time), ...) where,
     time = list(hours, minutes)
    """
    for times in (start_times, end_times):
        noon_flag = False
        # Bug - [12am, 1am) would be evaluated as pm
        previous_time = datetime.time(0)
        for index, time in enumerate(times):
            if time == "Lunch":
                continue
            time_list = list(int(component) for component in time.split(":"))
            time = datetime.time(*time_list)
            if time < previous_time:
                noon_flag = True
            if noon_flag:
                time_list[0] += 12
                time = datetime.time(*time_list)
            if not noon_flag:
                previous_time = time
            times[index] = time
    slot_times = list(zip(start_times, end_times))
    return slot_times


def add_events(
        day_rows: list[str],
        slot_timings: list[tuple[datetime.time]],
        courses: dict[str, dict],
        semester_dates: list[datetime.date],
        calendar: icalendar.cal.Calendar
) -> None:
    """Goes through the list of slots in the days and adds any classes found to the calendar as events"""
    for day_index, day_row in enumerate(day_rows):
        for slot_index, slot_cell in enumerate(day_row):
            if "-" not in slot_cell or slot_cell == "-":
                continue
            slot_cell = slot_cell.split("-")
            slot_course = slot_cell[1]
            slot_venue = "-".join(slot_cell[3:5])
            course = courses[slot_course]
            event = icalendar.Event()
            event['summary'] = course['title']
            event['location'] = slot_venue
            newline_character = "\n"
            event['description'] = f"""course_code = {slot_course}
{newline_character.join((" = ".join(map(str, item)) for item in course.items()))}"""
            semester_start = semester_dates[0]
            start_time, end_time = slot_timings[slot_index]
            ical_time_format = '%Y%m%dT%H%M%S'
            dtstart = datetime.datetime.combine(semester_start, start_time)
            event['dtstart'] = dtstart.strftime(ical_time_format)
            event['dtend'] = datetime.datetime.combine(
                semester_start,
                end_time
            ).strftime(ical_time_format)
            event['dtstamp'] = datetime.datetime.now().strftime(ical_time_format)
            event['tzinfo'] = "Asia/Kolkata"
            event['uid'] = str(day_index)+"-"+str(slot_index)
            event['rrule'] = icalendar.vRecur(freq='WEEKLY', byday=days[day_index])
            exdates = []
            for start_date, end_date in zip(semester_dates[1::2], semester_dates[2::2]):
                exdates.extend(dateutil_rrule.rrule(
                    dateutil_rrule.WEEKLY,
                    dtstart=start_date,
                    until=end_date,
                    byweekday=day_index
                ))
            event['exdate'] = [date.strftime("%Y%m%d") for date in exdates]
            calendar.add_component(event)


def split_timetable_line(line):
    return line.split('\t')


def split_text(page_text: str) -> tuple[str, str]:
    """
    Splits the text copied from VTopCC >> Academics >> Time Table to,
    courses_text, timetable_text
    """
    split_text = page_text.split("Total Number Of Credits:")
    courses_text = split_text[0]
    timetable_text = split_text[1][split_text[1].index("THEORY"):]
    return courses_text, timetable_text


def generate_calendar(
        page_text : str,
        semester_dates: list[datetime.date]
) -> bytes:
    """
    semester_dates: End date is exclusive
    """
    courses_text, timetable_text = split_text(page_text)
    courses = get_courses(courses_text)
    calendar = icalendar.Calendar()
    calendar['prodid'] = '-// Andhavarapu Balu // github.com/JustTheCoolest/VIT-Chennai-Timetable-to-Calendar //EN'
    calendar['version'] = "2.0"
    calendar['x-wr-timezone'] = 'Asia/Kolkata'
    rows = tuple(map(split_timetable_line, timetable_text.splitlines()))
    theory_slot_timings = get_slot_times(rows[0][2:], rows[1][1:])
    add_events((row[2:] for row in rows[4::2]), theory_slot_timings, courses, semester_dates, calendar)
    lab_slot_timings = get_slot_times(rows[2][2:], rows[3][1:])
    add_events((row[1:] for row in rows[5::2]), lab_slot_timings, courses, semester_dates, calendar)
    return calendar.to_ical()
