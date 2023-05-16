import asyncio
import logging
import os
import sys
import time
from datetime import datetime
from logging.handlers import RotatingFileHandler
from typing import Any, Dict

from aiohttp import ClientSession
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram import Client, __version__, enums, filters
from pyrogram.handlers import MessageHandler
from pyromod import listen
from pytgcalls import GroupCallFactory

from .config import (API_HASH, API_ID, BOT_TOKEN, CMD_HNDLR, SESSION1,
                     SESSION2, SESSION3, SESSION4, SESSION5, SESSION6,
                     SESSION7, SESSION8, SESSION9, SESSION10)
from .logging import LOGGER

StartTime = time.time()
cmd = CMD_HNDLR
ids = []
CMD_HELP = {}
START_TIME = datetime.now()


aiosession = ClientSession()


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="ubot",
            api_hash=API_HASH,
            api_id=API_ID,
            bot_token=BOT_TOKEN,
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = self.me
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username} based on Pyrogram v{__version__} "
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Naya-Pyro stopped. Bye.")


class Ubot(Client):
    __module__ = "pyrogram.client"
    _bots = []

    def __init__(self, name, **kwargs):
        super().__init__(name=name, **kwargs)
        self.group_call = GroupCallFactory(self).get_group_call()

    def on_message(self, filters=filters.Filter, group=0):
        def decorator(func):
            for bot in self._bots:
                bot.add_handler(MessageHandler(func, filters), group)
            return func

        return decorator

    async def start(self):
        await super().start()
        if self not in self._bots:
            self._bots.append(self)


app = Bot()

if not BOT_TOKEN:
    LOGGER(__name__).error("WARNING: BOT TOKEN TIDAK DITEMUKAN, SHUTDOWN BOT")
    sys.exit()

bot1 = (
    Ubot(
        name="bot1",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION1,
        in_memory=False,
    )
    if SESSION1
    else None
)

bot2 = (
    Ubot(
        name="bot2",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION2,
        in_memory=False,
    )
    if SESSION2
    else None
)

bot3 = (
    Ubot(
        name="bot3",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION3,
        in_memory=False,
    )
    if SESSION3
    else None
)

bot4 = (
    Ubot(
        name="bot4",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION4,
        in_memory=False,
    )
    if SESSION4
    else None
)

bot5 = (
    Ubot(
        name="bot5",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION5,
        in_memory=False,
    )
    if SESSION5
    else None
)
bot6 = (
    Ubot(
        name="bot6",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION6,
        in_memory=False,
    )
    if SESSION6
    else None
)

bot7 = (
    Ubot(
        name="bot7",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION7,
        in_memory=False,
    )
    if SESSION7
    else None
)

bot8 = (
    Ubot(
        name="bot8",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION8,
        in_memory=False,
    )
    if SESSION8
    else None
)

bot9 = (
    Ubot(
        name="bot9",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION9,
        in_memory=False,
    )
    if SESSION9
    else None
)

bot10 = (
    Ubot(
        name="bot10",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION10,
        in_memory=False,
    )
    if SESSION10
    else None
)
bots = Ubot(name="bots")

botlist = [
    bot for bot in [bot1, bot2, bot3, bot4, bot5, bot6, bot7, bot8, bot9, bot10] if bot
]

for bot in botlist:
    bots._bots.append(bot)
