import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account

import datetime
import json
import os
import base64
import traceback

from Backend import calendar_generator
from StreamlitFrontend.utils import *

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
    count = _downloads_doc_ref.get().to_dict().get('download_count')
    count = round_down(count)
    return count

def add_custom_css():
    css_path = "StreamlitFrontend/style.css"

    # Replace placeholder in CSS with base64 image
    with open(css_path, "r") as css_file:
        css = css_file.read()

    # Inject the CSS into the Streamlit app
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def provide_introduction_expander():
    with st.expander("⚡ Introduction"):
        st.text("""Import your semester timetable to any calendar application of your choice, such as Google Calendar, Apple Calendar, Microsoft Calendar, etc.
 
Works on iOS too!
 
Reasons to use a calendar app:
• All your events in a single place
• Colour coding for different categories
• Details custom category wise notification settings
• Sync between all devices (including smart watches!)
• Home screen widgets!
""")

def generate_calender(page_text):
    start_date = (datetime.datetime.now() - datetime.timedelta(days=1)).date()
    end_date = datetime.date(2025, 5, 31)
    ics_text = calendar_generator.generate_calendar(page_text, [start_date, end_date])
    return ics_text

def provide_download(downloads_doc_ref):
    ics_text=None
    timetable_input = st.text_area(
                        "🎯 INPUT YOUR TIMETABLE DATA:",
                        placeholder="Paste your complete VTOP timetable here... System ready for data input.",
                        height=200
                    )

    col1, col2 = st.columns([1, 1])  

    with col1:
        if st.button("⚡ GENERATE CALENDAR"):
            try:
                ics_text=generate_calender(timetable_input)
                st.session_state["ics_text"] = ics_text
            except Exception as e:
                print(traceback.format_exc())
                st.components.v1.html(f"""
                    <script>
                        alert("❌ ERROR: Failed to generate calendar. The format might be incorrect. Please paste your timetable from VTOP. Refer to the video guide in the instructions section for more details. \\n\\n If the issue persists, please report it using the 'Report Issue' section.");
                    </script>
                """, height=0)

    with col2:
        if "ics_text" in st.session_state:
            st.download_button(
                label="📥 Download Calendar",
                data=st.session_state["ics_text"],
                file_name="calendar.ics",
                mime="text/calendar",
                on_click=lambda: downloads_doc_ref.update({
                    "last_downloaded": datetime.datetime.now().isoformat(),
                    "download_count": firestore.Increment(1)
                })
            )

def provide_reporting_expander():
    with st.expander("📝 Report Issue / Give Feedback"):
        st.markdown("""
        For feature requests, please open an issue on the [GitHub repository](https://github.com/JustTheCoolest/VIT-Timetable-to-Calendar). You may also submit feedback in the discussions section.
                    
        If the calendar generation fails, you can submit your data privately using [this form](https://forms.gle/SvEHAEro9isNnorr6) for us to review and get back to you.
        """)

def provide_samples_expander():
    valid_extensions = ('.png', '.jpg', '.jpeg', '.gif')
    folder = "sample_screenshots"
    if not os.path.exists(folder):
        st.warning("Sample screenshots folder not found.")
        return

    screenshots = sorted([
        file for file in os.listdir(folder)
        if file.lower().endswith(valid_extensions)
    ])

    with st.expander("🖼 Use Cases (Screenshots)"):
        st.markdown('<div class="scrollable-images">', unsafe_allow_html=True)

        for i, sample in enumerate(screenshots):
            try:
                caption = sample.replace('_', ' ').replace('-', ' ')
                for ext in valid_extensions:
                    caption = caption.replace(ext, '')
                caption = caption.strip().title()
                st.markdown(f"**{caption}**")
                st.image(f"{folder}/{sample}")
            except Exception as e:
                st.error(f"Error loading image {sample}: {str(e)}")

        st.markdown("</div>", unsafe_allow_html=True)

def provide_instructions_expander():
    with st.expander("⚡ Quick Start Guide (Instructions)"):
        st.markdown("""
        ### 📡 *Video Guides*
                    
        *📱 [iPadOS tutorial with Apple Calendar](https://youtu.be/dafPgd-1Z98)*
        
        *🖥 [Google Calendar import tutorial on desktop](https://youtu.be/gzahLrDPKv4?si=gQwRu8u0e5qLGJE9)*

        ### 🚀 *Text Guide*
        
        *◆ Step 1:* Navigate to your VTOP timetable and copy ALL text from "SI.No" to "L94"
        
        *◆ Step 2:* Paste the complete text in the input field below and press Ctrl+Enter
        
        *◆ Step 3:* Hit the GENERATE button to create your calendar file
        
        *◆ Step 4:* Download the .ics file and import into your calendar app
        
        """)

def provide_privacy_policy_expander():
    with st.expander("🔒 Privacy Policy"):
        st.markdown("""
1. **Data Collection**: This application does not store the timetables or any personal data entered by users. 
2. **Data Processing**: The website is hosted on Streamlit Cloud, which does all the processing of data. 
3. **Analytics**: Analytical data such as download counts are collected to monitor usage. Streamlit and Google Firebase are used for this purpose.
4. **Submitted Data**: If users choose to submit their timetable data for issue reporting, it is collected via Google Forms and is only accessible to a few members of the development team for troubleshooting purposes. It may be stored privately and used for future testing too.
        """) 

def streamlit_stuff(downloads_doc_ref):
    add_custom_css()

    # Cyber Header
    st.markdown("""
    <div class="cyber-header">
        <div class="cyber-nav">
            <div class="nav-brand">
                <i class="fas fa-satellite-dish"></i> VTop to Calendar
            </div>
            <div class="nav-links">
                <a href="https://github.com/JustTheCoolest/VIT-Timetable-to-Calendar" target="_blank">
                    <i class="fab fa-github"></i> SOURCE CODE
                </a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h1><i class='fas fa-rocket'></i> TIMETABLE EXPORTER</h1>", unsafe_allow_html=True)
    st.markdown("<div class='author-credit'>⚡ Engineered by ANDHAVARAPU BALU and HARSHA DATTA⚡</div>", unsafe_allow_html=True)

    provide_introduction_expander()
    provide_instructions_expander()
    provide_download(downloads_doc_ref)

    count_to_display = get_downloads_count(downloads_doc_ref)
    st.subheader(f"{count_to_display}+ downloads so far!")

    provide_samples_expander()

    provide_privacy_policy_expander()

    provide_reporting_expander()

def main():
    doc_ref = get_firestore_downloads_doc_ref()
    streamlit_stuff(doc_ref)

if __name__ == "__main__":
    main()
