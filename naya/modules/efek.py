"""
CREDIST TOMAY GANTENG
"""

import asyncio
import os

from pyrogram import filters

from . import *

__MODULE__ = "Efek"
__HELP__ = f"""
๏ Perintah: <code>{cmd}efek</code> [efek_code - reply to voice note]
◉ Penjelasan: Untuk mengubah suara voice note.

<b>efek_code:</b>  <code>bengek</code> <code>robot</code> <code>jedug</code> <code>fast</code> <code>echo</code>
"""


@bots.on_message(filters.me & filters.command("efek", cmd))
async def _(client, message):
    helo = get_arg(message)
    rep = message.reply_to_message
    if rep and helo:
        tau = ["bengek", "robot", "jedug", "fast", "echo"]
        if helo in tau:
            Tm = await eor(message, f"Merubah suara menjadi {helo}")
            indir = await client.download_media(rep)
            KOMUT = {
                "bengek": '-filter_complex "rubberband=pitch=1.5"',
                "robot": "-filter_complex \"afftfilt=real='hypot(re,im)*sin(0)':imag='hypot(re,im)*cos(0)':win_size=512:overlap=0.75\"",
                "jedug": '-filter_complex "acrusher=level_in=8:level_out=18:bits=8:mode=log:aa=1"',
                "fast": "-filter_complex \"afftfilt=real='hypot(re,im)*cos((random(0)*2-1)*2*3.14)':imag='hypot(re,im)*sin((random(1)*2-1)*2*3.14)':win_size=128:overlap=0.8\"",
                "echo": '-filter_complex "aecho=0.8:0.9:500|1000:0.2|0.1"',
            }
            ses = await asyncio.create_subprocess_shell(
                f"ffmpeg -i '{indir}' {KOMUT[helo]} audio.mp3"
            )
            await ses.communicate()
            await Tm.delete()
            await rep.reply_voice("audio.mp3", caption=f"Efek {helo}")
            os.remove("audio.mp3")
        else:
            await Tm.edit(f"Silahkan isi sesuai {tau}")
    else:
        await Tm.edit(
            f"Silahkan balas ke audio atau mp3, contoh : <code>!efek bengek</code> sambil balas ke audio atau mp3"
        )
