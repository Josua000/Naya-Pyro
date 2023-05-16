from pyrogram import filters
from pyrogram.errors.exceptions.bad_request_400 import ChatNotModified
from pyrogram.types import ChatPermissions

from . import *

incorrect_parameters = "<b>Parameter Salah, Periksa Locks Parameter</b>."

data = {
    "msg": "can_send_messages",
    "stickers": "can_send_other_messages",
    "gifs": "can_send_other_messages",
    "media": "can_send_media_messages",
    "games": "can_send_other_messages",
    "inline": "can_send_other_messages",
    "url": "can_add_web_page_previews",
    "polls": "can_send_polls",
    "info": "can_change_info",
    "invite": "can_invite_users",
    "pin": "can_pin_messages",
}


async def current_chat_permissions(client, chat_id):
    perms = []
    perm = (await client.get_chat(chat_id)).permissions
    if perm.can_send_messages:
        perms.append("can_send_messages")
    if perm.can_send_media_messages:
        perms.append("can_send_media_messages")
    if perm.can_send_other_messages:
        perms.append("can_send_other_messages")
    if perm.can_add_web_page_previews:
        perms.append("can_add_web_page_previews")
    if perm.can_send_polls:
        perms.append("can_send_polls")
    if perm.can_change_info:
        perms.append("can_change_info")
    if perm.can_invite_users:
        perms.append("can_invite_users")
    if perm.can_pin_messages:
        perms.append("can_pin_messages")

    return perms


async def tg_lock(client, message, permissions: list, perm: str, lock: bool):
    if lock:
        if perm not in permissions:
            return await eor(message, "<b>🔒 Sudah Terkunci.</b>")
        permissions.remove(perm)
    else:
        if perm in permissions:
            return await eor(message, "<b>🔓 Sudah Terbuka.</b>")
        permissions.append(perm)

    permissions = {perm: True for perm in list(set(permissions))}

    try:
        await client.set_chat_permissions(
            message.chat.id, ChatPermissions(**permissions)
        )
    except ChatNotModified:
        return await eor(
            "<b>Untuk membuka kunci ini, Anda harus membuka 'pesan' terlebih dahulu.</b>"
        )

    await eor(
        message, ("<b>🔒 Sudah Terkunci.</b>" if lock else "<b>🔓 Sudah Terbuka.</b>")
    )


@bots.on_message(filters.command(["lock", "unlock"], cmd) & filters.me)
async def locks_func(client, message):
    if len(message.command) != 2:
        return await message.eor(message, incorrect_parameters)

    chat_id = message.chat.id
    parameter = message.text.strip().split(None, 1)[1].lower()
    state = message.command[0].lower()

    if parameter not in data and parameter != "all":
        return await message.eor(message, incorrect_parameters)

    permissions = await current_chat_permissions(client, chat_id)

    if parameter in data:
        await tg_lock(
            client,
            message,
            permissions,
            data[parameter],
            bool(state == "lock"),
        )
    elif parameter == "all" and state == "lock":
        await client.set_chat_permissions(chat_id, ChatPermissions())
        await eor(
            message, f"🔒 <b>Lock untuk semua</b> <code>{message.chat.title}</code>"
        )

    elif parameter == "all" and state == "unlock":
        await client.set_chat_permissions(
            chat_id,
            ChatPermissions(
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_other_messages=True,
                can_add_web_page_previews=True,
                can_send_polls=True,
                can_change_info=False,
                can_invite_users=True,
                can_pin_messages=False,
            ),
        )
        await eor(
            message, f"🔓 <b>Unlock untuk semua</b> <code>{message.chat.title}</code>"
        )


@bots.on_message(filters.command("locks", cmd) & filters.me)
async def locktypes(client, message):
    permissions = await current_chat_permissions(client, message.chat.id)

    if not permissions:
        return await eor(message, "<code>Anda bukan Admin.</code>.")

    perms = ""
    for i in permissions:
        perms += f"__<b>{i}</b>__\n"

    await eor(message, perms)


@bots.on_message(filters.text & ~filters.private, group=4)
async def url_detector(client, message):
    user = message.from_user
    chat_id = message.chat.id
    text = message.text.lower().strip()

    if not text or not user:
        return
    mods = await list_admins(client, chat_id)
    if user.id in mods:
        return

    check = get_urls_from_text(text)
    if check:
        permissions = await current_chat_permissions(client, chat_id)
        if "can_add_web_page_previews" not in permissions:
            try:
                await message.delete()
            except Exception:
                await eor(
                    message,
                    "This message contains a URL, "
                    + "but i don't have enough permissions to delete it",
                )


__MODULE__ = "Locks"
__HELP__ = f"""
๏ Perintah: <code>{cmd}lock or unlock</code> [query]
◉ Penjelasan: Untuk mengunci atau membuka izin grup.

๏ Perintah: <code>{cmd}locks</code>
◉ Penjelasan: Untuk izin grup.

Spesifikasi Kunci : Locks / Unlocks: <code>msg</code> | <code>media</code> | <code>stickers</code> | <code>polls</code> | <code>info</code>  | <code>invite</code> | <code>url</code> |<code>pin</code> | <code>all</code>.
"""
