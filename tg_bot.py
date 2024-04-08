from main import get_coins_info
from aiogram import Bot, Dispatcher, executor, types
from config import token
import json
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove


bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Обновить"]
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(*start_buttons)

    await message.answer("Старт", reply_markup=keyboard)


@dp.message_handler(Text(equals="Обновить"))
async def get_all_coins_info(message: types.Message):
    start_buttons = ["Обновить"]
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(*start_buttons)

    await message.answer("Обновляю...", reply_markup=ReplyKeyboardRemove())

    get_coins_info()

    with open("Coins_info.json") as file:
        coins_prices = json.load(file)

    for k, v in coins_prices.items():
        prices = f"{v['coin_name']}\n"\
                 f"<b>{v['coin_price']}</b>"

        await message.answer(prices, reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp)