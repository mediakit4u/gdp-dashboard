from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

# Define Data Model
class ClientData(BaseModel):
    name: str
    phone: str
    email: str
    job_title: str
    company: str
    website: str
    linkedin: str = None
    twitter: str = None
    instagram: str = None
    template: str

# Store Client Data
@app.post("/save_client_data")
def save_client_data(client: ClientData):
    with open("clients.json", "a") as file:
        file.write(json.dumps(client.dict()) + "\n")

    # Generate Business Card URL
    card_url = f"https://your-dbc-url.com/cards/{client.name.replace(' ', '_')}.html"
    return {"card_url": card_url}
