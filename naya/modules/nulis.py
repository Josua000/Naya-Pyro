# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


import requests

from . import *


@bots.on_message(filters.command(["nulis", "nl"], cmd) & filters.me)
async def handwrite(client, message):
    if message.reply_to_message:
        naya = message.reply_to_message.text
    else:
        naya = message.text.split(None, 1)[1]
    nan = await message.reply("`Processing...`")
    ajg = requests.get(f"https://api.sdbots.tk/write?text={naya}").url
    await message.reply_photo(
        photo=ajg, caption=f"**Ditulis Oleh :** {client.me.mention}"
    )
    await nan.delete()


__MODULE__ = "Nulis"
__HELP__ = f"""
๏ Perintah: <code>{cmd}nulis</code> [balas pesan atau berikan]
◉ Penjelasan: Untuk anda yang malas nulis.
"""
