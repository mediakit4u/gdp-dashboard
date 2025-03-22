from fastapi import FastAPI

app = FastAPI()

@app.get("/save_client_data")
def home():
    return {"message": "Backend is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000
