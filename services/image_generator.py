import requests
import logging
from config import TOGETHER_API_KEY, MODELS
from services.prompt_enhancer import PromptEnhancer

class ImageGenerator:
    @staticmethod
    def generate(prompt: str, mode: str = "image") -> str:
        if not TOGETHER_API_KEY:
            raise ValueError("TOGETHER_API_KEY is not set.")

        model_id = MODELS.get(mode, MODELS["image"])
        enhanced_prompt = PromptEnhancer.enhance(prompt, mode)

        url = "https://api.together.xyz/v1/images/generations"
        headers = {
            "Authorization": f"Bearer {TOGETHER_API_KEY}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": model_id,
            "prompt": enhanced_prompt,
            "width": 1024,
            "height": 1024,
            "steps": 4,
            "n": 1,
            "response_format": "url"
        }

        response = requests.post(url, json=payload, headers=headers, timeout=60)
        data = response.json()

        if response.status_code == 200 and "data" in data and len(data["data"]) > 0:
            return data["data"][0]["url"]
        else:
            err = data.get("error", {}).get("message", "Unknown image generation error.")
            raise Exception(err)
