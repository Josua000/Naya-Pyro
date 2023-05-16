import os

from pyrogram import filters
from pyrogram.types import *
from removebg import RemoveBg

from . import *

RMBG_API = os.environ.get("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

DOWN_PATH = "dowloads/"

IMG_PATH = DOWN_PATH + "naya.jpg"

__MODULE__ = "Rmbg"
__HELP__ = f"""
๏ Perintah: <code>{cmd}rmbg</code> [reply to photo]
◉ Penjelasan: Untuk menghapus background dari foto.
"""


@bots.on_message(filters.me & filters.command("rmbg", cmd))
async def remove_bg(client, message):
    if not RMBG_API:
        return
    Tm = await eor(message, "`Processing...`")
    replied = message.reply_to_message
    if replied.photo or replied.document or replied.sticker or replied.animation:
        if os.path.exists(IMG_PATH):
            os.remove(IMG_PATH)
        await client.download_media(message=replied, file_name=IMG_PATH)
        await Tm.edit("`Removing...`")
        try:
            rmbg = RemoveBg(RMBG_API, "rm_bg_error.log")
            rmbg.remove_background_from_img_file(IMG_PATH)
            remove_img = IMG_PATH + "_no_bg.png"
            await client.send_photo(
                chat_id=message.chat.id,
                photo=remove_img,
                reply_to_message_id=message.id,
                disable_notification=True,
            )
            await Tm.delete()
        except Exception as e:
            print(e)
            await Tm.edit("`Telah terjadi suatu kesalahan!.`")
    else:
        await Tm.edit(
            "**Usage: Mohon reply ke gambar yang ingin dihapus backgroundnya!**"
        )
