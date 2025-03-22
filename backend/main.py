from fastapi import FastAPI

app = FastAPI()

@app.get("/save_client_data")
def home():
    return {"message": "Backend is running!"}

if _name_ == "_main_":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000
