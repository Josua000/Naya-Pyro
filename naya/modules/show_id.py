from pyrogram import filters
from pyrogram.enums import ChatType

from . import *


@bots.on_message(filters.me & filters.command("id", cmd))
async def showid(client, message):
    chat_type = message.chat.type
    if chat_type == ChatType.PRIVATE:
        user_id = message.chat.id
        await eor(
            message,
            f"👤 <b> ID</b> <code>{user_id}</code>",
        )
    if chat_type == ChatType.CHANNEL:
        await eor(
            message,
            f"👤 <b> ID {message.sender_chat.title}:</b> <code>{message.sender_chat.id}</code>",
        )
    elif chat_type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        _id = ""
        _id += f"💬 <b>ID {message.chat.title}:</b> <code>{message.chat.id}</code>\n"
        if message.reply_to_message:
            _id += (
                f"👤 <b> ID {message.reply_to_message.from_user.first_name} Adalah:</b> "
                f"<code>{message.reply_to_message.from_user.id}</code>\n"
            )
            if file_info := get_file_id(message.reply_to_message):
                _id += (
                    f"📂 <b> ID {file_info.message_type}:</b> "
                    f"<code>{file_info.file_id}</code>\n"
                )
        else:
            _id += f"📂 <b> ID {message.from_user.first_name}:</b> <code>{message.from_user.id}</code>\n"
            if file_info := get_file_id(message):
                _id += (
                    f"<b>{file_info.message_type}</b>: "
                    f"<code>{file_info.file_id}</code>\n"
                )
        m = message.reply_to_message or message
        await eor(m, _id)
