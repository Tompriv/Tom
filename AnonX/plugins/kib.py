import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)



REPLY_MESSAGE = "**👋︙مـرحـبـا بـك عـزيـزي العـضـو ♥️**\n**✨︙فــي ازرار التسـليـه لـلـبـوت💞**"

REPLY_MESSAGE_BUTTONS = [
    [
        ("💠︙ابـراج︙💠"),
    ],
    [
        ("𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 𝘾𝙍 ")
    ],
    [
        ("⌔حـروف⌔"),
        ("⌔صـراحـه⌔")
    ],
    [
        ("⌔لـو خـيـروك⌔"),
        ("⌔تـويـت⌔")
    ],
    [
        ("نبذه عن الكيبورد ⚡")
    ],
    [
        ("⌔اذكـار⌔"),
        ("⌔يـوتـيـوب⌔")
    ],
    [
        ("⌔ايــدي⌔"),
        ("⌔اسـمـي⌔")
    ],
    [
        ("⌔كـتـبـات⌔"),
        ("⌔انـصـحـنـي⌔")
    ]
]

@app.on_message(
    filters.command("start")
    & filters.private
)
async def music(client: Client, message: Message):
    text = REPLY_MESSAGE
    reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    await message.reply(
        text=text,
        reply_markup=reply_markup
    )


