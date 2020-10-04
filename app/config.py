import os
from dotenv import load_dotenv


load_dotenv('.env')


class VKConfig:
    VK_TOKEN = os.getenv("VK_TOKEN") 
    STATUS = "🎧 Spotify | {track} - {artist} | {album}"
    DEFAULT_STATUS = os.getenv("DEFAULT_STATUS") or f"SpotifyToVKStatus"


class SpotifyConfig:
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    REDIRECT_URI = os.getenv("REDIRECT_URI") # http://localhost:5000/callback
    USERNAME = os.getenv("USERNAME")
    SCOPE = "user-read-currently-playing"
