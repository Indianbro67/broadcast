#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  Name     : broadcast-bot [ Telegram ]
#  Repo     : https://github.com/m4mallu/broadcast-bot
#  Author   : Renjith Mangal [ https://t.me/space4renjith ]
#  Licence  : GPL-3


import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):
    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5829214784:AAGjKk4AF3VYG6rn4dMZm8I0MEpqVuRFuJA")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "26670684"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "60592bded0f25a9633a8133601f2c779")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgresql://devil56:love@localhost:5432/devi56")

    # Group / channel username of the support chat
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "@adult_updates")

    # List of admin user ids for special functions(Storing as an array)
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5841005593").split())


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
