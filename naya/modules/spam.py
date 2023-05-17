# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


import asyncio

from pyrogram import Client, enums, filters
from pyrogram.types import Message

from . import *


@bots.on_message(filters.me & filters.command("dspam", cmd))
async def delayspammer(client, message):
    try:
        args = message.text.split(" ", 3)
        delay = float(args[1])
        count = int(args[2])
        if message.reply_to_message:
            msg = client.get_reply_message
        else:
            msg = str(args[3])
    except BaseException:
        return await message.edit(
            f"**Penggunaan :** {cmd}dspam [waktu] [jumlah] [balas pesan]"
        )
    await message.delete()
    try:
        for i in range(count):
            await client.send_message(message.chat.id, msg)
            await asyncio.sleep(delay)
    except Exception as u:
        await client.send_message(message.chat.id, f"**Error :** `{u}`")


@bots.on_message(filters.me & filters.command("spam", cmd))
async def spammer(client, message):
    text = message.text
    if message.reply_to_message:
        if not len(text.split()) >= 2:
            return await message.edit("`Gunakan dalam Format yang Tepat`")
        spam_message = message.reply_to_message
    else:
        if not len(text.split()) >= 3:
            return await message.edit(
                "`Membalas Pesan atau Memberikan beberapa Teks ..`"
            )
        spam_message = text.split(maxsplit=2)[2]
    counter = text.split()[1]
    try:
        counter = int(counter)
        if counter >= 100:
            return await message.edit(
                "`Maksimal jumlah 100, Gunakan bspam untuk jumlah lebih dari 100`"
            )
    except BaseException:
        return await message.edit("`Gunakan dalam Format yang Tepat`")
    await asyncio.wait(
        [client.send_message(message.chat.id, spam_message) for i in range(counter)]
    )
    await message.delete()


@bots.on_message(filters.me & filters.command("bspam", cmd))
async def bigspam(client, message):
    text = message.text
    if message.reply_to_message:
        if not len(text.split()) >= 2:
            return await message.edit(
                "`Gunakan dalam Format yang Tepat` **Contoh** : bspam [jumlah] [kata]"
            )
        spam_message = message.reply_to_message
    else:
        if not len(text.split()) >= 3:
            return await message.edit(
                "`Membalas Pesan atau Memberikan beberapa Teks ..`"
            )
        spam_message = text.split(maxsplit=2)[2]
    counter = text.split()[1]
    try:
        counter = int(counter)
    except BaseException:
        return await message.edit("`Gunakan dalam Format yang Tepat`")
    await asyncio.wait(
        [client.send_message(message.chat.id, spam_message) for i in range(counter)]
    )
    await message.delete()


@bots.on_message(filters.me & filters.command("sspam", cmd))
async def spam_stick(client: Client, message: Message):
    if not message.reply_to_message:
        await edit_or_reply(
            message, "**Reply to a sticker with amount you want to spam**"
        )
        return
    if not message.reply_to_message.sticker:
        await edit_or_reply(
            message, "**Reply to a sticker with amount you want to spam**"
        )
        return
    else:
        i = 0
        times = message.command[1]
        if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            for i in range(int(times)):
                sticker = message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id,
                    sticker,
                )
                await asyncio.sleep(0.10)

        if message.chat.type == enums.ChatType.PRIVATE:
            for i in range(int(times)):
                sticker = message.reply_to_message.sticker.file_id
                await client.send_sticker(message.chat.id, sticker)
                await asyncio.sleep(0.10)


__MODULE__ = "spam"
__HELP__ = f"""
✘ Bantuan Untuk Spam

๏ Perintah: <code>{cmd}dspam</code> [waktu] [jumlah] [balas pesan]
◉ Penjelasan: Untuk melakukan delay spam.

๏ Perintah: <code>{cmd}spam</code> [jumlah] [kata]
◉ Penjelasan: Untuk melakukan spam.

๏ Perintah: <code>{cmd}bspam</code> [jumlah] [kata]
◉ Penjelasan: Untuk melakukan bigspam.

๏ Perintah: <code>{cmd}sspam</code>
◉ Penjelasan: Untuk melakukan spam stiker.
"""
