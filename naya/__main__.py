from platform import python_version as py

from kynaylibs import *
from kynaylibs.nan import *
from kynaylibs.nan.load import *
from kynaylibs.nan.utils import *
from kynaylibs.nan.utils.db import *
from kynaylibs.version import __version__ as nay
from kynaylibs.version import kynay_version as nan
from pyrogram import __version__ as pyro
from pyrogram import idle
from uvloop import install

from naya import *
from naya.config import *

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
    await app.start()
    LOGGER("Startup").info("Memulai Naya-Pyro Premium..")
    for bot in botlist:
        try:
            await bot.start()
            ex = bot.me
            user = ex.id
            await ajg(bot)
            await babi(bot)
            botlog = await get_botlog(user)
            LOGGER("✓").info(f"Started as {ex.first_name} | {ex.id} ")
            try:
                await bot.send_message(botlog, MSG_ON.format(nan, py(), pyro, nay, cmd))
            except BaseException as a:
                LOGGER("Info").warning(f"{a}")

            ids.append(ex.id)
            LOGGER("Info").info("Startup Completed")

        except Exception as e:
            LOGGER("X").info(f"{e}")
    await loadprem()
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    install()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    finally:
        LOGGER("Logger").info("Stopping Bot! GoodBye")
