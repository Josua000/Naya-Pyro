from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


API_ID = int(getenv("API_ID", "123"))
API_HASH = getenv("API_HASH")
MONGO_URL = getenv("MONGO_URL", "")
BOT_TOKEN = getenv("BOT_TOKEN")
OPENAI_API = getenv("OPENAI_API", "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")
GIT_TOKEN = getenv("GIT_TOKEN")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
BRANCH = getenv("BRANCH", "naya")  # don't change
REPO_URL = getenv("REPO_URL", "https://github.com/naya1503/Naya-Pyro")
CMD_HNDLR = getenv("CMD_HNDLR", ".")
SESSION1 = getenv("SESSION1", "")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
