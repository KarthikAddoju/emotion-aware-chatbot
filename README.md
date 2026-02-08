# Emotion-Aware Chatbot 🤖💬

An end-to-end **Emotion-Aware Conversational AI system** that detects user emotions from **text and speech inputs** and generates emotionally adaptive responses.  
This project demonstrates how emotion intelligence can be integrated into modern chatbots to improve user interaction and engagement.

---

## 🔍 Overview

Traditional chatbots respond uniformly regardless of user emotions.  
This project enhances conversational AI by introducing **emotion awareness**, allowing the chatbot to adjust its responses based on the user's emotional state.

The system:
- Detects emotions from **text input**
- Optionally detects emotions from **speech input**
- Selects emotionally appropriate responses
- Exposes the entire pipeline via a **FastAPI-based REST API**

---

## ✨ Key Features

- 🧠 **Text Emotion Recognition**
  - Uses pretrained Transformer-based sentiment models
  - Maps sentiment to emotional states (happy, sad, neutral)

- 🎙️ **Speech Emotion Recognition**
  - Wav2Vec2-based emotion classification
  - Supports offline audio inference

- 🤖 **Emotion-Aware Response Generation**
  - Chatbot responses adapt based on detected emotion
  - Modular design for easy LLM integration

- 🌐 **End-to-End API Deployment**
  - Built using FastAPI
  - Interactive API documentation via Swagger UI

---



