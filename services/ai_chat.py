import requests
import logging
from config import GROQ_API_KEY

class AIChat:
    @staticmethod
    def get_response(user_message: str) -> str:
        if not GROQ_API_KEY:
            return "I am configured for images! To chat with AI, please set GROQ_API_KEY."

        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "llama-3.1-8b-instant",
            "messages": [
                {"role": "system", "content": "You are OpenArt AI assistant. Helpful, friendly, and concise."},
                {"role": "user", "content": user_message}
            ]
        }

        try:
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            data = response.json()
            if response.status_code == 200:
                return data["choices"][0]["message"]["content"]
            return "Sorry, I am having trouble thinking right now."
        except Exception as e:
            logging.error(f"Chat error: {e}")
            return "Apologies, my chat engine is currently unreachable."
