from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer("Здравствуйте! Это каталог интернет-магазина Emendgi. Чтобы не листать в самый верх канала, для вашего удобства мы создали бота, с помощью которого вы быстро найдете вещи, которые вам нужны.",
                         reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                             [InlineKeyboardButton(text="Каталог товаров", callback_data="catalog")]
                         ]))
    
@router.callback_query(F.data == "catalog")
async def show_catalog(callback_query: CallbackQuery):
    await callback_query.message.answer("Наш каталог товаров:")
    await callback_query.answer()