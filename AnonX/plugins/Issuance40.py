import asyncio
import os
import time
import requests
import aiohttp
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app

import re
import sys
from os import getenv

from dotenv import load_dotenv



@app.on_message(
    command(["اصدار","حول"])
  
)
async def bkouqw(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/be8fb2f02cf57e1725ccd.jpg",
        caption=f"""**⩹━★⊷⌯⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⌯⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention}\n
★᚜ اسم سورس:-cr
★᚜ نوعه:-ميوزك
★᚜ للغه برمجه:- بايثون
★᚜ اللغه:-اللغه العربيه ويدعم الانجليزيه 
★᚜ مجال تشغيل :- تشغيل بوتات الميوزك
★᚜ نظام تشغيل:-cr بوت ميوزك
★᚜ الاصدار 4.0.1 pyrogram 
★᚜ تاريخ تاسيس:-21-3-2023
★᚜ مأسس cr:- [𝙏َِ𝙊َِ𝙈ِ༄►](https://t.me/DEV_TOM)

**⩹━★⊷⌯𝐒𝐎𝐔𝐑𝐂𝐄 𝐕𝐄𝐆𝐀⌯⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝", url=f"https://t.me/pp_g3"), 
                 ],[
                 InlineKeyboardButton(
                        "◁", callback_data="hpdtsnju"),
               ],
          ]
        ),
    )


