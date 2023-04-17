from pyrogram import filters, Client
from AnonX import app
import asyncio
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from AnonX.core.call import Anon
from AnonX.utils.database import *
from pytgcalls.exceptions import NoActiveGroupCall, TelegramServerError

@app.on_message(filters.regex("تغيير اسم المساعد"))
async def tom_name(client, message):
    await message.reply("أرسل اسم المساعد الجديد:")
    try:
        msg = await app.listen(message.chat.id)
        new_name = msg.text
        
        assistant = await group_assistant(Anon, message.chat.id)
        await assistant.update_profile(first_name=new_name)
        
        await message.reply(f"تم تغيير اسم المساعد الى {new_name}")
    except Exception as e:
        print(str(e))
        await message.reply("حدث خطأ أثناء تغيير اسم المساعد!")
