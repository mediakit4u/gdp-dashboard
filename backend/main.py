from fastapi import FastAPI, HTTPException
import nfc
import sqlite3

app = FastAPI()

# ✅ Database Setup
conn = sqlite3.connect("nfc_data.db")  
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS nfc_cards (
        id INTEGER PRIMARY KEY, 
        card_id TEXT UNIQUE, 
        data TEXT
    )
""")
conn.commit()
conn.close()

# ✅ Function to Read NFC Card
def read_nfc():
    clf = nfc.ContactlessFrontend('usb')  # Ensure NFC reader is connected
    tag = clf.connect(rdwr={'on-connect': lambda tag: False})
    return str(tag)

# ✅ Function to Write Data to NFC Card
def write_nfc(data):
    clf = nfc.ContactlessFrontend('usb')
    tag = clf.connect(rdwr={'on-connect': lambda tag: True})
    tag.ndef.message = nfc.ndef.Message(nfc.ndef.TextRecord(data))
    return "Write successful"

# ✅ API Endpoint to Read NFC Card
@app.get("/read_nfc")
def get_nfc_data():
    try:
        card_id = read_nfc()
        return {"card_id": card_id, "message": "Card read successfully"}
    except:
        raise HTTPException(status_code=500, detail="Failed to read NFC card")

# ✅ API Endpoint to Write Data to NFC Card & Save to Database
@app.post("/write_nfc")
def write_to_nfc(data: str):
    try:
        write_nfc(data)

        # Save card data to database
        conn = sqlite3.connect("nfc_data.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO nfc_cards (card_id, data) VALUES (?, ?)", (data, data))
        conn.commit()
        conn.close()

        return {"message": "Data written to NFC card"}
    except:
        raise HTTPException(status_code=500, detail="Failed to write to NFC card")