@app.on_message(filters.regex("💠︙ابـراج︙💠"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/e7bb54b34faadd2c9b199.jpg",
        caption=f"""**نبذه سريعه عن الابراج** : **يتم استخدام هذا الامر لعرض الابراج فقط🫡**\n**استخدم الامر بهذا الشكل** `ابراج` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𓆩 👨‍💻︙قـنـاة الـسـورس 𓆪", url=f"https://t.me/pp_g3"),
            ]
         ]
     )
  )



@app.on_message(filters.regex("𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 𝘾𝙍 "))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/e7bb54b34faadd2c9b199.jpg",
        caption=f"""**sᴏᴜʀᴄᴇ cr ᴘʀᴏɢʀᴀᴍᴍᴇʀ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇʀ𖣩** : **ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴘʀᴏɢʀᴀᴍᴍɪɴɢ ʜᴏʙʙʏɪsᴛ父**\n**cr メ` **contact with me 𖡰**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𝙏َِ𝙊َِ𝙈َِّّ ( ٍّالبشمبرمج) ", url=f"https://t.me/DEV_TOM"),
            ]
         ]
     )
  )
  

@app.on_message(filters.regex("⌔حـروف⌔"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/e7bb54b34faadd2c9b199.jpg",
        caption=f"""**نبذه سريعه عن الاحرف** : **يتم استخدام هذا الامر لعرض لعبه جماد حيوان نبات فقط🫡**\n**استخدم الامر بهذا الشكل** `حروف` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𝙏َِ𝙊َِ𝙈َِّّ ( ٍّالبشمبرمج) ", url=f"https://t.me/DEV_TOM"),
            ]
         ]
     )
  )


@app.on_message(filters.regex("⌔صـراحـه⌔"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/e7bb54b34faadd2c9b199.jpg",
        caption=f"""**نبذه سريعه عن صراحه** : **يتم استخدام هذا الامر لعرض لعبه الصراحه فقط🫡**\n**استخدم الامر بهذا الشكل** `صراحه` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𝙏َِ𝙊َِ𝙈َِّّ ( ٍّالبشمبرمج) ", url=f"https://t.me/DEV_TOM"),
            ]
         ]
     )
  )


@app.on_message(filters.regex("⌔لـو خـيـروك⌔"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/e7bb54b34faadd2c9b199.jpg",
        caption=f"""**نبذه سريعه عن لو خيروك** : **يتم استخدام هذا الامر لعرض لعبه لو خيروك فقط🫡**\n**استخدم الامر بهذا الشكل** `لو خيروك` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𝙏َِ𝙊َِ𝙈َِّّ ( ٍّالبشمبرمج) ", url=f"https://t.me/DEV_TOM"),
            ]
         ]
     )
  )


@app.on_message(filters.regex("⌔تـويـت⌔"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/e7bb54b34faadd2c9b199.jpg",
        caption=f"""**نبذه سريعه عن كت تويت** : **يتم استخدام هذا الامر لعرض لعبه كت تويت فقط🫡**\n**استخدم الامر بهذا الشكل** `كت تويت` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𝙏َِ𝙊َِ𝙈َِّّ ( ٍّالبشمبرمج) ", url=f"https://t.me/DEV_TOM"),
            ]
         ]
     )
  )


@app.on_message(filters.regex("⌔كـتـبـات⌔"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/e7bb54b34faadd2c9b199.jpg",
        caption=f"""**نبذه سريعه عن الكتبات** : **يتم استخدام هذا الامر لعرض الكتبات فقط🫡**\n**استخدم الامر بهذا الشكل** `كتبات` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𝙏َِ𝙊َِ𝙈َِّّ ( ٍّالبشمبرمج) ", url=f"https://t.me/DEV_TOM"),
            ]
         ]
     )
  )


@app.on_message(filters.regex("⌔انـصـحـنـي⌔"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/e7bb54b34faadd2c9b199.jpg",
        caption=f"""**نبذه سريعه عن انصحني** : **يتم استخدام هذا الامر لعرض انصحني فقط🫡**\n**استخدم الامر بهذا الشكل** `انصحني` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𝙏َِ𝙊َِ𝙈َِّّ ( ٍّالبشمبرمج) ", url=f"https://t.me/DEV_TOM"),
            ]
         ]
     )
  )


@app.on_message(filters.regex("⌔يـوتـيـوب⌔"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/e7bb54b34faadd2c9b199.jpg",
        caption=f"""**نبذه سريعه عن تنزيل** : **يتم استخدام هذا الامر لعرض تحميل من اليوتيوب فقط🫡**\n**استخدم الامر بهذا الشكل** `تنزيل` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𝙏َِ𝙊َِ𝙈َِّّ ( ٍّالبشمبرمج) ", url=f"https://t.me/DEV_TOM"),
            ]
         ]
     )
  )


@app.on_message(filters.regex("⌔اذكـار⌔"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/e7bb54b34faadd2c9b199.jpg",
        caption=f"""**نبذه سريعه عن الاذكار** : **يتم استخدام هذا الامر لعرض الاذكار فقط🫡**\n**استخدم الامر بهذا الشكل** `اذكار` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𝙏َِ𝙊َِ𝙈َِّّ ( ٍّالبشمبرمج) ", url=f"https://t.me/DEV_TOM"),
            ]
         ]
     )
  )


@app.on_message(filters.regex("⌔ايــدي⌔"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/e7bb54b34faadd2c9b199.jpg",
        caption=f"""**نبذه سريعه عن الايدي** : **يتم استخدام هذا الامر لعرض الايدي فقط🫡**\n**استخدم الامر بهذا الشكل** `ايدي` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𝙏َِ𝙊َِ𝙈َِّّ ( ٍّالبشمبرمج) ", url=f"https://t.me/DEV_TOM"),
            ]
         ]
     )
  )


@app.on_message(filters.regex("⌔اسـمـي⌔"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/e7bb54b34faadd2c9b199.jpg",
        caption=f"""**نبذه سريعه عن اسمي** : **يتم استخدام هذا الامر لعرض اسمي فقط🫡**\n**استخدم الامر بهذا الشكل** `اسمي` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𝙏َِ𝙊َِ𝙈َِّّ ( ٍّالبشمبرمج) ", url=f"https://t.me/DEV_TOM"),
            ]
         ]
     )
  )


@app.on_message(filters.regex("نبذه عن الكيبورد ⚡"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/e7bb54b34faadd2c9b199.jpg",
        caption=f"""**نبذه سريعه عن** نبذه عن الكيبورد ⚡ **: **ماهو بيتا كيبورد🤔** **هو اصدار اولي قابل لتعديل في اي وقت قابل الاضافة مميزات واضافة جديد في اي وقت بي اختصار قابل لتحديث ولاضافه في اي وقت**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𝙏َِ𝙊َِ𝙈َِّّ ( ٍّالبشمبرمج) ", url=f"https://t.me/DEV_TOM"),
            ]
         ]
     )
  )
  
