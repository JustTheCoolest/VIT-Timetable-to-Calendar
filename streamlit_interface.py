import datetime
import streamlit as st

from Backend import calendar_generator

def main():
    st.title("VIT Time Table to iCal Converter")
    st.text("Made by Andhavarapu Balu")
    st.markdown("[GitHub repository](https://github.com/JustTheCoolest/VIT-Timetable-to-Calendar)")

    st.subheader("Instructions")
    st.text("1. Copy all the text from your VTOP timetable page from SI.No to L94")
    st.text("2. Paste the copied text in the section below and click Ctrl+Enter")
    st.text("3. Download the .ics file and import it into your preferred calendar service")

    st.markdown("""
**Refer the video tutorials below for detailed instructions**\n
[Google Calendar desktop tutorial](https://youtu.be/A3Rubu_3Le0?si=FA482m6ABF9n7szG)\n
[iPadOS with Apple Calendar tutorial](https://youtu.be/dafPgd-1Z98)\n
""")

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


    

    

main()
