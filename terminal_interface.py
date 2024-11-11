import datetime

from Backend import calendar_generator
file_path = input("Enter file path for the text copied fron the page: ")
with open(file_path) as text_source:
    page_text = text_source.read()

start_date = datetime.datetime.now().date()
end_date = datetime.date.fromisoformat(input("Enter end date (YYYY-MM-DD): "))

ics_text = calendar_generator.generate_calendar(page_text, [start_date, end_date])

file_path = input("Enter file path for output: ")
with open(file_path, "wb") as file:
    file.write(ics_text)
