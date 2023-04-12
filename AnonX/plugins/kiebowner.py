import asyncio
import config
from pyrogram import Client, filters
from pyrogram import filters
from strings import get_command
from strings.filters import command
from AnonX import app
from config import OWNER_ID
from AnonX.misc import SUDOERS
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX.misc import SUDOERS



REPLY_MESSAGE = "**👋︙مـرحـبـا بـك عـزيـزي الـمـطـور ♥️**\n**✨︙فــي قـائـمـة التحـكـم بـالـبـوت💞**"

REPLY_MESSAGE_BUTTONS = [
    [
        ("🔻︙قـنـاة الـسـورس︙🔺️"),
    ],
    [
        ("👌︙طـلـب سـورس︙👌"),
    ],
    [
        ("-︙Tom︙-")
    ],
    [
        ("-︙Cristin︙-")
    ],
    [
        ("-︙Zein︙-")
    ],
    [
        ("📥︙الـيـوتـيـوب︙📥")
    ],
    [
        ("🚫︙المحـظـوريـن︙🚫"),
    ],
    [
        ("🥁 ┉ ┉ ┉ ┉ ¦ [⌞ 𝘾𝙍 ⌯ َِ𝙈َِ𝙐َِ𝙎َِ𝙄َِ𝘾 ⌯ ˹🎧˼⁩ ⌝ ¦ ┉ ┉ ┉ ┉ 🥁")
    ],
    [
        ("👮‍♀️︙مـطـوريـنـك︙👮‍♀️"),
        ("🆔️︙ايـديـهـك︙🆔️")
    ],
    [
        ("💡︙جـروبـاتـك النـشـطـه︙💡"),
    ],
    [
        ("🥁 ┉ ┉ ┉ ┉ ¦ [⌞ 𝘾𝙍 ⌯ َِ𝙈َِ𝙐َِ𝙎َِ𝙄َِ𝘾 ⌯ ˹🎧˼⁩ ⌝ ¦ ┉ ┉ ┉ ┉ 🥁")
    ],
    [
        ("⛔︙حـظـر الـجـروبـات︙⛔"),
    ],
    [
        ("🥁 ┉ ┉ ┉ ┉ ¦ [⌞ 𝘾𝙍 ⌯ َِ𝙈َِ𝙐َِ𝙎َِ𝙄َِ𝘾 ⌯ ˹🎧˼⁩ ⌝ ¦ ┉ ┉ ┉ ┉ 🥁")
    ],
    [
        ("🙅‍♂️︙بـدون تـوكـن︙🙅‍♂️"),
    ],
    [
        ("قـفـل الـكـيـبـورد"),
    ]
]

@app.on_message(
    filters.command("start") & filters.private & SUDOERS)
async def crsourceowner(client: Client, message: Message):
    text = REPLY_MESSAGE
    reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    await message.reply(
        text=text,
        reply_markup=reply_markup
    )


@app.on_message(filters.regex("🔻︙قـنـاة الـسـورس︙🔺️"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://t.me/pp_g3",
        caption=f"""لـطـلـب ســورس مـيـوزك خـاص بــك او مــيـزه في ســورس مـيـوزك لا تـتـردد فـي الـتـواصـل مغ المبرمج توم [𝙏َِ𝙊َِ𝙈َِّّ ( ٍّالبشمبرمج)](https://t.me/DEV_TOM)""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𓆩 🔻︙قـنـاة الـسـورس︙🔺️ 𓆪", url=f"https://t.me/pp_g3"),
            ]
         ]
     )
  )


@app.on_message(filters.regex("👌︙طـلـب سـورس︙👌"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://t.me/pp_g3",
        caption=f"""[لـطـلـب ســورس مـيـوزك خـاص بــك او مــيـزه في ســورس مـيـوزك لا تـتـردد فـي الـتـواصـل مـعـي مـن خـلال الـزر فـي الأسـفـل ♬♪](https://t.me/DEV_TOM)""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𓆩🔻︙قـنـاة الـسـورس︙🔺️ 𓆪", url=f"https://t.me/pp_g3"),
            ]
         ]
     )
  )


