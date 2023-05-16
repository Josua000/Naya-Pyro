import os
import sys
import traceback
from io import BytesIO, StringIO

from . import *

__MODULE__ = "Devs"

__HELP__ = f"""
๏ Perintah: <code>{cmd}eval</code>
◉ Penjelasan: You know bruh.

๏ Perintah: <code>{cmd}trash</code>
◉ Penjelasan: You know bruh.

๏ Perintah: <code>{cmd}sh</code>
◉ Penjelasan: You know bruh.
"""


@bots.on_message(filters.command("sh", cmd) & filters.me)
async def _(client, message):
    if len(message.command) < 2:
        return await eor(message, "`Give me commands dude...`")
    try:
        if message.command[1] == "restart":
            # await message.delete()
            os.system(f"kill -9 {os.getpid()} && python3 -m naya")
        elif message.command[1] == "gitpull":
            # await message.delete()
            os.system(f"kill -9 {os.getpid()} && git pull && python3 -m naya")
            await eor(message, "`Processing...`")
            screen = (await bash(message.text.split(None, 1)[1]))[0]
            if int(len(str(screen))) > 4096:
                with BytesIO(str.encode(str(screen))) as out_file:
                    out_file.name = "result.txt"
                    await message.reply_document(
                        document=out_file,
                    )
                    # await msg.delete()
            else:
                await eor(message, screen)
                # await msg.delete()
    except Exception as error:
        await eor(message, error)


@bots.on_message(filters.command("trash", cmd) & filters.me)
async def _(client, message):
    if message.reply_to_message:
        if int(len(str(message.reply_to_message))) > 4096:
            with BytesIO(str.encode(str(message.reply_to_message))) as out_file:
                out_file.name = "result.txt"
                return await message.reply_document(
                    document=out_file,
                )
        else:
            return await message.reply_text(message.reply_to_message)
    else:
        return await eor(message, "`Reply ke pesan/media`")


@bots.on_message(filters.command("eval", cmd) & filters.me)
async def _(client, message):
    await eor(message, "`Processing ...`")
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
