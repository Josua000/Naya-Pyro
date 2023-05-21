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
from kynaylibs.nan import Ubot
from pyrogram import Client, __version__, enums, filters
from pyrogram.handlers import MessageHandler
from pyromod import listen
from pytgcalls import GroupCallFactory
from telegraph import Telegraph, exceptions, upload_file

from .config import (API_HASH, API_ID, BOT_TOKEN, CMD_HNDLR, SESSION1,
                     SESSION2, SESSION3, SESSION4, SESSION5, SESSION6,
                     SESSION7, SESSION8, SESSION9, SESSION10)

StartTime = time.time()
cmd = CMD_HNDLR
ids = []
scheduler = AsyncIOScheduler()
CMD_HELP = {}
START_TIME = datetime.now()
telegraph = Telegraph()
telegraph.create_account(short_name="Naya-Pyro")

aiosession = ClientSession()

import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("logs.txt", maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("asyncio").setLevel(logging.CRITICAL)
logging.getLogger("pytgcalls").setLevel(logging.WARNING)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("pyrogram.client").setLevel(logging.WARNING)
logging.getLogger("pyrogram.session.auth").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram.session.session").setLevel(logging.CRITICAL)
logging.basicConfig(level=logging.INFO)

LOGS = logging.getLogger(__name__)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)


app = Client(
    name="ubot", api_hash=API_HASH, api_id=API_ID, bot_token=BOT_TOKEN, in_memory=True
)

if not BOT_TOKEN:
    LOGGER(__name__).error("WARNING: BOT TOKEN TIDAK DITEMUKAN, SHUTDOWN BOT")
    sys.exit()


bot1 = (
    Ubot(
        name="bot1",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION1,
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
