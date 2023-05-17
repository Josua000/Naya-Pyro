"""

import os

from pyrogram import filters

from . import *

__MODULE__ = "telegraph"
__HELP__ = f"
✘ Bantuan Untuk Telegraph

๏ Perintah: <code>{cmd}tg</code> [reply media/text]
◉ Penjelasan: Untuk mengapload media/text ke telegra.ph.
"

telegraph = Telegraph()
r = telegraph.create_account(short_name="Naya-Pyro")
auth_url = r["auth_url"]


@bots.on_message(filters.me & filters.command("tg", cmd))
async def uptotelegraph(client, message):
    tex = await message.edit_text("`Processing . . .`")
    if not message.reply_to_message:
        await tex.edit("**Balas ke File atau Teks**")
        return
    if message.reply_to_message.media:
        if message.reply_to_message.sticker:
            m_d = await convert_to_image(message, client)
        else:
            m_d = await message.reply_to_message.download()
        try:
            media_url = upload_file(m_d)
        except exceptions.TelegraphException as exc:
            await tex.edit(f"**ERROR:** `{exc}`")
            os.remove(m_d)
            return
        U_done = f"**Uploaded on ** [Telegraph](https://telegra.ph/{media_url[0]})"
        await tex.edit(U_done)
        os.remove(m_d)
    elif message.reply_to_message.text:
        page_title = get_text(message) if get_text(message) else client.me.first_name
        page_text = message.reply_to_message.text
        page_text = page_text.replace("\n", "<br>")
        try:
            response = telegraph.create_page(page_title, html_content=page_text)
        except exceptions.TelegraphException as exc:
            await tex.edit(f"**ERROR:** `{exc}`")
            return
        wow_graph = (
            f"**Uploaded as** [Telegraph](https://telegra.ph/{response['path']})"
        )
        await tex.edit(wow_graph)
"""