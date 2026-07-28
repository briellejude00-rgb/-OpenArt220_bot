class PromptEnhancer:
    @staticmethod
    def enhance(prompt: str, mode: str) -> str:
        prefixes = {
            "logo": "minimalist professional logo design, vector art, iconic emblem, graphic design, high quality, isolated on clean background, ",
            "art": "masterpiece digital painting, concept art, highly detailed, vibrant lighting, trending on artstation, ",
            "anime": "masterpiece anime illustration, key visual, ultra-detailed, anime aesthetic, vibrant colors, ",
            "image": "photorealistic 8k photo, ultra realistic, highly detailed, cinematic lighting, "
        }
        prefix = prefixes.get(mode, "")
        return f"{prefix}{prompt}"
