import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4d412495ab546f9062898.jpg",
        caption=f"""**𝐓𝐡𝐢𝐬 𝐈𝐬 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 🥀𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦  𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝗖𝗮𝗻𝗱𝘆𝘅𝐌𝐮𝐬𝐢𝐜 🎧 𝐈𝐧 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 = [𝗖𝗔𝗡𝗗𝗬](https://t.me/C_A_N_D_Y_O_P)

𝐂𝐫𝐞𝐚𝐭𝐨𝐫 :- [ 𝗖𝗔𝗡𝗗𝗬](https://t.me/C_A_N_D_Y_O_P)
𝐒𝐮𝐩𝐩𝐨𝐫𝐭 :- [𝗚𝗥𝗢𝗨𝗣](https://t.me/DOSTO_KI_ZOPDI)
𝗢𝗪𝗡𝗘𝗥 :- [𝗖𝗔𝗡𝗗𝗬 ](https://t.me/C_A_N_D_Y_O_P)
𝐒𝐨𝐮𝐫𝐜𝐞  :- [✨  𝗖𝗹𝗶𝗰𝗸 ☑️ 𝗥𝗲𝗽𝗼 🌍](https://t.me/DOSTO_KI_ZOPDI)
𝗞𝗜𝗧𝗞𝗔𝗧 :- [𝗕𝗔𝗕𝗬](https://t.me/K_I_T_K_A_T)
𝗛𝗡𝗬 :- [𝗝𝗔𝗔𝗡](https://t.me/HNYOP)

𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐀𝐧𝐝 𝐇𝐞𝐥𝐩 𝐓𝐡𝐞𝐧 𝐃𝐦 𝐌𝐲 𝐁𝐨𝐬𝐬 = [𝗖𝗔𝗡𝗗𝗬](https://t.me/C_A_N_D_Y_O_P)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 Jᴏɪɴ Hᴇʀᴇ & Sᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/DOSTO_KI_ZOPDI")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4d412495ab546f9062898.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 Cʟɪᴄᴋ Mᴇ Tᴏ Gᴇᴛ Rᴇᴘᴏ 💞", url=f"https://t.me/DOSTO_KI_ZOPDI")
                ]
            ]
        ),
    )
