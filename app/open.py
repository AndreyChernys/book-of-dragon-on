from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, ChatPermissions
import random
from datetime import datetime, timedelta
from aiogram.exceptions import TelegramBadRequest

routerl = Router()

from app.list import RARE, SUPERARE, EPIC, MYTHIC, LEGENDARY, CHRONICLE
from app.diary import DIARY
import app.links as ln
from app.rstart import set_user
from run import bot


@routerl.message(F.text.lower() == 'открыть')
async def open1(message: Message):
  rand = random.randint(1, 100)

  if message.from_user:
    await set_user(message.from_user.id, message.from_user.first_name,
                   message.from_user.username)
    if 0 <= rand <= 49:
      random_choise1 = random.choice(RARE)
      await message.reply_photo(photo=random_choise1["photo"],
                                caption=random_choise1["text"],
                                reply_markup=ln.open)
    elif 51 <= rand <= 75:
      random_choise2 = random.choice(SUPERARE)
      await message.reply_photo(photo=random_choise2["photo"],
                                caption=random_choise2["text"],
                                reply_markup=ln.open)
    elif 76 <= rand <= 88:
      random_choise3 = random.choice(EPIC)
      await message.reply_photo(photo=random_choise3["photo"],
                                caption=random_choise3["text"],
                                reply_markup=ln.open)
    elif 89 <= rand <= 95:
      random_choise4 = random.choice(MYTHIC)
      await message.reply_photo(photo=random_choise4["photo"],
                                caption=random_choise4["text"],
                                reply_markup=ln.open)
    elif 96 <= rand <= 97:
      random_choise5 = random.choice(LEGENDARY)
      await message.reply_photo(photo=random_choise5["photo"],
                                caption=random_choise5["text"],
                                reply_markup=ln.open)
    elif 98 <= rand <= 100:
      random_choise6 = random.choice(CHRONICLE)
      await message.reply_photo(photo=random_choise6["photo"],
                                caption=random_choise6["text"],
                                reply_markup=ln.open)
      if random_choise6["id"] == '1':
        ud = datetime.now() + timedelta(hours=2)
        try:
          await bot.restrict_chat_member(
              chat_id=message.chat.id,
              user_id=message.from_user.id,
              until_date=ud,
              permissions=ChatPermissions(can_send_messages=False))
          await message.reply(
              f'Ликантр ведь и не существует, но.... тебя уже парализовало от страха, <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>',
              parse_mode="HTML")
        except TelegramBadRequest:
          await message.reply('Видимо подслушал Плеваку...')
      elif random_choise6["id"] == '2':
        ud = datetime.now() + timedelta(hours=10)
        try:
          await bot.restrict_chat_member(
              chat_id=message.chat.id,
              user_id=message.from_user.id,
              until_date=ud,
              permissions=ChatPermissions(can_send_messages=False))
          await message.reply(
              f"Вроде бы милашка, не так ли, <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>!?\nТак вот эта милашка отправляет тебя в нокаут, отдохни!",
              parse_mode="HTML")
        except TelegramBadRequest:
          await message.reply('Фу, гадость! Как ты его можешь терпеть!')
      elif random_choise6["id"] == '3':
        ud = datetime.now() + timedelta(hours=3)
        try:
          await bot.restrict_chat_member(
              chat_id=message.chat.id,
              user_id=message.from_user.id,
              until_date=ud,
              permissions=ChatPermissions(can_send_messages=False))
          await message.reply(
              f"Ликантрокрыл - один его укус и ты станешь таким же! А как известно драконы не умеют писать!\nНе так ли <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>!?",
              parse_mode="HTML")
        except TelegramBadRequest:
          await message.reply(
              'Ну и зачем ты слушаешь этих драконьих наездников!? Они говорят полную чушь, он существует!!!'
          )
      elif random_choise6["id"] == '4':
        ud = datetime.now() + timedelta(hours=1)
        try:
          await bot.restrict_chat_member(
              chat_id=message.chat.id,
              user_id=message.from_user.id,
              until_date=ud,
              permissions=ChatPermissions(can_send_messages=False))
          await message.reply(
              f"Кажется Сарделька подкинула тебе Драконий корень, отдохни немного, <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>",
              parse_mode="HTML")
        except TelegramBadRequest:
          await message.reply('Кажеться ты эволюционировал от Громелей, жаль')

    elif rand == 50:
      random_choise7 = random.choice(DIARY)
      await message.reply(text=random_choise7, reply_markup=ln.open)
      await message.reply(
          'Ошибка!!!\nПерешлите ошибку разработчику @gerahomeoff')
    else:
      await message.reply("Фатальная ошибка\n@gerahomeoff")


