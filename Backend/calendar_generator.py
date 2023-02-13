import icalendar


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
        slot = header[0]
        courses[slot] = {
            'title': header[1],
            'LTPJC': tuple(map(float, data[line_index + 8].split())),
            'class_code': data[line_index + 13],
            'slot': slot,
            'venue': data[line_index + 18],
            'professor': data[line_index + 20][:-2]
        }
    return courses


def generate_calendar(courses: list[dict]) -> icalendar.cal.Calendar:
    calendar = icalendar.Calendar()
    calendar['prodid'] = '-// Andhavarapu Balu // github.com/JustTheCoolest/VIT-Chennai-Timetable-to-Calendar //EN'
    calendar['x-wr-timezone'] = 'Asia/Kolkata'
