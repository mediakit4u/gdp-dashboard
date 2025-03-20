from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

class BusinessCard(BaseModel):
    name: str
    job_title: str
    company: str
    email: str
    phone: str
    website: str
    template: str

@app.post("/create_card")
def create_card(card: BusinessCard):
    # Store user details in JSON (or database)
    with open("cards.json", "a") as file:
        file.write(json.dumps(card.dict()) + "\n")
    
    card_url = f"https://your-frontend-url.com/cards/{card.name.replace(' ', '_')}.html"
    return {"card_url": card_url}
