# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT

import random
from asyncio import gather
from random import choice

from pyrogram import enums, filters
from pyrogram.enums import MessagesFilter

from . import *


@bots.on_message(filters.me & filters.command(["asupan"], cmd))
async def asupan(client, message):
    ky = await message.reply("`Mencari asupan... 🔎`")
    await gather(
        ky.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupan.video.file_id
                    async for asupan in client.search_messages(
                        "AsupanNyaSaiki", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )


# WARNING PORNO VIDEO THIS !!!


@bots.on_message(filters.me & filters.command("bokep", cmd))
async def _(client, message):
    if message.chat.id in BL_UBOT:
        return await eor(message, "<b>Maaf perintah ini dilarang di sini</b>")
    y = await eor(message, "<b>🔍 Mencari Video Bokep...</b>")
    try:
        await client.join_chat("https://t.me/+kJJqN5kUQbs1NTVl")
    except:
        pass
    try:
        bokepnya = []
        async for bokep in client.search_messages(
            -1001867672427, filter=MessagesFilter.VIDEO
        ):
            bokepnya.append(bokep)
        video = random.choice(bokepnya)
        await video.copy(
            message.chat.id,
            caption=f"<b>Bokep By <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a></b>",
            reply_to_message_id=message.id,
        )
        await y.delete()
    except Exception:
        await y.edit("<b>Video tidak ditemukan silahkan ulangi beberapa saat lagi</b>")
    if client.me.id == 1898065191:
        return
    await client.leave_chat(-1001867672427)


@bots.on_message(filters.me & filters.command("cewe", cmd))
async def _(client, message):
    y = await eor(message, "<b>🔍 Mencari Ayang...</b>")
    try:
        ayangnya = []
        async for ayang in client.search_messages(
            "@AyangSaiki", filter=MessagesFilter.PHOTO
        ):
            ayangnya.append(ayang)
        photo = random.choice(ayangnya)
        await photo.copy(
            message.chat.id,
            caption=f"<b>Ayang By <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a></b>",
            reply_to_message_id=message.id,
        )
        await y.delete()
    except Exception:
        await y.edit("<b>Ayang tidak ditemukan silahkan ulangi beberapa saat lagi</b>")


@bots.on_message(filters.me & filters.command("cowo", cmd))
async def _(client, message):
    y = await eor(message, "<b>🔍 Mencari Ayang...</b>")
    try:
        ayang2nya = []
        async for ayang2 in client.search_messages(
            "@Ayang2Saiki", filter=MessagesFilter.PHOTO
        ):
            ayang2nya.append(ayang2)
        photo = random.choice(ayang2nya)
        await photo.copy(
            message.chat.id,
            caption=f"<b>Ayang By <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a></b>",
            reply_to_message_id=message.id,
        )
        await y.delete()
    except Exception:
        await y.edit("<b>Ayang tidak ditemukan silahkan ulangi beberapa saat lagi</b>")


@bots.on_message(filters.me & filters.command(["ppcp"], cmd))
async def pcp(client, message):
    darmi = await message.edit("🔎 `Search PPCP...`")
    await message.reply_photo(
        choice(
            [
                ky.photo.file_id
                async for ky in client.search_messages(
                    "ppcpcilik", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Upload by {client.me.mention}",
    )

    await darmi.delete()


@bots.on_message(filters.me & filters.command(["ppcp2"], cmd))
async def cp(client, message):
    dar = await message.edit("🔎 `Search Ppcp 2...`")
    await message.reply_photo(
        choice(
            [
                cot.photo.file_id
                async for cot in client.search_messages(
                    "mentahanppcp", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Upload by {client.me.mention}",
    )

    await dar.delete()


@bots.on_message(filters.me & filters.command(["anime"], cmd))
async def anim(client, message):
    iis = await message.edit("🔎 `Search Anime...`")
    await message.reply_photo(
        choice(
            [
                jir.photo.file_id
                async for jir in client.search_messages(
                    "animehikarixa", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Upload by {client.me.mention}",
    )

    await iis.delete()


@bots.on_message(filters.me & filters.command(["anime2"], cmd))
async def nimek(client, message):
    erna = await message.edit("🔎 `Search Anime...`")
    await message.reply_photo(
        choice(
            [
                tai.photo.file_id
                async for tai in client.search_messages(
                    "Anime_WallpapersHD", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Upload by {client.me.mention}",
    )

    await erna.delete()


@bots.on_message(filters.me & filters.command(["pap"], cmd))
async def pap(client, message):
    kazu = await message.edit("🔎 `Nih PAP Nya...`")
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "mm_kyran", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption="**Buat Kamu..**",
    )

    await kazu.delete()


__MODULE__ = "Asupan"
__HELP__ = f"""
๏ Perintah: <code>{cmd}pap</code>
◉ Penjelasan: Untuk mengirim pap secara random.

๏ Perintah: <code>{cmd}asupan</code>
◉ Penjelasan: Untuk mengirim asupan secara random.

๏ Perintah: <code>{cmd}cowo or cewe</code>
◉ Penjelasan: Untuk mengirim pap cowo atau cewe secara random.

๏ Perintah: <code>{cmd}ppcp or ppcp2</code>
◉ Penjelasan: Untuk mengirim pp couple secara random.

๏ Perintah: <code>{cmd}bokep</code>
◉ Penjelasan: Untuk anda kalo pengen coli.

๏ Perintah: <code>{cmd}anime or anime2</code>
◉ Penjelasan: Untuk Untuk mengirim gambar anime secara random.
"""
