import datetime

from Backend import calendar_generator
file_path = input("Enter file path for courses text: ")
with open(file_path) as courses_text_source:
    courses_text = courses_text_source.read()
file_path = input("Enter file path for timetable text: ")
with open(file_path) as timetable_text_source:
    timetable_text = timetable_text_source.read()

start_date = datetime.datetime.now().date()
end_date = datetime.date.fromisoformat(input("Enter end date (YYYY-MM-DD): "))

ics_text = calendar_generator.generate_calendar(courses_text, timetable_text, [start_date, end_date])

file_path = input("Enter file path for output: ")
with open(file_path, "wb") as file:
    file.write(ics_text)
