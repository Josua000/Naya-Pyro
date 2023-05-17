from kynaylibs.nan.utils import eor
from pyrogram import filters

from naya import *

__MODULE__ = "openai"
__HELP__ = f"""
✘ Bantuan Untuk OpenAI

๏ Perintah: <code>{cmd}ai</code> [query]
◉ Penjelasan: Untuk mengajukan pertanyaan ke AI

๏ Perintah: <code>{cmd}img</code> [query]
◉ Penjelasan: Untuk mencari gambar ke AI
"""


import openai

from naya.config import OPENAI_API


class OpenAi:
    def Text(question):
        openai.api_key = OPENAI_API
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Q: {question}\nA:",
            temperature=0,
            max_tokens=500,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        return response.choices[0].text

    def Photo(question):
        openai.api_key = OPENAI_API
        response = openai.Image.create(prompt=question, n=1, size="1024x1024")
        return response["data"][0]["url"]


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
