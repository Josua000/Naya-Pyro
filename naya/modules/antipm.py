# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


from kynaylibs.nan.utils.db import permit as set
from pyrogram import filters

from . import *
from .apm import get_arg


@bots.on_message(filters.me & filters.command("antipm", cmd))
async def pm_permit(client, message):
    arg = get_arg(message)
    user_id = client.me.id
    if not arg:
        await eor(message, "<b>Gunakan format</b>:\n <code>antipm</code> on atau off")
        return
    if arg == "off":
        await set.set_pm(user_id, False)
        await eor(message, "<b>AntiPM Dimatikan</b>")
    elif arg == "on":
        await set.set_pm(user_id, True)
        await eor(message, "<b>AntiPM Diaktifkan</b>")


@bots.on_message(filters.me & filters.command("setmsg", cmd))
async def setpmmsg(client, message):
    if message.reply_to_message:
        naya = message.reply_to_message.text
    else:
        naya = message.text.split(None, 1)[1]
    user_id = client.me.id
    if not naya:
        await eor(
            message,
            "<b>Berikan pesan untuk mengatur</b>\nContoh : <code>setpm</code>[balas pesan atau berikan pesan].",
        )
        return
    if naya == "default":
        await set.set_permit_message(user_id, set.PMPERMIT_MESSAGE)
        await eor(message, "<b>Pesan AntiPM Diatur ke Default</b>.")
        return
    await set.set_permit_message(user_id, f"<code>{naya}</code>")
    await eor(message, f"<b>Berhasil mengatur pesan AntiPM</b> ke <code>{naya}</code>")


__MODULE__ = "Anti PM"
__HELP__ = f"""
๏ Perintah: <code>{cmd}antipm</code> [on atau off]
◉ Penjelasan: Untuk menghidupkan atau mematikan antipm

๏ Perintah: <code>{cmd}setmsg</code> [balas atau berikan pesan]
◉ Penjelasan: Untuk mengatur pesan antipm.

๏ Perintah: <code>{cmd}setblock</code> [balas atau berikan pesan]
◉ Penjelasan: Untuk mengatur pesan blokir.

๏ Perintah: <code>{cmd}setlimit</code> [angka]
◉ Penjelasan: Untuk mengatur peringatan pesan blokir.

๏ Perintah: <code>{cmd}ok</code>
◉ Penjelasan: Untuk menyetujui pesan.

๏ Perintah: <code>{cmd}no</code>
◉ Penjelasan: Untuk menolak pesan.

◉ Notes: Untuk mengatur ke default ketik
<code>{cmd}setmsg default</code>
<code>{cmd}setblock default</code>
<code>{cmd}setlimit default</code>
"""
