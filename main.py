import logging
from aiogram import Bot, Dispatcher, executor, types
import os

# Вставка токена из переменной среды
TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я помогу тебе найти документы.")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(f"Вы написали: {message.text}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)