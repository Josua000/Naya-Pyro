# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


import asyncio
import logging
import os
import random
import string
import threading
import time
from datetime import timedelta

import ffmpeg
from pyrogram import filters
from pyrogram.errors import FloodWait, MessageNotModified
from pytgcalls import GroupCallFactory, GroupCallFileAction
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL

from . import *

s_dict = {}
GPC = {}


@bots.on_message(filters.me & filters.command(["playlist"], cmd))
async def pl(client, message):
    group_call = GPC.get((message.chat.id, client.me.id))
    play = await eor(message, "<code>Processing...</code>")
    song = f"<b>📋 Daftar Playlist {message.chat.title}</b> : \n"
    s = s_dict.get((message.chat.id, client.me.id))
    if not group_call:
        return await play.edit("<code>Obrolan Suara Tidak Ditemukan</code>")
    if not s:
        if group_call.is_connected:
            return await play.edit(
                f"<b>📀 Sedang diputar :</b> <code>{group_call.song_name}</code>"
            )
        else:
            return await play.edit("<code>Obrolan Suara Tidak Ditemukan</code>")
    if group_call.is_connected:
        song += f"<b>📀 Sedang diputar :</b> <code>{group_call.song_name}</code> \n\n"
    for sno, i in enumerate(s, start=1):
        song += f"<code>{sno} 🎧</code> [{i['song_name']}]({i['url']}) `| {i['singer']} | {i['dur']}` \n\n"
    await play.edit(song, disable_web_page_preview=True)


async def get_chat_(client, chat_):
    chat_ = str(chat_)
    if chat_.startswith("-100"):
        try:
            return (await client.get_chat(int(chat_))).id
        except ValueError:
            chat_ = chat_.split("-100")[1]
            chat_ = f"-{str(chat_)}"
            return int(chat_)


async def playout_ended_handler(group_call, filename):
    client_ = group_call.client
    chat_ = await get_chat_(client_, f"-100{group_call.full_chat.id}")
    chat_ = int(chat_)
    s = s_dict.get((chat_, client_.me.id))
    if os.path.exists(group_call.input_filename):
        os.remove(group_call.input_filename)
    if not s:
        await group_call.stop()
        del GPC[(chat_, client_.me.id)]
        return
    name_ = s[0]["song_name"]
    singer_ = s[0]["singer"]
    dur_ = s[0]["dur"]
    raw_file = s[0]["raw"]
    link = s[0]["url"]
    file_size = humanbytes(os.stat(raw_file).st_size)
    song_info = f'📌 <b>Sedang dimainkan</b> \n\n📀 <b>Judul:</b> <a href="{link}">{name_}</a> \n🎸 <b>Channel:</b> <code>{singer_}</code> \n⏲️ <b>Durasi:</b> <code>{dur_}</code> \n📂 <b>Ukuran:</b> <code>{file_size}</code>'
    await client_.send_message(
        chat_,
        song_info,
        disable_web_page_preview=True,
    )
    s.pop(0)
    logging(song_info)
    group_call.song_name = name_
    group_call.input_filename = raw_file


@bots.on_message(filters.me & filters.command(["skip"], cmd))
async def skip_m(client, message):
    group_call = GPC.get((message.chat.id, client.me.id))
    s_d = s_dict.get((message.chat.id, client.me.id))
    if not group_call:
        return await eor(message, "<code>Tidak sedang memutar apa-apa!</code>")
    if not s_d:
        return await eor(message, "<code>Antrian kosong!</code>")
    next_song = s_d.pop(0)
    raw_file_name = next_song["raw"]
    vid_title = next_song["song_name"]
    uploade_r = next_song["singer"]
    next_song["dur"]
    url = next_song["url"]
    if os.path.exists(raw_file_name):
        group_call.input_filename = raw_file_name
        group_call.song_name = vid_title
        return await eor(
            message,
            f"📌 <b>Memutar Lagu Berikutnya</b>\n\n📀 <b>Judul</b>: <code>{vid_title}</code>\n💌 <b>Channel</b>: </code>{uploade_r}</code>",
        )
    else:
        start = time.time()
        try:
            audio_original = await yt_dl(url, client, message, start)
        except BaseException as e:
            return await eor(message, f"<b>Error :</b> <code>{str(e)}</code>")
        try:
            raw_file_name = await convert_to_raw(audio_original, raw_file_name)
        except BaseException as e:
            return await eor(message, f"<b>Error :<b> <code>{e}</code>")
        if os.path.exists(audio_original):
            os.remove(audio_original)
        group_call.input_filename = raw_file_name
        group_call.song_name = vid_title
        return await eor(
            message,
            f"📌 <b>Memutar Lagu Berikutnya</b>\n\n📀 <b>Judul</b>: {vid_title}\n💌 <b>Channel</b>: {uploade_r}",
        )


