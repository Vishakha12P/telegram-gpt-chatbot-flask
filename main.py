import os
from boltiotai import openai
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from example import example

bot = Bot(token="8563113575:AAFePhyALF4lun4MFLuNDUwgbS3LPGJkrbk")
dp = Dispatcher()
openai.api_key = os.environ['OPENAI_API_KEY']
example()

@dp.message(CommandStart(["start", "help"]))
async def welcome(message: types.Message):
  await message.reply('Hello! I am GPT chat bot, You can ask me anything :) ')

@dp.message()
async def gpt(message: types.Message):
  messages=[{"role": "system", "content": "you are a helpful assistant."}, {"role": "user", "content": message.text}]
  response = openai.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
  await message.reply(response['choices'][0]['message']['content'])

async def main():
  await bot.delete_webhook(drop_pending_updates=True)
  await dp.start_polling(bot)

if __name__ == "__main__":
  asyncio.run(main())