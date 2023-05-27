# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


import html

from pyrogram import Client, enums
from pyrogram.types import Message

from . import *


@bots.on_message(filters.me & filters.command(["admins"], cmd))
async def adminlist(client, message):
    toolong = False
    if len(message.text.split()) >= 2:
        chat = message.text.split(None, 1)[1]
    else:
        chat = message.chat.id
    grup = await client.get_chat(chat)
    replyid = message.reply_to_message.id if message.reply_to_message else None
    creator = []
    admin = []
    badmin = []
    async for a in client.get_chat_members(
        message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS
    ):
        try:
            nama = f"{a.user.first_name} {a.user.last_name}"
        except BaseException:
            nama = a.user.first_name
        if nama is None:
            nama = "☠️ Deleted account"
        if a.status == enums.ChatMemberStatus.ADMINISTRATOR:
            if a.user.is_bot:
                badmin.append(mention_markdown(a.user.id, nama))
            else:
                admin.append(mention_markdown(a.user.id, nama))
        elif a.status == enums.ChatMemberStatus.OWNER:
            creator.append(mention_markdown(a.user.id, nama))
    admin.sort()
    badmin.sort()
    totaladmins = len(creator) + len(admin) + len(badmin)
    teks = f"**Daftar Admin Di {grup.title}**\n" + "**Pemilik**\n"
    for x in creator:
        teks += f"• {x}\n\n"
        if len(teks) >= 4096:
            await eor(message, message.chat.id, teks, reply_to_message_id=replyid)
            teks = ""
            toolong = True
    teks += f"\n**{len(admin)} Admin**\n"
    for x in admin:
        teks += f"• {x}\n"
        if len(teks) >= 4096:
            await eor(message, message.chat.id, teks, reply_to_message_id=replyid)
            teks = ""
            toolong = True
    teks += f"\n**{len(badmin)} Bot Admin**\n"
    for x in badmin:
        teks += f"• {x}\n"
        if len(teks) >= 4096:
            await eor(message, message.chat.id, teks, reply_to_message_id=replyid)
            teks = ""
            toolong = True
    teks += f"\n**Total {totaladmins} Admins**"
    if toolong:
        await eor(message, message.chat.id, teks, reply_to_message_id=replyid)
    else:
        await eor(message, teks)


@bots.on_message(filters.me & filters.command(["report"], cmd))
async def report_admin(client: Client, message: Message):
    await message.delete()
    if len(message.text.split()) >= 2:
        text = message.text.split(None, 1)[1]
    else:
        text = None
    grup = await client.get_chat(message.chat.id)
    admin = []
    async for a in client.get_chat_members(
        message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS
    ):
        if a.status in [
            enums.ChatMemberStatus.ADMINISTRATOR,
            enums.ChatMemberStatus.OWNER,
        ]:
            if not a.user.is_bot:
                admin.append(mention_html(a.user.id, "\u200b"))
    if message.reply_to_message:
        teks = (
            f"{text}"
            if text
            else f"{mention_html(message.reply_to_message.from_user.id, message.reply_to_message.from_user.first_name)} reported to admins."
        )
    else:
        teks = f"{html.escape(text)}" if text else f"Calling admins in {grup.title}."
    teks += "".join(admin)
    if message.reply_to_message:
        await client.send_message(
            message.chat.id,
            teks,
            reply_to_message_id=message.reply_to_message.id,
            parse_mode=enums.ParseMode.HTML,
        )
    else:
        await client.send_message(
            message.chat.id, teks, parse_mode=enums.ParseMode.HTML
        )


@bots.on_message(filters.me & filters.command(["bots"], cmd))
async def get_list_bots(client: Client, message: Message):
    if len(message.text.split()) >= 2:
        chat = message.text.split(None, 1)[1]
    else:
        chat = message.chat.id
    grup = await client.get_chat(chat)
    replyid = message.reply_to_message.id if message.reply_to_message else None
    getbots = client.get_chat_members(chat)
    bots = []
    async for a in getbots:
        try:
            nama = f"{a.user.first_name} {a.user.last_name}"
        except BaseException:
            nama = a.user.first_name
        if nama is None:
            nama = "☠️ Deleted account"
        if a.user.is_bot:
            bots.append(mention_markdown(a.user.id, nama))
    teks = f"**Daftar Bot Di {grup.title}**\n" + "Bots\n"
    for x in bots:
        teks += f"• {x}\n"
    teks += f"Total {len(bots)} Bot"
    if replyid:
        await client.send_message(message.chat.id, teks, reply_to_message_id=replyid)
    else:
        await eor(message, teks)


__MODULE__ = "chats"
__HELP__ = f"""
✘ Bantuan Untuk Chat

๏ Perintah: <code>{cmd}admins</code>
◉ Penjelasan: Untuk melihat daftar admin.

๏ Perintah: <code>{cmd}botlist</code>
◉ Penjelasan: Untuk melihat daftar bot.

๏ Perintah: <code>{cmd}report</code> [balas pesan]
◉ Penjelasan: Untuk melaporkan pesan ke admin.
"""
