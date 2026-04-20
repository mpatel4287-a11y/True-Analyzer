import urllib.parse

def get_preview_url(prompt: str) -> str:
    """
    Returns a Pollinations AI image URL for the given prompt.
    Pollinations is free, needs no API key, and renders on-the-fly.
    """
    if not prompt:
        return ""
        
    encoded_prompt = urllib.parse.quote(prompt)
    # Using Pollinations AI for free, non-auth image generation
    # Parameters: width=1024, height=1024, model=flux (standard quality)
    return f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true&model=flux"
