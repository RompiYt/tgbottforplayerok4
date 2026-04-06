from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from aiogram.filters import CommandStart

router = Router()

user_last_category = {}

PRODUCTS = {
    "Зип-худи:Balenciaga": {
        "name": "Зип-худи:Balenciaga",
        "category": "Зип-худи",
        "material": "плотный хлопок",
        "price": "4390",
        "sizes": "S,M,L,XL,2XL(46,48,50,52,54)",
        "photos": [
            "AgACAgIAAxkBAAMUadNvRVXH9NKocazjvEBGfcxN6k8AAkMVaxuHV5hK8UI5i71IETsBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAMVadNvRWUQLK05Jfc4ZLSd8_SnUC4AAkQVaxuHV5hK22Z8xGPs08sBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAMPadNuQ0zSLASEATZsMd71T_vOgO4AAkAVaxuHV5hKz0SwF1GIX98BAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAMSadNvRXcAARFfRiPmTBZk0ZBCsZDzAAJFFWsbh1eYSmhlj_agiHN5AQADAgADeQADOwQ",
            "AgACAgIAAxkBAAMTadNvReGSsvuHG5434g9P4TikvQYAAkIVaxuHV5hK-zwwlzbYx0gBAAMCAAN5AAM7BA"
        ]
    },
    "Зип-худи:Polo ralph lauren":{
        "name": "Зип-худи:Polo ralph lauren",
        "category": "Зип-худи",
        "material": "хлопок",
        "price": "4390",
        "sizes": "S,M,L,XL(46,48,50,52)",
        "photos": [
            "AgACAgIAAxkBAANVadQExD9P-3KeKLo9pEgfqe4hVyUAApYRaxu4LKBKH9-k9ekXVLwBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAANXadQE1VtzOpdXKUfpGAgUWjbvMeQAApcRaxu4LKBKa3ZWPyfLiaQBAAMCAAN5AAM7BA"
        ]
    },
    "Зип-худи:Lacoste":{
        "name": "Зип-худи:Lacoste",
        "category": "Зип-худи",
        "material": "плотный хлопок",
        "price": "3990",
        "sizes": "S,M,L,XL,2XL(46,48,50,52,54)",
        "photos": [
            "."
        ]
    },
    "Зип-худи:Karl Lagerfeld"{
        "name": "Зип-худи:Karl Lagerfeld",
        "category": "Зип-худи",
        "material": "плотный хлопок",
        "price": "3890",
        "sizes": "S,M,L,XL,XXL(46,48,50,52,54)",
        "photos": [
            "."
        ]
    },
    "Зип-худи:Burberry"{
        "name": "Зип-худи:Burberry",
        "category": "Зип-худи",
        "material": "плотный хлопок",
        "price": "3390",
        "sizes": "M,L,XL,XXL",
        "photos": [
            "."
        ]
    }
}

CATEGORIES = {
    "Зип-худи": ["Зип-худи:Balenciaga", "Зип-худи:Polo ralph lauren", "Зип-худи:Lacoste", "Зип-худи:Karl Lagerfeld", "Зип-худи:Burberry"]
}

user_photo_index = {}

# ======================== START ========================================

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
            [InlineKeyboardButton(text="🧥 Зип худи", callback_data="Зип-худи")]
        ])
    )
    await callback.answer()

# ====================== ОТКРЫТЬ ТОВАР ======================

