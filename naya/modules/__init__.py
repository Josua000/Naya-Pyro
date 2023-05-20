import asyncio
from glob import glob
from os.path import basename, dirname, isfile

from kynaylibs import DEVS
from kynaylibs.nan import *
from kynaylibs.nan.utils import *
from kynaylibs.nan.utils.db import *
from pyrogram import *
from pyrogram.types import *
from requests import get

from naya import *

BL_UBOT = [-1001812143750]

while 0 < 6:
    _BL_GCAST = get(
        "https://raw.githubusercontent.com/naya1503/blacklist/master/blacklistgcast.json"
    )
    if _BL_GCAST.status_code != 200:
        if 0 != 5:
            continue
        BL_GCAST = [
            -1001812143750,
            -1001473548283,
            -1001390552926,
            -1001573099403,
            -1001810928340,
            -1001619428365,
            -1001825363971,
        ]
        break
    BL_GCAST = _BL_GCAST.json()
    break

del _BL_GCAST


def loadModule():
    mod_paths = glob(f"{dirname(__file__)}/*.py")
    return sorted(
        [
            basename(f)[:-3]
            for f in mod_paths
            if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
        ]
    )
