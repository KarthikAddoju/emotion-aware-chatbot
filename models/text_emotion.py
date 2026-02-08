from transformers import pipeline

class TextEmotionModel:
    def __init__(self):
        self.classifier = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )

    def predict(self, text):
        result = self.classifier(text)[0]
        label = result["label"]
        score = result["score"]

        emotion_map = {
            "POSITIVE": "happy",
            "NEGATIVE": "sad"
        }

        return emotion_map[label], score
