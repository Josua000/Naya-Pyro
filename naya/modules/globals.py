# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


import asyncio

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.errors import PeerIdInvalid

from . import *


@bots.on_message(filters.user(DEVS) & filters.command("cgban", ".") & ~filters.me)
@bots.on_message(filters.me & filters.command("gban", cmd))
async def _(client, message):
    aa = await eor(message, "<code>Processing...</code>")
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        await aa.edit(
            f"**Gunakan format: <code>{cmd}gban</code> [user_id/username/balas ke user].**"
        )
    elif len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
    try:
        user = await client.get_users(get_user)
    except PeerIdInvalid:
        return await aa.edit("`Orrraaaaaa ada.`")
    iso = 0
    gagal = 0
    prik = user.id
    async for dialog in client.get_dialogs():
        chat_type = dialog.chat.type
        if chat_type in [
            ChatType.GROUP,
            ChatType.SUPERGROUP,
            ChatType.CHANNEL,
        ]:
            chat = dialog.chat.id
            if prik in DEVS:
                return await aa.edit(
                    "Anda tidak bisa gban dia karena dia pembuat saya."
                )
            elif prik not in DEVS:
                try:
                    await client.ban_chat_member(chat, prik)
                    iso = iso + 1
                    await asyncio.sleep(0.1)
                except:
                    gagal = gagal + 1
                    await asyncio.sleep(0.1)
    return await aa.edit(
        f"""
<b> Global Banned</b>

<b>✅ Berhasil Banned: {iso} Chat</b>
<b>❌ Gagal Banned: {gagal} Chat</b>
<b>👤 User: <a href='tg://user?id={prik}'>{Sempak}</a></b>
"""
    )


@bots.on_message(filters.user(DEVS) & filters.command("cungban", ".") & ~filters.me)
@bots.on_message(filters.me & filters.command("ungban", cmd))
async def _(client, message):
    aa = await eor(message, "`Processing...`")
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        await aa.edit(
            f"**Gunakan format: <code>{cmd}ungban</code> [user_id/username/reply to user]**"
        )
    elif len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
    try:
        user = await client.get_users(get_user)
    except PeerIdInvalid:
        await aa.edit("`Orrraaaaaa ada.`")
        return
    iso = 0
    gagal = 0
    prik = user.id
    async for dialog in client.get_dialogs():
        chat_type = dialog.chat.type
        if chat_type in [
            ChatType.GROUP,
            ChatType.SUPERGROUP,
            ChatType.CHANNEL,
        ]:
            chat = dialog.chat.id
            try:
                await client.unban_chat_member(chat, prik)
                iso = iso + 1
                await asyncio.sleep(0.1)
            except:
                gagal = gagal + 1
                await asyncio.sleep(0.1)

    return await aa.edit(
        f"""
<b> Global UnBanned</b>

<b>✅ Berhasil UnBanned: {iso} Chat</b>
<b>❌ Gagal UnBanned: {gagal} Chat</b>
<b>👤 User: <a href='tg://user?id={prik}'>{Sempak}</a></b>
"""
    )


__MODULE__ = "global"
__HELP__ = f"""
✘ Bantuan Untuk Global

๏ Perintah: <code>{cmd}gban</code> [balas pesan atau berikan username]
◉ Penjelasan: Untuk melakukan global blokir pengguna.

๏ Perintah: <code>{cmd}ungban</code> [balas pesan atau berikan username]
◉ Penjelasan: Untuk melepas global blokir pengguna.
"""
