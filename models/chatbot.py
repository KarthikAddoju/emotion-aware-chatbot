class EmotionAwareChatbot:
    def __init__(self):
        self.responses = {
            "happy": "That's great to hear! 😊 Tell me more!",
            "sad": "I'm really sorry you're feeling this way. I'm here for you 💙",
            "angry": "I sense some frustration. Let's take a moment and talk it through.",
            "fear": "That sounds stressful. You're not alone in this.",
            "neutral": "I understand. How can I help you further?"
        }

    def respond(self, emotion, user_text):
        return self.responses.get(emotion, self.responses["neutral"])
