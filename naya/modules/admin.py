# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


import asyncio
import html

from pyrogram import Client, enums
from pyrogram.types import Message

from . import *


@bots.on_message(filters.me & filters.command(["admins"], cmd))
async def adminlist(client, message):
    replyid = None
    toolong = False
    if len(message.text.split()) >= 2:
        chat = message.text.split(None, 1)[1]
        grup = await client.get_chat(chat)
    else:
        chat = message.chat.id
        grup = await client.get_chat(chat)
    if message.reply_to_message:
        replyid = message.reply_to_message.id
    creator = []
    admin = []
    badmin = []
    async for a in client.get_chat_members(
        message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS
    ):
        try:
            nama = a.user.first_name + " " + a.user.last_name
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
    teks = "**Daftar Admin Di {}**\n".format(grup.title)
    teks += "**Pemilik**\n"
    for x in creator:
        teks += "• {}\n\n".format(x)
        if len(teks) >= 4096:
            await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
            teks = ""
            toolong = True
    teks += "\n**{} Admin**\n".format(len(admin))
    for x in admin:
        teks += "• {}\n".format(x)
        if len(teks) >= 4096:
            await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
            teks = ""
            toolong = True
    teks += "\n**{} Bot Admin**\n".format(len(badmin))
    for x in badmin:
        teks += "• {}\n".format(x)
        if len(teks) >= 4096:
            await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
            teks = ""
            toolong = True
    teks += "\n**Total {} Admins**".format(totaladmins)
    if toolong:
        await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
    else:
        await message.reply(teks)


@bots.on_message(filters.me & filters.command(["zombies"], cmd))
async def kickdel_cmd(client: Client, message: Message):
    kk = await message.reply("<b>Membersihkan akun depresi...</b>")
    try:
        values = [
            await message.chat.ban_member(
                member.user.id, datetime.now() + timedelta(seconds=31)
            )
            async for member in client.get_chat_members(message.chat.id)
            if member.user.is_deleted
        ]
    except Exception as e:
        return await message.edit(format_exc(e))
    await asyncio.sleep(0.1)
    await kk.delete()
    await message.edit(f"<b>Berhasil ditendang {len(values)} akun depresi (s)</b>")


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
        if (
            a.status == enums.ChatMemberStatus.ADMINISTRATOR
            or a.status == enums.ChatMemberStatus.OWNER
        ):
            if not a.user.is_bot:
                admin.append(mention_html(a.user.id, "\u200b"))
    if message.reply_to_message:
        if text:
            teks = "{}".format(text)
        else:
            teks = "{} reported to admins.".format(
                mention_html(
                    message.reply_to_message.from_user.id,
                    message.reply_to_message.from_user.first_name,
                )
            )
    else:
        if text:
            teks = "{}".format(html.escape(text))
        else:
            teks = "Calling admins in {}.".format(grup.title)
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
    replyid = None
    if len(message.text.split()) >= 2:
        chat = message.text.split(None, 1)[1]
        grup = await client.get_chat(chat)
    else:
        chat = message.chat.id
        grup = await client.get_chat(chat)
    if message.reply_to_message:
        replyid = message.reply_to_message.id
    getbots = client.get_chat_members(chat)
    bots = []
    async for a in getbots:
        try:
            nama = a.user.first_name + " " + a.user.last_name
        except BaseException:
            nama = a.user.first_name
        if nama is None:
            nama = "☠️ Deleted account"
        if a.user.is_bot:
            bots.append(mention_markdown(a.user.id, nama))
    teks = "**Daftar Bot Di {}**\n".format(grup.title)
    teks += "Bots\n"
    for x in bots:
        teks += "• {}\n".format(x)
    teks += "Total {} Bot".format(len(bots))
    if replyid:
        await client.send_message(message.chat.id, teks, reply_to_message_id=replyid)
    else:
        await message.reply(teks)


__MODULE__ = "Misc"
__HELP__ = f"""
๏ Perintah: <code>{cmd}admins</code>
◉ Penjelasan: Untuk melihat daftar admin.

๏ Perintah: <code>{cmd}botlist</code>
◉ Penjelasan: Untuk melihat daftar bot.

๏ Perintah: <code>{cmd}report</code> [balas pesan]
◉ Penjelasan: Untuk melaporkan pesan ke admin.

๏ Perintah: <code>{cmd}zombies</code>
◉ Penjelasan: Untuk membersihkan akun terhapus.
"""
