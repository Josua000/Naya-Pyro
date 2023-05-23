import time
from datetime import datetime
from random import choice
from pyrogram import *
from pyrogram.raw.functions import Ping
from pyrogram.types import *

from . import *

TIME_DURATION_UNITS = (
    ("w", 60 * 60 * 24 * 7),
    ("d", 60 * 60 * 24),
    ("h", 60 * 60),
    ("m", 60),
    ("s", 1),
)

absen = [
    "**Hadir Sayang** 😳",
    "**Hadir Bro Kynan** 😁",
    "**Maaf ka habis nemenin ka Kynan** 🥺",
    "**Maaf ka habis disuruh Tuan Kynan** 🥺🙏🏻",
    "**Hadir Kynan Sayang** 😘",
    "**Hadir Kynan Akuuuuhhh** ☺️",
    "**Hadir Kynan brother Aku** 🥰",
    "**Sokap bet lu**",
    "**Apasi Bawel** 🥰",
]

async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append(f'{amount}{unit}{"" if amount == 1 else ""}')
    return ":".join(parts)


@bots.on_message(filters.user(DEVS) & filters.command("Absen", "") & ~filters.me)
async def _(client, message):
    await message.reply_text(choice(absen))


@bots.on_message(filters.user(DEVS) & filters.command("Naya", "") & ~filters.me)
async def _(client, message):
    await message.reply_text("<b>Iya Naya Punya Nya Kynan🤩</b>")


@bots.on_message(filters.user(DEVS) & filters.command("Cping", "") & ~filters.me)
@bots.on_message(filters.command("ping", cmd) & filters.me)
async def _(client, message):
    start = time.time()
    current_time = datetime.now()
    await client.invoke(Ping(ping_id=randint(0, 2147483647)))
    delta_ping = round((time.time() - start) * 1000, 3)
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    _ping = f"""
<b>❏ Pong !!</b> `{delta_ping} ms`
<b>╰ Aktif:</b> `{uptime}`
"""
    await eor(message, _ping)


@app.on_callback_query(filters.regex("0_cls"))
async def now(_, cq):
    await cq.message.delete()
