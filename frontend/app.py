import streamlit as st
import requests

BACKEND_URL = "https://gdp-dashboard-1-qnmi.onrender.com"  # Update with your backend deployment URL

st.title("NFC Business Suite - Client Information")

# Step 1: NFC Card Basic Information
st.header("1️⃣ NFC Card Details")
name = st.text_input("Full Name")
phone = st.text_input("Phone")
email = st.text_input("Email")

# Step 2: Digital Business Card (DBC) Profile
st.header("2️⃣ Business Card Profile")
job_title = st.text_input("Job Title")
company = st.text_input("Company Name")
website = st.text_input("Website")
profile_pic = st.file_uploader("Upload Profile Picture", type=["jpg", "png"])
company_logo = st.file_uploader("Upload Company Logo", type=["jpg", "png"])

# Step 3: Social Media & Custom Links
st.header("3️⃣ Social Media Links (Optional)")
linkedin = st.text_input("LinkedIn URL")
twitter = st.text_input("Twitter URL")
instagram = st.text_input("Instagram URL")

# Choose a Template
st.header("4️⃣ Choose Your Business Card Template")
template = st.selectbox("Template Style", ["Modern", "Classic", "Minimalist"])

# Submit Button
if st.button("Save & Generate Business Card"):
    data = {
        "name": name,
        "phone": phone,
        "email": email,
        "job_title": job_title,
        "company": company,
        "website": website,
        "linkedin": linkedin,
        "twitter": twitter,
        "instagram": instagram,
        "template": template
    }

    response = requests.post(f"{BACKEND_URL}/save_client_data", json=data)
    
    if response.status_code == 200:
        card_url = response.json()["card_url"]
        st.success(f"✅ Business Card Created! Access it here: [View Card]({card_url})")
    else:
        st.error("❌ Error: Could not save data.")
