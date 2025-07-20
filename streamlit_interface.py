import streamlit as st

from google.cloud import firestore
from google.oauth2 import service_account

import sigfig

import base64
import datetime
import json
import os

from Backend import calendar_generator

def add_custom_css():
    background_image_path = "background.jpg"
    background_image_url = f"data:image/jpg;base64,{base64.b64encode(open(background_image_path, 'rb').read()).decode()}"

    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');

    html, body, .stApp {{
        height: 100%;
        margin: 0;
        padding: 0;
        font-family: 'Inter', sans-serif;
        color: #ffffff;
    }}

    .stApp {{
        background: url('{background_image_url}') no-repeat center center fixed;
        background-size: cover;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
        overflow-x: hidden;
        padding: 1rem;
    }}

    .glass-navbar {{
        width: 100%;
        max-width: 900px;
        background: rgba(255, 255, 255, 0.07);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 16px;
        padding: 10px 30px;
        margin: 1rem 0;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}

    .main .block-container {{
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 24px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.37),
                     inset 0 0 0 0.5px rgba(255, 255, 255, 0.4);
        backdrop-filter: blur(30px) saturate(180%);
        -webkit-backdrop-filter: blur(30px) saturate(180%);
        padding: 40px 30px;
        max-width: 700px;
        margin: auto;
        width: 100%;
        animation: fadeInUp 1s ease;
    }}

    .stTextArea textarea {{
        background-color: rgba(255, 255, 255, 0.85);
        color: black;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }}

    .stButton button {{
        background-color: #007bff;
        color: white;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        border: none;
    }}

    .stButton button:hover {{
        background-color: #0056b3;
    }}

    .stDownloadButton button {{
        background-color: #28a745;
        color: white;
        font-weight: 600;
        padding: 0.6rem 1.2rem;
        font-size: 1rem;
        border-radius: 8px;
        border: none;
    }}

    .stDownloadButton button:hover {{
        background-color: #218838;
    }}

    h1 {{
        text-align: center;
        font-size: 2rem;
        font-weight: bold;
    }}

    @keyframes fadeInUp {{
        from {{
            opacity: 0;
            transform: translateY(20px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}

    .scrollable-images {{
        max-height: 400px;
        overflow-y: auto;
        padding-right: 10px;
    }}

    .scrollable-images img {{
        max-height: 280px;
        width: auto;
        object-fit: contain;
        display: block;
        margin-bottom: 16px;
    }}

    @media (max-width: 768px) {{
        .glass-navbar {{
            flex-direction: column;
            gap: 10px;
        }}
    }}
    </style>
    """, unsafe_allow_html=True)



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
    folder = "sample_screenshots"
    if not os.path.exists(folder):
        st.warning("Sample screenshots folder not found.")
        return

    screenshots = sorted([
        file for file in os.listdir(folder)
        if file.lower().endswith(valid_extensions)
    ])

    with st.expander("📸 Use Cases (Screenshots)"):
        st.markdown('<div class="scrollable-images">', unsafe_allow_html=True)

        for i, sample in enumerate(screenshots):
            try:
                caption = sample.replace('_', ' ').replace('-', ' ')
                for ext in valid_extensions:
                    caption = caption.replace(ext, '')
                caption = caption.strip().title()
                st.image(f"{folder}/{sample}", caption=f"{i+1}. {caption}")
            except Exception as e:
                st.error(f"Error loading image {sample}: {str(e)}")

        st.markdown("</div>", unsafe_allow_html=True)

def provide_instructions_expander():
    with st.expander("📋 Instructions"):
        st.markdown("""
[🎥 Google Calendar desktop tutorial](https://youtu.be/A3Rubu_3Le0?si=FA482m6ABF9n7szG)\n
[🎥 iPadOS with Apple Calendar tutorial](https://youtu.be/dafPgd-1Z98)\n
""")
        st.text("1. Copy all the text from your VTOP timetable page from top to bottom (\"SI.No\" to \"L94\")")
        st.text("2. Paste the copied text in the section below and click outside the box (or click Ctrl+Enter)")
        st.text("3. Download the file (.ics) and import it into your preferred calendar service")

def streamlit_stuff(downloads_doc_ref):
    add_custom_css()

    # Navbar Title Only (No GitHub link here)
    st.markdown("""
    <div class="glass-navbar">
        <div><strong>📅 VIT Timetable Converter</strong></div>
    </div>
    """, unsafe_allow_html=True)

    # GitHub Link Outside the Block, styled and right-aligned
    st.markdown(
        """
        <div style='width:100%; max-width:900px; display:flex; justify-content: flex-end; margin-top:-1rem; margin-bottom:1rem;'>
            <a href="https://github.com/andhanarapu-balu" target="_blank"
               style="color:#00acee; font-weight:600; text-decoration:underline; font-family: 'Inter', sans-serif;">
                GitHub
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1>🎓 VIT Time Table to iCal Converter</h1>", unsafe_allow_html=True)
    st.markdown("Made by Andhanarapu Balu")

    provide_introduction_expander()
    provide_instructions_expander()

    timetable_input = st.text_area("Paste your VIT timetable here:")

    if st.button("Generate Calendar"):
        if timetable_input.strip() == "":
            st.error("❗ Please paste your timetable text.")
        else:
            provide_download(timetable_input, downloads_doc_ref)

    provide_samples_expander()

def main():
    doc_ref = get_firestore_downloads_doc_ref()
    streamlit_stuff(doc_ref)

if __name__ == "__main__":
    main()
