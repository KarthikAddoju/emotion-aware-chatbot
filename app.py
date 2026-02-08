from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="Emotion-Aware Chatbot")

app.include_router(router)

@app.get("/")
def root():
    return {"status": "Emotion-Aware Chatbot API is running"}
