#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  Name     : broadcast-bot [ Telegram ]
#  Repo     : https://github.com/m4mallu/broadcast-bot
#  Author   : Renjith Mangal [ https://t.me/space4renjith ]
#  Licence  : GPL-3

import os
import asyncio
from presets import Presets
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import (InlineKeyboardButton,InlineKeyboardMarkup, Message)
from library.support import users_info
from library.sql import add_user, query_msg


if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config


# ------------------------------- Start Message --------------------------------- # 
@Client.on_message(filters.private & filters.command('start')) 
 async def start_bot(bot, m: Message): 
     id = m.from_user.id 
     user_name = '@' + m.from_user.username if m.from_user.username else None 
     await add_user(id, user_name) 
     await m.reply_audio(audio=f"https://dl.sndup.net/hp75/How%20To%20Download%20Restricted%20Photo%20and.mp3",caption=f"""𝗦𝗲𝗻𝗱 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗢r 𝗚𝗿𝗼𝘂𝗽 𝗟𝗶𝗻𝗸 . \n𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐑𝐞𝐬𝐭𝐫𝐢𝐜𝐭𝐞𝐝 𝐏𝐡𝐨𝐭𝐨 𝐚𝐧𝐝 𝐕𝐢𝐝𝐞𝐨\n\n@adult_updates""",reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ɪɴᴠɪᴛᴇ ᴀɴᴅ ɢᴇᴛ ᴠɪᴘ ᴀᴄᴄᴇꜱꜱ 🗝️🔐", url=f"https://telegram.me/share/url?url=https://t.me/save_all_file_bot?start=1521651151"),
                ]
           ]
)

# ------------------------------- View Subscribers --------------------------------- #
@Client.on_message(filters.private & filters.command('subscribers'))
async def subscribers_count(bot, m: Message):
    id = m.from_user.id
    if id not in Config.AUTH_USERS:
        return
    msg = await m.reply_text(Presets.WAIT_MSG)
    messages = await users_info(bot)
    active = messages[0]
    blocked = messages[1]
    await m.delete()
    await msg.edit(Presets.USERS_LIST.format(active, blocked))


# ------------------------ Send messages to subs ----------------------------- #
@Client.on_message(filters.private & filters.command('send'))
async def send_text(bot, m: Message):
    id = m.from_user.id
    if id not in Config.AUTH_USERS:
        return
    if (" " not in m.text) and ("send" in m.text) and (m.reply_to_message is not None):
        query = await query_msg()
        for row in query:
            chat_id = int(row[0])
            try:
                await bot.copy_message(
                    chat_id=chat_id,
                    from_chat_id=m.chat.id,
                    message_id=m.reply_to_message.message_id,
                    caption=m.reply_to_message.caption,
                    reply_markup=m.reply_to_message.reply_markup
                )
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except Exception:
                pass
    else:
        msg = await m.reply_text(Presets.REPLY_ERROR, m.message_id)
        await asyncio.sleep(8)
        await msg.delete()
