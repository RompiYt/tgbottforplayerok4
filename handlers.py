from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from aiogram.filters import CommandStart

router = Router()

# Пример каталога товаров
PRODUCTS = {
    "hoodie_1": [
        "file_id_1",
        "file_id_2",
        "file_id_3",
        "file_id_4",
        "file_id_5"
    ],
    # сюда можно добавлять новые товары
    # "hoodie_2": [...],
}

# храним индекс текущей фотки для каждого пользователя и товара
user_photo_index = {}  # user_id -> {product_id: index}


# ====================== START ======================
@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        "Здравствуйте! Это каталог интернет-магазина Emendgi.\n"
        "Чтобы не листать канал, используйте каталог ниже 👇",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="📦 Каталог товаров", callback_data="catalog")]
        ])
    )


# ====================== КАТАЛОГ ======================
@router.callback_query(F.data == "catalog")
async def show_catalog(callback: CallbackQuery):
    await callback.message.edit_text(
        "📦 Наш каталог товаров:\nВыберите категорию:",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🧥 Зип худи", callback_data="zip_hoodie")]
        ])
    )
    await callback.answer()


@router.callback_query(F.data == "zip_hoodie")
async def zip_hoodie(callback: CallbackQuery):
    # Список товаров в категории
    await callback.message.edit_text(
        "🧥 Зип худи\nВыберите товар:",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔥 Hoodie Black", callback_data="hoodie_1")],
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="catalog")]
        ])
    )
    await callback.answer()


# ====================== ОТКРЫТЬ ТОВАР ======================
@router.callback_query(F.data.startswith("hoodie_"))
async def open_product(callback: CallbackQuery):
    product_id = callback.data
    user_id = callback.from_user.id
    if user_id not in user_photo_index:
        user_photo_index[user_id] = {}
    user_photo_index[user_id][product_id] = 0
    await update_product(callback, product_id, 0)
    await callback.answer()


# ====================== КАРУСЕЛЬ ======================
@router.callback_query(F.data.startswith("next_photo:"))
async def next_photo(callback: CallbackQuery):
    user_id = callback.from_user.id
    product_id = callback.data.split(":")[1]

    index = user_photo_index.get(user_id, {}).get(product_id, 0)
    if index < len(PRODUCTS[product_id]) - 1:
        index += 1
        user_photo_index[user_id][product_id] = index
        await update_product(callback, product_id, index)
    await callback.answer()


@router.callback_query(F.data.startswith("prev_photo:"))
async def prev_photo(callback: CallbackQuery):
    user_id = callback.from_user.id
    product_id = callback.data.split(":")[1]

    index = user_photo_index.get(user_id, {}).get(product_id, 0)
    if index > 0:
        index -= 1
        user_photo_index[user_id][product_id] = index
        await update_product(callback, product_id, index)
    await callback.answer()


# ====================== ОБНОВЛЕНИЕ ФОТО ======================
async def update_product(callback: CallbackQuery, product_id: str, index: int):
    await callback.message.edit_media(
        media=InputMediaPhoto(
            media=PRODUCTS[product_id][index],
            caption=(
                "🧥 Зип-худи:Balenciaga\n"
                "•📐размерная сетка:S,M,L,XL,2XL(46,48,50,52,54)\n"
                "•🪽материал-плотный хлопок\n"
                "•🏷️ бирки фирменные\n"
                "•📌 логотип-вышит\n"
                "•💸 цена - 4390\n"
                "•✅ по поводу оформления заказа писать @EYRoyul  @Emendgi_manager\n"
                "•‼️ уточнять о наличии товара у менеджера\n"
                f"\n📸 {index+1}/{len(PRODUCTS[product_id])}"
            )
        ),
        reply_markup=get_keyboard(product_id, index)
    )


# ====================== КНОПКИ ======================
def get_keyboard(product_id, index):
    buttons = []
    nav_row = []

    if index > 0:
        nav_row.append(InlineKeyboardButton(text="⬅️", callback_data=f"prev_photo:{product_id}"))
    if index < len(PRODUCTS[product_id]) - 1:
        nav_row.append(InlineKeyboardButton(text="➡️", callback_data=f"next_photo:{product_id}"))
    if nav_row:
        buttons.append(nav_row)

    buttons.append([InlineKeyboardButton(text="⬅️ Назад", callback_data="zip_hoodie")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


# ====================== ПОЛУЧЕНИЕ FILE_ID ======================
@router.message(F.photo)
async def get_file_ids(message: Message):
    file_id = message.photo[-1].file_id  
    await message.answer(f"✅ File ID для этой фотки:\n`{file_id}`", parse_mode="Markdown")
