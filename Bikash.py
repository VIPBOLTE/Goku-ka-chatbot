from pyrogram import Client, filters, idle
from pyrogram.types import *
from pymongo import MongoClient
from pyrogram import enums
import requests
import random
import os
import re


API_ID = os.environ.get("API_ID", "none") 
API_HASH = os.environ.get("API_HASH", "none") 
BOT_TOKEN = os.environ.get("BOT_TOKEN", "none") 
MONGO_URL = os.environ.get("MONGO_URL", "none")
BOT_IMAGE = os.environ.get("BOT_IMAGE", "none")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "none")
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "none")
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "none")
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "none")


bot = Client(
    "GOKU_CHAT_Bot" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)


async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.get_chat_members(
            chat_id, filter="administrators"
        )
    ]


@bot.on_message(filters.command("start") & filters.private)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_IMAGE}",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
✨ʜᴇʏ ɪ'ᴍ ʙʜᴏᴘᴀʟɪ🥀.\n\n⚡ ᴀᴅᴠᴀɴᴄᴇᴅ ᴄʜᴀᴛ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ. \n\n💫 ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs ❣️\n\n /chatbot - [on|off] ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴜsᴇ ᴏɴʟʏ ɪɴ ɢʀᴏᴜᴘ

┏━━━━━━━━━━━━━━━━━┓
┣❥︎ ♕︎𝐎𝐰𝐧𝐞𝐫♕︎   » [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://t.me/{OWNER_USERNAME})
┣❥︎ 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 ➪ » [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://t.me/{UPDATES_CHANNEL})
┣❥︎ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 ➪ » [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://t.me/{SUPPORT_GROUP})
┣❥︎ 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 ➪ » [✪☠︎︎➳ᴹᴿ᭄ᴳᴼᴷᵁ ᴳᴼᴰ ᴼᶠ ᶜᴸᴬᴺˢᴼᴾ᭄★](https://t.me/Zindagi_hai_tere_nal)
┗━━━━━━━━━━━━━━━━━┛

💞 💞 ᴀᴅᴅ ᴍᴇ » ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ
ᴇɴᴊᴏʏ sᴜᴘᴇʀ ǫᴜᴀʟɪᴛʏ ❥︎ᴄʜᴀᴛ.
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❰ ❤ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✨ ❱", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@bot.on_message(filters.command(["/start", f"start@{BOT_USERNAME}", "/alive", ".alive", "#GOKU", "#Krishna"]) & filters.group)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_IMAGE}",
        caption=f"""✨ʜᴇʏ ɪ'ᴍ ᴀᴅᴠᴀɴᴄᴇᴅ ᴄʜᴀᴛ ʙᴏᴛ.❤️‍🔥 \n\n🪐 ɪ'ᴍ ʙʜᴏᴘᴀʟɪ ғʀᴏᴍ ɪɴᴅɪᴀ 🌹 \n\n🍂 ɪ'ᴍ ᴀʀᴛɪғɪᴄɪᴀʟ ɪɴᴛᴇʟʟɪɢᴇɴᴄᴇ 🌷\n\nᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛᴏ [ʀᴇᴘᴏʀᴛ](https://t.me/{SUPPORT_GROUP})  🥀\n\n[𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/{UPDATES_CHANNEL}) 🌷\n\n /chatbot - [on|off]""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 💥 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐭 𝐆𝐫𝐨𝐮𝐩 💞", url=f"https://t.me/goku_groupz")
                ]
            ]
        ),
    )



@bot.on_message(
    filters.command("chatbot off", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbotofd(client, message):
    vdb = MongoClient(MONGO_URL)    
    v = vdb["vDb"]["v"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
           await is_admins(chat_id)
        ):
           return await message.reply_text(
                "💥 𝐇𝐞𝐲 𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀 𝐀𝐝𝐦𝐢𝐧 💥"
            )
    is_v = v.find_one({"chat_id": message.chat.id})
    if not is_v:
        v.insert_one({"chat_id": message.chat.id})
        await message.reply_text(f"🌷 𝐕 𝐂𝐡𝐚𝐭𝐛𝐨𝐭 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝 🥀!\n\n𝐀𝐧𝐲 𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐓𝐨 [𝐑𝐞𝐩𝐨𝐫𝐭](https://t.me/{SUPPORT_GROUP})  🥀\n\n[𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/{UPDATES_CHANNEL}) 🌷")
    if is_v:
        await message.reply_text(f"🌷𝐕 𝐂𝐡𝐚𝐭𝐛𝐨𝐭 𝐈𝐬 𝐀𝐥𝐫𝐞𝐚𝐝𝐭 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝 🥀!\n\n𝐀𝐧𝐲 𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐓𝐨 [𝐑𝐞𝐩𝐨𝐫𝐭](https://t.me/{SUPPORT_GROUP})  🥀\n\n[𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/{UPDATES_CHANNEL}) 🌷")
    

@bot.on_message(
    filters.command("chatbot on", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatboton(client, message):
    vdb = MongoClient(MONGO_URL)    
    v = vdb["vDb"]["v"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "You are not admin"
            )
    is_v = v.find_one({"chat_id": message.chat.id})
    if not is_v:           
        await message.reply_text(f"💥 𝐕 𝐂𝐡𝐚𝐭𝐛𝐨𝐭 𝐈𝐬 𝐀𝐥𝐫𝐞𝐚𝐝𝐲𝐄𝐧𝐚𝐛𝐥𝐞𝐝🌷!\n\n𝐀𝐧𝐲 𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐓𝐨 [𝐑𝐞𝐩𝐨𝐫𝐭](https://t.me/{SUPPORT_GROUP})  🥀\n\n[𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/{UPDATES_CHANNEL}) 🌷")
    if is_v:
        v.delete_one({"chat_id": message.chat.id})
        await message.reply_text(f"💥 𝐕 𝐂𝐡𝐚𝐭𝐛𝐨𝐭 𝐈𝐬 𝐄𝐧𝐚𝐛𝐥𝐞𝐝 🌷!\n\n𝐀𝐧𝐲 𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐓𝐨 [𝐑𝐞𝐩𝐨𝐫𝐭](https://t.me/{SUPPORT_GROUP})  🥀\n\n[𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/{UPDATES_CHANNEL}) 🌷")
    

@bot.on_message(
    filters.command("chatbot", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.reply_text(f"**🇮🇳 𝐔𝐬𝐚𝐠𝐞 🌷 :**\n/chatbot [on|off] 𝐎𝐧𝐥𝐲 𝐆𝐫𝐨𝐮𝐩 🇮🇳 !\n\n𝐀𝐧𝐲 𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐓𝐨 [𝐑𝐞𝐩𝐨𝐫𝐭](https://t.me/{SUPPORT_GROUP})  🥀\n\n[𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/{UPDATES_CHANNEL}) 🌷")


@bot.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.bot,
)
async def vai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       vdb = MongoClient(MONGO_URL)
       v = vdb["vDb"]["v"] 
       is_v = v.find_one({"chat_id": message.chat.id})
       if not is_v:
           await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       vdb = MongoClient(MONGO_URL)
       v = vdb["vDb"]["v"] 
       is_v = v.find_one({"chat_id": message.chat.id})    
       getme = await bot.get_me()
       bot_id = getme.id                             
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_v:                   
               await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})    
               

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.bot,
)
async def vstickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       vdb = MongoClient(MONGO_URL)
       v = vdb["vDb"]["v"] 
       is_v = v.find_one({"chat_id": message.chat.id})
       if not is_v:
           await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       vdb = MongoClient(MONGO_URL)
       v = vdb["vDb"]["v"] 
       is_v = v.find_one({"chat_id": message.chat.id})
       getme = await bot.get_me()
       bot_id = getme.id
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_v:                    
               await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
               


@bot.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.bot,
)
async def vprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
       K = []  
       is_chat = chatai.find({"word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "sticker":
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
           K = []  
           is_chat = chatai.find({"word": message.text})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
       

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.bot,
)
async def vprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")
       
bot.start()
print("BGT CHAT BOT BOOTED SUCCESSFULLY")
idle()
