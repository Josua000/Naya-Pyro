import json

import requests
from pyrogram import filters

from . import *

__MODULE__ = "Adzan"
__HELP__ = f"""
๏ Perintah: <code>{cmd}adzan</code> [nama kota]
◉ Penjelasan: Untuk mengetahui jadwal adzan di lokasi anda.
"""


@bots.on_message(filters.me & filters.command("adzan", cmd))
async def _(client, message):
    LOKASI = message.text.split(None, 1)[1]
    if len(message.command) < 2:
        return await eor(message, "<b>Silahkan Masukkan Nama Kota Anda</b>")
    url = f"http://muslimsalat.com/{LOKASI}.json?key=bd099c5825cbedb9aa934e255a81a5fc"
    request = requests.get(url)
    if request.status_code != 200:
        await eor(message, f"<b>Maaf Tidak Menemukan Kota <code>{LOKASI}</code>")
    result = json.loads(request.text)
    catresult = f"""
Jadwal Shalat Hari Ini

<b>Tanggal</b> <code>{result['items'][0]['date_for']}</code>
<b>Kota</b> <code>{result['query']} | {result['country']}</code>

<b>Terbit:</b> <code>{result['items'][0]['shurooq']}</code>
<b>Subuh:</b> <code>{result['items'][0]['fajr']}</code>
<b>Zuhur:</b> <code>{result['items'][0]['dhuhr']}</code>
<b>Ashar:</b> <code>{result['items'][0]['asr']}</code>
<b>Maghrib:</b> <code>{result['items'][0]['maghrib']}</code>
<b>Isya:</b> <code>{result['items'][0]['isha']}</code>
"""
    await eor(message, catresult)
