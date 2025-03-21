import streamlit as st
import requests
import qrcode
from io import BytesIO

# Backend API URL
BACKEND_URL = "https://your-backend-url.com"

st.title("📇 Digital Business Card Generator")

# Collect Client Information
st.header("Enter Client Details")
name = st.text_input("Full Name")
phone = st.text_input("Phone Number")
email = st.text_input("Email Address")
job_title = st.text_input("Job Title")
company = st.text_input("Company Name")
website = st.text_input("Website")
linkedin = st.text_input("LinkedIn Profile")
twitter = st.text_input("Twitter Profile")

# Choose Template
st.header("Choose Business Card Template")
template_choice = st.selectbox("Select a Template", ["Modern", "Classic", "Minimalist"])

if st.button("Generate Card"):
    # Send Data to Backend
    data = {
        "name": name, "phone": phone, "email": email,
        "job_title": job_title, "company": company, "website": website,
        "linkedin": linkedin, "twitter": twitter, "template": template_choice
    }
    response = requests.post(f"{BACKEND_URL}/generate_card", json=data)

    if response.status_code == 200:
        card_url = response.json()["card_url"]
        
        # Generate QR Code
        qr = qrcode.make(card_url)
        qr_bytes = BytesIO()
        qr.save(qr_bytes, format="PNG")

        # Display Business Card Template
        st.success("✅ Business Card Generated Successfully!")
        st.write("📌 *Preview Below:*")
        st.image(card_url, caption="Your Digital Business Card", use_column_width=True)

        # Display QR Code
        st.image(qr_bytes, caption="Scan to View", use_column_width=False)
        st.write(f"[🔗 View Business Card Here]({card_url})")
    else:
        st.error("❌ Failed to generate card. Try again.")
