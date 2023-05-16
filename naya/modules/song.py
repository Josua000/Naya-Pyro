"""
✅ Edit Code Boleh
❌ Hapus Credits Jangan
THANKS TO TOMI
👤 Telegram: @T0M1_X
"""
# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT

import os
from asyncio import get_event_loop
from functools import partial

import wget
from pyrogram import *
from pyrogram.types import *
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL

from . import *

__MODULE__ = "Youtube"
__HELP__ = f"""
๏ Perintah: <code>{cmd}song</code> [judul]
◉ Penjelasan: Untuk mendownload lagu dari youtube.

๏ Perintah: <code>{cmd}video</code> [judul]
◉ Penjelasan: Untuk mendownload video dari youtube.
"""


def run_sync(func, *args, **kwargs):
    return get_event_loop().run_in_executor(None, partial(func, *args, **kwargs))


@bots.on_message(filters.me & filters.command("video", cmd))
async def yt_video(client, message):
    if len(message.command) < 2:
        return await eor(
            message,
            "❌ <b>Video tidak ditemukan,</b>\nMohon masukan judul video dengan benar.",
        )
    infomsg = await eor(message, "<code>🔍 Pencarian...</code>")
    try:
        search = (
            SearchVideos(
                str(message.text.split(None, 1)[1]),
                offset=1,
                mode="dict",
                max_results=1,
            )
            .result()
            .get("search_result")
        )
        link = f"https://youtu.be/{search[0]['id']}"
    except Exception as error:
        return await infomsg.edit(f"<code>🔍 Pencarian...\n\n❌ Error: {error}</code>")
    ydl = YoutubeDL(
        {
            "quiet": True,
            "no_warnings": True,
            "format": "(bestvideo[height<=?720][width<=?1280][ext=mp4])+(bestaudio[ext=m4a])",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "nocheckcertificate": True,
            "geo_bypass": True,
        }
    )
    await infomsg.edit(f"<code>📥 Downloader...</code>")
    try:
        ytdl_data = await run_sync(ydl.extract_info, link, download=True)
        file_path = ydl.prepare_filename(ytdl_data)
        videoid = ytdl_data["id"]
        title = ytdl_data["title"]
        url = f"https://youtu.be/{videoid}"
        duration = ytdl_data["duration"]
        channel = ytdl_data["uploader"]
        views = f"{ytdl_data['view_count']:,}".replace(",", ".")
        thumbs = f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg"
    except Exception as error:
        return await infomsg.edit(f"<code>📥 Downloader...\n\n❌ Error: {error}</code>")
    thumbnail = wget.download(thumbs)
    await client.send_video(
        message.chat.id,
        video=file_path,
        thumb=thumbnail,
        file_name=title,
        duration=duration,
        supports_streaming=True,
        caption="<b>💡 Informasi {}</b>\n\n<b>🏷 Nama:</b> {}\n<b>🧭 Durasi:</b> {}\n<b>👀 Dilihat:</b> {}\n<b>📢 Channel:</b> {}\n<b>🔗 Tautan:</b> <a href={}>Youtube</a>\n\n<b>⚡ Upload By:</b> {}".format(
            "video",
            title,
            duration,
            views,
            channel,
            url,
            client.me.mention,
        ),
        reply_to_message_id=message.id,
    )
    await infomsg.delete()
    for files in (thumbnail, file_path):
        if files and os.path.exists(files):
            os.remove(files)


@bots.on_message(filters.me & filters.command("song", cmd))
async def yt_audio(client, message):
    if len(message.command) < 2:
        return await eor(
            message,
            "❌ <b>Audio tidak ditemukan,</b>\nMohon masukan judul video dengan benar.",
        )
    infomsg = await eor(message, "<code>🔍 Pencarian...</code>")
    try:
        search = (
            SearchVideos(
                str(message.text.split(None, 1)[1]),
                offset=1,
                mode="dict",
                max_results=1,
            )
            .result()
            .get("search_result")
        )
        link = f"https://youtu.be/{search[0]['id']}"
    except Exception as error:
        return await infomsg.edit(f"<code>🔍 Pencarian...\n\n❌ Error: {error}</code>")
    ydl = YoutubeDL(
        {
            "quiet": True,
            "no_warnings": True,
            "format": "bestaudio[ext=m4a]",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "nocheckcertificate": True,
            "geo_bypass": True,
        }
    )
    await infomsg.edit(f"<code>📥 Downloader...</code>")
    try:
        ytdl_data = await run_sync(ydl.extract_info, link, download=True)
        file_path = ydl.prepare_filename(ytdl_data)
        videoid = ytdl_data["id"]
        title = ytdl_data["title"]
        url = f"https://youtu.be/{videoid}"
        duration = ytdl_data["duration"]
        channel = ytdl_data["uploader"]
        views = f"{ytdl_data['view_count']:,}".replace(",", ".")
        thumbs = f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg"
    except Exception as error:
        return await infomsg.edit(f"<code>📥 Downloader...\n\n❌ Error: {error}</code>")
    thumbnail = wget.download(thumbs)
    await client.send_audio(
        message.chat.id,
        audio=file_path,
        thumb=thumbnail,
        file_name=title,
        duration=duration,
        caption="<b>💡 Informasi {}</b>\n\n<b>🏷 Nama:</b> {}\n<b>🧭 Durasi:</b> {}\n<b>👀 Dilihat:</b> {}\n<b>📢 Channel:</b> {}\n<b>🔗 Tautan:</b> <a href={}>Youtube</a>\n\n<b>⚡ Upload By:</b> {}".format(
            "Audio",
            title,
            duration,
            views,
            channel,
            url,
            client.me.mention,
        ),
        reply_to_message_id=message.id,
    )
    await infomsg.delete()
    for files in (thumbnail, file_path):
        if files and os.path.exists(files):
            os.remove(files)
