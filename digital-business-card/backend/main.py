from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

class ClientData(BaseModel):
    name: str
    phone: str
    email: str
    job_title: str
    company: str
    website: str
    linkedin: str
    twitter: str
    template: str

@app.post("/generate_card")
def generate_card(client: ClientData):
    # Save client data
    with open("clients.json", "a") as file:
        file.write(json.dumps(client.dict()) + "\n")

    # Create business card URL
    card_url = f"https://your-dbc-url.com/cards/{client.name.replace(' ', '_')}.html"
    
    return {"card_url": card_url}
