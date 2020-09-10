import os
from dotenv import load_dotenv


load_dotenv('.env')

class VKConfig:
	VK_TOKEN = os.getenv("VK_TOKEN") 
	STATUS = "Now playing (Spotify): {track} - {artist} | {album}"
	STANDARD_STATUS = ""


class SpotifyConfig:
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    REDIRECT_URI = os.getenv("REDIRECT_URI") # http://localhost:5000/callback
    USERNAME = os.getenv("USERNAME")
    SCOPE = "user-read-playback-state user-library-read"