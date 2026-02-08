from fastapi import APIRouter
from models.text_emotion import TextEmotionModel
from models.chatbot import EmotionAwareChatbot

router = APIRouter()
text_model = TextEmotionModel()
chatbot = EmotionAwareChatbot()

@router.post("/chat")
def chat_endpoint(message: str):
    emotion, confidence = text_model.predict(message)
    response = chatbot.respond(emotion, message)

    return {
        "detected_emotion": emotion,
        "confidence": confidence,
        "bot_response": response
    }
