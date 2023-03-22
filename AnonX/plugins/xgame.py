import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from typing import Union
from AnonX import app
import re
import sys

GAME_MESSAGE = "⩹━★⊷━⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺\n\n★¦ مرحبا بك عزيزي:\n★¦في قسم العاب cr\n\n⩹━★⊷━⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺"
GAME_BUTTONS = [
    [ 
        InlineKeyboardButton ('★¦العاب 3D', callback_data= 'GAME1'),
        InlineKeyboardButton ('cr cr', callback_data= 'GAME2'),
        ],[
        InlineKeyboardButton ('⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⚡️', url =f"https://t.me/pp_g3")              
                 ],[
                InlineKeyboardButton(
                        "◁", callback_data="close"),
               ],
          ]
    

nmla = []

@app.on_message(command("رفع نمله"))
async def rf3nmla(client, message):
  if not message.reply_to_message.from_user.mention in nmla:
    nmla.append(message.reply_to_message.from_user.mention)
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n نمله 😂♥️")


@app.on_message(command("تنزيل نمله"))
async def tnzelnmla(client, message):
  if message.reply_to_message.from_user.mention in nmla:
    nmla.remove(message.reply_to_message.from_user.mention)
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n نمله 😂♥️")


@app.on_message(command("المرفوعين نمل"))
async def nml(client, message):
  nq = ""
  for n in nmla:
      nq += n + "\n"
  await message.reply_text(nq)





