# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport | XtomiX Somplak
# FULL MONGO NIH JING FIX MULTI CLIENT


import asyncio

from pyrogram import Client, enums, filters
from pyrogram.types import Message

from . import *


@bots.on_message(filters.command(["spam", "dspam"], cmd) & filters.me)
async def spam_cmd(client, message):
    if message.command[0] == "spam":
        if message.reply_to_message:
            spam = await eor(message, "`Processing...`")
            try:
                quantity = int(message.text.split(None, 2)[1])
                spam_text = message.text.split(None, 2)[2]
            except Exception as error:
                return await spam.edit(error)
            await asyncio.sleep(1)
            await message.delete()
            await spam.delete()
            for _ in range(quantity):
                await client.send_message(
                    message.chat.id,
                    spam_text,
                    reply_to_message_id=message.reply_to_message.id,
                )
                await asyncio.sleep(0.3)
        elif len(message.command) < 3:
            await eor(message, f"**Gunakan format:\n`{cmd}spam [jumlah] [pesan]`**")
        else:
            spam = await eor(message, "`Processing...`")
            try:
                quantity = int(message.text.split(None, 2)[1])
                spam_text = message.text.split(None, 2)[2]
            except Exception as error:
                return await spam.edit(error)
            await asyncio.sleep(1)
            await message.delete()
            await spam.delete()
            for _ in range(quantity):
                await client.send_message(message.chat.id, spam_text)
                await asyncio.sleep(0.3)
    elif message.command[0] == "dspam":
        if message.reply_to_message:
            if len(message.command) < 3:
                return await eor(
                    message,
                    f"**Gunakan format:\n`{cmd}dspam[jumlah] [waktu delay] [balas pesan]`**",
                )
            spam = await eor(message, "`Processing...`")
            try:
                quantity = int(message.text.split(None, 3)[1])
                delay_msg = int(message.text.split(None, 3)[2])
            except Exception as error:
                return await spam.edit(error)
            await asyncio.sleep(1)
            await message.delete()
            await spam.delete()
            for _ in range(quantity):
                await message.reply_to_message.copy(message.chat.id)
                await asyncio.sleep(delay_msg)
        else:
            if len(message.command) < 4:
                return await eor(
                    message,
                    f"**Gunakan format:\n`{cmd}dspam[jumlah] [waktu delay] [balas pesan]`**",
                )
            spam = await eor(message, "`Processing...`")
            try:
                quantity = int(message.text.split(None, 3)[1])
                delay_msg = int(message.text.split(None, 3)[2])
                spam_text = message.text.split(None, 3)[3]
            except Exception as error:
                return await spam.edit(error)
            await asyncio.sleep(1)
            await message.delete()
            await spam.delete()
            for _ in range(quantity):
                await client.send_message(message.chat.id, spam_text)
                await asyncio.sleep(delay_msg)


@bots.on_message(filters.me & filters.command("bspam", cmd))
async def bigspam(client, message):
    text = message.text
    if message.reply_to_message:
        if len(text.split()) < 2:
            return await message.edit(
                "`Gunakan dalam Format yang Tepat` **Contoh** : bspam [jumlah] [kata]"
            )
        spam_message = message.reply_to_message
    elif len(text.split()) < 3:
        return await message.edit("`Membalas Pesan atau Memberikan beberapa Teks ..`")
    else:
        spam_message = text.split(maxsplit=2)[2]
    counter = text.split()[1]
    try:
        counter = int(counter)
    except BaseException:
        return await message.edit("`Gunakan dalam Format yang Tepat`")
    await asyncio.wait(
        [client.send_message(message.chat.id, spam_message) for _ in range(counter)]
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
        times = message.command[1]
        if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            for _ in range(int(times)):
                sticker = message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id,
                    sticker,
                )
                await asyncio.sleep(0.10)

        if message.chat.type == enums.ChatType.PRIVATE:
            for _ in range(int(times)):
                sticker = message.reply_to_message.sticker.file_id
                await client.send_sticker(message.chat.id, sticker)
                await asyncio.sleep(0.10)


__MODULE__ = "spam"
__HELP__ = f"""
✘ Bantuan Untuk Spam

๏ Perintah: <code>{cmd}dspam</code> [jumlah] [waktu delay] [balas pesan]
◉ Penjelasan: Untuk melakukan delay spam.

๏ Perintah: <code>{cmd}spam</code> [jumlah] [kata]
◉ Penjelasan: Untuk melakukan spam.

๏ Perintah: <code>{cmd}bspam</code> [jumlah] [kata]
◉ Penjelasan: Untuk melakukan bigspam.

๏ Perintah: <code>{cmd}sspam</code>
◉ Penjelasan: Untuk melakukan spam stiker.
"""
