import time
import typing
import spotipy
import logging
import app.logger

from spotipy.oauth2 import SpotifyOAuth
from VKLight import (VKLight, VKLightError)
from .config import (VKConfig, SpotifyConfig)


logger = logging.getLogger("spotifyToVKStatus")

spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=SpotifyConfig.SCOPE,
        client_id=SpotifyConfig.CLIENT_ID,
        client_secret=SpotifyConfig.CLIENT_SECRET,
        redirect_uri=SpotifyConfig.REDIRECT_URI,
        username=SpotifyConfig.USERNAME,
    )
)

vk = VKLight(dict(
        access_token=VKConfig.VK_TOKEN,
        lang='ru',
        host="api.vk.me",
        v='5.130'
    )
)

current_playing = typing.List[typing.Union[str, str, str]]


def update_status(_current_playing):
    current = spotify.current_user_playing_track()

    if current is not None:

        track = current["item"]["name"]
        album = current["item"]["album"]["name"]
        artist = current["item"]["artists"][0]["name"]

        if _current_playing != [track, album, artist]:
            set_status(VKConfig.STATUS.format(track=track, album=album, artist=artist))
            logger.info(f"🎧 Spotify | {track} - {artist}")

        return [track, album, artist]

    if _current_playing is not None:
        set_default_status()

    return


def set_default_status() -> dict:
    logger.info("Установлен стандартный статус")
    return vk.call("status.set", {"text": VKConfig.DEFAULT_STATUS})


def set_status(status) -> dict:
    return vk.call("status.set", {"text": status})


if __name__ == '__main__':
    try:
        logger.info(f"Текущий статус: {VKConfig.DEFAULT_STATUS}")

        while True:
            logger.debug("Получаю обновления")
            current_playing = update_status(current_playing)
            time.sleep(8)

    except VKLightError as e:
        logger.exception(e)

    except (SystemExit, KeyboardInterrupt) as e:
        set_default_status()

    except Exception as e:
        logger.exception(e)
