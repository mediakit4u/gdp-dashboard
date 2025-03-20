import streamlit as st
import requests
import qrcode
from io import BytesIO

BACKEND_URL = "https://your-backend-url.com"  # Update after backend deployment

st.title("Digital Business Card Creator")

# User Inputs
name = st.text_input("Full Name")
job_title = st.text_input("Job Title")
company = st.text_input("Company Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
website = st.text_input("Website")

# Upload profile picture & logo
profile_pic = st.file_uploader("Upload Profile Picture", type=["jpg", "png"])
company_logo = st.file_uploader("Upload Company Logo", type=["jpg", "png"])

# Choose a Template
template = st.selectbox("Choose Template", ["template1", "template2"])

# Generate Business Card
if st.button("Generate Card"):
    data = {
        "name": name,
        "job_title": job_title,
        "company": company,
        "email": email,
        "phone": phone,
        "website": website,
        "template": template
    }
    response = requests.post(f"{BACKEND_URL}/create_card", json=data)
    
    if response.status_code == 200:
        card_url = response.json()["card_url"]
        st.success("Business Card Created!")

        # Generate QR Code
        qr = qrcode.make(card_url)
        buf = BytesIO()
        qr.save(buf, format="PNG")
        st.image(buf.getvalue(), caption="Scan this QR Code")
    else:
        st.error("Failed to create card")
