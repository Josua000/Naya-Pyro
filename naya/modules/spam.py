"""
CREDITS TOMAY
"""


import asyncio

from pyrogram import filters

from . import *

__MODULE__ = "Spam"
__HELP__ = f"""
๏ Perintah: <code>{cmd}spam</code> [number_messages - message_text]
◉ Penjelasan: Untuk spam pesan.

๏ Perintah: <code>{cmd}spam</code> [reply_user - number_messages - message_text]
◉ Penjelasan: Untuk spam pesan ke user yang di reply.
"""


@bots.on_message(filters.me & filters.command("spam", cmd))
async def _(client, message):
    if message.reply_to_message:
        spam = await eor(message, "Processing...")
        reply_id = message.reply_to_message.id
        quantity = int(message.text.split(None, 2)[1])
        spam_text = message.text.split(None, 2)[2]
        await asyncio.sleep(1)
        await message.delete()
        await spam.delete()
        for i in range(quantity):
            await client.send_message(
                message.chat.id, spam_text, reply_to_message_id=reply_id
            )
            await asyncio.sleep(0.1)
    else:
        if len(message.text.split()) < 2:
            await eor(message, "Gunakan format:\n spam jumlah spam, text spam...")
        else:
            spam = await eor(message, "Processing...")
            quantity = int(message.text.split(None, 2)[1])
            spam_text = message.text.split(None, 2)[2]
            await asyncio.sleep(1)
            await message.delete()
            await spam.delete()
            for i in range(quantity):
                await client.send_message(message.chat.id, spam_text)
                await asyncio.sleep(0.1)
