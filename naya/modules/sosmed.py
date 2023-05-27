import asyncio

from pyrogram import filters
from pyrogram.raw.functions.messages import DeleteHistory

from . import *

__MODULE__ = "sosmed"
__HELP__ = f"""
✘ Bantuan Untuk Sosmed

๏ Perintah: <code>{cmd}sosmed</code> [link]
◉ Penjelasan: Untuk Mendownload Media Dari Facebook/Tiktok/Instagram/Twitter/YouTube.
"""


@bots.on_message(filters.me & filters.command("sosmed", cmd))
async def _(client, message):
    if len(message.command) < 2:
        return
    Tm = await eor(message, "<code>Processing . . .</code>")
    link = message.text.split()[1]
    bot = "thisvidbot"
    await client.unblock_user(bot)
    xnxx = await client.send_message(bot, link)
    await xnxx.delete()
    await asyncio.sleep(8)
    async for sosmed in client.search_messages(bot):
        try:
            if sosmed.video:
                await sosmed.copy(
                    message.chat.id,
                    caption=f"<b>Upload By <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a></b>",
                    reply_to_message_id=message.id,
                )
                await Tm.delete()
        except Exception:
            await Tm.edit(
                "<b>Video tidak ditemukan silahkan ulangi beberapa saat lagi</b>"
            )
    user_info = await client.resolve_peer(bot)
    return await client.send(DeleteHistory(peer=user_info, max_id=0, revoke=True))
