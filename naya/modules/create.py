# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT

from pyrogram import Client
from pyrogram.types import Message

from . import *


@bots.on_message(filters.command(["buat", "create"], cmd) & filters.me)
async def create(client: Client, message: Message):
    if len(message.command) < 3:
        return await message.reply(
            f"**buat gc => Untuk Membuat Grup, buat ch => Untuk Mebuat Channel**"
        )
    group_type = message.command[1]
    split = message.command[2:]
    group_name = " ".join(split)
    xd = await message.edit("`Processing...`")
    desc = "Welcome To My " + ("Group" if group_type == "gc" else "Channel")
    if group_type == "gc":  # for supergroup
        _id = await client.create_supergroup(group_name, desc)
        link = await client.get_chat(_id.id)
        await xd.edit(
            f"**Successfully Created Telegram Group: [{group_name}]({link.invite_link})**",
            disable_web_page_preview=True,
        )
    elif group_type == "ch":  # for channel
        _id = await client.create_channel(group_name, desc)
        link = await client.get_chat(_id.id)
        await xd.edit(
            f"**Successfully Created Telegram Channel: [{group_name}]({link.invite_link})**",
            disable_web_page_preview=True,
        )


__MODULE__ = "Create"
__HELP__ = f"""
๏ Perintah: <code>{cmd}buat or create</code> [gc or ch]
◉ Penjelasan: Untuk membuat supergrup atau channel telegram.
"""