@app.on_message(filters.regex("☎️︙للتواصل معنآ ♬"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://t.me/S_EG_P",
        caption=f"""[لـطـلـب ســورس مـيـوزك خـاص بــك او مــيـزه في ســورس مـيـوزك لا تـتـردد فـي الـتـواصـل مـعـي مـن خـلال الـزر فـي الأسـفـل ♬♪](https://t.me/DEV_TOM)""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𓆩🔻︙قـنـاة الـسـورس︙🔺️ 𓆪", url=f"https://t.me/pp_g3"),
                InlineKeyboardButton("𓆩👨‍💻︙مطور الـسـورس 𓆪", url=f"https://t.me/DEV_TOM"),
            ]
         ]
     )
  )


@app.on_message(filters.regex("-︙Tom︙-"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://t.me/DEV_TOM",
        caption=f"""[مبرمج ســورس 𝘾𝙍 ♬](https://t.me/DEV_TOM)""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("ᯓ𓆩˹ ََ𝙏َِ𝙊َِ𝙈ِ ،ِّّ⸙⛥َٰ ( ٍّالبشمبرمج)⏤͟͟͞͞𓆃", url=f"https://t.me/DEV_TOM"),
            ]
         ]
     )
  )


@app.on_message(filters.regex("-︙Cristin︙-"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://t.me/dr_criss",
        caption=f"""[صاحبة سورس - 𝘾𝙍 - 🔥](https://t.me/dr_criss)""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𝙲 . 𝚁 . 𝙸 . 𝚂 . 𝚃 . 𝙸 . 𝙽", url=f"https://t.me/dr_criss"),
            ]
         ]
     )
  )


@app.on_message(filters.regex("-︙Zein︙-"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://t.me/devpokemon",
        caption=f"""[مطور في ســورس 𝘾𝙍 ♬](https://t.me/devpokemon)""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("༗𓌹💲 ĐËV PÖĶËMÖŅ 𓌺", url=f"https://t.me/devpokemon"),
            ]
         ]
     )
  )


@app.on_message(filters.regex("لغة البوت 🚩") & filters.private & SUDOERS)
async def italy(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**نبذه سريعه عن لغات البوت** : **يتم استخدام هذا الامر لعرض لغات البوت فقط🫡**\n**استخدم الامر بهذا الشكل** `لغة` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⸥", url=f"https://t.me/pp_g3"),
                ],
            ]
        ),
    )


@app.on_message(filters.regex("📥︙الـيـوتـيـوب︙📥") & filters.private & SUDOERS)
async def italy(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**نبذه سريعه عن تحميل من اليوتيوب** : **يتم استخدام هذا الامر لتحميل بشكل مباشر من اليوتيوب **\n**استخدم الامر بهذا الشكل** `تنزيل + اسم الاغنية` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⸥", url=f"https://t.me/pp_g3"),
                ],
            ]
        ),
    )


@app.on_message(filters.regex("🚫︙المحـظـوريـن︙🚫") & filters.private & filters.private & SUDOERS)
async def italy(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**نبذه سريعه عن قائمه الحظر❌** : **يتم استخدام هذا الامر لعرض من هم المحظورين من تشغيل البوت من قبل المالك او المطورين الذي تم رفعهم🫡**\n**استخدم الامر بهذا الشكل** `قائمه الحظر` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⸥", url=f"https://t.me/pp_g3"),
                ],
            ]
        ),
    )


@app.on_message(filters.regex("👮‍♀️︙مـطـوريـنـك︙👮‍♀️") & filters.private & filters.private & SUDOERS)
async def italy(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**نبذه سريعه عن قائمة المطورين👨‍💻** : **يتم استخدام هذا الامر لعرض من هم الذي تم ترقيتهم من قبل مالك البوت🫡**\n**استخدم الامر بهذا الشكل** `قائمة الثانويين` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⸥", url=f"https://t.me/pp_g3"),
                ],
            ]
        ),
    )


