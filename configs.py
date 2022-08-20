# (c) Blacky2002

import os


class Config(object):
  API_ID = int(os.environ.get("API_ID", "6309305"))
	API_HASH = os.environ.get("API_HASH", "8b0473750d327598c8585b0049f09e2d")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "5458768378:AAGrwPBrwpKtFdiHM3hwziCQChVJb56mfM4")
