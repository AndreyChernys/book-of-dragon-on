from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton,
                           ReplyKeyboardRemove)

open = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Открыть')]],
    resize_keyboard=True,
)

input_start = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Открыть', callback_data='open')
], [InlineKeyboardButton(text='Помощь', callback_data='help')]])
input_help = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Назад', callback_data='back')
]])

input_help2 = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Главное меню', callback_data='back')
]])

stop = ReplyKeyboardRemove()