@app.on_message(command("رفع صرصار"))
async def rf3srsar(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n صرصار 😂♥️")


@app.on_message(command("تنزيل صرصار"))
async def tnzelsrar(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n صرصار 😂♥️")


@app.on_message(command("رفع رقاصه"))
async def yasooo(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n رقاصه حد يرمي فلوس عليها 😂💃")


@app.on_message(command("تنزيل رقاصه"))
async def yaso(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n رقاصه تابت😂😔")
  
  
@app.on_message(command("رفع متناك"))
async def bjoiuyjk(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n متناك حد يركبو 😂♥️")


@app.on_message(command("تنزيل متناك"))
async def kamal(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n متناك اعرث تاب 😂♥️")
  
  
@app.on_message(command("رفع نجس"))
async def fdsa(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n نجس بنجاح  😂♥️")


@app.on_message(command("تنزيل نجس"))
async def kophvc(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n النجس استحمي 😂♥️")
  
  
@app.on_message(command("رفع عره"))
async def roky(client, message):
  await message.reply_text(f"تم رفع العض\n│ \n└ʙʏو : {message.reply_to_message.from_user.mention}\n\n عره عالمجتمع 😂♥️")


@app.on_message(command("تنزيل عره"))
async def zerso(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n عره خلاص 😂♥️")
  
  
@app.on_message(command("رفع بقره"))
async def vvvtyy(client, message):
  await message.reply_text(f"تم رفع العض\n│ \n└ʙʏو : {message.reply_to_message.from_user.mention}\n\n بقا بقر حديحلبو 🐄🤭")


@app.on_message(command("تنزيل بقره"))
async def tttryuh(client, message):
  await message.reply_text(f"تم تنزيل العض\n│ \n└ʙʏو : {message.reply_to_message.from_user.mention}\n\n خلاص خلص لبن 😂")
  
  
@app.on_message(command("رفع قرد"))
async def uiipppl(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n قرد حد يديلو موزه 😂🐒")


@app.on_message(command("تنزيل قرد"))
async def bjhupq(client, message):
  await message.reply_text(f"تم تنزيل العض\n│ \n└ʙʏو : {message.reply_to_message.from_user.mention}\n\n القرد بقا انسان🙊🧍")
  
  
@app.on_message(command("رفع قلبي"))
async def pooiejh(client, message):
  await message.reply_text(f"تم رفع العض\n│ \n└ʙʏو : {message.reply_to_message.from_user.mention}\n\n خلاص بقيت قلبو 😂♥️")


@app.on_message(command("تنزيل قلبي"))
async def ttrqew(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\nمبقتش قلبوو 😭💔")
  
  
@app.on_message(command("رفع خدام"))
async def qyui(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n خدام تع خدم ع البار    😂🤓")


@app.on_message(command("تنزيل خدام"))
async def klhj(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n الخدام ساب الشغل  😢🚶")
  
  
@app.on_message(command("رفع معرص"))
async def wqew(client, message):
  await message.reply_text(f"تم رفع العض\n│ \n└ʙʏو : {message.reply_to_message.from_user.mention}\n\n معرص البار  😂🤓")


@app.on_message(command("تنزيل معرص"))
async def ohho(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n المعرص بقا راجل   😂🧔")
  
  
@app.on_message(command("رفع ارمله"))
async def drsss(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n  بقيتي ارمله وجوزك مات 🥹")


@app.on_message(command("تنزيل ارمله"))
async def gkvdr(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n خلاث متبقيش قموصه جوزك عايش اهو 😂🫶🏻")
  
  
@app.on_message(command("رفع مزه"))
async def cgfyu6f(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n يمزه خدي بالك من نفسك 🥹❤️")


@app.on_message(command("تنزيل مزه"))
async def hhhhug(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n انتي صدقتي انك مزه ولا اي انا كنت بطبل 😂😝")
  
  
@app.on_message(command("رفع ابني"))
async def cbky(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n  بقيت ابنو وكل حياتو🥹🖤")


@app.on_message(command("تنزيل ابني"))
async def ccgy(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n حتي عيلتك مش طيقاك ورموك في الشارع ")
  
  
@app.on_message(command("رفع خاينه"))
async def mkloo(client, message):
  await message.reply_text(f"تم رفع العض\n│ \n└ʙʏو : {message.reply_to_message.from_user.mention}\n\n  ي خاينه ي مهزأه ")


@app.on_message(command("تنزيل خاينه"))
async def fkijbh(client, message):
  await message.reply_text(f"تم تنزيل العض\n│ \n└ʙʏو : {message.reply_to_message.from_user.mention}\n\n مين الاهبل للي كان مفكر القمر دا ممكن يبقي خاين 🥹🥹💕")  
  
  
@app.on_message(command("رفع بنتي"))
async def yuhhss(client, message):
  await message.reply_text(f"تم رفع العض\n│ \n└ʙʏو : {message.reply_to_message.from_user.mention}\n\n بقيتي بنتي وحته من قلبي 🥹❤️❤️❤️")


@app.on_message(command("تنزيل بنتي"))
async def hloih(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\nكنت بهزر انا مخلفتش لسه🤡😂  ")  
  
  
@app.on_message(command("رفع خاين"))
async def kloss(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n خنتها كام مره قول متتكسفش يخاين")


@app.on_message(command("تنزيل خاين"))
async def fiihug(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n ايدا طلع سوء تفاهم انت اشرف من الشرف يسالك😂❤️")
  
  
@app.on_message(command("رفع خول"))
async def dadr(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n 😂 خول طول عمرك مش اول مره")


@app.on_message(command("تنزيل خول"))
async def hjj7gv(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n  اهو يعم نزلتك 🙂💕")
  
  
@app.on_message(command("رفع حمار"))
async def cgfyu6f(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n خلاص بقت حمار رسمي نظمي😹")


@app.on_message(command("تنزيل حمار"))
async def cxxv(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n خلاث يعم كنا بنهزر معاك متبقاش قفوش 😂😝")
  
  



@app.on_message(command("رفع غبي"))
async def polkij(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n غبي و هتفضل غبي😹🤞")


@app.on_message(command("تنزيل غبي"))
async def nbvcc(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n غبي و بقي بيفهم😹🫶")
  
  
@app.on_message(command("رفع مراتي"))
async def ttttuhyp(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n مراتك خد و عملو واحد😹😽")


@app.on_message(command("تنزيل مراتي"))
async def xxxxt(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n طلقتها شوف غيرها 😂😝")  
  
  
@app.on_message(command("رفع زبال"))
async def oooph(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n زبال تع  نضف الجروب😹")


@app.on_message(command("تنزيل زبال"))
async def zzzas(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n زبال تعب و استقال 😂😝")  
  
  
@app.on_message(command("رفع خدامه"))
async def ggggop(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n خدامه تع اغسلي رجلي 😹🤞")


@app.on_message(command("تنزيل خدامه"))
async def vvvuu(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\nخدامه نزلت اجازه😹🫶")  
  
  
@app.on_message(command("رفع كلبه"))
async def mmmuy(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n كلبه خدي عضمه😹🤞")


@app.on_message(command("تنزيل كلبه"))
async def dfrewq(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n خلاث كلبه تحولت الانسان😿😹")  
  
  
@app.on_message(command("رفع طيز"))
async def ssoss(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n طيز و كبيره كمان😹🤞")


@app.on_message(command("تنزيل طيز"))
async def nobo(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n طيز متزعلش نزلتك😹🫶")  
  
  
@app.on_message(command("رفع حرامي"))
async def llok(client, message):
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n حرامي وهبلغ عنه😹🚓")


@app.on_message(command("تنزيل حرامي"))
async def kaompj(client, message):
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n حرامي ربنا تاب عليه😂😔")
  

@app.on_message(
    command(["الالعاب","العاب"])
    & ~filters.edited
)
async def zohary(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/e7bb54b34faadd2c9b199.jpg",
        caption= GAME_MESSAGE,
        reply_markup=InlineKeyboardMarkup(GAME_BUTTONS)
    )  
@app.on_callback_query()
async def callback_query(client, CallbackQuery):
          if CallbackQuery.data == "GAME1":
            
             GAME1_MESSAGE = "⩹━★⊷━⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺\n\nمرحبا بك في قسم العاب cr 3D\n\n⩹━★⊷━⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺"

             GAME1_BUTTONS = [
                 [
                    InlineKeyboardButton(
                        "°فلابي بيرد°", url=f"http://t.me/awesomebot?game=FlappyBird"), 
                    InlineKeyboardButton (
                        "°تبديل النجوم°", url=f"http://t.me/gamee?game=Switchy"),
                ],[
                    InlineKeyboardButton (
                        "°موتسيكلات°" , url=f"http://t.me/gamee?game=motofx"),
                    InlineKeyboardButton (
                        "°اطلاق النار°" , url=f"http://t.me/gamee?game=NeonBlaster"),
                ],[
                    InlineKeyboardButton (
                        "°كرة القدم°" , url=f"http://t.me/gamee?game=Footballstar"),
                    InlineKeyboardButton (
                        "°تجميع الالوان°" , url=f"http://t.me/awesomebot?game=Hextris"),
                ],[        
                    InlineKeyboardButton (
                        "°المجوهرات°" , url=f"http://t.me/gamee?game=DiamondRows"),
                    InlineKeyboardButton (
                        "°ركل الكرة°" , url=f"http://t.me/gamee?game=KeepitUP"),
                ],[        
                    InlineKeyboardButton (
                        "°بطولة السحق°" , url=f"http://t.me/gamee?game=SmashRoyale"),
                    InlineKeyboardButton (
                        "°2048°" , url=f"http://t.me/awesomebot?game=g2048"),
                ],[        
                    InlineKeyboardButton (
                        "°كرة السلة°" , url=f"http://t.me/gamee?game=BasketBoy"),
                    InlineKeyboardButton (
                        "°القط المجنون°" , url=f"http://t.me/gamee?game=CrazyCat"),
                ],[
                    InlineKeyboardButton (
                        "◁" , callback_data= 'GAME')
                  ],
             ]
             await CallbackQuery.edit_message_text( 
                 GAME1_MESSAGE ,
                 reply_markup = InlineKeyboardMarkup(GAME1_BUTTONS) 
              )
          elif CallbackQuery.data == "GAME":
               
               RETURN_GAME = "⩹━★⊷━⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺\n\n★¦مرحبا بك في قسم العاب cr\n★¦اختار ما تشاء من الالعاب مسليه وستمتع بها\n\n⩹━★⊷━⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺" 

               RETURN_BUTTON = [
                    [ 
                      InlineKeyboardButton ('★¦العاب 3D', callback_data= 'GAME1'),
                      InlineKeyboardButton ('★¦العاب cr', callback_data= 'GAME2')
                      ],[
        InlineKeyboardButton ('⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⚡️', url =f"https://t.me/pp_g3")              
                 ],[
                InlineKeyboardButton(
                        "◁", callback_data="close"),
               ],
          ]
     
               await CallbackQuery.edit_message_text( 
                 RETURN_GAME ,
                 reply_markup = InlineKeyboardMarkup(RETURN_BUTTON) 
                    )
          elif CallbackQuery.data == "GAME2":
               
               SOURCE_GAME = "⩹━★⊷━⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺\n\n★¦العاب cr\n★¦كت\n★¦تويت\n★¦اسال\n★¦اصراحه\n\n⩹━★⊷━⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺." 

               SORGAM_BUTTON = [
                    [ 
                      InlineKeyboardButton ('⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⚡️', url =f"https://t.me/pp_g3")
                      ],[
                         InlineKeyboardButton ('◁', callback_data= 'GAME')
                    ]
               ]    
               await CallbackQuery.edit_message_text( 
                 SOURCE_GAME ,
                 reply_markup = InlineKeyboardMarkup(SORGAM_BUTTON) 
                    )
    
