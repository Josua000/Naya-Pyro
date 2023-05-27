import asyncio
import math
import os
import sys
from os import environ, execle, remove

import dotenv
import heroku3
import requests
import urllib3
from dotenv import load_dotenv
from pyrogram import *
from pyrogram.types import *

from naya.config import *

from . import *

HAPP = None

load_dotenv(".env")


def anu_heroku():
    return "DYNO" in os.environ


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "naya"])


XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(HEROKU_API_KEY),
    "https",
    str(HEROKU_APP_NAME),
    "HEAD",
    "main",
]


@bots.on_message(filters.command(["restart"], "") & filters.user(DEVS) & ~filters.me)
@bots.on_message(filters.command("restart", cmd) & filters.me)
async def restart_bot(_, message):
    try:
        msg = await message.reply(" `Restarting bot...`")
        LOGGER(__name__).info("BOT SERVER RESTARTED !!")
    except BaseException as err:
        LOGGER(__name__).info(f"{err}")
        return
    await msg.edit("✅ **Bot has restarted !**\n")
    if HAPP is not None:
        await bash("git pull && pip3 install -U -r requirements.txt")
        HAPP.restart()
    else:
        await bash("git pull && pip3 install -U -r requirements.txt")
        args = [sys.executable, "-m", "naya"]
        execle(sys.executable, *args, environ)


@bots.on_message(filters.command("usage", cmd) & filters.me)
async def usage_dynos(client, message):
    if not await is_heroku():
        return await eor(message, "Hanya untuk Heroku Deployment")
    if HEROKU_API_KEY == cmd and HEROKU_APP_NAME == cmd:
        return await eor(
            message,
            "<b>Menggunakan App Heroku!</b>\n\nMasukan/atur  `HEROKU_API_KEY` dan `HEROKU_APP_NAME` untuk bisa melakukan update!",
        )
    elif HEROKU_API_KEY == cmd or HEROKU_APP_NAME == cmd:
        return await eor(
            message,
            "<b>Menggunakan App Heroku!</b>\n\n<b>pastikan</b> `HEROKU_API_KEY` **dan** `HEROKU_APP_NAME` <b>sudah di configurasi dengan benar!</b>",
        )
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await message.reply_text(
            " Pastikan Heroku API Key, App name sudah benar"
        )
    await eor(message, "Memeriksa penggunaan dyno...")
    account_id = Heroku.account().id
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = f"/accounts/{account_id}/actions/get-quota"
    r = requests.get(f"https://api.heroku.com{path}", headers=headers)
    if r.status_code != 200:
        return await dyno.edit("Unable to fetch.")
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    await asyncio.sleep(1.5)
    text = f"""
**Penggunaan Dyno Naya-Premium**

 ❏ Dyno terpakai:
 ├ Terpakai: `{AppHours}`**h**  `{AppMinutes}`**m**  [`{AppPercentage}`**%**]
Dyno tersisa:
  ╰ Tersisa: `{hours}`**h**  `{minutes}`**m**  [`{percentage}`**%**]"""
    return await message.edit(text)


@bots.on_message(filters.command("shutdown", cmd) & filters.me)
async def shutdown_bot(client, message):
    botlog_chat_id = await get_log_groups(user_id)
    if not botlog_chat_id:
        return await message.reply(
            "`Maaf, tidak dapat menemukan ID chat log bot.`\nPastikan Anda Telah Mengtur Log Group Anda"
        )
    await client.send_message(
        botlog_chat_id,
        "**#SHUTDOWN** \n"
        "**Naya-Premium** telah di matikan!\nJika ingin menghidupkan kembali silahkan buka heroku",
    )
    await message.reply(" **Naya-Premium Berhasil di matikan!**")
    if HAPP is not None:
        HAPP.process_formation()["worker"].scale(0)
    else:
        sys.exit(0)


@bots.on_message(filters.command("logs", cmd) & filters.me)
async def logs_ubot(client, message):
    if HAPP is None:
        return await message.reply(
            "Pastikan `HEROKU_API_KEY` dan `HEROKU_APP_NAME` anda dikonfigurasi dengan benar di config vars heroku",
        )
    biji = await message.reply("🧾 `Get Logs your Bots...`")
    with open("Logs-Heroku.txt", "w") as log:
        log.write(HAPP.get_log())
    await client.send_document(
        message.chat.id,
        "Logs-Heroku.txt",
        thumb="https://telegra.ph//file/976ad753d6073dde1f579.jpg",
        caption="**This is your Heroku Logs**",
    )
    await biji.delete()
    remove("Logs-Heroku.txt")


