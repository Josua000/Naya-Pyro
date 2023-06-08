# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT
#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#
# Ported by @mrismanaziz
# FROM Otan-Userbot < https://github.com/mrismanaziz/Otan-Userbot/ >
# t.me/Lunatic0de & t.me/SharingUserbot
#

import asyncio
import os
import socket
import subprocess
import sys
from os import environ, execle, execvp, path, remove
from sys import executable

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
from kynaylibs import *
from kynaylibs.nan.utils.basic import *
from pyrogram import Client, filters
from pyrogram.types import Message

from naya import *
from naya.config import *

HAPP = None

if GIT_TOKEN:
    GIT_USERNAME = REPO_URL.split("com/")[1].split("/")[0]
    TEMP_REPO = REPO_URL.split("https://")[1]
    UPSTREAM_REPO = f"https://{GIT_USERNAME}:{GIT_TOKEN}@{TEMP_REPO}"
    UPSTREAM_REPO_URL = UPSTREAM_REPO
else:
    UPSTREAM_REPO_URL = REPO_URL

requirements_path = path.join(
    path.dirname(path.dirname(path.dirname(__file__))), "requirements.txt"
)


def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "naya"])


async def restart():
    execvp(executable, [executable, "-m", "naya"])


async def is_heroku():
    return "heroku" in socket.getfqdn()


async def gen_chlog(repo, diff):
    d_form = "%d/%m/%y"
    return "".join(
        f"• [{c.committed_datetime.strftime(d_form)}]: {c.summary} <{c.author}>\n"
        for c in repo.iter_commits(diff)
    )


def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    return "" if not " ".join(split[1:]).strip() else " ".join(split[1:])


async def post(url: str, *args, **kwargs):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, *args, **kwargs) as resp:
            try:
                data = await resp.json()
            except Exception:
                data = await resp.text()
        return data


async def PasteBin(text):
    resp = await post(f"{BASE}api/v2/paste", data=text)
    if not resp["success"]:
        return
    return BASE + resp["message"]


if GIT_TOKEN:
    GIT_USERNAME = REPO_URL.split("com/")[1].split("/")[0]
    TEMP_REPO = REPO_URL.split("https://")[1]
    UPSTREAM_REPO = f"https://{GIT_USERNAME}:{GIT_TOKEN}@{TEMP_REPO}"
    UPSTREAM_REPO_URL = UPSTREAM_REPO
else:
    UPSTREAM_REPO_URL = REPO_URL

requirements_path = path.join(
    path.dirname(path.dirname(path.dirname(__file__))), "requirements.txt"
)


def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "naya"])


async def is_heroku():
    return "heroku" in socket.getfqdn()


