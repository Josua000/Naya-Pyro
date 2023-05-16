# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


import asyncio

from pyrogram import enums, filters

from . import *


@bots.on_message(
    filters.group
    & filters.mentioned
    & filters.incoming
    & ~filters.bot
    & ~filters.via_bot
)
async def log_tagged_messages(client, message):
    message.chat.id
    user_id = client.me.id
    botlog_chat_id = await get_botlog(user_id)
    knl = f"📨<b><u>ANDA TELAH DI TAG</u></b>\n<b> • Dari : </b>{message.from_user.mention}"
    knl += f"\n<b> • Grup : </b>{message.chat.title}"
    knl += f"\n<b> • 👀 </b><a href = '{message.link}'>Lihat Pesan</a>"
    knl += f"\n<b> • Message : </b><code>{message.text}</code>"
    await asyncio.sleep(0.5)
    await client.send_message(
        botlog_chat_id,
        knl,
        parse_mode=enums.ParseMode.HTML,
        disable_web_page_preview=True,
    )


@bots.on_message(filters.command("setlog", cmd) & filters.me)
async def set_log(client, message):
    botlog_chat_id = message.chat.id
    user_id = client.me.id
    chat = await client.get_chat(botlog_chat_id)
    if chat.type == "private":
        return await message.reply("Maaf, perintah ini hanya berlaku untuk grup.")
    await set_botlog(user_id, botlog_chat_id)
    await message.reply_text(
        f"**ID Grup Log telah diatur ke `{botlog_chat_id}` untuk grup ini.**"
    )


__MODULE__ = "Logger"
__HELP__ = f"""
๏ Perintah: <code>{cmd}setlog</code>
◉ Penjelasan: Untuk mengaktifkan PMLogger dan TagLogger
"""
