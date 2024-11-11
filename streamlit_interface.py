import datetime
import streamlit as st

from Backend import calendar_generator

def main():
    st.title("VIT Time Table to iCal Converter")
    st.text("Made by Andhavarapu Balu")
    st.markdown("[GitHub repository](https://github.com/JustTheCoolest/VIT-Timetable-to-Calendar)")
    
    page_text = st.text_area("Paste the text copied from the page here:")

    if not page_text:
        return

    start_date = datetime.datetime.now().date()
    try:
        end_date = datetime.date.fromisoformat(st.text_area("Enter end date (YYYY-MM-DD): "))
    except ValueError:
        st.error("Invalid date format")
        return

    ics_text = calendar_generator.generate_calendar(page_text, [start_date, end_date])

    st.download_button(
        label="Download Calendar",
        data=ics_text,
        file_name="calendar.ics",
        mime="text/calendar"
    )

main()
