from pyrogram import filters

from . import *

__MODULE__ = "zombies"
__HELP__ = f"""
✘ Bantuan Untuk Zombie

๏ Perintah: <code>{cmd}zombies</code>
◉ Penjelasan: Untuk mengeluarkan akun depresi digrup anda.
"""


@bots.on_message(filters.command("zombies", cmd) & filters.me)
async def _(client, message):
    chat_id = message.chat.id
    deleted_users = []
    m = await eor(
        message, "<code>Sedang mencari akun-akun depresi ditinggal kawin...</code>"
    )

    async for i in client.get_chat_members(chat_id):
        if i.user.is_deleted:
            deleted_users.append(i.user.id)
    if deleted_users:
        banned_users = 0
        for deleted_user in deleted_users:
            try:
                await message.chat.ban_member(deleted_user)
            except Exception:
                pass
            banned_users += 1
        await m.edit(
            f"<b>Berhasil mengkawinkan {banned_users} Akun Depresi Ditinggal Kawin.</b>"
        )
    else:
        await m.edit("<b>Saya tidak menemukan akun depresi di tinggal kawin.</b>")
