# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT

import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from . import *


@bots.on_message(filters.me & filters.group & filters.command("jamet", cmd))
async def ngejamet(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await eor(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await eor(message, "**WOII**")
    await asyncio.sleep(1.5)
    await xx.edit("**JAMET**")
    await asyncio.sleep(1.5)
    await xx.edit("**CUMA MAU BILANG**")
    await asyncio.sleep(1.5)
    await xx.edit("**GAUSAH SO ASIK**")
    await asyncio.sleep(1.5)
    await xx.edit("**EMANG KENAL?**")
    await asyncio.sleep(1.5)
    await xx.edit("**GAUSAH REPLY**")
    await asyncio.sleep(1.5)
    await xx.edit("**KITA BUKAN KAWAN**")
    await asyncio.sleep(1.5)
    await xx.edit("**GASUKA PC ANJING**")
    await asyncio.sleep(1.5)
    await xx.edit("**BOCAH KAMPUNG**")
    await asyncio.sleep(1.5)
    await xx.edit("**MENTAL TEMPE**")
    await asyncio.sleep(1.5)
    await xx.edit("**LEMBEK NGENTOT🔥**")


@bots.on_message(filters.me & filters.group & filters.command("ywc", cmd))
async def ywc(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "ok sama sama",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@bots.on_message(filters.me & filters.group & filters.command("pp", cmd))
async def toxicpp(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await eor(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "PASANG PP DULU GOBLOK,BIAR ORANG-ORANG PADA TAU BETAPA HINA NYA MUKA LU 😆",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@bots.on_message(filters.me & filters.group & filters.command("dp", cmd))
async def toxicdp(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await eor(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "MUKA LU HINA, GAUSAH SOK KERAS YA ANJENGG!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@bots.on_message(filters.me & filters.group & filters.command("so", cmd))
async def toxicso(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await eor(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "GAUSAH SOKAB SAMA GUA GOBLOK, LU BABU GA LEVEL!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@bots.on_message(filters.me & filters.group & filters.command("nb", cmd))
async def toxicnb(client: Client, message: Message):
    user_id = await extract_user(message)
    if message.chat.id in BL_GCAST:
        return await eor(message, "**Perintah ini Dilarang digunakan di Group ini**")
    if user_id in DEVS:
        return await eor(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "MAEN BOT MULU ALAY NGENTOTT, KESANNYA NORAK GOBLOK!!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@bots.on_message(filters.me & filters.group & filters.command("met", cmd))
async def toxicmet(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await eor(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "NAMANYA JUGA JAMET CAPER SANA SINI BUAT CARI NAMA",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@bots.on_message(filters.me & filters.group & filters.command("war", cmd))
async def toxicwer(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await eor(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "WAR WAR PALAK BAPAK KAU WAR, SOK KERAS BANGET GOBLOK, DI TONGKRONGAN JADI BABU, DI TELE SOK JAGOAN.",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@bots.on_message(filters.me & filters.group & filters.command("wartai", cmd))
async def toxicwartai(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await eor(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "WAR WAR TAI ANJING, KETRIGGER MINTA SHARELOK LU KIRA MAU COD-AN GOBLOK, BACOTAN LU AJA KGA ADA KERAS KERASNYA GOBLOK",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@bots.on_message(filters.me & filters.group & filters.command("kismin", cmd))
async def toxickismin(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await eor(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "CUIHHHH, MAKAN AJA MASIH NGEMIS LO GOBLOK, JANGAN SO NINGGI YA KONTOL GA KEREN LU KEK GITU GOBLOK!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@bots.on_message(filters.me & filters.group & filters.command("ded", cmd))
async def toxicded(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await eor(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "MATI AJA LU GOBLOK, GAGUNA LU HIDUP DI BUMI",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@bots.on_message(filters.me & filters.group & filters.command("sokab", cmd))
async def toxicsokab(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await eor(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "SOKAB BET LU GOBLOK, KAGA ADA ISTILAH NYA BAWAHAN TEMENAN AMA BOS!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@bots.on_message(filters.me & filters.group & filters.command("gembel", cmd))
async def toxicgembel(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await eor(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "MUKA BAPAK LU KEK KELAPA SAWIT ANJING, GA USAH NGATAIN ORANG, MUKA LU AJA KEK GEMBEL TEXAS GOBLOK!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@bots.on_message(filters.me & filters.group & filters.command("cuih", cmd))
async def toxiccuih(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await eor(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "GAK KEREN LO KEK BEGITU GOBLOK, KELUARGA LU BAWA SINI GUA LUDAHIN SATU-SATU. CUIHH!!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@bots.on_message(filters.me & filters.group & filters.command("dih", cmd))
async def toxicdih(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await eor(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "DIHHH NAJISS ANAK HARAM LO GOBLOK, JANGAN BELAGU DIMARI KAGA KEREN LU KEK BGITU TOLOL!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@bots.on_message(filters.me & filters.group & filters.command("gc", cmd))
async def toxicgcs(client: Client, message: Message):
    user_id = await extract_user(message)
    if message.chat.id in BL_GCAST:
        return await eor(message, "**Perintah ini Dilarang digunakan di Group ini**")
    if user_id in DEVS:
        return await eor(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "GC SAMPAH KAYA GINI, BUBARIN AJA GOBLOK!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@bots.on_message(filters.me & filters.group & filters.command("skb", cmd))
async def toxicskb(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await eor(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "EMANG KITA KENAL? KAGA GOBLOK SOKAB BANGET LU GOBLOK",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@bots.on_message(filters.me & filters.group & filters.command("virtual", cmd))
async def toxicvirtual(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await eor(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await eor(message, "**OOOO**")
    await asyncio.sleep(1.5)
    await xx.edit("**INI YANG VIRTUAL**")
    await asyncio.sleep(1.5)
    await xx.edit("**YANG KATANYA SAYANG BANGET**")
    await asyncio.sleep(1.5)
    await xx.edit("**TAPI TETEP AJA DI TINGGAL**")
    await asyncio.sleep(1.5)
    await xx.edit("**NI INGET**")
    await asyncio.sleep(1.5)
    await xx.edit("**TANGANNYA AJA GA BISA DI PEGANG**")
    await asyncio.sleep(1.5)
    await xx.edit("**APALAGI OMONGANNYA**")
    await asyncio.sleep(1.5)
    await xx.edit("**BHAHAHAHA**")
    await asyncio.sleep(1.5)
    await xx.edit("**KASIAN MANA MASIH MUDA**")


__MODULE__ = "toxic"
__HELP__ = f"""
✘ Bantuan Untuk Toxic

๏ Perintah: <code>{cmd}jamet or pp</code>
◉ Penjelasan: Coba sendiri.

๏ Perintah: <code>{cmd}dp or so</code>
◉ Penjelasan: Coba sendiri.

๏ Perintah: <code>{cmd}nb or skb</code>
◉ Penjelasan: Coba sendiri.

๏ Perintah: <code>{cmd}met or war</code>
◉ Penjelasan: Coba sendiri.

๏ Perintah: <code>{cmd}wartai or kismin</code>
◉ Penjelasan: Coba sendiri.

๏ Perintah: <code>{cmd}ded or sokab</code>
◉ Penjelasan: Coba sendiri.

๏ Perintah: <code>{cmd}gembel or cuih</code>
◉ Penjelasan: Coba sendiri.

๏ Perintah: <code>{cmd}dih or gc</code>
◉ Penjelasan: Coba sendiri.
"""
