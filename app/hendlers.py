from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

import app.links as ln

router = Router()


@router.message(Command('start'))
async def start(message: Message):
  stop = await message.answer("Обработка запроса•••",
                              reply_markup=ReplyKeyboardRemove())
  await stop.delete()
  await message.reply(
      "Бот симулятор кейсов с драконами!\nНажмите <b>Открыть</b> что бы открыть кейс!",
      parse_mode="HTML",
      reply_markup=ln.input_start)


@router.message(Command('help'))
async def help1(message: Message):
  stop = await message.answer("Обработка запроса•••", reply_markup=ln.stop)
  await stop.delete()
  await message.answer(
      "Все новости или сообщить про баг здесь:\n<a href = 'https://t.me/book_of_dragon_news'>Книга Драконов Новости</a>",
      parse_mode="HTML",
      reply_markup=ln.input_help2)


@router.callback_query(F.data == 'back')
async def back(callback: CallbackQuery):
  await callback.answer("Возвращаемься ....", reply_markup=ln.stop)
  await callback.message.edit_text(
      text=
      'Бот симулятор кейсов с драконами!\nНажмите <b>Открыть</b> что бы открыть кейс!',
      parse_mode="HTML",
      reply_markup=ln.input_start)


@router.callback_query(F.data == 'help')
async def help2(callback: CallbackQuery):
  await callback.answer("Обращаемься за помощью....", reply_markup=ln.stop)
  await callback.message.edit_text(
      text=
      "Все новости или сообщить про баг здесь:\n<a href = 'https://t.me/book_of_dragon_news'>Книга Драконов Новости</a>",
      parse_mode="HTML",
      reply_markup=ln.input_help)
