import asyncio
import os
from io import BytesIO

from pyrogram import filters
from pyrogram.enums import MessageMediaType
from pyrogram.raw.functions.messages import DeleteHistory

from . import *

__MODULE__ = "Convert"
__HELP__ = f"""
๏ Perintah: <code>{cmd}toaudio</code> [reply to video]
◉ Penjelasan: Untuk merubah video menjadi audio mp3.
           
๏ Perintah: <code>{cmd}toanime</code> [reply to photo]
◉ Penjelasan: Untuk merubah foto menjadi anime.

๏ Perintah: <code>{cmd}toimg</code> [balas stikers]
◉ Penjelasan: Untuk membuat nya menjadi foto.
"""


@bots.on_message(filters.me & filters.command("toanime", cmd))
async def _(client, message):
    Tm = await eor(message, "<b>Tunggu sebentar...</b>")
    if message.reply_to_message:
        if len(message.command) < 2:
            if message.reply_to_message.photo:
                type = "Foto"
                get_photo = message.reply_to_message.photo.file_id
            if message.reply_to_message.sticker:
                type = "Stiker"
            if message.reply_to_message.animation:
                type = "Animasi"
            path = await client.download_media(message.reply_to_message)
            with open(path, "rb") as f:
                content = f.read()
            os.remove(path)
            get_photo = BytesIO(content)
        else:
            if message.command[1] in ["foto", "profil", "photo"]:
                chat = (
                    message.reply_to_message.from_user
                    or message.reply_to_message.sender_chat
                )
                type = "Foto"
                get = await client.get_chat(chat.id)
                photo = get.photo.big_file_id
                get_photo = await client.download_media(photo)
    else:
        if len(message.command) < 2:
            return await Tm.edit(
                "Balas ke foto dan saya akan merubah foto anda menjadi anime"
            )
        else:
            type = "Foto"
            get = await client.get_chat(message.command[1])
            photo = get.photo.big_file_id
            get_photo = await client.download_media(photo)
    await client.unblock_user("@qq_neural_anime_bot")
    Tm_S = await client.send_photo("@qq_neural_anime_bot", get_photo)
    await Tm.edit("<b>Sedang diproses...</b>")
    await Tm_S.delete()
    await asyncio.sleep(30)
    async for anime in client.search_messages("@qq_neural_anime_bot"):
        try:
            if anime.photo:
                await client.copy_media_group(
                    message.chat.id,
                    "@qq_neural_anime_bot",
                    anime.id,
                    captions=[f"@{bot.me.username}", f"@{bot.me.username}"],
                    reply_to_message_id=message.id,
                )
                await Tm.delete()
            elif "Failed" in anime.text:
                await Tm.edit(anime.text)
            elif "You're" in anime.text:
                await Tm.edit(anime.text)
        except:
            await Tm.edit(
                f"<b>Gagal merubah {type} menjadi anime,\nSilahkan ulangi beberapa saat lagi</b>"
            )
        user_info = await client.resolve_peer("@qq_neural_anime_bot")
        return await client.send(DeleteHistory(peer=user_info, max_id=0, revoke=True))


@bots.on_message(filters.me & filters.command("toaudio", cmd))
async def _(client, message):
    replied = message.reply_to_message
    Tm = await eor(message, "<b>Tunggu sebentar</b>")
    if not replied:
        await Tm.edit("<b>Mohon Balas Ke Video</b>")
        return
    if replied.media == MessageMediaType.VIDEO:
        await Tm.edit("<b>Downloading Video . . .</b>")
        file = await client.download_media(
            message=replied,
            file_name="logs/",
        )
        out_file = file + ".mp3"
        try:
            await Tm.edit("<b>Mencoba Ekstrak Audio. . .</b>")
            cmd = f"ffmpeg -i {file} -q:a 0 -map a {out_file}"
            await run_cmd(cmd)
            await Tm.edit("<b>Uploading Audio . . .</b>")
            await client.send_audio(
                message.chat.id,
                audio=out_file,
                reply_to_message_id=message.id,
            )
            await Tm.delete()
        except BaseException as e:
            await Tm.edit(f"<b>INFO:</b> {e}")
    else:
        await Tm.edit("<b>Mohon Balas Ke Video</b>")
        return
