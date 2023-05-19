from io import *

import openai
from kynaylibs.nan.utils.http import *
from pyrogram import filters
from pyrogram.types import *
from naya.config import *
from naya import *


class OpenAi:
    def text(question):
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

    def photo(question):
        openai.api_key = OPENAI_API
        response = openai.Image.create(prompt=question, n=1, size="1024x1024")
        return response["data"][0]["url"]


@bots.on_message(filters.me & filters.command(["ai", "ask"], cmd))
async def ai(client, message):
    if len(message.command) == 1:
        return await message.edit_text(
            f"Ketik <code>{cmd}ai [pertanyaan]</code> untuk menggunakan OpenAI"
        )
    msg = await message.edit_text("`Memproses...`")
    biji = message.text.split(None, 1)[1]
    try:
        response = OpenAi.text(biji)
        await msg.edit_text(f"**Q:** {biji}\n\n**A:** {response}")
    except Exception as e:
        await msg.edit_text(f"**Terjadi Kesalahan!!\n`{e}`**")


@bots.on_message(filters.me & filters.command(["img"], cmd))
async def img(client, message):
    if len(message.command) == 1:
        return await eor(
            message, f"Ketik <code>{cmd}img [question]</code> untuk menggunakan OpenAI"
        )
    try:
        biji = message.text.split(None, 1)[1]
        response = OpenAi.photo(biji)
        await client.send_photo(message.chat.id, response)
    except Exception as e:
        await message.edit(f"**Terjadi Kesalahan!!\n`{e}`**")
        #await msg.delete()


__MODULE__ = "openai"
__HELP__ = f"""
✘ Bantuan Untuk OpenAI

๏ Perintah: <code>{cmd}ai</code> [query]
◉ Penjelasan: Untuk mengajukan pertanyaan ke AI

๏ Perintah: <code>{cmd}img</code> [query]
◉ Penjelasan: Untuk mencari gambar ke AI
"""
