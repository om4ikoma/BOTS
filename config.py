from aiogram import Bot, Dispatcher
from decouple import config

Token = config("TOKEN")
bot =Bot(Token)
dp = Dispatcher(bot=bot)
ADMIN = 1121073609