@router.callback_query(F.data.in_(list(CATEGORIES.keys())))
async def show_category(callback: CallbackQuery):
    category_id = callback.data
    buttons = [[InlineKeyboardButton(text=f"🔥 {product_id}", callback_data=product_id)] for product_id in CATEGORIES[category_id]]
    buttons.append([InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_catalog")])
    await callback.message.edit_text(
        f"Категория: {category_id}\nВыберите товар:",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons)
    )
    await callback.answer()

@router.callback_query(F.data.in_(list(PRODUCTS.keys())))
async def open_product(callback: CallbackQuery):
    product_id = callback.data
    user_id = callback.from_user.id

    category_id = PRODUCTS[product_id]["category"]
    user_last_category[user_id] = category_id

    if user_id not in user_photo_index:
        user_photo_index[user_id] = {}

    user_photo_index[user_id][product_id] = 0

    await update_product(callback, product_id, 0)
    await callback.answer()

# ====================== КАРУСЕЛЬ ======================

@router.callback_query(F.data.startswith("next_photo:"))
async def next_photo(callback: CallbackQuery):
    user_id = callback.from_user.id
    product_id = ":".join(callback.data.split(":")[1:])  # 💥 фикс
    index = user_photo_index.get(user_id, {}).get(product_id, 0)
    if index < len(PRODUCTS[product_id]["photos"]) - 1:
        index += 1
        user_photo_index[user_id][product_id] = index
        await update_product(callback, product_id, index)
    await callback.answer()

@router.callback_query(F.data.startswith("prev_photo:"))
async def prev_photo(callback: CallbackQuery):
    user_id = callback.from_user.id
    product_id = ":".join(callback.data.split(":")[1:])  # 💥 фикс
    index = user_photo_index.get(user_id, {}).get(product_id, 0)
    if index > 0:
        index -= 1
        user_photo_index[user_id][product_id] = index
        await update_product(callback, product_id, index)
    await callback.answer()

@router.callback_query(F.data == "back_to_category")
async def back_to_category(callback: CallbackQuery):
    user_id = callback.from_user.id
    category_id = user_last_category.get(user_id)

    if not category_id:
        await callback.answer("Ошибка возврата", show_alert=True)
        return

    buttons = [
        [InlineKeyboardButton(text=f"🔥 {pid}", callback_data=pid)]
        for pid in CATEGORIES[category_id]
    ]
    buttons.append([InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_catalog")])

    await callback.message.delete()  # 💥 ВАЖНО

    await callback.message.answer(
        f"Категория: {category_id}\nВыберите товар:",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons)
    )

    await callback.answer()

@router.callback_query(F.data == "back_to_catalog")
async def back_to_catalog(callback: CallbackQuery):
    await show_catalog(callback)

# ====================== ОБНОВЛЕНИЕ ФОТО ======================

async def update_product(callback: CallbackQuery, product_id: str, index: int):
    product = PRODUCTS[product_id]
    photos = product["photos"]

    caption = (
        f"🧥 {product['name']}\n"
        f"•📐размерная сетка:{product['sizes']}\n"
        f"•🪽материал-{product['material']}\n"
        f"•🏷️ бирки фирменные\n"
        f"•📌 логотип-вышит\n"
        f"•💸 цена - {product['price']}\n"
        f"•✅ по поводу оформления заказа писать @EYRoyul  @Emendgi_manager\n"
        f"•‼️ уточнять о наличии товара у менеджера\n"
        f"\n📸 {index+1}/{len(photos)}"
    )

    await callback.message.edit_media(
        media=InputMediaPhoto(
            media=photos[index],
            caption=caption
        ),
        reply_markup=get_keyboard(product_id, index)
    )


def get_keyboard(product_id, index):
    photos = PRODUCTS[product_id]["photos"]
    buttons = []
    nav_row = []
    if index > 0:
        nav_row.append(InlineKeyboardButton(text="⬅️", callback_data=f"prev_photo:{product_id}"))
    if index < len(photos) - 1:
        nav_row.append(InlineKeyboardButton(text="➡️", callback_data=f"next_photo:{product_id}"))
    if nav_row:
        buttons.append(nav_row)
    buttons.append([InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_category")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

@router.message(F.photo)
async def get_file_ids(message: Message):
    file_id = message.photo[-1].file_id
    await message.answer(f"✅ File ID для этой фотки:\n`{file_id}`", parse_mode="Markdown")
