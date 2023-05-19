__MODULE__ = "openai"
__HELP__ = f"""
✘ Bantuan Untuk OpenAI

๏ Perintah: <code>{cmd}ai</code> [query]
◉ Penjelasan: Untuk mengajukan pertanyaan ke AI

๏ Perintah: <code>{cmd}img</code> [query]
◉ Penjelasan: Untuk mencari gambar ke AI
"""


from naya import *
from naya.config import OPENAI_API

from . import *


@bots.on_message(filters.me & filters.command(["ai", "ask"], cmd))
async def _(client, message):
    if len(message.command) == 1:
        return await message.reply(
            f"Ketik <code>{cmd}ai [question]</code> untuk menggunakan OpenAI"
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
        "temperature": 0,
    }
    msg = await eor(message, "`Processing...`")
    try:
        response = (
            await http.post(
                "https://api.openai.com/v1/completions", headers=headers, json=json_data
            )
        ).json()
        await msg.edit(response["choices"][0]["text"])
    except MessageNotModified:
        pass
    except Exception as e:
        await msg.edit(f"**Terjadi Kesalahan!!\n`{e}`**")


@bots.on_message(filters.me & filters.command(["img"], cmd))
async def _(client, message):
    if len(message.command) == 1:
        return await message.reply(
            f"Ketik <code>{cmd}img [question]</code> untuk menggunakan OpenAI"
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
        await msg.delete()
        await client.send_photo(message.chat.id, response["data"][0]["url"])
    except MessageNotModified:
        pass
    except Exception as e:
        await msg.edit(f"**Terjadi Kesalahan!!\n`{e}`**")
