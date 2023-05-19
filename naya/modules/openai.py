from io import *

import openai
from kynaylibs.nan.utils.http import *
from pyrogram import filters
from pyrogram.errors import MessageNotModified
from pyrogram.types import *

from naya import *
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
async def ai(client, message):
    if len(message.command) == 1:
        return await message.edit_text(
            f"Ketik <code>{cmd}ai [pertanyaan]</code> untuk menggunakan OpenAI"
        )
    question = message.text.split(" ", maxsplit=1)[1]
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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",
    }

    json_data = {
        "model": "text-davinci-003",
        "prompt": question,
        "max_tokens": 500,
        "temperature": 0,
    }
    msg = await message.edit_text("`Memproses...`")
    try:
        response = (
            await http.post(
                "https://api.openai.com/v1/completions", headers=headers, json=json_data
            )
        ).json()
        await msg.edit_text(response["choices"][0]["text"])
    except Exception as e:
        await msg.edit_text(f"**Terjadi Kesalahan!!\n`{e}`**")


@bots.on_message(filters.me & filters.command(["img"], cmd))
async def img(client, message):
    if len(message.command) == 1:
        return await eor(
            message, f"Ketik <code>{cmd}img [question]</code> untuk menggunakan OpenAI"
        )
    question = message.text.split(" ", maxsplit=1)[1]
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API}",
    }

    json_data = {
        "model": "text-davinci-003",
        "prompt": question,
        "max_tokens": 500,
        "n": 1,
        "size": 1024,
    }
    msg = await eor(message, "`Processing...`")
    try:
        response = (
            await http.post(
                "https://api.openai.com/v1/image", headers=headers, json=json_data
            )
        ).json()
        await client.send_photo(message.chat.id, response["data"][0]["url"])
    except MessageNotModified:
        pass
    except Exception as e:
        await msg.edit(f"**Terjadi Kesalahan!!\n`{e}`**")
        await msg.delete()


__MODULE__ = "openai"
__HELP__ = f"""
✘ Bantuan Untuk OpenAI

๏ Perintah: <code>{cmd}ai</code> [query]
◉ Penjelasan: Untuk mengajukan pertanyaan ke AI

๏ Perintah: <code>{cmd}img</code> [query]
◉ Penjelasan: Untuk mencari gambar ke AI
"""
