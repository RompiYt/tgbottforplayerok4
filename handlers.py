from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart

router = Router()

@router.message()
async def get_file_ids(message: Message):
    if message.photo:
        file_id = message.photo[-1].file_id
        with open("file_ids.txt", "a") as f:
            f.write(file_id + "\n")

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        "Здравствуйте! Это каталог интернет-магазина Emendgi.\n"
        "Чтобы не листать канал, используйте каталог ниже 👇",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="📦 Каталог товаров", callback_data="catalog")]
        ])
    )

@router.callback_query(F.data == "catalog")
async def show_catalog(callback: CallbackQuery):
    await callback.message.edit_text(
        "📦 Наш каталог товаров:\n"
        "Выберите категорию:",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🧥 Зип худи", callback_data="zip_hoodie")]
        ])
    )
    await callback.answer()

@router.callback_query(F.data == "zip_hoodie")
async def zip_hoodie(callback: CallbackQuery):
    await callback.message.edit_text(
        "🧥 Зип худи\n"
        "Тут скоро появятся товары 👀",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="catalog")]
        ])
    )
    await callback.answer()