@routerl.message(Command('open'))
async def open2(message: Message):
  rand = random.randint(1, 100)

  if message.from_user:
    await set_user(message.from_user.id, message.from_user.first_name,
                   message.from_user.username)
    if 0 <= rand <= 49:
      random_choise1 = random.choice(RARE)
      await message.reply_photo(photo=random_choise1["photo"],
                                caption=random_choise1["text"],
                                reply_markup=ln.open)
    elif 51 <= rand <= 75:
      random_choise2 = random.choice(SUPERARE)
      await message.reply_photo(photo=random_choise2["photo"],
                                caption=random_choise2["text"],
                                reply_markup=ln.open)
    elif 76 <= rand <= 88:
      random_choise3 = random.choice(EPIC)
      await message.reply_photo(photo=random_choise3["photo"],
                                caption=random_choise3["text"],
                                reply_markup=ln.open)
    elif 89 <= rand <= 95:
      random_choise4 = random.choice(MYTHIC)
      await message.reply_photo(photo=random_choise4["photo"],
                                caption=random_choise4["text"],
                                reply_markup=ln.open)
    elif 96 <= rand <= 97:
      random_choise5 = random.choice(LEGENDARY)
      await message.reply_photo(photo=random_choise5["photo"],
                                caption=random_choise5["text"],
                                reply_markup=ln.open)
    elif 98 <= rand <= 100:
      random_choise6 = random.choice(CHRONICLE)
      await message.reply_photo(photo=random_choise6["photo"],
                                caption=random_choise6["text"],
                                reply_markup=ln.open)
      if random_choise6["id"] == '1':
        ud = datetime.now() + timedelta(hours=2)
        try:
          await bot.restrict_chat_member(
              chat_id=message.chat.id,
              user_id=message.from_user.id,
              until_date=ud,
              permissions=ChatPermissions(can_send_messages=False))
          await message.reply(
              f'Ликантр ведь и не существует, но.... тебя уже парализовало от страха, <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>',
              parse_mode="HTML")
        except TelegramBadRequest:
          await message.reply('Видимо подслушал Плеваку...')
      elif random_choise6["id"] == '2':
        ud = datetime.now() + timedelta(hours=10)
        try:
          await bot.restrict_chat_member(
              chat_id=message.chat.id,
              user_id=message.from_user.id,
              until_date=ud,
              permissions=ChatPermissions(can_send_messages=False))
          await message.reply(
              f"Вроде бы милашка, не так ли, <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>!?\nТак вот эта милашка отправляет тебя в нокаут, отдохни!",
              parse_mode="HTML")
        except TelegramBadRequest:
          await message.reply('Фу, гадость! Как ты его можешь терпеть!')
      elif random_choise6["id"] == '3':
        ud = datetime.now() + timedelta(hours=3)
        try:
          await bot.restrict_chat_member(
              chat_id=message.chat.id,
              user_id=message.from_user.id,
              until_date=ud,
              permissions=ChatPermissions(can_send_messages=False))
          await message.reply(
              f"Ликантрокрыл - один его укус и ты станешь таким же! А как известно драконы не умеют писать!\nНе так ли <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>!?",
              parse_mode="HTML")
        except TelegramBadRequest:
          await message.reply(
              'Ну и зачем ты слушаешь этих драконьих наездников!? Они говорят полную чушь, он существует!!!'
          )
      elif random_choise6["id"] == '4':
        ud = datetime.now() + timedelta(hours=1)
        try:
          await bot.restrict_chat_member(
              chat_id=message.chat.id,
              user_id=message.from_user.id,
              until_date=ud,
              permissions=ChatPermissions(can_send_messages=False))
          await message.reply(
              f"Кажется Сарделька подкинула тебе Драконий корень, отдохни немного, <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>",
              parse_mode="HTML")
        except TelegramBadRequest:
          await message.reply('Кажеться ты эволюционировал от Громелей, жаль')

    elif rand == 50:
      random_choise7 = random.choice(DIARY)
      await message.reply(text=random_choise7, reply_markup=ln.open)
      await message.reply(
          'Ошибка!!!\nПерешлите ошибку разработчику @gerahomeoff')
    else:
      await message.reply("Фатальная ошибка\n@gerahomeoff")


