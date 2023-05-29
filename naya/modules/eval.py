import sys
import traceback
from io import BytesIO, StringIO
import asyncio
import pyromod
from io import BytesIO
import io
import os
import sys
import re
import traceback
import subprocess
from random import randint
from typing import Optional
from contextlib import suppress
from asyncio import sleep
from io import StringIO
from pyrogram import *
from pyrogram.types import *

from . import *

__MODULE__ = "devs"

__HELP__ = f"""
✘ Bantuan Untuk Devs

๏ Perintah: <code>{cmd}eval</code>
◉ Penjelasan: You know bruh.

๏ Perintah: <code>{cmd}trash</code>
◉ Penjelasan: You know bruh.

๏ Perintah: <code>{cmd}sh</code>
◉ Penjelasan: You know bruh.
"""


@bots.on_message(filters.command("sh", cmd) & filters.me)
async def _(client, message):
    cmd = message.text.split(" ", maxsplit=1)[1]

    reply_to_id = message.id
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.id

    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    e = stderr.decode()
    if not e:
        e = "No errors"
    o = stdout.decode()
    if not o:
        o = "No output"

    OUTPUT = ""
    OUTPUT += f"<b>Command:</b>\n<code>{cmd}</code>\n\n"
    OUTPUT += f"<b>Output</b>: \n<code>{o}</code>\n"
    OUTPUT += f"<b>Errors</b>: \n<code>{e}</code>"

    if len(OUTPUT) > 4096:
        with open("exec.text", "w+", encoding="utf8") as out_file:
            out_file.write(str(OUTPUT))
        await message.reply_document(
            document="exec.text",
            caption=cmd,
            disable_notification=True,
            reply_to_message_id=ReplyCheck(message),
        )
        os.remove("exec.text")
    else:
        await message.reply_text(OUTPUT)


@bots.on_message(filters.command("trash", cmd) & filters.me)
async def _(client, message):
    if not message.reply_to_message:
        return await eor(message, "`Reply ke pesan/media`")
    if len(str(message.reply_to_message)) <= 4096:
        return await message.reply_text(message.reply_to_message)
    with BytesIO(str.encode(str(message.reply_to_message))) as out_file:
        out_file.name = "result.txt"
        return await message.reply_document(
            document=out_file,
        )


@bots.on_message(filters.command("eval", cmd) & filters.me)
async def _(client, message):
    if ajg := get_arg(message):
        await eor(message, "`Processing ...`")
    else:
        return await eor(message, "`Give me commands dude...`")
    cmd = message.text.split(" ", maxsplit=1)[1]
    reply_to_ = message.reply_to_message or message
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    final_output = "OUTPUT:\n"
    final_output += f"{evaluation.strip()}"
    if len(final_output) > 4096:
        with BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await reply_to_.reply_document(
                document=out_file,
                caption=cmd[: 4096 // 4 - 1],
                disable_notification=True,
                quote=True,
            )
    else:
        await reply_to_.reply_text(final_output, quote=True)
    # await TM.delete()