@app.on_message(filters.regex("🆔️︙ايـديـهـك︙🆔️") & filters.private & SUDOERS)
async def italy(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**نبذه سريعه عن الايدي** : **يتم استخدام هذا الامر لعرض الايدي بصورة من طلب الامر لماذا تم عمل هذا الميزه في خاص البوت بدل من المجموعه ؟! : السبب ان بعض الاشخاص الفاشلين يضعون صور اباحيه ويقوم بكتبه امر ايدي عندم يظهر البوت الصوره يقوم بعمل ابلاغ في المجموعه حتي يقوم تليجرام بأغلاق المجموعه لذلك تم نقل الامر في الخاص ووضع امر ايدي ايضا بدون صوره في المجموعه🫡**\n**استخدم الامر بهذا الشكل** `ايدي` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⸥", url=f"https://t.me/pp_g3"),
                ],
            ]
        ),
    )


@app.on_message(filters.regex("💡︙جـروبـاتـك النـشـطـه︙💡") & filters.private & SUDOERS)
async def italy(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**نبذه سريعه عن 💡︙جـروبـاتـك النـشـطـه︙💡 : **يتم استخدام هذا الامر لعرض من يقوم بتشغيل البوت الان في المحادثه الصوتية🫡**\n**استخدم الامر بهذا الشكل** `اونلاين` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⸥", url=f"https://t.me/pp_g3"),
                ],
            ]
        ),
    )


@app.on_message(filters.regex("⛔︙حـظـر الـجـروبـات︙⛔") & filters.private & SUDOERS)
async def italy(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**نبذه سريعه عن حظر جـروب**🔒❌ : **هذا الامر يستخدم لحظر الجروب من التشغيل عن طريق اليوزر او الايدي🫡**\n**استخدم الامر بهذا الشكل** `blacklistchat` **اضغط علي الامر لنسخ والاستخدام واتبع التعليمات**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⸥", url=f"https://t.me/pp_g3"),
                ],
            ]
        ),
    )


@app.on_message(filters.regex("༺┉⊶﴿♡  𝘾𝙍 ĶËŸBÖÄŖĐ ♡﴾⊷┉༻") & filters.private & SUDOERS)
async def italy(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**نبذه سريعه عن** 𝘾𝙍 ĶËŸBÖÄŖĐ **: **ماهو بيتا كيبورد🤔** **هو اصدار اولي قابل لتعديل في اي وقت قابل الاضافة مميزات واضافة جديد في اي وقت بي اختصار قابل لتحديث ولاضافه في اي وقت**🫡""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⸥", url=f"https://t.me/pp_g3"),
                ],
            ]
        ),
    )


@app.on_message(filters.regex("🙅‍♂️︙بـدون تـوكـن︙🙅‍♂️") & filters.private & SUDOERS)
async def italy(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**نبذه سريعه عن 🙅‍♂️︙بـدون تـوكـن︙🙅‍♂️ **: **هذا الامر يستخدم لجلب معلومات التنصيب بلكامل من علي السيرفر و GitHub لاكن للحفاظ علي سلامتك قمنا بمنع اي شخص من كتابة هذا الامر فقط مطور السورس هو وحده من يستطيع جلب معلومات التنصيب بلكامل تأكد ان لا احد يستطيع جلب معلومات التنصيب الخاص بك ابدا🫡**\n**استخدم الامر بهذا الشكل** `config` **اضغط علي الامر لنسخ والاستخدام واتبع التعليمات**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⸥", url=f"https://t.me/pp_g3"),
                ],
            ]
        ),
    )


@app.on_callback_query(filters.regex("قـفـل الـكـيـبـورد") & filters.private & SUDOERS)
async def italy(_, query: CallbackQuery):
   await callback_query.edit_message_caption(caption =f"""**♬ تــم حــذف الــڪــيــبــورد .**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⸥", url=f"https://t.me/pp_g3"),
               ],
            ]
        ),
    )

