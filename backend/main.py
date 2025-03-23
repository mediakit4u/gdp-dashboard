from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Database Model
class ClientData(BaseModel):
    name: str
    phone: str
    email: str
    job_title: str
    company: str
    website: str
    linkedin: str
    twitter: str
    instagram: str
    template: str

# Initialize Database
def init_db():
    conn = sqlite3.connect("nfc_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            email TEXT,
            job_title TEXT,
            company TEXT,
            website TEXT,
            linkedin TEXT,
            twitter TEXT,
            instagram TEXT,
            template TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.get("/")
def home():
    return {"message": "Backend is running!"}

@app.post("/save_client_data")
def save_client_data(client: ClientData):
    try:
        conn = sqlite3.connect("nfc_data.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO clients (name, phone, email, job_title, company, website, linkedin, twitter, instagram, template)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (client.name, client.phone, client.email, client.job_title, client.company, client.website,
              client.linkedin, client.twitter, client.instagram, client.template))
        conn.commit()
        conn.close()

        # Generate a mock card URL (Replace this with actual logic)
        card_url = f"https://gdp-dashboard-1-rbqi.onrender.com/{client.name.replace(' ', '_')}_card"

        return {"card_url": card_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if "__name__" == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 10000))  # Render assigns a port dynamically
    uvicorn.run(app, host="0.0.0.0", port=port)
