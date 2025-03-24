from fastapi import FastAPI, HTTPException, UploadFile, File, Form, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from pathlib import Path
import sqlite3
import os
from contextlib import contextmanager
from typing import Optional

app = FastAPI(title="NFC Business Card API")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database Model
class ClientData(BaseModel):
    name: str
    phone: str
    email: str
    job_title: Optional[str] = None
    company: Optional[str] = None
    website: Optional[str] = None
    linkedin: Optional[str] = None
    twitter: Optional[str] = None
    instagram: Optional[str] = None
    template: str = "Modern"

# Database Setup
def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT NOT NULL,
                job_title TEXT,
                company TEXT,
                website TEXT,
                linkedin TEXT,
                twitter TEXT,
                instagram TEXT,
                template TEXT,
                profile_pic_path TEXT,
                company_logo_path TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

@contextmanager
def get_db():
    conn = sqlite3.connect("nfc_data.db")
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

# Initialize DB and create uploads directory
os.makedirs("uploads", exist_ok=True)
init_db()

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home():
    return {"status": "OK", "message": "NFC Business Card API"}

@app.post("/save_client_data")
async def save_client_data(
    request: Request,
    name: str = Form(...),
    phone: str = Form(...),
    email: str = Form(...),
    job_title: str = Form(None),
    company: str = Form(None),
    website: str = Form(None),
    linkedin: str = Form(None),
    twitter: str = Form(None),
    instagram: str = Form(None),
    template: str = Form("Modern"),
    profile_pic: UploadFile = File(None),
    company_logo: UploadFile = File(None)
):
    try:
        # Save files if provided
        profile_pic_path = None
        company_logo_path = None
        
        if profile_pic:
            profile_pic_path = f"uploads/profile_{email}_{profile_pic.filename}"
            with open(profile_pic_path, "wb") as buffer:
                buffer.write(await profile_pic.read())
        
        if company_logo:
            company
