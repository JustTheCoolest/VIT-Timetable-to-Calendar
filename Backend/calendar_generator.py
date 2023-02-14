import icalendar
import datetime


def get_courses(text: str) -> dict[str, dict]:
    """
    Converts the text copied from the course list in, VTopCC >> Academics >> Time Table, to a list of courses with the
    relevant data.
    """
    data = text.splitlines()
    start_index = data.index('1')
    courses = {}
    for line_index in range(start_index, len(data), 31):
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


def get_slot_times(start_times: list[str], end_times: list[str]) -> list[tuple[list[int]]]:
    """
    Slots times from first two lines of timetable text becomes,
     list(tuple(start_time, end_time), ...) where,
     time = list(hours, minutes)
    """
    for times in (start_times, end_times):
        for index, time in enumerate(times):
            if time == "Lunch":
                continue
            time = time.split(":")
            time = [int(component) for component in time]
            times[index] = time
    slot_times = list(zip(start_times, end_times))
    return slot_times


def add_events(
        day_rows: list[str],
        slot_timings: list[tuple[list[int]]],
        courses: dict[str, dict],
        semester_dates: list[datetime.datetime]
) -> None:
    """Goes through the list of slots in the days and adds any classes found to the calendar as events"""
    for day_index, day_row in enumerate(day_rows):
        for slot_index, slot_cell in enumerate(day_row):
            if "-" in slot_cell:
                slot_cell = slot_cell.split()
                slot_course = slot_cell[1]
                slot_venue = "-".join(slot_cell[3:5])
                event = icalendar.Event()
                event['summary'] = courses[slot_course]['title']
                event['location'] = slot_venue
                # flag - Unfinished function


def generate_calendar(
        courses: dict[str, dict],
        timetable_text: str,
        semester_dates: list[datetime.datetime]
) -> icalendar.cal.Calendar:
    calendar = icalendar.Calendar()
    calendar['prodid'] = '-// Andhavarapu Balu // github.com/JustTheCoolest/VIT-Chennai-Timetable-to-Calendar //EN'
    calendar['x-wr-timezone'] = 'Asia/Kolkata'
    rows = map(str.split, timetable_text.splitlines())
    theory_slot_timings = get_slot_times(rows[0][2:], rows[1][1:])
    lab_slot_timings = get_slot_times(rows[2][2:], rows[3][1:])
