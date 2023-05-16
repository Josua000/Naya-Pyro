from pyrogram import filters

from . import *

__MODULE__ = "OpenAI"
__HELP__ = f"""
๏ Perintah: <code>{cmd}ai</code> [query]
◉ Penjelasan: Untuk mengajukan pertanyaan ke AI

๏ Perintah: <code>{cmd}img</code> [query]
◉ Penjelasan: Untuk mencari gambar ke AI
"""


@bots.on_message(filters.me & filters.command(["ai", "ask"], cmd))
async def _(client, message):
    Tm = await eor(message, "<code>Memproses...</code>")
    if len(message.command) < 2:
        return await Tm.edit(f"<b>Gunakan format :<code>ai</code> [pertanyaan]</b>")
    try:
        response = OpenAi.Text(message.text.split(None, 1)[1])
        await message.reply(response)
        await Tm.delete()
    except Exception as error:
        await message.reply(error)
        await Tm.delete()


@bots.on_message(filters.me & filters.command(["img"], cmd))
async def _(client, message):
    Tm = await eor(message, "<code>Memproses...</code>")
    if len(message.command) < 2:
        return await Tm.edit(f"<b>Gunakan format<code>img</code> [pertanyaan]</b>")
    try:
        response = OpenAi.Photo(message.text.split(None, 1)[1])
        msg = message.reply_to_message or message
        await client.send_photo(message.chat.id, response, reply_to_message_id=msg.id)
        return await Tm.delete()
    except Exception as error:
        await message.reply(error)
        return await Tm.delete()
