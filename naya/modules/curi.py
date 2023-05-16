import os

from pyrogram import *
from pyrogram import filters
from pyrogram.types import *

from . import *

__MODULE__ = "Curi"

__HELP__ = f"""
๏ Perintah: <code>{cmd}curi</code> [balas ke pesan]
◉ Penjelasan: Untuk mengambil pap timer, cek pesan tersimpan.
"""


@bots.on_message(filters.command(["curi"], cmd) & filters.me)
async def pencuri(client, message):
    dia = message.reply_to_message
    if not dia:
        await eor(message, "`Mohon balas ke media.`")
    anjing = dia.caption or None
    await eor(message, "`Processing...`")
    if dia.text:
        await dia.copy("me")
        await message.delete()
    if dia.photo:
        anu = await client.download_media(dia)
        await client.send_photo("me", anu, anjing)
        await message.delete()
        os.remove(anu)
    if dia.video:
        anu = await client.download_media(dia)
        await client.send_video("me", anu, anjing)
        await message.delete()
        os.remove(anu)
    if dia.audio:
        anu = await client.download_media(dia)
        await client.send_audio("me", anu, anjing)
        await message.delete()
        os.remove(anu)
    if dia.voice:
        anu = await client.download_media(dia)
        await client.send_voice("me", anu, anjing)
        await message.delete()
        os.remove(anu)
    if dia.document:
        anu = await client.download_media(dia)
        await client.send_document("me", anu, anjing)
        await message.delete()
        os.remove(anu)
    else:
        await eor(message, "**Sepertinya terjadi kesalahan.**")
