from asyncio import gather
from base64 import b64decode
from io import BytesIO

from pyrogram import filters

from . import *

__MODULE__ = "Webshot"
__HELP__ = f"""
๏ Perintah: <code>{cmd}ss or webss</code> [link]
◉ Penjelasan: Untuk mendapatkan screenshot dari link tersebut.
"""


async def take_screenshot(url: str, full: bool = False):
    url = "https://" + url if not url.startswith("http") else url
    payload = {
        "url": url,
        "width": 1920,
        "height": 1080,
        "scale": 1,
        "format": "jpeg",
    }
    if full:
        payload["full"] = True
    data = await post(
        "https://webscreenshot.vercel.app/api",
        data=payload,
    )
    if "image" not in data:
        return None
    b = data["image"].replace("data:image/jpeg;base64,", "")
    file = BytesIO(b64decode(b))
    file.name = "webss.jpg"
    return file


@bots.on_message(filters.command(["ss", "webss"], cmd) & filters.me)
async def take_ss(_, message):
    if len(message.command) < 2:
        return await eor(message, "<code>Berikan saya link yang valid</code>")

    if len(message.command) == 2:
        url = message.text.split(None, 1)[1]
        full = False
    elif len(message.command) == 3:
        url = message.text.split(None, 2)[1]
        full = message.text.split(None, 2)[2].lower().strip() in [
            "yes",
            "y",
            "1",
            "true",
        ]
    else:
        return await eor(message, "<code>Ada yang salah.</code>")

    m = await eor(message, "<code>Processing...</code>")

    try:
        photo = await take_screenshot(url, full)
        if not photo:
            return await m.edit("<code>Terjadi kesalahan.</code>")

        m = await m.edit("<code>Uploading...</code>")

        if not full:
            # Full size images have problem with reply_photo, that's why
            # we need to only use reply_photo if we're not using full size
            await gather(*[message.reply_document(photo), message.reply_photo(photo)])
        else:
            await message.reply_document(photo)
        await m.delete()
    except Exception as e:
        await m.edit(str(e))
