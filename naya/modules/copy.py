import asyncio

from pyrogram import filters
from pyrogram.raw.functions.messages import DeleteHistory

from . import *

__MODULE__ = "Nyolong"
__HELP__ = f"""
๏ Perintah: <code>{cmd}copy</code> [link]
◉ Penjelasan: Untuk mengambil konten ch private.
"""


@bots.on_message(filters.me & filters.command("copy", cmd))
async def _(client, message):
    if len(message.command) < 2:
        return
    else:
        Tm = await eor(message, "<code>Processing . . .</code>")
        link = message.text.split()[1]
        bot = "Nyolongbang_bot"
        await client.unblock_user(bot)
        xnxx = await client.send_message(bot, link)
        await xnxx.delete()
        await asyncio.sleep(8)
        await Tm.delete()
        async for sosmed in client.search_messages(bot, limit=1):
            try:
                await sosmed.copy(
                    message.chat.id,
                    reply_to_message_id=message.id,
                )
            except Exception:
                await Tm.edit(
                    "<b>Video tidak ditemukan silahkan ulangi beberapa saat lagi</b>"
                )
        user_info = await client.resolve_peer(bot)
        return await client.send(DeleteHistory(peer=user_info, max_id=0, revoke=True))
