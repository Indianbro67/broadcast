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
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6289264953:AAG1N1Q3_KXM-V2KB-nDb9LFlMXq9WpZPv8")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "26670684"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "60592bded0f25a9633a8133601f2c779")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgres://vjqqkgqwskeiti:b8cc62ff1d1b7304fb7b5bbc2f722f3ea504fc66f95518e3634563438d69ee7a@ec2-35-169-184-61.compute-1.amazonaws.com:5432/d4nqs96vutghj7")

    # Group / channel username of the support chat
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "@adult_updates")

    # List of admin user ids for special functions(Storing as an array)
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5841005593").split())


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
