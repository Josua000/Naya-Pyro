# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT

import os
from asyncio import sleep
from time import time

from kynaylibs.nan.utils import eor
from pyrogram import Client, enums
from pyrogram.types import Message

from naya import *

flood = {}
profile_photo = "https://telegra.ph//file/94cc3c815a9e063dad4f0.jpg"



@bots.on_message(filters.command(["unblock", "unblck"], cmd) & filters.me)
async def unblock_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    tex = await message.reply_text("`Processing . . .`")
    if not user_id:
        return await message.edit(
            "Berikan username atau reply pesan untuk membuka blokir."
        )
    if user_id == client.me.id:
        return await tex.edit("Ok done ✅.")
    await client.unblock_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await message.edit(f"**Berhasil membuka blokir** {umention}")


@bots.on_message(filters.command(["block", "blok"], cmd) & filters.me)
async def block_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    tex = await message.reply_text("`Processing . . .`")
    if not user_id:
        return await tex.edit_text("Berikan username untuk di blok.")
    if user_id == client.me.id:
        return await tex.edit_text("ok ✅.")
    await client.block_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit_text(f"**Berhasil mem-blokir** {umention}")


@bots.on_message(filters.command(["setname", "stname"], cmd) & filters.me)
async def setname(client, message):
    if message.reply_to_message:
        name = message.reply_to_message.text
    else:
        name = message.text.split(None, 1)[1]
    tex = await message.reply_text("`Processing . . .`")
    if not name:
        return await tex.edit(
            "Berikan text atau balas text untuk diatur sebagai nama anda."
        )
    try:
        await client.update_profile(first_name=name)
        await tex.edit(f"**Berhasil mengganti nama menjadi** `{name}`")
    except Exception as e:
        await tex.edit(f"**ERROR:** `{e}`")


@bots.on_message(filters.command(["setbio", "sbio"], cmd) & filters.me)
async def set_bio(client: Client, message: Message):
    if message.reply_to_message:
        bio = message.reply_to_message.text
    else:
        bio = message.text.split(None, 1)[1]
    tex = await message.reply_text("`Processing . . .`")
    if not bio:
        return await tex.edit(
            "Berikan text atau balas text untuk diatur sebagai nama anda."
        )
    try:
        await client.update_profile(bio=bio)
        await tex.edit(f"**Berhasil mengganti bio menjadi** `{bio}`")
    except Exception as e:
        await tex.edit(f"**ERROR:** `{e}`")


@bots.on_message(filters.command(["setpp", "setpf"], cmd) & filters.me)
async def set_pfp(client, message):
    replied = message.reply_to_message
    if (
        replied
        and replied.media
        and (
            replied.photo_or_video
            or (
                replied.document
                and "image" in replied.document.mime_type
                or "video" in replied.document.mime_type
            )
        )
    ):
        profile_photo = "pfp.jpg"
        await client.download_media(message=replied, file_name=profile_photo)
        await client.set_profile_photo(profile_photo)
        if os.path.exists(profile_photo):
            os.remove(profile_photo)
        await eor(message, "<b>Foto profil berhasil di ganti.</b>")
    else:
        await eor(message, "Balas ke media untuk atur sebagai foto profil")
        await sleep(3)
        await message.delete()


__MODULE__ = "profile"
__HELP__ = f"""
✘ Bantuan Untuk Profile

๏ Perintah: <code>{cmd}block</code> [balas pengguna]
◉ Penjelasan: Untuk blokir pengguna.

๏ Perintah: <code>{cmd}unblock</code> [balas pengguna]
◉ Penjelasan: Untuk membuka blokir pengguna.

๏ Perintah: <code>{cmd}setname</code> [berikan pesan]
◉ Penjelasan: Untuk mengubah nama anda.

๏ Perintah: <code>{cmd}setbio</code> [nama kota]
◉ Penjelasan: Untuk mengubah bio anda.

๏ Perintah: <code>{cmd}setpp</code> [nama kota]
◉ Penjelasan: Untuk mengubah foto profil anda.
"""
