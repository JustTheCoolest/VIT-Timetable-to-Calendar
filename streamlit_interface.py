import datetime
import streamlit as st
from Backend import calendar_generator

def main():
    st.title("VIT Time Table to iCal Converter")
    st.text("Made by Andhavarapu Balu")
    st.markdown("[GitHub repository](https://github.com/JustTheCoolest/VIT-Timetable-to-Calendar)")

    st.subheader("Instructions")
    st.text("1. Copy all the text from your VTOP timetable page from top to bottom (SI.No to L94)")
    st.text("2. Paste the copied text in the section below and click outside the box (or click Ctrl+Enter)")
    st.text("3. Download the file (.ics) and import it into your preferred calendar service")

    st.markdown("""
    **Refer the video tutorials below for detailed instructions**\n
    [Google Calendar desktop tutorial](https://youtu.be/A3Rubu_3Le0?si=FA482m6ABF9n7szG)
    [iPads with Apple Calendar tutorial](https://youtu.be/dafPgd-IZ98)
    """)

    page_text = st.text_area("Paste the text copied from the page here:")

    if page_text:
        try:
            start_date = (datetime.datetime.now() - datetime.timedelta(days=1)).date()
            end_date = datetime.date(2025, 5, 31)
            ics_text = calendar_generator.generate_calendar(page_text, [start_date, end_date])

            st.download_button(label="Download Calendar", data=ics_text, file_name="calendar.ics", mime="text/calendar")

        except Exception as e:
            st.text(f"An error occurred: {e}")
            st.text("Please report this issue on GitHub")
            st.markdown("[GitHub Error Page](https://github.com/JustTheCoolest/VIT-Timetable-to-Calendar/issues)")

    c1, c2 = st.columns(2)
    with c1:
        st.image("images/pg1_stream.png", use_container_width=True)
    with c2:
        st.image("images/pg2_stream.png", use_container_width=True)


main()

