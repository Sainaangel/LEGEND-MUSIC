#

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", "6296490")
        self.API_HASH: str = os.environ.get("API_HASH", "24385183c93a98ae4155c25d9f5f64b2")
        self.SESSION: str = os.environ.get("SESSION", "BABgE6oAQp-t7hNDOyOd7zBcDPr_SkdelqrkKRviBQY1l5n2vjEay2zAOdwTnl_vWKaJjwrcouZy7jm3QR9W8hKxKtdCMyQ9Lx5yq-d8whxrsPAaCkpPlP3Ke9MVLBdSSrd-vmwZkTmIHCy3N_2tZh0jwWrRpWHe_VLSkXjHfZabNpdFrtSN0rt0xg1KEjkWU7JzmiGmNMVR5VWkMmQHpLSbc_EMZYtOmjshUPLjulwgDtzOHMap2GAMSD4rNGmtqNkM9yRFSzn6lROVd2GYpseMXWXhV_4JCZJq81r_FpH6RtBrIb5VZ2n_gapRmCvdYZuqlamICTEneq7clvyXCKV_3PyFuAAAAAFF4IyQAA")
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "5941659598:AAGnHLMYzgoDjZtyn5KpbewyAF0BUzkWnlw")
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", "5763920115").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "/").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "video"
            if (os.environ.get("STREAM_MODE", "video").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", None)


config = Config()
