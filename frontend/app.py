import streamlit as st
import requests

BACKEND_URL = https://gdp-dashboard-0qc8.onrender.com      # "http://127.0.0.1:8000"  # Update this if backend is hosted online

st.title("NFC Card Manager")

if st.button("Scan NFC Card"):
    response = requests.get(f"{BACKEND_URL}/read_nfc")
    if response.status_code == 200:
        st.success(f"Card ID: {response.json()['card_id']}")
    else:
        st.error("Failed to read NFC card")

data_input = st.text_input("Enter data to write to NFC card")
if st.button("Write to NFC Card"):
    response = requests.post(f"{BACKEND_URL}/write_nfc", json={"data": data_input})
    if response.status_code == 200:
        st.success("Data written to NFC card successfully!")
    else:
        st.error("Failed to write to NFC card")
