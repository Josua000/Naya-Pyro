import asyncio

from pyrogram import filters
from pyrogram.raw.functions.messages import DeleteHistory

from . import *

__MODULE__ = "pinterest"
__HELP__ = f"""
✘ Bantuan Untuk Pinterest

๏ Perintah: <code>{cmd}pinter</code> [link]
◉ Penjelasan: Untuk mengunduh media dari pinterest.
"""


@bots.on_message(filters.me & filters.command("pinter", cmd))
async def _(client, message):
    if len(message.command) < 2:
        return
    Tm = await eor(message, "<code>Processing . . .</code>")
    link = message.text.split()[1]
    bot = "SaveAsbot"
    await client.unblock_user(bot)
    await client.send_message(bot, link)
    # await xnxx.delete()
    await asyncio.sleep(8)
    async for sosmed in client.search_messages(bot):
        try:
            if sosmed.video:
                await sosmed.copy(
                    message.chat.id,
                    caption=f"<b>Upload By <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a></b>",
                    reply_to_message_id=message.id,
                )
            else:
                try:
                    if sosmed.photo:
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
        except Exception:
            pass
    user_info = await client.resolve_peer(bot)
    return await client.send(DeleteHistory(peer=user_info, max_id=0, revoke=True))
