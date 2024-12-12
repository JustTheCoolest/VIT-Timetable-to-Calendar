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

    start_date = (datetime.datetime.now() - datetime.timedelta(days=1)).date()
    end_date = datetime.date(2025, 5, 31)
    ics_text = calendar_generator.generate_calendar(page_text, [start_date, end_date])
    
    st.download_button(
        label="Download Calendar",
        data=ics_text,
        file_name="calendar.ics",
        mime="text/calendar"
    )
    
    st.image("instructions/images/pg1 image.png")
    st.image("instructions/images/pg2 image.png")
    st.text("select all the text shown in the above images from SI.No to L94")
    

main()
