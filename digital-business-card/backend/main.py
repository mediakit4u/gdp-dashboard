from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ClientData(BaseModel):
    name: str
    phone: str
    email: str
    job_title: str
    company: str
    website: str
    template: str

@app.post("/generate_card")
def generate_card(client: ClientData):
    card_url = f"https://your-dbc-frontend.onstreamlit.app/cards/{client.name.replace(' ', '_')}.html"
    return {"card_url": card_url}
