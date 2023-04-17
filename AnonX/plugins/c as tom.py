from pyrogram import filters, Client
from AnonX import app
import asyncio
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from AnonX.core.call import Anon
from AnonX.utils.database import *
from pytgcalls.exceptions import NoActiveGroupCall, TelegramServerError

@app.on_message(filters.command('setname') & filters.private)
async def set_name(client, message):
    await message.reply("ارسل الاسم الجديد:")
    assistant = await group_assistant(Anon, message.chat.id)
    try:
        text = message.text.split()[1:]
        new_name = " ".join(text)
        await assistant.update_profile(first_name=new_name)
        await message.reply(f"تم تغيير الاسم الى {new_name}")
    except Exception as e:
        await message.reply("حدث خطأ اثناء تغيير الاسم!")
