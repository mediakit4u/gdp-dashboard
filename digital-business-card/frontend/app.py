import streamlit as st
import requests
import qrcode
from io import BytesIO
from PIL import Image

BACKEND_URL = "https://your-backend.onrender.com"  # Update this with your Render backend URL

st.title("🎨 Digital Business Card Generator")

# Collect User Info
name = st.text_input("Full Name")
phone = st.text_input("Phone")
email = st.text_input("Email")
job_title = st.text_input("Job Title")
company = st.text_input("Company Name")
website = st.text_input("Website")

# Choose a template
template = st.selectbox("Choose Card Template", ["Modern", "Classic", "Minimalist"])

# Button to Generate Card
if st.button("Generate Card"):
    data = {
        "name": name,
        "phone": phone,
        "email": email,
        "job_title": job_title,
        "company": company,
        "website": website,
        "template": template
    }

    response = requests.post(f"{BACKEND_URL}/generate_card", json=data)

    if response.status_code == 200:
        card_url = response.json()["card_url"]
        st.success(f"✅ Your Business Card is Ready! [View Here]({card_url})")

        # Generate QR Code
        qr = qrcode.make(card_url)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")
        st.image(Image.open(buffer), caption="Scan to View Business Card", use_column_width=False)

    else:
        st.error("❌ Error generating business card. Try again.")
