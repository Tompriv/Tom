from random import randint
from random import randint
from typing import Optional
from AnonX import app
from pyrogram import Client, filters
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message
from config import *

async def get_group_call(
    client: Client, message: Message, err_msg: str = ""
) -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, InputPeerChannel):
        full_chat = (
            await client.invoke(GetFullChannel(channel=chat_peer))
        ).full_chat
    elif isinstance(chat_peer, InputPeerChat):
        full_chat = (
            await client.invoke(GetFullChat(chat_id=chat_peer.chat_id))
        ).full_chat
    else:
        full_chat = None
        
    if full_chat is not None:
        return full_chat.call

    await message.reply_text(f"**No group call found** {err_msg}")
    return None


@app.on_message(
    filters.regex("فتح الكول")
    & filters.me
)
async def opengc(client: Client, message: Message):
    args = message.text.split(" ", 1)
    chat_id = message.chat.title if len(args) == 1 else args[1]
    vctitle = None if len(args) == 1 else args[1]
    
    tex = await message.reply_text("Processing...")
    
    try:
        await client.invoke(
            CreateGroupCall(
                peer=await client.resolve_peer(chat_id),
                random_id=randint(10000, 999999999),
                title=vctitle,
            )
        )
        await tex.edit(f"**Started group call**\n**Chat ID:** `{chat_id}`\n**Title:** `{vctitle}`" if vctitle else f"**Started group call**\n**Chat ID:** `{chat_id}`")
    except Exception as e:
        await tex.edit(f"**Error:** `{str(e)}`")


@app.on_message(
    filters.regex("قفل الكول")
    & filters.me
)
async def closegc(client: Client, message: Message):
    group_call = await get_group_call(client, message, ", group call already ended")
    
    if group_call is None:
        return
    
    await client.invoke(DiscardGroupCall(call=group_call))
    await message.reply_text("**Ended group call**")
