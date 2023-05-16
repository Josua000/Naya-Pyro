# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


from kynaylibs.nan.utils.db import permit as set
from kynaylibs.nan.utils.db.permit import *
from pyrogram import enums, filters

from . import *

PM_LOGGER = 1
FLOOD_CTRL = 0
ALLOWED = []
USERS_AND_WARNS = {}


class LOG_CHATS:
    def __init__(self):
        self.RECENT_USER = None
        self.NEWPM = None
        self.COUNT = 0


LOG_CHATS_ = LOG_CHATS()


async def denied_users(filter, client, message):
    user_id = client.me.id
    if not await pm_guard(user_id):
        return False
    if message.chat.id in (await get_approved_users(user_id)):
        return False
    else:
        return True


@bots.on_message(filters.me & filters.command("setlimit", cmd))
async def pmguard(client, message):
    user_id = client.me.id
    arg = get_arg(message)
    if not arg:
        await eor(
            message,
            "<b>Berikan Angka\n<b>Contoh</b>: <code>setlimit 5</code> defaultnya adalah 5</b>.",
        )
        return
    await set.set_limit(user_id, int(arg))
    await eor(message, f"<b>Limit diatur ke <code>{arg}</code></b>")


@bots.on_message(filters.me & filters.command("setblock", cmd))
async def setpmmsg(client, message):
    user_id = client.me.id
    if message.reply_to_message:
        naya = message.reply_to_message.text
    else:
        naya = message.text.split(None, 1)[1]
    if not naya:
        await eor(
            message,
            "<b>Berikan pesan untuk mengatur</b>\nContoh : <code>setblock</code>[balas pesan atau berikan pesan]",
        )
        return
    if naya == "default":
        await set.set_block_message(user_id, set.BLOCKED)
        await eor(message, "<b>Pesan Blokir Diatur ke Default</b>.")
        return
    await set.set_block_message(user_id, f"<code>{naya}</code>")
    await eor(message, f"<b>Pesan Blokir Berhasil Diatur Ke <code>{naya}</code></b>")


@bots.on_message(filters.me & filters.command("ok", cmd))
async def allow(client, message):
    user_id = client.me.id

    chat_id = message.chat.id

    pmpermit, pm_message, limit, block_message = await get_pm_settings(user_id)
    await set.allow_user(chat_id)
    await eor(
        message,
        f"<b>Disetujui untuk mengirim pesan</b>",
    )
    async for message in client.search_messages(
        chat_id=message.chat.id, query=pm_message, limit=1, from_user="me"
    ):
        await message.delete()
    USERS_AND_WARNS.update({chat_id: 0})


@bots.on_message(filters.me & filters.command("no", cmd))
async def deny(client, message):
    chat_id = message.chat.id

    await set.deny_user(chat_id)
    await eor(
        message,
        f"<b>Saya belum menyetujui kamu untuk mengirim pesan.</b>",
    )


@bots.on_message(
    filters.private
    & filters.create(denied_users)
    & filters.incoming
    & ~filters.service
    & ~filters.me
    & ~filters.bot
)
async def reply_pm(client, message):
    user_id = client.me.id
    chat_id = message.chat.id

    global FLOOD_CTRL
    pmpermit, pm_message, limit, block_message = await set.get_pm_settings(user_id)
    user = message.from_user.id
    biji = message.from_user.first_name
    user_warns = 0 if user not in USERS_AND_WARNS else USERS_AND_WARNS[user]
    if user in DEVS:
        try:
            await set.allow_user(chat_id)
            await client.send_message(
                chat_id,
                f"<b>Menerima Pesan!!!</b>\n{biji} <b>Terdeteksi Developer SkyProject Ubot.</b>",
                parse_mode=enums.ParseMode.HTML,
            )
        except:
            pass
        return
    elif user_warns <= limit - 2:
        user_warns += 1
        USERS_AND_WARNS.update({user: user_warns})
        if not FLOOD_CTRL > 0:
            FLOOD_CTRL += 1
        else:
            FLOOD_CTRL = 0
            return
        async for message in client.search_messages(
            chat_id=message.chat.id, query=pm_message, limit=1, from_user="me"
        ):
            await message.delete()
        await message.reply(pm_message, disable_web_page_preview=True)
        return
    await message.reply(block_message, disable_web_page_preview=True)
    await client.block_user(message.chat.id)
    USERS_AND_WARNS.update({user: 0})


@bots.on_message(
    filters.private & filters.incoming & ~filters.service & ~filters.me & ~filters.bot
)
async def pm_log(client, message):
    user = message.from_user.id
    biji = message.from_user.mention
    message.text
    user_id = client.me.id
    botlog = await get_log_groups(user_id)
    if message.chat.id != 777000:
        if LOG_CHATS_.RECENT_USER != message.chat.id:
            LOG_CHATS_.RECENT_USER = message.chat.id
            if LOG_CHATS_.NEWPM:
                await LOG_CHATS_.NEWPM.edit(
                    LOG_CHATS_.NEWPM.text.replace(
                        "**💌 #NEW_MESSAGE**",
                        f" • `{LOG_CHATS_.COUNT}` **Pesan**",
                    )
                )
                LOG_CHATS_.COUNT = 0
            LOG_CHATS_.NEWPM = await client.send_message(
                botlog,
                f"💌 <b><u>MENERUSKAN PESAN BARU</u></b>\n<b> • Dari :</b> {biji}\n<b> • User ID :</b> <code>{user}</code>\n",
                parse_mode=enums.ParseMode.HTML,
            )
        try:
            async for pmlog in client.search_messages(message.chat.id, limit=1):
                await pmlog.forward(botlog)
            LOG_CHATS_.COUNT += 1
        except BaseException:
            pass
