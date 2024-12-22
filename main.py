# FastAPI backend for facial recognition and GPT integration
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend is running!"}
