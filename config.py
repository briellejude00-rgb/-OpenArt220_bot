import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY", "").strip()
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "").strip()

# AI Models Setup
MODELS = {
    "image": "black-forest-labs/FLUX.1-schnell",
    "logo": "black-forest-labs/FLUX.1-schnell",
    "art": "stabilityai/stable-diffusion-xl-base-1.0",
    "anime": "stabilityai/stable-diffusion-xl-base-1.0"
}
