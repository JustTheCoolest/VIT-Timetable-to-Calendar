INPUT_PATH = "input.txt"
OUTPUT_PATH = "output.ics"

import datetime

from Backend import calendar_generator

with open(INPUT_PATH) as text_source:
    page_text = text_source.read()

start_date = datetime.datetime.now().date()
end_date = datetime.date.fromisoformat("2099-12-31")

ics_text = calendar_generator.generate_calendar(page_text, [start_date, end_date])

with open(OUTPUT_PATH, "wb") as file:
    file.write(ics_text)