@bots.on_message(filters.me & filters.command(["play"], cmd))
async def play_m(client, message):
    group_call = GPC.get((message.chat.id, client.me.id))
    u_s = await eor(message, "<code>Processing..</code>")
    if input_str := get_text(message):
        search = SearchVideos(str(input_str), offset=1, mode="dict", max_results=1)
        rt = search.result()
        result_s = rt.get("search_result")
        if not result_s:
            return await u_s.edit(f"<b>Lagu tidak ditemukan</b> {input_str}")
        url = result_s[0]["link"]
        dur = result_s[0]["duration"]
        vid_title = result_s[0]["title"]
        result_s[0]["id"]
        uploade_r = result_s[0]["channel"]
        start = StartTime
        try:
            audio_original = await yt_dl(url, client, message, start)
        except BaseException as e:
            return await u_s.edit(f"<b>Error :<b> <code>{str(e)}</code>")
        raw_file_name = (
            "".join(random.choice(string.ascii_lowercase) for _ in range(5)) + ".raw"
        )

    else:
        if not message.reply_to_message:
            return await u_s.edit("<b>Berikan Judul Lagu/Balas Ke File Audio..</b>")
        if not message.reply_to_message.audio:
            return await u_s.edit("<b>Berikan Judul Lagu/Balas Ke File Audio..</b>")
        audio = message.reply_to_message.audio
        audio_original = await message.reply_to_message.download()
        vid_title = audio.title or audio.file_name
        uploade_r = message.reply_to_message.audio.performer or "Unknown Artist."
        dura_ = message.reply_to_message.audio.duration
        dur = timedelta(seconds=dura_)
        raw_file_name = (
            "".join(random.choice(string.ascii_lowercase) for _ in range(5)) + ".raw"
        )

        url = message.reply_to_message.link
    try:
        raw_file_name = await convert_to_raw(audio_original, raw_file_name)
    except BaseException as e:
        return await u_s.edit(f"<b>Error :</b> <code>{e}</code>")
    if os.path.exists(audio_original):
        os.remove(audio_original)
    if not group_call:
        group_call = GroupCallFactory(client).get_file_group_call()
        group_call.song_name = vid_title
        GPC[(message.chat.id, client.me.id)] = group_call
        try:
            await group_call.start(message.chat.id)
        except BaseException as e:
            return await u_s.edit(f"<b>Error:</b> <code>{e}</code>")
        group_call.add_handler(playout_ended_handler, GroupCallFileAction.PLAYOUT_ENDED)
        group_call.input_filename = raw_file_name
        return await u_s.edit(
            f"🔖 <b>Sedang memainkan</b> \n\n📀 <b>Judul</b>: {vid_title}\n 💌 <b>Group</b>: {message.chat.title}"
        )
    if os.path.exists(group_call.input_filename):
        os.remove(group_call.input_filename)
    elif not group_call.is_connected:
        try:
            await group_call.start(message.chat.id)
        except BaseException as e:
            return await u_s.edit(f"<b>Error:</b> {e}")
        group_call.add_handler(playout_ended_handler, GroupCallFileAction.PLAYOUT_ENDED)
        group_call.input_filename = raw_file_name
        group_call.song_name = vid_title
        return await u_s.edit(
            f"🔖 <b>Sedang memainkan</b> \n\n📀 <b>Judul</b>: {vid_title}\n 💌 <b>Group</b>: {message.chat.title}"
        )
    else:
        s_d = s_dict.get((message.chat.id, client.me.id))
        f_info = {
            "song_name": vid_title,
            "raw": raw_file_name,
            "singer": uploade_r,
            "dur": dur,
            "url": url,
        }
        if s_d:
            s_d.append(f_info)
        else:
            s_dict[(message.chat.id, client.me.id)] = [f_info]
        s_d = s_dict.get((message.chat.id, client.me.id))
        return await u_s.edit(
            f"✚ <b>Ditambahkan ke antrian</b>\n 🔖 <b>Judul</b>: {vid_title}\n 📑 <b>Di posisi</b>: #{len(s_d)+1}"
        )


