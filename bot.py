from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import logging
logging.basicConfig(level=logging.INFO)

token = "5530500111:AAGKBBdY1SX7KANvrrGMAWCgvmgnWQ0xTzk"

bot = Bot(token)
disp = Dispatcher(bot)
@disp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привіт, я бот, що тобі допоможе.")
    #await message.reply("Привіт, я бот, що тобі допоможе.")

@disp.message_handler(commands=["help"])
async def help(message: types.Message):
    help_t = "Доступні команди - /start - початок роботи, /help - вибір кнопки"
    await message.answer(help_t)

    keyboard = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton(text = 'But1', callback_data="button1")
    but2 = InlineKeyboardButton(text = 'But2', callback_data="button2")
    keyboard.add(but1, but2)
    await message.answer("Обери потрібну кнопку.", reply_markup=keyboard)

@disp.callback_query_handler(lambda c: c.data == 'button1')
async def butt1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Ви обрали кнопку 1.")

@disp.callback_query_handler(lambda c: c.data == 'button2')
async def butt2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Ви обрали кнопку 2.")



executor.start_polling(disp, skip_updates=True)