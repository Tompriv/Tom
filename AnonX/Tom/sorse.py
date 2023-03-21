
import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

@app.on_message(
    command(["سورس مين","سورس","السورس","سورسي", "cr"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/be8fb2f02cf57e1725ccd.jpg",
        caption=f"""╭═★⊷⌯⧼[⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝](https://t.me/pp_g3)⧽⌯⊶★═╮\n★‹ [⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝𝐀](https://t.me/pp_g3)\n★‹ [𝐶𝑅𝐼𝑆𝑇𝐼𝑁](https://t.me/dr_criss)\n★‹ [𝙏َِ𝙊َِ𝙈ِ](https://t.me/DEV_TOM)\n★‹ [ρ᥆kᥱꪔ᥆ꪀ](https://t.me/devpokemon)\n╰═★⊷⌯⧼[⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝](https://t.me/pp_g3)⧽⌯⊶★═╯\n ⍟ Welcome to source Avatar""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙏َِ𝙊َِ𝙈ِ༄►", url=f"https://t.me/DEV_TOM"), 
                ],[
                    InlineKeyboardButton(
                        "⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⚡️", url=f"https://t.me/pp_g3"),
                ],[
                    InlineKeyboardButton(
                        "𝐀𝐃𝐃 𝐌𝐄💞", url=f"https://t.me/DEVTOM_bot?startgroup=true"),
                ],

            ]

        ),

    )



@app.on_message(command(["غنيلي", "غني", "غ", "🎙 ¦ غـنيـلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاغـنـية لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )



