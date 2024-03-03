import random
from datetime import datetime

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import IMG, OWNER_USERNAME, STICKER
from SACHINxSANATANI import BOT_NAME, dev
from SACHINxSANATANI.database.chats import add_served_chat
from SACHINxSANATANI.database.users import add_served_user
from SACHINxSANATANI.modules.helpers import PNG_BTN


@dev.on_message(filters.command("ping", prefixes=["+", "/", "-", "?", "$", "&"]))
async def ping(_, message: Message):
    await message.reply_sticker(sticker=random.choice(STICKER))
    start = datetime.now()
    loda = await message.reply_photo(
        photo=random.choice(IMG),
        caption="๏ ᴘɪɴɢ ᴘᴏɴɢ...",
    )
    try:
        await message.delete()
    except:
        pass

    ms = (datetime.now() - start).microseconds / 1000
    await loda.edit_text(
        text=f"**๏ ʜᴇʏ ʙᴀʙʏ..!\n\n๏ {BOT_NAME} ɪs ᴀʟɪᴠᴇ ᴀɴᴅ ᴡᴏʀᴋɪɴɢ ғɪɴᴇ.\n\n๏ ᴘɪɴɢ ᴘᴏɴɢ ➥ `{ms}` ᴍs\n\n๏ ᴍᴀᴅᴇ ʙʏ ➛ [🇸ᴀ ɴ ᴀ ᴛ ᴀ ɴ ɪ ₰](https://t.me/{OWNER_USERNAME}) !**",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )
    if message.chat.type == ChatType.PRIVATE:
        await add_served_user(message.from_user.id)
    else:
        await add_served_chat(message.chat.id)
