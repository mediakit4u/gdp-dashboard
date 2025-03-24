import streamlit as st
import requests
from io import BytesIO

# Config
st.set_page_config(page_title="NFC Business Suite", layout="wide")

# Initialize session state
if 'form_data' not in st.session_state:
    st.session_state.form_data = {}

# Get backend URL from secrets or use default
BACKEND_URL = st.secrets.get("BACKEND_URL", "https://gdp-dashboard-1-rbqi.onrender.com")

st.title("NFC Business Suite - Client Information")

# Section 1: Basic Information
with st.expander("1️⃣ NFC Card Details", expanded=True):
    name = st.text_input("Full Name*", value=st.session_state.form_data.get('name', ''))
    phone = st.text_input("Phone*", value=st.session_state.form_data.get('phone', ''))
    email = st.text_input("Email*", value=st.session_state.form_data.get('email', ''))
    
    # Update session state
    st.session_state.form_data.update({
        'name': name,
        'phone': phone,
        'email': email
    })

# Section 2: Business Profile
with st.expander("2️⃣ Business Card Profile"):
    job_title = st.text_input("Job Title", value=st.session_state.form_data.get('job_title', ''))
    company = st.text_input("Company Name", value=st.session_state.form_data.get('company', ''))
    website = st.text_input("Website", value=st.session_state.form_data.get('website', ''))
    profile_pic = st.file_uploader("Upload Profile Picture", type=["jpg", "png", "jpeg"])
    company_logo = st.file_uploader("Upload Company Logo", type=["jpg", "png", "jpeg"])
    
    st.session_state.form_data.update({
        'job_title': job_title,
        'company': company,
        'website': website
    })

# Section 3: Social Media
with st.expander("3️⃣ Social Media Links (Optional)"):
    linkedin = st.text_input("LinkedIn URL", value=st.session_state.form_data.get('linkedin', ''))
    twitter = st.text_input("Twitter URL", value=st.session_state.form_data.get('twitter', ''))
    instagram = st.text_input("Instagram URL", value=st.session_state.form_data.get('instagram', ''))
    
    st.session_state.form_data.update({
        'linkedin': linkedin,
        'twitter': twitter,
        'instagram': instagram
    })

# Section 4: Template Selection
template = st.selectbox(
    "4️⃣ Choose Your Business Card Template",
    ["Modern", "Classic", "Minimalist"],
    index=["Modern", "Classic", "Minimalist"].index(
        st.session_state.form_data.get('template', 'Modern')
    )
)
st.session_state.form_data['template'] = template

# Submission
if st.button("💾 Save & Generate Business Card", type="primary"):
    # Validate required fields
    if not all([name, email, phone]):
        st.error("Please fill in all required fields (marked with *)")
    else:
        with st.spinner("Creating your business card..."):
            try:
                # Prepare files
                files = {}
                if profile_pic:
                    files['profile_pic'] = ('profile.jpg', profile_pic.getvalue())
                if company_logo:
                    files['company_logo'] = ('logo.jpg', company_logo.getvalue())
                
                # Send data to backend
                response = requests.post(
                    f"{BACKEND_URL}/save_client_data",
                    data=st.session_state.form_data,
                    files=files if files else None
                )
                
                if response.status_code == 200:
                    card_url = response.json().get("card_url")
                    st.success(f"✅ Business Card Created!")
                    st.markdown(f"[View Your Card]({card_url})", unsafe_allow_html=True)
                    st.balloons()
                else:
                    st.error(f"Error: {response.text}")
                    
            except requests.exceptions.RequestException as e:
                st.error(f"Connection error: {str(e)}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {str(e)}")
