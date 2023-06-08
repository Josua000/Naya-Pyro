# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


import os

from PIL import *

from . import *


def text_set(text):
    lines = []
    if len(text) <= 55:
        lines.append(text)
    else:
        all_lines = text.split("\n")
        for line in all_lines:
            if len(line) <= 55:
                lines.append(line)
            else:
                k = len(line) // 55
                lines.extend(line[((z - 1) * 55) : (z * 55)] for z in range(1, k + 2))
    return lines[:25]


@bots.on_message(filters.command(["nulis", "nl"], cmd) & filters.me)
async def handwrite(client, message):
    if message.reply_to_message:
        naya = message.reply_to_message.text
    else:
        naya = message.text.split(None, 1)[1]
    nan = await eor(message, "Processing...")
    try:
        img = Image.open("naya/resources/kertas.jpg")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("naya/resources/fonts/assfont.ttf", 30)
        x, y = 150, 140
        lines = text_set(naya)
        line_height = font.getsize("hg")[1]
        for line in lines:
            draw.text((x, y), line, fill=(1, 22, 55), font=font)
            y = y + line_height - 5
        file = "nulis.jpg"
        img.save(file)
        if os.path.exists(file):
            await message.reply_photo(
                photo=file, caption=f"<b>Ditulis Oleh :</b> {client.me.mention}"
            )
            os.remove(file)
            await nan.delete()
    except Exception as e:
        return await message.reply(e)


__MODULE__ = "nulis"
__HELP__ = f"""
✘ Bantuan Untuk Nulis

๏ Perintah: <code>{cmd}nulis</code> [balas pesan atau berikan]
◉ Penjelasan: Untuk anda yang malas nulis.
"""