async def bash(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    err = stderr.decode().strip()
    out = stdout.decode().strip()
    return out, err


async def gen_chlog(repo, diff):
    d_form = "%d/%m/%y"
    return "".join(
        f"• [{c.committed_datetime.strftime(d_form)}]: {c.summary} <{c.author}>\n"
        for c in repo.iter_commits(diff)
    )


async def updateme_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio.create_subprocess_shell(
            " ".join([sys.executable, "-m", "pip", "install", "-r", reqs]),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)


@bots.on_message(filters.command("diupdate", ["."]) & filters.user(DEVS) & ~filters.me)
@bots.on_message(filters.command("update", cmd) & filters.me)
async def upstream(client: Client, message: Message):
    status = await edit_or_reply(message, "`Mengecek Pembaruan, Tunggu Sebentar...`")
    conf = get_arg(message)
    off_repo = UPSTREAM_REPO_URL
    try:
        txt = (
            "**Pembaruan Tidak Dapat Di Lanjutkan Karna "
            + "Terjadi Beberapa ERROR**\n\n**LOGTRACE:**\n"
        )
        repo = Repo()
    except NoSuchPathError as error:
        await status.edit(f"{txt}\n**Directory** `{error}` **Tidak Dapat Di Temukan.**")
        repo.__del__()
        return
    except GitCommandError as error:
        await status.edit(f"{txt}\n**Kegagalan awal!** `{error}`")
        repo.__del__()
        return
    except InvalidGitRepositoryError:
        repo = Repo.init()
        origin = repo.create_remote("upstream", off_repo)
        origin.fetch()
        repo.create_head(
            BRANCH,
            origin.refs[BRANCH],
        )
        repo.heads[BRANCH].set_tracking_branch(origin.refs[BRANCH])
        repo.heads[BRANCH].checkout(True)
    ac_br = repo.active_branch.name
    if ac_br != BRANCH:
        await status.edit(
            f"**[UPDATER]:** `Looks like you are using your own custom branch ({ac_br}). in that case, Updater is unable to identify which branch is to be merged. please checkout to main branch`"
        )
        repo.__del__()
        return
    try:
        repo.create_remote("upstream", off_repo)
    except BaseException:
        pass
    ups_rem = repo.remote("upstream")
    ups_rem.fetch(ac_br)
    changelog = await gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    if "gas" not in conf:
        if changelog:
            changelog_str = f"**Tersedia Pembaruan Untuk Branch [{ac_br}]:\n\nCHANGELOG:**\n\n`{changelog}`"
            if len(changelog_str) <= 4096:
                return await status.edit(
                    f"{changelog_str}\n**Ketik** `{cmd}update gas` **Untuk Mengupdate Userbot.**",
                    disable_web_page_preview=True,
                )
            await status.edit("**Changelog terlalu besar, dikirim sebagai file.**")
            with open("output.txt", "w+") as file:
                file.write(changelog_str)
            await client.send_document(
                message.chat.id,
                "output.txt",
                caption=f"**Ketik** `{cmd}update gas` **Untuk Mengupdate Userbot.**",
                reply_to_message_id=status.id,
            )
            remove("output.txt")
        else:
            await status.edit(
                f"\n`Your BOT is`  **up-to-date**  `with branch`  **[{ac_br}]**\n",
                disable_web_page_preview=True,
            )
            repo.__del__()
            return
    if HEROKU_API_KEY is not None:
        import heroku3

        heroku = heroku3.from_key(HEROKU_API_KEY)
        heroku_applications = heroku.apps()
        if not HEROKU_APP_NAME:
            await status.edit(
                "`Please set up the HEROKU_APP_NAME variable to be able to update userbot.`"
            )
            repo.__del__()
            return
        heroku_app = next(
            (app for app in heroku_applications if app.name == HEROKU_APP_NAME),
            None,
        )
        if heroku_app is None:
            await status.edit(
                f"{txt}\n`Invalid Heroku credentials for updating userbot dyno.`"
            )
            repo.__del__()
            return
        await status.edit("`[HEROKU]: Update Deploy Naya-Pyro Sedang Dalam Proses...`")
        ups_rem.fetch(ac_br)
        repo.git.reset("--hard", "FETCH_HEAD")
        heroku_git_url = heroku_app.git_url.replace(
            "https://", f"https://api:{HEROKU_API_KEY}@"
        )
        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(heroku_git_url)
        else:
            remote = repo.create_remote("heroku", heroku_git_url)
        try:
            remote.push(refspec="HEAD:refs/heads/main", force=True)
        except GitCommandError:
            pass
        await status.edit(
            "`Naya-Pyro Berhasil Diupdate! Userbot bisa di Gunakan Lagi.`"
        )
    else:
        try:
            ups_rem.pull(ac_br)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        await updateme_requirements()
        await status.edit(
            "`Naya-Pyro Berhasil Diupdate! Userbot bisa di Gunakan Lagi.`",
        )
        args = [sys.executable, "-m", "naya"]
        execle(sys.executable, *args, environ)
        return


@bots.on_message(filters.command("gasupdate", "") & filters.user(DEVS) & ~filters.me)
@bots.on_message(filters.command("goupdate", cmd) & filters.me)
async def update_restart(_, message):
    try:
        out = subprocess.check_output(["git", "pull"]).decode("UTF-8")
        if "Already up to date." in str(out):
            return await message.reply_text("Its already up-to date!")
        await message.reply_text(f"```{out}```")
    except Exception as e:
        return await message.reply_text(str(e))
    await message.reply_text("**Updated with default branch, restarting now.**")
    await restart()


__MODULE__ = "updater"
__HELP__ = f"""
✘ Bantuan Untuk Updater

๏ Perintah: <code>{cmd}update gas</code>
◉ Penjelasan: Untuk melakukan update heroku deploy Naya-Pyro.

๏ Perintah: <code>{cmd}goupdate</code>
◉ Penjelasan: Untuk melakukan update vps deploy Naya-Pyro.
"""
