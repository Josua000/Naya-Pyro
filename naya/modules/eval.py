import os
import sys
import traceback
from io import BytesIO, StringIO
from subprocess import PIPE, Popen, TimeoutExpired
from time import perf_counter

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
async def shell(_, message: Message):
    if len(message.command) < 2:
        return await message.reply("<b>Specify the command in message text</b>")
    cmd_text = message.text.split(maxsplit=1)[1]
    cmd_obj = Popen(
        cmd_text,
        shell=True,
        stdout=PIPE,
        stderr=PIPE,
        text=True,
    )

    char = "#" if os.getuid() == 0 else "$"
    text = f"<b>{char}</b> <code>{cmd_text}</code>\n\n"

    mmk = await message.reply(text + "<b>Running...</b>")
    try:
        start_time = perf_counter()
        stdout, stderr = cmd_obj.communicate(timeout=60)
    except TimeoutExpired:
        text += "<b>Timeout expired (60 seconds)</b>"
    else:
        stop_time = perf_counter()
        if stdout:
            text += f"<b>Output:</b>\n<code>{stdout}</code>\n\n"
        if stderr:
            text += f"<b>Error:</b>\n<code>{stderr}</code>\n\n"
        text += f"<b>Completed in {round(stop_time - start_time, 5)} seconds with code {cmd_obj.returncode}</b>"
        if int(len(str(text))) > 4096:
            with BytesIO(str.encode(str(text))) as out_file:
                out_file.name = "result.txt"
                await message.reply_document(
                    document=out_file,
                )
                await mmk.delete()
        else:
            await mmk.edit(text)
    cmd_obj.kill()


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
