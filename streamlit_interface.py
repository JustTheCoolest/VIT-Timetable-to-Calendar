import streamlit as st
import base64
import os
from datetime import datetime

# --------------------------- Futuristic UI CSS ---------------------------
def add_custom_css():
    background_image_path = "background.jpg"
    background_image_url = f"data:image/jpg;base64,{base64.b64encode(open(background_image_path, 'rb').read()).decode()}"

    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;500;600;700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }}

    :root {{
        --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        --accent-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        --success-gradient: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        --danger-gradient: linear-gradient(135deg, #fc466b 0%, #3f5efb 100%);
        --dark-gradient: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 100%);
        --glow-primary: 0 0 20px rgba(102, 126, 234, 0.5);
        --glow-secondary: 0 0 20px rgba(240, 147, 251, 0.5);
        --glow-accent: 0 0 20px rgba(79, 172, 254, 0.5);
    }}

    html, body, .stApp {{
        height: 100vh;
        font-family: 'Rajdhani', sans-serif;
        color: #ffffff;
        overflow-x: hidden;
    }}

    .stApp {{
        background: 
            radial-gradient(circle at 20% 80%, rgba(120, 119, 198, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(255, 119, 198, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 40% 40%, rgba(79, 172, 254, 0.1) 0%, transparent 50%),
            var(--dark-gradient),
            url('{background_image_url}') no-repeat center center fixed;
        background-size: cover;
        position: relative;
    }}

    /* Animated geometric shapes */
    .stApp::before {{
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            polygon(50% 0%, 0% 100%, 100% 100%),
            polygon(0% 20%, 60% 20%, 60% 0%, 100% 50%, 60% 100%, 60% 80%, 0% 80%);
        background-size: 150px 150px, 200px 200px;
        background-position: 0 0, 100px 100px;
        background-repeat: repeat;
        opacity: 0.03;
        animation: geometricFloat 25s linear infinite;
        pointer-events: none;
        z-index: -1;
    }}

    @keyframes geometricFloat {{
        0% {{ transform: translate(0, 0) rotate(0deg); }}
        100% {{ transform: translate(-200px, -200px) rotate(360deg); }}
    }}

    /* Floating orbs */
    .stApp::after {{
        content: '';
        position: fixed;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(4px 4px at 100px 50px, rgba(255, 255, 255, 0.3), transparent),
            radial-gradient(3px 3px at 200px 150px, rgba(79, 172, 254, 0.4), transparent),
            radial-gradient(2px 2px at 300px 100px, rgba(240, 147, 251, 0.5), transparent),
            radial-gradient(4px 4px at 400px 200px, rgba(102, 126, 234, 0.3), transparent);
        background-repeat: repeat;
        background-size: 500px 300px;
        animation: orbFloat 15s ease-in-out infinite;
        pointer-events: none;
        z-index: -1;
    }}

    @keyframes orbFloat {{
        0%, 100% {{ transform: translate(0, 0); }}
        50% {{ transform: translate(50px, -30px); }}
    }}

    .cyber-container {{
        width: calc(100% - 4rem);
        max-width: 1200px;
        min-height: calc(100vh - 8rem);
        background: linear-gradient(145deg, rgba(15, 15, 35, 0.95), rgba(25, 25, 45, 0.9));
        border: 2px solid;
        border-image: var(--primary-gradient) 1;
        border-radius: 20px;
        padding: 0;
        margin: 2rem auto;
        box-shadow: 
            0 25px 80px rgba(0, 0, 0, 0.4),
            0 0 0 1px rgba(102, 126, 234, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
        position: relative;
        overflow: hidden;
        animation: containerPulse 3s ease-in-out infinite alternate;
    }}

    @keyframes containerPulse {{
        0% {{ box-shadow: 0 25px 80px rgba(0, 0, 0, 0.4), 0 0 0 1px rgba(102, 126, 234, 0.2); }}
        100% {{ box-shadow: 0 30px 100px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(102, 126, 234, 0.4); }}
    }}

    .cyber-container::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: var(--accent-gradient);
        z-index: 1;
        animation: scanLine 2s linear infinite;
    }}

    @keyframes scanLine {{
        0% {{ transform: translateX(-100%); opacity: 0; }}
        50% {{ opacity: 1; }}
        100% {{ transform: translateX(100%); opacity: 0; }}
    }}

    .cyber-container::after {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            repeating-linear-gradient(
                90deg,
                transparent,
                transparent 98px,
                rgba(79, 172, 254, 0.03) 100px
            );
        pointer-events: none;
        z-index: 1;
    }}

    .cyber-header {{
        background: linear-gradient(135deg, rgba(15, 15, 35, 0.98), rgba(25, 25, 50, 0.95));
        border-bottom: 2px solid rgba(102, 126, 234, 0.3);
        border-radius: 20px 20px 0 0;
        padding: 25px 40px;
        position: relative;
        z-index: 10;
    }}

    .cyber-nav {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }}

    .nav-brand {{
        font-family: 'Orbitron', monospace;
        font-size: 1.5rem;
        font-weight: 900;
        background: var(--primary-gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: var(--glow-primary);
        position: relative;
    }}

    .nav-brand::before {{
        content: '◆';
        position: absolute;
        left: -30px;
        color: #4facfe;
        animation: rotate 2s linear infinite;
    }}

    @keyframes rotate {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
    }}

    .nav-links a {{
        color: rgba(255, 255, 255, 0.9);
        font-weight: 600;
        text-decoration: none;
        margin: 0 15px;
        padding: 10px 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 25px;
        background: transparent;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }}

    .nav-links a:hover::before {{
        left: 0;
    }}

    .nav-links a:hover {{
        color: #ffffff;
        border-color: rgba(79, 172, 254, 0.5);
        box-shadow: var(--glow-accent);
        transform: translateY(-3px);
    }}

    .main .block-container {{
        background: transparent;
        border: none;
        padding: 3rem 3rem 2rem 3rem;
        max-width: none;
        margin: 0;
        width: 100%;
        position: relative;
        z-index: 5;
    }}

    h1 {{
        font-family: 'Orbitron', monospace;
        text-align: center;
        font-size: 3.2rem;
        font-weight: 900;
        margin: 2rem 0 1rem;
        background: var(--secondary-gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: var(--glow-secondary);
        animation: titleGlow 2s ease-in-out infinite alternate;
        position: relative;
    }}

    h1::before, h1::after {{
        content: '▸';
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        color: #f5576c;
        font-size: 2rem;
        animation: arrowPulse 1.5s ease-in-out infinite alternate;
    }}

    h1::before {{
        left: -60px;
    }}

    h1::after {{
        right: -60px;
        transform: translateY(-50%) scaleX(-1);
    }}

    @keyframes titleGlow {{
        0% {{ text-shadow: 0 0 20px rgba(240, 147, 251, 0.5); }}
        100% {{ text-shadow: 0 0 40px rgba(240, 147, 251, 0.8), 0 0 60px rgba(245, 87, 108, 0.4); }}
    }}

    @keyframes arrowPulse {{
        0% {{ opacity: 0.5; transform: translateY(-50%) scale(1); }}
        100% {{ opacity: 1; transform: translateY(-50%) scale(1.1); }}
    }}

    .author-credit {{
        text-align: center;
        font-size: 1.2rem;
        font-weight: 500;
        margin-bottom: 2.5rem;
        color: rgba(255, 255, 255, 0.7);
        font-family: 'Rajdhani', sans-serif;
    }}

    .stTextArea label {{
        color: #ffffff !important;
        font-family: 'Rajdhani', sans-serif;
        font-weight: 600;
        font-size: 1.1rem;
    }}

    .stTextArea textarea {{
        background: linear-gradient(145deg, rgba(25, 25, 45, 0.9), rgba(35, 35, 55, 0.8));
        color: #ffffff;
        border: 2px solid rgba(79, 172, 254, 0.3);
        border-radius: 15px;
        font-size: 1rem;
        font-weight: 400;
        padding: 1.2rem;
        font-family: 'Rajdhani', sans-serif;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 
            0 8px 25px rgba(0, 0, 0, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
    }}

    .stTextArea textarea:focus {{
        border-color: rgba(79, 172, 254, 0.8);
        box-shadow: 
            0 12px 35px rgba(0, 0, 0, 0.4),
            0 0 0 3px rgba(79, 172, 254, 0.2),
            var(--glow-accent);
        transform: translateY(-2px);
    }}

    .stButton button {{
        background: var(--primary-gradient);
        color: white;
        border-radius: 25px;
        padding: 1rem 2.5rem;
        font-weight: 700;
        font-size: 1.1rem;
        font-family: 'Rajdhani', sans-serif;
        border: none;
        box-shadow: 
            0 10px 30px rgba(102, 126, 234, 0.4),
            0 5px 15px rgba(0, 0, 0, 0.3);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}

    .stButton button::before {{
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
        transition: left 0.6s;
    }}

    .stButton button:hover::before {{
        left: 100%;
    }}

    .stButton button:hover {{
        background: linear-gradient(135deg, #5a67d8 0%, #6b5b95 100%);
        box-shadow: 
            0 15px 40px rgba(102, 126, 234, 0.6),
            var(--glow-primary);
        transform: translateY(-5px);
    }}

    .stDownloadButton button {{
        background: var(--success-gradient);
        color: white;
        font-weight: 700;
        padding: 1rem 2.5rem;
        font-size: 1.1rem;
        font-family: 'Rajdhani', sans-serif;
        border-radius: 25px;
        border: none;
        box-shadow: 
            0 10px 30px rgba(17, 153, 142, 0.4),
            0 5px 15px rgba(0, 0, 0, 0.3);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}

    .stDownloadButton button::before {{
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
        transition: left 0.6s;
    }}

    .stDownloadButton button:hover::before {{
        left: 100%;
    }}

    .stDownloadButton button:hover {{
        background: linear-gradient(135deg, #0d7a6f 0%, #2dd4bf 100%);
        box-shadow: 
            0 15px 40px rgba(17, 153, 142, 0.6),
            0 0 20px rgba(56, 239, 125, 0.5);
        transform: translateY(-5px);
    }}

    .stExpander {{
        background: linear-gradient(145deg, rgba(25, 25, 45, 0.8), rgba(35, 35, 55, 0.7));
        border: 1px solid rgba(79, 172, 254, 0.2);
        border-radius: 15px;
        margin: 1.5rem 0;
        overflow: hidden;
        position: relative;
    }}

    .stExpander::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: var(--accent-gradient);
    }}

    .stExpander details summary {{
        background: linear-gradient(135deg, rgba(79, 172, 254, 0.1), rgba(102, 126, 234, 0.1));
        color: white;
        font-weight: 700;
        font-size: 1.2rem;
        font-family: 'Rajdhani', sans-serif;
        padding: 1.2rem 1.8rem;
        transition: all 0.3s ease;
        border-left: 4px solid transparent;
    }}

    .stExpander details summary:hover {{
        background: linear-gradient(135deg, rgba(79, 172, 254, 0.2), rgba(102, 126, 234, 0.2));
        border-left: 4px solid #4facfe;
        transform: translateX(10px);
    }}

    .cyber-divider {{
        height: 2px;
        background: var(--accent-gradient);
        margin: 3rem 0;
        border-radius: 1px;
        position: relative;
        overflow: hidden;
    }}

    .cyber-divider::before {{
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.5), transparent);
        animation: dividerScan 2s linear infinite;
    }}

    @keyframes dividerScan {{
        0% {{ left: -100%; }}
        100% {{ left: 100%; }}
    }}

    .scrollable-images {{
        max-height: 450px;
        overflow-y: auto;
        padding-right: 15px;
        border-radius: 15px;
    }}

    .scrollable-images::-webkit-scrollbar {{
        width: 10px;
    }}

    .scrollable-images::-webkit-scrollbar-track {{
        background: rgba(25, 25, 45, 0.5);
        border-radius: 5px;
    }}

    .scrollable-images::-webkit-scrollbar-thumb {{
        background: var(--accent-gradient);
        border-radius: 5px;
        box-shadow: var(--glow-accent);
    }}

    .scrollable-images img {{
        max-height: 300px;
        width: 100%;
        object-fit: contain;
        border-radius: 12px;
        margin-bottom: 1rem;
        border: 1px solid rgba(79, 172, 254, 0.2);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
    }}

    .scrollable-images img:hover {{
        transform: scale(1.02);
        border-color: rgba(79, 172, 254, 0.5);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.4), var(--glow-accent);
    }}

    .success-alert {{
        background: linear-gradient(135deg, rgba(17, 153, 142, 0.2), rgba(56, 239, 125, 0.15));
        border: 2px solid rgba(56, 239, 125, 0.3);
        border-radius: 15px;
        padding: 1.2rem;
        margin: 1.5rem 0;
        font-family: 'Rajdhani', sans-serif;
        font-weight: 600;
        animation: alertSlide 0.5s ease;
        position: relative;
        overflow: hidden;
    }}

    .success-alert::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        background: var(--success-gradient);
        animation: alertPulse 2s ease-in-out infinite;
    }}

    @keyframes alertSlide {{
        from {{ transform: translateX(-20px); opacity: 0; }}
        to {{ transform: translateX(0); opacity: 1; }}
    }}

    @keyframes alertPulse {{
        0%, 100% {{ opacity: 0.5; }}
        50% {{ opacity: 1; }}
    }}

    .error-alert {{
        background: linear-gradient(135deg, rgba(252, 70, 107, 0.2), rgba(63, 94, 251, 0.15));
        border: 2px solid rgba(252, 70, 107, 0.3);
        border-radius: 15px;
        padding: 1.2rem;
        margin: 1.5rem 0;
        font-family: 'Rajdhani', sans-serif;
        font-weight: 600;
        position: relative;
        overflow: hidden;
    }}

    .error-alert::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        background: var(--danger-gradient);
        animation: alertPulse 2s ease-in-out infinite;
    }}

    /* Responsive Design */
    @media (max-width: 768px) {{
        .cyber-container {{
            width: calc(100% - 2rem);
            margin: 1rem auto;
            border-radius: 15px;
        }}

        .cyber-nav {{
            flex-direction: column;
            gap: 15px;
        }}

        h1 {{
            font-size: 2.5rem;
        }}

        h1::before, h1::after {{
            display: none;
        }}

        .main .block-container {{
            padding: 2rem 1.5rem;
        }}

        .nav-brand {{
            font-size: 1.3rem;
        }}
    }}

    @media (max-width: 480px) {{
        .cyber-container {{
            width: calc(100% - 1rem);
            margin: 0.5rem auto;
            border-radius: 12px;
        }}

        h1 {{
            font-size: 2rem;
        }}

        .main .block-container {{
            padding: 1.5rem 1rem;
        }}

        .cyber-header {{
            border-radius: 12px 12px 0 0;
        }}
    }}
    </style>
    """, unsafe_allow_html=True)

# ---------------------- ICS Generator ----------------------
def generate_ics_from_timetable(timetable_text):
    lines = timetable_text.splitlines()
    ics_content = "BEGIN:VCALENDAR\nVERSION:2.0\nCALSCAL:GREGORIAN\n"
    for line in lines:
        if line.strip() == "":
            continue
        dtstart = datetime.now().strftime('%Y%m%dT080000')
        dtend = datetime.now().strftime('%Y%m%dT090000')
        ics_content += (
            "BEGIN:VEVENT\n"
            f"SUMMARY:{line.strip()}\n"
            f"DTSTART:{dtstart}\n"
            f"DTEND:{dtend}\n"
            "END:VEVENT\n"
        )
    ics_content += "END:VCALENDAR"
    return ics_content

# ---------------------- Use Case Screenshots ----------------------
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
                st.image(f"{folder}/{sample}", caption=f"{i+1}. {caption}")
            except Exception as e:
                st.error(f"Error loading image {sample}: {str(e)}")

        st.markdown("</div>", unsafe_allow_html=True)

# ---------------------- Instructions Expander ----------------------
def provide_instructions_expander():
    with st.expander("⚡ Quick Start Guide"):
        st.markdown("""
        ### 🚀 *Launch Sequence*
        
        *◆ Step 1:* Navigate to your VTOP timetable and copy ALL text from "SI.No" to "L94"
        
        *◆ Step 2:* Paste the complete text in the input field below and press Ctrl+Enter
        
        *◆ Step 3:* Hit the GENERATE button to create your calendar file
        
        *◆ Step 4:* Download the .ics file and import into your calendar app
        
        ---
        
        ### 📡 *Video Transmissions*
        
        *🖥 [Desktop Calendar Integration](https://youtu.be/A3Rubu_3Le0?si=FA482m6ABF9n7szG)*
        
        *📱 [Mobile Device Setup](https://youtu.be/dafPgd-1Z98)*
        """)

# ---------------------- Main App UI ----------------------
def main():
    add_custom_css()

    # Cyber Header
    st.markdown("""
    <div class="cyber-header">
        <div class="cyber-nav">
            <div class="nav-brand">
                <i class="fas fa-satellite-dish"></i> VIT CALENDAR
            </div>
            <div class="nav-links">
                <a href="https://github.com/andhanarapu-balu" target="_blank">
                    <i class="fab fa-github"></i> SOURCE CODE
                </a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h1><i class='fas fa-rocket'></i> TIMETABLE CONVERTER</h1>", unsafe_allow_html=True)
    st.markdown("<div class='author-credit'>⚡ ENGINEERED BY ANDHANARAPU BALU ⚡</div>", unsafe_allow_html=True)

    provide_instructions_expander()

    timetable_input = st.text_area(
        "🎯 INPUT YOUR TIMETABLE DATA:",
        placeholder="Paste your complete VTOP timetable here... System ready for data input.",
        height=200
    )

    ics_data = None

    if st.button("⚡ GENERATE CALENDAR"):
        if timetable_input.strip() == "":
            st.markdown("""
            <div class="error-alert">
                <i class="fas fa-exclamation-triangle"></i> 
                ERROR: No timetable data detected. Please input your schedule data.
            </div>
            """, unsafe_allow_html=True)
        else:
            ics_data = generate_ics_from_timetable(timetable_input)
            st.markdown("""
            <div class="success-alert">
                <i class="fas fa-check-circle"></i> 
                SUCCESS: Calendar file generated! Download initiated.
            </div>
            """, unsafe_allow_html=True)

    if ics_data:
        st.markdown('<div class="cyber-divider"></div>', unsafe_allow_html=True)
        st.markdown("### 📡 *DOWNLOAD TRANSMISSION*")
        st.download_button(
            label="⬇ DOWNLOAD CALENDAR FILE",
            data=ics_data,
            file_name="vit_cyber_calendar.ics",
            mime="text/calendar",
            help="Download your generated calendar file"
        )

    provide_samples_expander()

if __name__ == "__main__":
    main()