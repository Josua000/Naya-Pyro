# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT

import re

from pyrogram import filters

from . import *

__MODULE__ = "filter"
__HELP__ = f"""
✘ Bantuan Untuk Filter

๏ Perintah: <code>{cmd}addfil</code> [nama filter] [balas ke pesan]
◉ Penjelasan: Untuk mengatur filter grup.

๏ Perintah: <code>{cmd}delfil</code> [nama filter]
◉ Penjelasan: Untuk menghapus filter grup.

๏ Perintah: <code>{cmd}filters</code>
◉ Penjelasan: Untuk melihat filter grup.
"""


@bots.on_message(filters.me & filters.command("addfil", cmd))
async def save_filters(client, message):
    if len(message.command) < 2 or not message.reply_to_message:
        return await eor(
            message,
            f"<b>Gunakan Format:</b>\n Balas ke pesan atau sticker <code>addfil</code> [nama filter] [balas ke pesan] untuk save filter.",
        )
    if not message.reply_to_message.text and not message.reply_to_message.sticker:
        return await eor(message, "<b>Hanya bisa save text atau sticker.</b>")
    name = message.text.split(None, 1)[1].strip()
    if not name:
        return await eor(
            message,
            f"<b>Gunakan Format:</b>\n Balas ke pesan atau sticker <code>addfil</code> [nama filter] [balas ke pesan] untuk save filter.",
        )
    chat_id = message.chat.id
    user_id = client.me.id
    if message.chat.id in BL_UBOT:
        await eor(message, "<code>Filter tidak diperkenankan di group support.</code>")
        return
    _type = "text" if message.reply_to_message.text else "sticker"
    _filter = {
        "type": _type,
        "data": message.reply_to_message.text.markdown
        if _type == "text"
        else message.reply_to_message.sticker.file_id,
    }
    await save_filter(user_id, chat_id, name, _filter)
    await eor(message, f"<b>Filter <code>{name}</code> disimpan!.</b>")


@bots.on_message(filters.me & filters.command("filters", cmd))
async def get_filterss(client, message):
    user_id = client.me.id
    chat_id = message.chat.id
    _filters = await get_filters_names(user_id, chat_id)
    if not _filters:
        return await eor(message, "<b>Tidak ada filter tersimpan di group ini.</b>")
    _filters.sort()
    msg = f"๏ Daftar filter tersimpan di <code>{message.chat.title}</code>\n"
    for _filter in _filters:
        msg += f"<b>•<b> <code>{_filter}</code>\n"
    await eor(message, msg)


@bots.on_message(filters.me & filters.command("delfil", cmd))
async def del_filter(client, message):
    if len(message.command) < 2:
        return await eor(
            message, f"<b>Gunakan Format:</b>\n<code>delfil</code> [nama filter]"
        )
    user_id = client.me.id
    chat_id = message.chat.id
    name = message.text.split(None, 1)[1].strip()
    if not name:
        return await eor(
            message, f"<b>Gunakan format:</b>\n<code>delfil</code> [nama filter]"
        )

    deleted = await delete_filter(user_id, chat_id, name)
    if deleted:
        await eor(message, f"<b>Filter <code>{name}</code> berhasil dihapus.</b>")
    else:
        await eor(message, "<b>Filter tidak ditemukan.</b>")


@bots.on_message(
    filters.text & ~filters.private & ~filters.via_bot & ~filters.forwarded, group=1
)
async def filters_re(client, message):
    text = message.text.lower().strip()
    if not text:
        return
    user_id = client.me.id
    chat_id = message.chat.id
    list_of_filters = await get_filters_names(user_id, chat_id)
    for word in list_of_filters:
        pattern = r"( |^|[^\w])" + re.escape(word) + r"( |$|[^\w])"
        if re.search(pattern, text, flags=re.IGNORECASE):
            _filter = await get_filter(user_id, chat_id, word)
            data_type = _filter["type"]
            data = _filter["data"]
            if data_type == "text":
                keyb = None
                if re.findall(r"\[.+\,.+\]", data):
                    if keyboard := extract_text_and_keyb(ikb, data):
                        data, keyb = keyboard

                if message.reply_to_message:
                    await message.reply_to_message.reply_text(
                        data,
                        reply_markup=keyb,
                        disable_web_page_preview=True,
                    )

                    if text.startswith("~"):
                        await message.delete()
                    return

                return await message.reply_text(
                    data,
                    reply_markup=keyb,
                    disable_web_page_preview=True,
                )
            if message.reply_to_message:
                await message.reply_to_message.reply_sticker(data)

                if text.startswith("~"):
                    await message.delete()
                return
            return await message.reply_sticker(data)