@routerl.callback_query(F.data == 'open')
async def open3(callback: CallbackQuery):
  rand = random.randint(1, 100)
  if callback.from_user:  # Use callback.from_user instead of message.from_user
    await set_user(callback.from_user.id, callback.from_user.first_name,
                   callback.from_user.username)
    if 0 <= rand <= 49:
      random_choise1 = random.choice(RARE)
      await callback.message.reply_photo(photo=random_choise1["photo"],
                                         caption=random_choise1["text"],
                                         reply_markup=ln.open)
    elif 51 <= rand <= 75:
      random_choise2 = random.choice(SUPERARE)
      await callback.message.reply_photo(photo=random_choise2["photo"],
                                         caption=random_choise2["text"],
                                         reply_markup=ln.open)
    elif 76 <= rand <= 88:
      random_choise3 = random.choice(EPIC)
      await callback.message.reply_photo(photo=random_choise3["photo"],
                                         caption=random_choise3["text"],
                                         reply_markup=ln.open)
    elif 89 <= rand <= 95:
      random_choise4 = random.choice(MYTHIC)
      await callback.message.reply_photo(photo=random_choise4["photo"],
                                         caption=random_choise4["text"],
                                         reply_markup=ln.open)
    elif 96 <= rand <= 97:
      random_choise5 = random.choice(LEGENDARY)
      await callback.message.reply_photo(photo=random_choise5["photo"],
                                         caption=random_choise5["text"],
                                         reply_markup=ln.open)
    elif 98 <= rand <= 100:
      random_choise6 = random.choice(CHRONICLE)
      await callback.message.reply_photo(photo=random_choise6["photo"],
                                         caption=random_choise6["text"],
                                         reply_markup=ln.open)
      if random_choise6["id"] == '1':
        ud = datetime.now() + timedelta(hours=2)
        try:
          await bot.restrict_chat_member(
              chat_id=callback.message.chat.id,
              user_id=callback.from_user.id,
              until_date=ud,
              permissions=ChatPermissions(can_send_messages=False))
          await callback.message.reply(
              f'Ликантр ведь и не существует, но.... тебя уже парализовало от страха, <a href="tg://user?id={callback.from_user.id}">{callback.from_user.first_name}</a>',
              parse_mode="HTML")
        except TelegramBadRequest:
          await callback.message.reply('Видимо подслушал Плеваку...')
      elif random_choise6["id"] == '2':
        ud = datetime.now() + timedelta(hours=10)
        try:
          await bot.restrict_chat_member(
              chat_id=callback.message.chat.id,
              user_id=callback.from_user.id,
              until_date=ud,
              permissions=ChatPermissions(can_send_messages=False))
          await callback.message.reply(
              f"Вроде бы милашка, не так ли, <a href='tg://user?id={callback.from_user.id}'>{callback.from_user.first_name}</a>!?\nТак вот эта милашка отправляет тебя в нокаут, отдохни!",
              parse_mode="HTML")
        except TelegramBadRequest:
          await callback.message.reply(
              'Фу, гадость! Как ты его можешь терпеть!')
      elif random_choise6["id"] == '3':
        ud = datetime.now() + timedelta(hours=3)
        try:
          await bot.restrict_chat_member(
              chat_id=callback.message.chat.id,
              user_id=callback.from_user.id,
              until_date=ud,
              permissions=ChatPermissions(can_send_messages=False))
          await callback.message.reply(
              f"Ликантрокрыл - один его укус и ты станешь таким же! А как известно драконы не умеют писать!\nНе так ли <a href='tg://user?id={callback.from_user.id}'>{callback.from_user.first_name}</a>!?",
              parse_mode="HTML")
        except TelegramBadRequest:
          await callback.message.reply(
              'Ну и зачем ты слушаешь этих драконьих наездников!? Они говорят полную чушь, он существует!!!'
          )
      elif random_choise6["id"] == '4':
        ud = datetime.now() + timedelta(hours=1)
        try:
          await bot.restrict_chat_member(
              chat_id=callback.message.chat.id,
              user_id=callback.from_user.id,
              until_date=ud,
              permissions=ChatPermissions(can_send_messages=False))
          await callback.message.reply(
              f"Кажется Сарделька подкинула тебе Драконий корень, отдохни немного, <a href='tg://user?id={callback.from_user.id}'>{callback.from_user.first_name}</a>",
              parse_mode="HTML")
        except TelegramBadRequest:
          await callback.message.reply(
              'Кажеться ты эволюционировал от Громелей, жаль')

    elif rand == 50:
      random_choise7 = random.choice(DIARY)
      await callback.message.reply(text=random_choise7, reply_markup=ln.open)
      await callback.message.reply(
          'Ошибка!!!\nПерешлите ошибку разработчику @gerahomeoff')
    else:
      await callback.message.reply("Фатальная ошибка\n@gerahomeoff")
