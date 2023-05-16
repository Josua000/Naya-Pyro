from glob import glob
from os.path import basename, dirname, isfile

from kynaylibs import *
from kynaylibs.nan import *
from kynaylibs.nan.utils import *
from kynaylibs.nan.utils.db import *

from naya import *

BL_UBOT = [-1001812143750]


def loadModule():
    mod_paths = glob(f"{dirname(__file__)}/*.py")
    return sorted(
        [
            basename(f)[:-3]
            for f in mod_paths
            if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
        ]
    )
