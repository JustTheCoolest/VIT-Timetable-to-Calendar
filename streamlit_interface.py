import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account

import sigfig

import datetime
import json
import os

from Backend import calendar_generator

@st.cache_resource
def get_firestore_downloads_doc_ref():
    key_dict = json.loads(st.secrets["textkey"])
    creds = service_account.Credentials.from_service_account_info(key_dict)
    db = firestore.Client(credentials=creds)

    # Create a reference to the Google post.
    doc_ref = db.collection("siteStats").document("downloads")

    return doc_ref

@st.cache_data(ttl = 600) # Cache for 10 minutes
def get_downloads_count(_downloads_doc_ref):
    return sigfig.round(_downloads_doc_ref.get().to_dict().get('download_count'), sigfigs=1)

def provide_introduction_expander():
    with st.expander("Introduction"):
        st.text("""Import your semester timetable to any calendar application of your choice, such as Google Calendar, Apple Calendar, Microsoft Calendar, etc.
 
Works on iOS!
 
Reasons to use a calendar app:
• All your events in a single place
• Colour coding for different categories
• Details custom category wise notification settings
• Sync between all devices (including smart watches!)
• Home screen widgets!
""")

def provide_download(page_text, downloads_doc_ref):
    start_date = (datetime.datetime.now() - datetime.timedelta(days=1)).date()
    end_date = datetime.date(2025, 5, 31)
    ics_text = calendar_generator.generate_calendar(page_text, [start_date, end_date])

    st.download_button(
        label="Download Calendar",
        data=ics_text,
        file_name="calendar.ics",
        mime="text/calendar",
        on_click=lambda: downloads_doc_ref.update({
            "last_downloaded": datetime.datetime.now().isoformat(),
            "download_count": firestore.Increment(1)
        })
    )

def provide_samples_expander():
    valid_extensions = ('.png', '.jpg', '.jpeg', '.gif')
    with st.expander("Use Cases (Screenshots)"):
        for sample in sorted(os.listdir("sample_screenshots")):
            if not sample.endswith(valid_extensions):
                continue
            st.image(f"sample_screenshots/{sample}")

def provide_instructions_expander():
    with st.expander("Instructions"):
        st.markdown("""
[Google Calendar desktop tutorial](https://youtu.be/A3Rubu_3Le0?si=FA482m6ABF9n7szG)\n
[iPadOS with Apple Calendar tutorial](https://youtu.be/dafPgd-1Z98)\n
""")
        st.text("1. Copy all the text from your VTOP timetable page from top to bottom (\"SI.No\" to \"L94\")")
        st.text("2. Paste the copied text in the section below and click outside the box (or click Ctrl+Enter)")
        st.text("3. Download the file (.ics) and import it into your preferred calendar service")

def streamlit_stuff(downloads_doc_ref):
    st.title("VIT Time Table to iCal Converter")
    st.text("Made by Andhavarapu Balu")
    st.markdown("[GitHub repository](https://github.com/JustTheCoolest/VIT-Timetable-to-Calendar)")

    provide_introduction_expander()

    provide_instructions_expander()

    page_text = st.text_area("Paste the text copied from the timetable page here:")

    if page_text:
        provide_download(page_text, downloads_doc_ref)

    count_to_display = get_downloads_count(downloads_doc_ref)
    st.subheader(f"{count_to_display}+ downloads so far!")
    
    provide_samples_expander()

def main():
    doc_ref = get_firestore_downloads_doc_ref()
    streamlit_stuff(doc_ref)

main()
