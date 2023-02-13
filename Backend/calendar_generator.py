import icalendar


def get_courses(text: str) -> list[dict]:
    """
    Converts the text copied from the course list in, VTopCC >> Academics >> Time Table, to a list of courses with the
    relevant data alone.
    Omits courses that do not have a slot assigned to them (like non-graded courses)
    """
    data = text.splitlines()
    start_index = data.index('1')
    courses = []
    for line_index in range(start_index, len(data), 31):
        slot = data[line_index + 15][:-2]
        if slot == 'NIL':
            continue
        header = (data[line_index + 4].split(' - '))
        course = {
            'code': header[0],
            'title': header[1],
            'slot': slot,
            'venue': data[line_index + 18],
            'professor': data[line_index + 20][:-2]
        }
        courses.append(course)
    return courses


def generate_ical(courses: list[dict]) -> icalendar.cal.Calendar:
    return


def generate_ics(ical: icalendar.cal.Calendar) -> str:
    return
