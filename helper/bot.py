import telegram.ext as tg
from .config import BOT_TOKEN

updater = tg.Updater(token=BOT_TOKEN, request_kwargs={'read_timeout': 30, 'connect_timeout': 10})
bot = updater.bot
dispatcher = updater.dispatcher
