from pyrogram import filters, Client
from AnonX import app
import asyncio
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from AnonX.core.call import Anon
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError)
from AnonX.utils.database import db

async def is_call_active(chat_id: int) -> bool:
    group_call = db.active_calls.get(str(chat_id))
    return group_call is not None

async def add_active_call(chat_id: int, call: GroupCall) -> None:
    db.active_calls[str(chat_id)] = {
        "chat_id": chat_id,
        "voice_chat_id": call.voice_chat.id,
        "voice_chat_discussion": call.voice_chat_discussion.id
    }

async def remove_active_call(chat_id: int) -> None:
    del db.active_calls[str(chat_id)]

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
