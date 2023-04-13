from pyrogram import filters, Client
from AnonX import app
import asyncio
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from AnonX.core.call import Anon
from AnonX.utils.database import is_call_active, add_active_call, remove_active_call
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError)

@app.on_message(filters.regex("فتح الكول"))
async def start_call(client, message):
    assistant = await group_assistant(Anon, message.chat.id)
    if await is_call_active(message.chat.id):
        await message.reply("محادثة صوتية مفتوحة بالفعل")
        return
    await message.reply("جاري فتح المحادثة الصوتية...")
    try:
        await assistant.join_group_call(
            message.chat.id,
            AudioPiped("./assets/music.mp3"),
            stream_type=StreamType().pulse_stream
        )
        await add_active_call(message.chat.id)
        await message.reply("تم فتح المحادثة الصوتية بنجاح")
    except Exception as e:
        await message.reply(f"حدث خطأ أثناء فتح المحادثة الصوتية: {str(e)}")

@app.on_message(filters.regex("قفل الكول"))
async def stop_call(client, message):
    assistant = await group_assistant(Anon, message.chat.id)
    if not await is_call_active(message.chat.id):
        await message.reply("لا يوجد محادثة صوتية مفتوحة")
        return
    await message.reply("جاري إغلاق المحادثة الصوتية...")
    try:
        await assistant.leave_group_call(message.chat.id)
        await remove_active_call(message.chat.id)
        await message.reply("تم إغلاق المحادثة الصوتية بنجاح")
    except Exception as e:
        await message.reply(f"حدث خطأ أثناء إغلاق المحادثة الصوتية: {str(e)}")