@run_in_exc
def convert_to_raw(audio_original, raw_file_name):
    ffmpeg.input(audio_original).output(
        raw_file_name,
        format="s16le",
        acodec="pcm_s16le",
        ac=2,
        ar="48k",
        loglevel="error",
    ).overwrite_output().run()
    return raw_file_name


def edit_msg(client, message, to_edit):
    try:
        client.loop.create_task(message.edit(to_edit))
    except MessageNotModified:
        pass
    except FloodWait as e:
        client.loop.create_task(asyncio.sleep(e.x))
    except TypeError:
        pass


def download_progress_hook(d, message, client, start):
    if d["status"] == "downloading":
        current = d.get("_downloaded_bytes_str") or humanbytes(
            d.get("downloaded_bytes", 1)
        )
        d.get("_total_bytes_str") or d.get("_total_bytes_estimate_str")
        d.get("filename")
        d.get("_eta_str", "N/A")
        d.get("_percent_str", "N/A")
        d.get("_speed_str", "N/A")
        to_edit = "<b>🔄 Processing</b>"
        threading.Thread(target=edit_msg, args=(client, message, to_edit)).start()


@run_in_exc
def yt_dl(url, client, message, start):
    opts = {
        "format": "bestaudio",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "progress_hooks": [lambda d: download_progress_hook(d, message, client, start)],
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3"}],
        "outtmpl": "%(id)s",
        "quiet": True,
        "logtostderr": False,
    }
    with YoutubeDL(opts) as ytdl:
        ytdl_data = ytdl.extract_info(url, download=True)
    return str(ytdl_data["id"]) + ".mp3"


RD_ = {}
FFMPEG_PROCESSES = {}


@bots.on_message(filters.me & filters.command(["pause"], cmd))
async def no_song_play(client, message):
    group_call = GPC.get((message.chat.id, client.me.id))
    if not group_call:
        await eor(message, "<b>Tidak Ada Pemutaran</b>")
        return
    if not group_call.is_connected:
        await eor(message, "<b>Tidak Ada Pemutaran</b>")
        return
    await eor(message, "⏸ <b>Pemutaran Dijeda.</b>")
    group_call.pause_playout()


@bots.on_message(filters.me & filters.command(["resume"], cmd))
async def wow_dont_stop_songs(client, message):
    group_call = GPC.get((message.chat.id, client.me.id))
    if not group_call:
        await eor(message, "<b>Tidak Ada Pemutaran</b>")
        return
    if not group_call.is_connected:
        await eor(message, "<b>Tidak Ada Pemutaran</b>")
        return
    group_call.resume_playout()
    await eor(message, "▶️<b>Pemutaran Dilanjutkan.</b>")


@bots.on_message(filters.me & filters.command(["end"], cmd))
async def leave_vc_test(client, message):
    group_call = GPC.get((message.chat.id, client.me.id))
    if not group_call:
        await eor(message, "<b>Tidak Ada Pemutaran</b>")
        return
    if not group_call.is_connected:
        await eor(message, "<b>Tidak Ada Pemutaran</b>")
        return
    if os.path.exists(group_call.input_filename):
        os.remove(group_call.input_filename)
    await group_call.stop()
    await eor(message, "❌ <b>Pemutaran Dihentikan.</b>")
    del GPC[(message.chat.id, client.me.id)]


__MODULE__ = "music"
__HELP__ = f"""
✘ Bantuan Untuk Music

๏ Perintah: <code>{cmd}skip</code>
◉ Penjelasan: Untuk melewati trek.

๏ Perintah: <code>{cmd}pause</code>
◉ Penjelasan: Untuk menjeda lagu.

๏ Perintah: <code>{cmd}resume</code>
◉ Penjelasan: Untuk melanjutkan lagu.

๏ Perintah: <code>{cmd}play</code> [judul lagu/balas audio/link youtube]
◉ Penjelasan: Untuk memutar lagu.

๏ Perintah: <code>{cmd}end</code>
◉ Penjelasan: Untuk memberhentikan pemutaran.

๏ Perintah: <code>{cmd}playlist</code>
◉ Penjelasan: Untuk melihat daftar putar.
"""
