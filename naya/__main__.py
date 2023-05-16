from asyncio import get_event_loop_policy
from importlib import import_module
from platform import python_version as py

from kynaylibs import *
from kynaylibs.nan import *
from kynaylibs.nan.utils import *
from kynaylibs.nan.utils.db import *
from kynaylibs.version import __version__ as nay
from kynaylibs.version import kynay_version as nan
from pyrogram import __version__ as pyro
from pyrogram import idle
from uvloop import install

from naya import *
from naya.modules import loadModule

MSG_ON = """
**Naya Premium Actived ✅**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
◉ **Versi** : `{}`
◉ **Phython** : `{}`
◉ **Pyrogram** : `{}`
◉ **Kynaylibs** : `{}`
**Ketik** `{}alive` **untuk Mengecheck Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""


async def main():
    modules = loadModule()
    for mod in modules:
        imported_module = import_module(f"naya.modules.{mod}")
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            imported_module.__MODULE__ = imported_module.__MODULE__
            if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
                CMD_HELP[
                    imported_module.__MODULE__.replace(" ", "_").lower()
                ] = imported_module
    await app.start()
    LOGGER("Naya Premium").info("Memulai Naya-Pyro..")
    for bot in botlist:
        try:
            await bot.start()
            ex = await bot.get_me()
            user_id = ex.id
            await ajg(bot)
            await buat_log(bot)
            botlog_chat_id = await get_botlog(user_id)
            try:
                await bot.send_message(
                    botlog_chat_id, MSG_ON.format(nan, py(), pyro, nay, CMD_HNDLR)
                )
            except BaseException as a:
                LOGGER("Info").warning(f"{a}")
            LOGGER("Info").info("Startup Completed")
            LOGGER("✓").info(f"Started as {ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            LOGGER("X").info(f"{e}")
    await idle()
    install()


if __name__ == "__main__":
    get_event_loop_policy().get_event_loop().run_until_complete(main())
