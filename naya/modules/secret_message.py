"""
CREDITS TOMAY
"""

from gc import get_objects

from pyrogram import filters
from pyrogram.types import *

from . import *

__MODULE__ = "Dm"
__HELP__ = f"""
๏ Perintah: <code>{cmd}dm</code> [reply to user - text]
◉ Penjelasan: Untuk mengirim pesan secara rahasia.
"""


@bots.on_message(filters.me & filters.command("dm", cmd))
async def _(client, message):
    if not message.reply_to_message:
        return await eor("<code>dm</code> [reply to user - text]")
    text = f"secret {id(message)}"
    await message.delete()
    x = await client.get_inline_bot_results(app.me.username, text)
    for m in x.results:
        await message.reply_to_message.reply_inline_bot_result(x.query_id, m.id)


@app.on_inline_query(filters.regex("^secret"))
async def _(client, q):
    m = [obj for obj in get_objects() if id(obj) == int(q.query.split(None, 1)[1])][0]
    await client.answer_inline_query(
        q.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="Pesan Rahasia!",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="💬 Baca Pesan Rahasia 💬",
                                    callback_data=f"read {q.query.split(None, 1)[1]}",
                                )
                            ],
                        ]
                    ),
                    input_message_content=InputTextMessageContent(
                        f"<b>👉🏻 Ada Pesan Rahasia Untuk Mu Nih:</b> <a href=tg://user?id={m.reply_to_message.from_user.id}>{m.reply_to_message.from_user.first_name} {m.reply_to_message.from_user.last_name or ''}</a>"
                    ),
                )
            )
        ],
    )


@app.on_callback_query(filters.regex("^read"))
async def _(client, cq):
    m = [obj for obj in get_objects() if id(obj) == int(cq.data.split(None, 1)[1])][0]
    if not cq.from_user.id == m.reply_to_message.from_user.id:
        return await cq.answer(
            f"❌ Jangan asal pencet gue jijik {cq.from_user.first_name} {cq.from_user.last_name or ''}",
            True,
        )
    await cq.answer(m.text.split(None, 1)[1], True)