@bots.on_message(filters.command("setvar", cmd) & filters.me)
async def set_var(client, message):
    if len(message.command) < 3:
        return await eor(message, f"<b>Usage:</b> {cmd}setvar [Var Name] [Var Value]")
    tai = await eor(message, "`Processing...`")
    to_set = message.text.split(None, 2)[1].strip()
    value = message.text.split(None, 2)[2].strip()
    if "HEROKU_APP_NAME" in os.environ and "HEROKU_API_KEY" in os.environ:
        api_key = os.environ["HEROKU_API_KEY"]
        app_name = os.environ["HEROKU_APP_NAME"]
        heroku = heroku3.from_key(api_key)
        app = heroku.apps()[app_name]
        config_vars = app.config()
        if to_set in config_vars:
            config_vars[to_set] = value
            await tai.edit(f"**Berhasil Mengubah var `{to_set}` menjadi `{value}`**")
        else:
            config_vars[to_set] = value
            await tai.edit(f"**Berhasil Menambahkan var `{to_set}` menjadi `{value}`**")
        app.update_config(config_vars)
    else:
        path = ".env"
        if not os.path.exists(path):
            return await tai.edit("`.env file not found.`")
        with open(path, "a") as file:
            file.write(f"\n{to_set}={value}")
        if dotenv.get_key(path, to_set):
            await tai.edit(f"**Berhasil Mengubah var `{to_set}` menjadi `{value}`**")
        else:
            await tai.edit(f"**Berhasil Menambahkan var `{to_set}` menjadi `{value}`**")
        restart()


@bots.on_message(filters.command("delvar", cmd) & filters.me)
async def vardel_(client, message):
    if len(message.command) != 2:
        return await message.edit(f"<b>Usage:</b> {cmd}delvar [Var Name]")
    ajg = await eor(message, "`Processing...`")
    check_var = message.text.split(None, 2)[1]

    if os.environ.get("DYNO"):
        if "HEROKU_APP_NAME" in os.environ and "HEROKU_API_KEY" in os.environ:
            api_key = os.environ["HEROKU_API_KEY"]
            app_name = os.environ["HEROKU_APP_NAME"]

            heroku = heroku3.from_key(api_key)
            app = heroku.apps()[app_name]
            config_vars = app.config()

            if check_var in config_vars:
                del config_vars[check_var]
                await ajg.edit(f"**Berhasil Menghapus var `{check_var}`**")
                app.update_config(config_vars)
            else:
                return await ajg.edit(f"**Tidak dapat menemukan var `{check_var}`**")
        else:
            await ajg.edit(
                "**Pastikan HEROKU_API_KEY dan HEROKU_APP_NAME Anda dikonfigurasi dengan benar di config vars Heroku.**"
            )
    else:
        path = ".env"
        if not os.path.exists(path):
            return await ajg.edit("`.env file not found.`")
        dotenv.unset_key(path, check_var)

        if dotenv.get_key(path, check_var) is None:
            await ajg.edit(f"**Berhasil Menghapus var `{check_var}`.**")
        else:
            return await ajg.edit(f"**Tidak dapat menemukan var `{check_var}`**")

        restart()


@bots.on_message(filters.command("getvar", cmd) & filters.me)
async def varget_(client, message):
    if len(message.command) != 2:
        return await eor(message, f"<b>Usage:</b> {cmd}getvar [Var Name]")
    babi = await eor(message, "`Processing...`")
    check_var = message.text.split(None, 2)[1]
    if anu_heroku():
        return (
            await babi.edit(
                f"<b>{check_var}:</b> <code>{os.environ[check_var]}</code>"
            )
            if check_var in os.environ
            else await babi.edit(
                f"**Tidak dapat menemukan var `{check_var}`.**"
            )
        )
    path = ".env"
    if not os.path.exists(path):
        return await babi.edit("`.env file not found.`")
    if output := dotenv.get_key(path, check_var):
        return await babi.edit(f"<b>{check_var}:</b> <code>{str(output)}</code>")
    else:
        await babi.edit(f"**Tidak dapat menemukan var `{check_var}`.**")


@bots.on_message(filters.command("setdb", cmd) & filters.me)
async def set_db(client, message):
    if len(message.command) < 3:
        await eor(message, f"`Usage: {cmd}setdb [Database Name] [Variable Value].`")
        return
    user_id = client.me.id
    db_name = message.command[1]
    variable_value = message.command[2]
    collection = db[db_name]
    collection.insert_one({"user_id": user_id, "value": variable_value})
    await eor(message, f"**Variabel telah diatur di database `{db_name}`.**")


@bots.on_message(filters.command("deldb", cmd) & filters.me)
async def del_db(client, message):
    if len(message.command) < 2:
        await eor(message, f"`Usage: {cmd}deldb [Database Name].`")
        return
    db_name = message.command[1]
    user_id = client.me.id
    collection = db[db_name]
    collection.delete_one({"user_id": user_id, "value": db_name})
    await message.reply_text(f"**`{db_name}` telah dihapus dari database.**")


__MODULE__ = "heroku"
__HELP__ = f"""
✘ Bantuan Untuk Heroku

๏ Perintah: <code>{cmd}setvar</code> [variable][value]
◉ Penjelasan: Untuk mengatur variable di heroku atau vps.

๏ Perintah: <code>{cmd}delvar</code> [variable]
◉ Penjelasan: Untuk menghapus variable di heroku atau vps.

๏ Perintah: <code>{cmd}getvar</code> [variable]
◉ Penjelasan: Untuk mengambil variable di heroku atau vps.

๏ Perintah: <code>{cmd}usage</code>
◉ Penjelasan: Untuk mengecek dyno heroku only.
"""
