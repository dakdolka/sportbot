from aiogram import Bot, Router, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
# from buttons import kb_for_songs, kb_main, kb_confirm_for_file, kb_confirm_for_link, kb_confirm_for_name, create_kb_for_change, Last_kb, kb_exit_to_main
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.command import Command
# from config import settings
from aiogram.utils.keyboard import InlineKeyboardBuilder
from typing import Optional
from aiogram.filters.callback_data import CallbackData
from collections import defaultdict

rt = Router()

class User_info(StatesGroup):
    full_name = State()
    user_nickname = State()
    tg_is = State()
    sex = State()
    height = State()
    weight = State()

@rt.message(Command('start'))
async def start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(f'Здравствуйте, {message.from_user.full_name}!')
    await state.update_data(full_name=message.from_user.full_name, user_nickname=message.from_user.username)
    await state.set_state(User_info.sex)
    # For elem in lalala
    
 
