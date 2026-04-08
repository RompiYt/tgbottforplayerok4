from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from aiogram.filters import CommandStart

router = Router()

user_last_category = {}

PRODUCTS = {
    "Зип-худи:Balenciaga": {
        "type": "clothes",
        "name": "Зип-худи:Balenciaga",
        "category": "Зип-худи",
        "material": "плотный хлопок",
        "colors": "черный🖤",
        "price": "4390",
        "sizes": "S,M,L,XL,2XL(46,48,50,52,54)",
        "logo": "вышит",
        "photos": [
            "AgACAgIAAxkBAAMUadNvRVXH9NKocazjvEBGfcxN6k8AAkMVaxuHV5hK8UI5i71IETsBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAMVadNvRWUQLK05Jfc4ZLSd8_SnUC4AAkQVaxuHV5hK22Z8xGPs08sBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAMPadNuQ0zSLASEATZsMd71T_vOgO4AAkAVaxuHV5hKz0SwF1GIX98BAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAMSadNvRXcAARFfRiPmTBZk0ZBCsZDzAAJFFWsbh1eYSmhlj_agiHN5AQADAgADeQADOwQ",
            "AgACAgIAAxkBAAMTadNvReGSsvuHG5434g9P4TikvQYAAkIVaxuHV5hK-zwwlzbYx0gBAAMCAAN5AAM7BA"
        ]
    },
    "Зип-худи:Polo ralph lauren":{
        "type": "clothes",
        "name": "Зип-худи:Polo ralph lauren",
        "category": "Зип-худи",
        "material": "хлопок",
        "colors": "черный🖤",
        "price": "4390",
        "sizes": "S,M,L,XL(46,48,50,52)",
        "logo": "вышит",
        "photos": [
            "AgACAgIAAxkBAANVadQExD9P-3KeKLo9pEgfqe4hVyUAApYRaxu4LKBKH9-k9ekXVLwBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAANXadQE1VtzOpdXKUfpGAgUWjbvMeQAApcRaxu4LKBKa3ZWPyfLiaQBAAMCAAN5AAM7BA"
        ]
    },
    "Зип-худи:Lacoste":{
        "type": "clothes",
        "name": "Зип-худи:Lacoste",
        "category": "Зип-худи",
        "material": "плотный хлопок",
        "colors": "черный🖤",
        "price": "3990",
        "sizes": "S,M,L,XL,2XL(46,48,50,52,54)",
        "logo": "вышит",
        "photos": [
            "AgACAgIAAxkBAANoadS4wBJxWanC_5JpaCsqKDrkcvwAAooTaxu4LKBKQ5m_dREv690BAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAANjadS4wJxnLcphqcxLxZ3asRHMMhkAAoMTaxu4LKBKHBrzFYDRF8IBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAANladS4wOViQtKfLtyK0IQbOW9tGEoAAoUTaxu4LKBKsPZCz_lQtKwBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAANpadS4wLrUPXFCs2-axLxweAbacygAAogTaxu4LKBKa-IunSJamKYBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAANnadS4wAgInRY0wdAyNZRbpm1gP2AAAokTaxu4LKBKUSfcev_oewIBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAANradS4wHPBlT9y3EX5p57yhqyJ_pcAAocTaxu4LKBKGbZ5DsBOA4UBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAANkadS4wB9K0f22KmfLV9xKJnPF3wwAAoQTaxu4LKBKJYZCjoKs5MsBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAANmadS4wDzDGGd5c1AtIRTuoXNvcPIAAosTaxu4LKBKzKNfYP4AAfpHAQADAgADeQADOwQ",
            "AgACAgIAAxkBAANqadS4wFenr0tEkBfVlI79CiUsOqUAAoYTaxu4LKBKobYYqcTjdMgBAAMCAAN5AAM7BA"
        ]
    },
    "Зип-худи:Karl Lagerfeld":{
        "type": "clothes",
        "name": "Зип-худи:Karl Lagerfeld",
        "category": "Зип-худи",
        "material": "плотный хлопок",
        "colors": "черный🖤",
        "price": "3890",
        "sizes": "S,M,L,XL,XXL(46,48,50,52,54)",
        "logo": "3D силикон",
        "photos": [
            "AgACAgIAAxkBAAN3adS6C9ZADwzW9IfCNyJ8hmy7dNAAApMTaxu4LKBKf0BMJtsbVD4BAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAN1adS6C8dIxUWD-1pu97A-xifTf4gAApITaxu4LKBKfTOTuQcmCAYBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAN6adS6Cz9YHz9vXNhB_8LE_zny_fgAApQTaxu4LKBKAfxf9vJZTVQBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAN5adS6C23JA6U7SFbb_1ffoBMAAbuWAAKXE2sbuCygSoKpuVNN-09-AQADAgADeQADOwQ",
            "AgACAgIAAxkBAAN2adS6C0ABVM7726iA_T8Vl5MV5LMAApETaxu4LKBKgoXTr63lDi4BAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAN7adS6CxYQv2P1Vc787MvWhS573VAAApYTaxu4LKBKWFluthe_24oBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAN8adS6C4XR6l9i9L3HtE6EtYLDQacAApATaxu4LKBK6KewSbmVKfcBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAN4adS6C46k1W0SWifat0OYQW8csnUAApUTaxu4LKBK4UnO8ellEVYBAAMCAAN5AAM7BA"
        ]
    },
    "Зип-худи:Burberry":{
        "type": "clothes",
        "name": "Зип-худи:Burberry",
        "category": "Зип-худи",
        "material": "плотный хлопок",
        "colors": "черный🖤/серый🩶",
        "price": "3390",
        "sizes": "M,L,XL,XXL",
        "logo": "вышит",
        "photos": [
            "AgACAgIAAxkBAAOHadTIN9BWll1r65-PhUanYndXD9wAAssTaxu4LKBKUOETptCbb6kBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAOJadTINz_fyNYP-JJ6HjxtViJjlt4AAswTaxu4LKBKB8-Je2cI-isBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAOMadTIN3tFBmZjugeqbO6GsblWQ0MAAs8Taxu4LKBKkV4VZkaDSjUBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAOKadTIN20rDurF3mKTRVxUIU1AAAH-AALNE2sbuCygSt36fJl4lFCnAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAOFadTIN6p1sEjN5w0_GmYPhaEAAQrTAALIE2sbuCygSqJQ9ti21J2xAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAOIadTINxPd_amRZit8g76TnI-tj0sAAsoTaxu4LKBKqtBObw-JZYoBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAOLadTIN6ve80zmStb28G7mbp6-jEoAAs4Taxu4LKBKzXHNxhVgx1cBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAONadTIN4v5CQqk82gSiKLXbCcR7NgAAtATaxu4LKBKWF9VFqOQk_cBAAMCAAN5AAM7BA",
            "AgACAgIAAxkBAAOGadTINzxdEGiW74MI7gNGmWLInacAAskTaxu4LKBKkXmGntN-XoABAAMCAAN5AAM7BA"
        ]
    },
    "Футболка:Aerounautica Мilitare":{
        "type": "clothes",
        "name": "Футболка:Aerounautica Мilitare",
        "category": "Футболка",
        "material": "хлопок",
        "colors": "белый🤍/черный🖤",
        "price": "2690",
        "sizes": "S,M,L,XL,2XL(46,48,50,52,54)",
        "logo": "вышит",
        "photos": [
            "AgACAgIAAxkBAAMUadNvRVXH9NKocazjvEBGfcxN6k8AAkMVaxuHV5hK8UI5i71IETsBAAMCAAN5AAM7BA",
        ]
    },
    "Футболка:Balenciaga":{
        "type": "clothes",
        "name": "Футболка:Balenciaga",
        "category": "Футболка",
        "material": "хлопок",
        "colors": "белый🤍/черный🖤",
        "price": "2690",
        "sizes": "S,M,L,XL,2XL(46,48,50,52,54)",
        "logo": "вышит",
        "photos": [
            "AgACAgIAAxkBAAMUadNvRVXH9NKocazjvEBGfcxN6k8AAkMVaxuHV5hK8UI5i71IETsBAAMCAAN5AAM7BA",
        ]
    },
    "Футболка:Tommy Hilfiger":{
        "type": "clothes",
        "name": "Футболка:Tommy Hilfiger",
        "category": "Футболка",
        "material": "100% хлопок",
        "colors": "белый🤍",
        "price": "2190",
        "sizes": "S,M,L,XL,2XL(46,48,50,52,54)",
        "logo": "вышит",
        "photos": [
            "AgACAgIAAxkBAAMUadNvRVXH9NKocazjvEBGfcxN6k8AAkMVaxuHV5hK8UI5i71IETsBAAMCAAN5AAM7BA",
        ]
    },
    "Футболка:Emporio Armani":{
        "type": "clothes",
        "name": "Футболка:Emporio Armani",
        "category": "Футболка",
        "material": "хлопок",
        "colors": "черный🖤",
        "price": "2190",
        "sizes": "S,M,L,XL,2XL(46,48,50,52,54)",
        "logo": "термонаклейка",
        "photos": [
            "AgACAgIAAxkBAAMUadNvRVXH9NKocazjvEBGfcxN6k8AAkMVaxuHV5hK8UI5i71IETsBAAMCAAN5AAM7BA",
        ]
    },
    "Футболка:Hugo Dobermann":{
        "type": "clothes",
        "name": "Футболка:Hugo Dobermann",
        "category": "Футболка",
        "material": "100% хлопок",
        "colors": "белый🤍/черный🖤",
        "price": "2190",
        "sizes": "S,M,L,XL,2XL(46,48,50,52,54)",
        "logo": "графический принт",
        "photos": [
            "AgACAgIAAxkBAAMUadNvRVXH9NKocazjvEBGfcxN6k8AAkMVaxuHV5hK8UI5i71IETsBAAMCAAN5AAM7BA",
        ]
    },
    "Футболка:Hugo Full House":{
        "type": "clothes",
        "name": "Футболка:Hugo Full House",
        "category": "Футболка",
        "material": "100% хлопок",
        "colors": "черный🖤",
        "price": "2550",
        "sizes": "S,M,L,XL,2XL(46,48,50,52,54)",
        "logo": "вышит",
        "photos": [
            "AgACAgIAAxkBAAMUadNvRVXH9NKocazjvEBGfcxN6k8AAkMVaxuHV5hK8UI5i71IETsBAAMCAAN5AAM7BA",
        ]
    },
    "Футболка:Polo Ralph lauren chief keef":{
        "type": "clothes",
        "name": "Футболка:Polo Ralph lauren chief keef",
        "category": "Футболка",
        "material": "хлопок",
        "colors": "черный🖤",
        "price": "1990",
        "sizes": "S,M,L,XL(46,48,50,52)",
        "logo": "вышит",
        "photos": [
            "AgACAgIAAxkBAAMUadNvRVXH9NKocazjvEBGfcxN6k8AAkMVaxuHV5hK8UI5i71IETsBAAMCAAN5AAM7BA",
        ]
    },
    "Футболка:Tommy Hilfiger":{
        "type": "clothes",
        "name": "Футболка:Tommy Hilfiger",
        "category": "Футболка",
        "material": "100% хлопок",
        "colors": "белый🤍",
        "price": "1990",
        "sizes": "S,M,L,XL,2XL(46,48,50,52,54)",
        "logo": "вышит",
        "photos": [
            "AgACAgIAAxkBAAMUadNvRVXH9NKocazjvEBGfcxN6k8AAkMVaxuHV5hK8UI5i71IETsBAAMCAAN5AAM7BA",
        ]
    },
    "Футболка:Hugo":{
        "type": "clothes",
        "name": "Футболка:Hugo ",
        "category": "Футболка",
        "material": "100% хлопок",
        "colors": "черный🖤",
        "price": "1990",
        "sizes": "S,M,L,XL,2XL(46,48,50,52,54)",
        "logo": "графический принт",
        "photos": [
            "AgACAgIAAxkBAAMUadNvRVXH9NKocazjvEBGfcxN6k8AAkMVaxuHV5hK8UI5i71IETsBAAMCAAN5AAM7BA",
        ]
    },
    "Футболка:Guess":{
        "type": "clothes",
        "name": "Футболка:Guess",
        "category": "Футболка",
        "material": "100% хлопок",
        "colors": "черный🖤",
        "price": "1990",
        "sizes": "S,M,L,XL,2XL(46,48,50,52,54)",
        "logo": "вышит",
        "photos": [
            "AgACAgIAAxkBAAMUadNvRVXH9NKocazjvEBGfcxN6k8AAkMVaxuHV5hK8UI5i71IETsBAAMCAAN5AAM7BA",
        ]
    },
    "Свитшот:GAP Palace":{
        "type": "clothes",
        "name": "Свитшот:GAP Palace",
        "category": "Свитшот",
        "material": "хлопок,полиэстер",
        "colors": "серый🩶",
        "price": "3600",
        "sizes": "S,M,L,XL,2XL(46,48,50,52,54)",
        "logo": "DTF печать",
        "photos": [
            "AgACAgIAAxkBAAMUadNvRVXH9NKocazjvEBGfcxN6k8AAkMVaxuHV5hK8UI5i71IETsBAAMCAAN5AAM7BA",
        ]
    },
    "Свитшот:BAPE":{
        "type": "clothes",
        "name": "Свитшот:BAPE",
        "category": "Свитшот",
        "material": "хлопок,полиэстер",
        "colors": "белый🤍",
        "price": "3000",
        "sizes": "S,M,L,XL,2XL(46,48,50,52,54)",
        "logo": "DTF печать",
        "photos": [
            "AgACAgIAAxkBAAMUadNvRVXH9NKocazjvEBGfcxN6k8AAkMVaxuHV5hK8UI5i71IETsBAAMCAAN5AAM7BA",
        ]
    },
    "Худи:Supreme":{
        "type": "clothes",
        "name": "Худи:Supreme",
        "category": "Худи",
        "material": "хлопок",
        "colors": "красный❤️",
        "price": "3600",
        "sizes": "S,M,L,XL,2XL(46,48,50,52,54)",
        "logo": "DTF печать",
        "photos": [
            "AgACAgIAAxkBAAMUadNvRVXH9NKocazjvEBGfcxN6k8AAkMVaxuHV5hK8UI5i71IETsBAAMCAAN5AAM7BA",
        ]
    },
    "Лонгслив:BAPE Chrome Hearts":{
        "type": "clothes",
        "name": "Лонгслив:BAPE Chrome Hearts",
        "category": "Лонгслив",
        "material": "хлопок,полиэстер",
        "colors": "черный🖤",
        "price": "2890",
        "sizes": "S,M,L,XL,2XL(46,48,50,52,54)",
        "logo": "DTF печать",
        "photos": [
            "",
        ]
    },
    "Лонгслив:Gucci Garden":{
        "type": "clothes",
        "name": "Лонгслив:Gucci Garden",
        "category": "Лонгслив",
        "material": "хлопок,полиэстер",
        "colors": "белый🤍",
        "price": "3199",
        "sizes": "",
        "logo": "DTF печать",
        "photos": [
            "",
        ]
    },
    "Джинсы:Fred Perry and Lyle Scott":{
        "type": "clothes",
        "name": "Джинсы:Fred Perry and Lyle Scott",
        "category": "Джинсы",
        "material": "деним",
        "colors": "черный🖤",
        "price": "4390",
        "sizes": "XS,S,M,L,XL,2XL(44,46,48,50,52,54)",
        "logo": "вышит",
        "photos": [
            "",
        ]
    },
    "Штаны широкие:Corteiz":{
        "type": "clothes",
        "name": "Штаны широкие:Corteiz",
        "category": "Спортивные-штаны",
        "material": "трикотаж",
        "colors": "черный🖤",
        "price": "3700",
        "sizes": "S,M,L,XL,2XL(46,48,50,52,54)",
        "logo": "вышит",
        "photos": [
            "",
        ]
    },
    "Жилетка:Polo x Italy":{
        "type": "clothes",
        "name": "Жилетка:Polo x Italy",
        "category": "Жилетка",
        "material": "хлопок",
        "colors": "черный🖤/серый🩶",
        "price": "3500",
        "sizes": "S,M,L,XL,2XL(46,48,50,52,54)",
        "logo": "DTF печать",
        "photos": [
            "",
        ]
    },
    "Поло:Corteiz":{
        "type": "clothes",
        "name": "Поло:Corteiz",
        "category": "Поло",
        "material": "хлопок",
        "colors": "черный🖤",
        "price": "2890",
        "sizes": "S,M,L,XL,2XL(46,48,50,52,54)",
        "logo": "DTF печать",
        "photos": [
            "",
        ]
    },
    "Лонгслив:Chrome Hearts":{
        "type": "clothes",
        "name": "Лонгслив:Chrome Hearts",
        "category": "Лонгслив",
        "material": "хлопок,полиэстер",
        "colors": "черный🖤",
        "price": "3000",
        "sizes": "S,M,L,XL,2XL(46,48,50,52,54)",
        "logo": "DTF печать",
        "photos": [
            "",
        ]
    },
    "Поло:polo ralph lauren":{
        "type": "clothes",
        "name": "Поло:polo ralph lauren",
        "category": "Поло",
        "material": "хлопок",
        "colors": "черный🖤/белый🤍",
        "price": "1690",
        "sizes": "S,M,L,XL(46,48,50,52)",
        "logo": "вышит",
        "photos": [
            "",
        ]
    },
    "Лонгслив:Martine Rose":{
        "type": "clothes",
        "name": "Лонгслив:Martine Rose",
        "category": "Лонгслив",
        "material": "хлопок,полиэстер",
        "colors": "черный🖤",
        "price": "3000",
        "sizes": "S,M,L,XL,2XL(46,48,50,52,54)",
        "logo": "DTF печать",
        "photos": [
            "",
        ]
    },
    "Штаны:Nike":{
        "type": "clothes",
        "name": "Штаны:Nike",
        "category": "Спортивные-штаны",
        "material": "хлопок",
        "colors": "белый🤍",
        "price": "3500",
        "sizes": "XS,S,M,L,XL(44,46,48,50,52)",
        "logo": "вышит",
        "photos": [
            "",
        ]
    },
   "Костюм:Nike x Brazil":{
       "type": "clothes",
       "name": "Костюм:Nike x Brazil",
       "category": "Костюм",
       "material": "100% полиэстер",
       "colors": "белая🤍ветровка и черные🖤/темно-зеленые💚 штаны",
       "price": "штаны - 4000, ветровка - 4500",
       "sizes": "штаны - S,M,L,XL / ветровка- S,M,L,XL",
       "logo": "вышит",
       "photos": [
           "",
       ]
   },
   "Джинсы:Maison Margiela"{
       "type": "clothes",
       "name": "Джинсы:Maison Margiela",
       "category": "Джинсы",
       "material": "деним",
       "colors": "синие",
       "price": "3890",
       "sizes": "XS,S,M,L,XL,2XL(38,40,42,44,46,48)",
       "logo": "вышит",
       "photos": [
           "",
       ]
   },
   "Джинсы:Dime":{
       "type": "clothes",
       "name": "Джинсы:Dime",
       "category": "Джинсы",
       "material": "деним",
       "colors": "черный🖤/белый🤍",
       "price": "3990",
       "sizes": "XS,S,M,L,XL,2XL(38,40,42,44,46,48)",
       "logo": "вышит",
       "photos": [
           "",
       ]
   },
   "Свитшот:Armani Exchange":{
       "type": "clothes",
       "name": "Свитшот:Armani Exchange",
       "category": "Свитшот",
       "material": "хлопковый трикотаж",
       "colors": "черный🖤/белый🤍",
       "price": "3550",
       "sizes": "S,M,L,XL,2XL(46,48,50,52,54)",
       "logo": "флекс",
       "photos": [
           "",
       ]
   },
   "Костюм:Nike Tn":{
       "type": "clothes",
       "name": "Костюм:Nike Tn",
       "category": "Костюм",
       "material": "высококачественная плащевка(водонепроницаемая)",
       "colors": "черный🖤",
       "price": "4300(весь костюм)",
       "sizes": "S,M,L,XL,2XL(46,48,50,52,54)",
       "logo": "вышит",
       "photos": [
           "",
       ]
   },
   "Худи:Russia":{
       "type": "clothes",
       "name": "Худи:Russia",
       "category": "Худи",
       "material": "плотный высококачественный хлопок",
       "colors": "черный🖤",
       "price": "4499",
       "sizes": "S,M,L,XL,2XL(40,42,44,46,48)",
       "logo": "вышит",
       "photos": [
           "",
       ]
   },
   "Джемпер:Polo Ralph Lauren":{
       "type": "clothes",
       "name": "Джемпер:Polo Ralph Lauren",
       "category": "Джемпер",
       "material": "плотный хлопок",
       "colors": "белый🤍/синий💙",
       "price": "3390",
       "sizes": "M,L,XL(42,44,46)",
       "logo": "вышит",
       "photos": [
           "",
       ]
   },
   "Джемпер:Karl Lagerfeld":{
       "type": "clothes",
       "name": "Джемпер:Karl Lagerfeld",
       "category": "Джемпер",
       "material": "плотный хлопок",
       "colors": "черный🖤",
       "price": "3590",
       "sizes": "S,M,L,XL,2XL(46,48,50,52,54)",
       "logo": "3D силикон",
       "photos": [
           "",
       ]
   },
   "Куртка:Lacoste":{
       "type": "clothes",
       "name": "Куртка:Lacoste",
       "category": "Куртка",
       "material": "стеганный текстиль",
       "colors": "черный🖤",
       "price": "3690",
       "sizes": "M,L,XL,2XL,3XL(48,50,52,54,56)",
       "logo": "вышит",
       "photos": [
           "",
       ]
   },
   "Свитшот:Karl Lagerfeld":{
       "type": "clothes",
       "name": "Свитшот:Karl Lagerfeld",
       "category": "Свитшот",
       "material": "плотный хлопок",
       "colors": "черный🖤",
       "price": "3590",
       "sizes": "S,M,L,XL,2XL(46,48,50,52,54)",
       "logo": "вышит",
       "photos": [
           "",
       ]
   },
   "Майка:Hermes":{
       "type": "clothes",
       "name": "Майка:Hermes",
       "category": "Футболка",
       "material": "хлопок",
       "colors": "черный🖤",
       "price": "2490",
       "sizes": "M,L,XL,2XL,3XL(маломерит)",
       "logo": "вышит",
       "photos": [
           "",
       ]
   },
   "Спортивный костюм:Zarra Suvene":{
       "type": "clothes",
       "name": "Спортивный костюм:Zarra Suvene",
       "category": "Костюм",
       "material": "плотный хлопок",
       "colors": "черный🖤/серый🩶",
       "price": "3890",
       "sizes": "S,M,L,XS,XL,2XL,3XL",
       "logo": "вышит",
       "photos": [
           "",
       ]
   },
   "Свитшот:Chrome Hearts":{
       "type": "clothes",
       "name": "Свитшот:Chrome Hearts",
       "category": "Свитшот",
       "material": "хлопок",
       "colors": "черный🖤/белый🤍",
       "price": "3690",
       "sizes": "S,M,L",
       "logo": "вышит",
       "photos": [
           "",
       ]
   },
   "Кардиган:Maison margiela":{
       "type": "clothes",
       "name": "Кардиган:Maison margiela",
       "category": "Кардиган",
       "material": "плотный хлопок",
       "colors": "черный🖤/белый🤍/серый🩶/синий💙",
       "price": "2990",
       "sizes": "S,M,L,XL(46,48,50,52)",
       "logo": "нет",
       "photos": [
           "",
       ]
   },
   "Полузамок:Polo Ralph Lauren":{
       "type": "clothes",
       "name": "Полузамок:Polo Ralph Lauren",
       "category": "Поло",
       "material": "плотный хлопок",
       "colors": "черный🖤",
       "price": "2790",
       "sizes": "M,L,XL,2XL(48,50,52,54)",
       "logo": "вышит",
       "photos": [
           "",
       ]
   },
   "Джинсы:Lacoste":{
       "type": "clothes",
       "name": "Джинсы:Lacoste",
       "category": "Джинсы",
       "material": "деним",
       "colors": "синий💙",
       "price": "3660",
       "sizes": "XS,S,M,L,XL,2XL(38,40,42,44,46,48)",
       "logo": "вышит",
       "photos": [
           "",
       ]
   },
   "Кроссовки:Nike Initiator Custom":{
       "type": "shoes",
       "name": "Кроссовки:Nike Initiator Custom",
       "category": "Кроссовки",
       "material": "сетчатые вставки/пеноматериал/прочная резина",
       "price": "4199",
       "sizes": "37,38,39,40,41",
       "box": "оригинальная коробка",
       "photos": [
           "",
       ]
   },
   "Кроссовки:Raf Simons":{
       "type": "shoes",
       "name": "Кроссовки:Raf Simons",
       "category": "Кроссовки",
       "material": "замша/нейлон/эко-кожа",
       "colors": "черный🖤/белый🤍/черно-белый🔲",
       "price": "5200",
       "sizes": "40,41,42,43,44",
       "box": "оригинальная коробка",
       "photos": [
           "",
       ]
   },
   "Кроссовки:Nike Air Jordan Retro 13":{
       "type": "shoes",
       "name": "Кроссовки:Nike Air Jordan Retro 13",
       "category": "Кроссовки",
       "material": "натуральная кожа, замша, баллистический нейлон",
       "price": "4690",
       "sizes": "40,41,42,43,44,45",
       "photos": [
           "",
       ]
   },
   "Кеды:Golden Goose":{
       "type": "shoes",
       "name": "Кеды:Golden Goose",
       "category": "Кеды",
       "material": "кожа",
       "colors": "белый🤍",
       "price": "5700",
       "box": "оригинальная коробка",
       "sizes": "41,42,43,44,45",
       "photos": [
           "",
       ]
   },
   "Кеды:Golden Goose Stardan"{
       "type": "shoes",
       "name": "Кеды:Golden Goose Stardan",
       "category": "Кеды",
       "material": "кожа",
       "colors": "черный🖤",
       "price": "5700",
       "sizes": "41,42,43,44,45",
       "box": "оригинальная коробка",
       "photos": [
           "",
       ]
   },
   "Кроссовки:Adidas ozweego x Raf Simons":{
       "type": "shoes",
       "name": "Кроссовки:Adidas ozweego x Raf Simons",
       "category": "Кроссовки",
       "material": "кожа",
       "price": "6000",
       "sizes": "41,42,43,44,45",
       "box": "оригинальная коробка",
       "photos": [
           "",
       ]
   },
   "Кроссовки:New Balance 9060":{
       "type": "shoes",
       "name": "Кроссовки:New Balance 9060",
       "category": "Кроссовки",
       "material": "натуральная замша/сетчатые вставки",
       "price": "4199",
       "box": "оригинальная коробка",
       "sizes": "37,38,39,40,41,42,43,44",
       "photos": [
           "",
       ]
   },
   "Кроссовки:RAF Simons Antei Runner":{
       "type": "shoes",
       "name": "Кроссовки:RAF Simons Antei Runner",
       "category": "Кроссовки",
       "material": "кожа,замша",
       "box": "оригинальная коробка",
       "price": "6000",
       "sizes": "41,42,43,44,45",
       "photos": [
           "",
       ]
   },
   "Кроссовки:Maison Margiela Future high":{
       "type": "shoes",
       "name": "Кроссовки:Maison Margiela Future high",
       "category": "Кроссовки",
       "material": "эко кожа",
       "box": "оригинальная коробка",
       "price": "3890",
       "sizes": "38,39,40,41,42,43,44,45",
       "photos": [
           "",
       ]
   },
   "Кроссовки:New Balance 1906A":{
       "type": "shoes",
       "name": "Кроссовки:New Balance 1906A",
       "category": "Кроссовки",
       "material": "сетчатые вставки/прочная резина/пеноматареил",
       "price": "4999",
       "sizes": "40,41,42,43,44,46",
       "box": "оригинальная коробка",
       "photos": [
           "",
       ]
   },
   "Кроссовки:Adidas x Yeezy Boost 350 V2":{
       "type": "shoes",
       "name": "Кроссовки:Adidas x Yeezy Boost 350 V2",
       "category": "Кроссовки",
       "material": "ткань primeknit",
       "colors": "белый🤍",
       "price": "4500",
       "sizes": "37,38,39,40,41,42,43,44,45",
       "box": "оригинальная коробка",
       "photos": [
           "",
       ]
   },
   "Кроссовки:Adidas Cp Company":{
       "type": "shoes",
       "name": "Кроссовки:Adidas Cp Company",
       "category": "Кроссовки",
       "material": "замша(верх),прочная резина(низ)",
       "colors": "темно-синий💙/голубой🐬",
       "price": "4199",
       "sizes": "41,42,43,44,45",
       "box": "оригинальная коробка",
       "photos": [
           "",
       ]
   },
   "Низкие кроссовки:Nike Cortez":{
       "type": "shoes",
       "name": "Низкие кроссовки:Nike Cortez",
       "category": "Кроссовки",
       "material": "кожа,замш",
       "price": "3290",
       "box": "оригинальная коробка",
       "sizes": "37,38,39,40,41",
       "photos": [
           "",
       ]
   },
   "Кроссовки:Balenciaga Track":{
       "type": "shoes",
       "name": "Кроссовки:Balenciaga Track",
       "category": "Кроссовки",
       "material": "сетчатый текстиль/нейлон/искусственная кожа/прочная резина",
       "colors": "белый🤍/черный🖤/оранжевый🧡",
       "box": "оригинальная коробка",
       "price": "6000",
       "sizes": "37,38,39,40,41,42,43,44,45",
       "photos": [
           "",
       ]
   },
   "Кроссовки:New Balance 327":{
       "type": "shoes",
       "name": "Кроссовки:New Balance 327",
       "category": "Кроссовки",
       "material": "замша/нейлон/сетчатый материал",
       "box": "оригинальная коробка",
       "colors": "серый🩶/зеленый💚",
       "price": "3990",
       "sizes": "40,41,42,43,44",
       "photos": [
           "",
       ]
   },
   "Кроссовки:Nike air jordan 4":{
       "type": "shoes",
       "name": "Кроссовки:Nike air jordan 4",
       "category": "Кроссовки",
       "material": "(верх)нубук,(низ)резина Air Sole",
       "box": "фирменная коробка",
       "price": "3890",
       "sizes": "41,42,43,44,45",
       "photos": [
           "",
       ]
   },
   "Кроссовки:Nike Dunk Low":{
       "type": "shoes",
       "name": "Кроссовки:Nike Dunk Low",
       "category": "Кроссовки",
       "material": "кожа",
       "price": "3590",
       "sizes": "37,38,39,40,41,42,43,44,45",
       "box": "фирменная коробка",
       "photos": [
           "",
       ]
   },
   "Кроссовки:Nike Air Tailwind 4":{
       "type": "shoes",
       "name": "Кроссовки:Nike Air Tailwind 4",
       "category": "Кроссовки",
       "material": "сетчатые вставки/синтетические накладки/пеноматериал",
       "colors": "на фото",
       "price": "3990",
       "box": "оригинальная коробка",
       "sizes": "41,42,43,44,45",
       "photos": [
           "",
       ]
   },
   "Кроссовки:Nike Air Jordan Low 1":{
       "type": "shoes",
       "name": "Кроссовки:Nike Air Jordan Low 1",
       "category": "Кроссовки",
       "material": "натуральная кожа",
       "box": "оригинальная коробка",
       "price": "3890",
       "sizes": "37,38,39,40,41,42,43,44,45",
       "photos": [
           "",
       ]
   },
   "Кроссовки:New balance 574":{
       "type": "shoes",
       "name": "Кроссовки:New balance 574",
       "category": "Кроссовки",
       "material": "замша",
       "box": "фирменная коробка",
       "price": "3990",
       "sizes": "41,42,43,44,45,46",
       "photos": [
           "",
       ]
   },
   "Кеды:Adidas Samba":{
       "type": "shoes",
       "name": "Кеды:Adidas Samba",
       "category": "Кеды",
       "material": "натуральная кожа/замша",
       "price": "3590",
       "box": "оригинальная коробка",
       "sizes": "41,42,43,44,45",
       "photos": [
           "",
       ]
   },
   "Кеды:Maison Margiela Replica Low":{
       "type": "shoes",
       "name": "Кеды:Maison Margiela Replica Low",
       "category": "Кеды",
       "material": "замша/кожа",
       "colors": "черный🖤/серый🩶",
       "price": "5000",
       "box": "оригинальная коробка",
       "sizes": "41,42,43,44,45",
       "photos": [
           "",
       ]
   },
   "Кроссовки:Adidas Yeezy 700 V3":{
       "type": "shoes",
       "name": "Кроссовки:Adidas Yeezy 700 V3",
       "category": "Кроссовки",
       "material": "моноволоконная сетка,текстиль",
       "price": "3390",
       "sizes": "41,42,43,44,45",
       "box": "оригинальная коробка",
       "photos": [
           "",
       ]
   },
   "Кроссовки:Nike Air Jordan Retro 13":{
       "type": "shoes",
       "name": "Кроссовки:Nike Air Jordan Retro 13",
       "category": "Кроссовки",
       "material": "натуральная кожа, замша, баллистический нейлон",
       "price": "4690",
       "sizes": "40,41,42,43,44,45",
       "photos": [
           "",
       ]
   },
   "Кроссовки:Asics Gel pickax":{
       "type": "shoes",
       "name": "Кроссовки:Asics Gel pickax",
       "category": "Кроссовки",
       "material": "кожа-замша(верх), пеноматериал(низ)",
       "price": "4490",
       "sizes": "41,42,43,44,45",
       "photos": [
           "",
       ]
   },
   "Кеды:numeris":{
       "type": "shoes",
       "name": "Кеды:numeris",
       "category": "Кеды",
       "material": "плотная ткань,кожа",
       "price": "5290",
       "sizes": "39,40,41,42,43,44,45",
       "photos": [
           "",
       ]
   },
   "Мужские кроссовки:louis vuitton":{
       "type": "shoes",
       "name": "Мужские кроссовки:louis vuitton",
       "category": "Кроссовки",
       "material": "полиуритан,ткань",
       "price": "3990",
       "sizes": "41,42,43,44,45",
       "photos": [
           "",
       ]
   },
   "Кеды:Golden Goose/DB":{
       "type": "shoes",
       "name": "Кеды:Golden Goose/DB",
       "category": "Кеды",
       "material": "кожа,замша",
       "price": "4190",
       "sizes": "39,40,41,42,43,44",
       "photos": [
           "",
       ]
   },
   "Кеды:premiata":{
       "type": "shoes",
       "name": "Кеды:premiata",
       "category": "Кеды",
       "material": "эко-кожа",
       "price": "4990",
       "sizes": "40,41,42,43,44,45",
       "photos": [
           "",
       ]
   }
}

CATEGORIES = {
    "Зип-худи": ["Зип-худи:Balenciaga", "Зип-худи:Polo ralph lauren", "Зип-худи:Lacoste", "Зип-худи:Karl Lagerfeld", "Зип-худи:Burberry"],
    "Футболка": ["Футболка:Aerounautica Мilitare", "Футболка:Balenciaga", "Футболка:Tommy Hilfiger", "Футболка:Emporio Armani", "Футболка:Hugo Dobermann", "Футболка:Hugo Full House", "Футболка:Polo Ralph lauren chief keef", "Футболка:Tommy Hilfiger", "Футболка:Hugo", "Футболка:Guess", "Майка:Hermes"],
    "Свитшот": ["Свитшот:GAP Palace", "Свитшот:BAPE", "Свитшот:Armani Exchange", "Свитшот:Karl Lagerfeld", "Свитшот:Chrome Hearts"],
    "Худи": ["Худи:Supreme", "Худи:Russia"],
    "Лонгслив": ["Лонгслив:BAPE Chrome Hearts", "Лонгслив:Gucci Garden", "Лонгслив:Chrome Hearts", "Лонгслив:Martine Rose"],
    "Джинсы": ["Джинсы:Fred Perry and Lyle Scott", "Джинсы:Maison Margiela", "Джинсы:Dime", "Джинсы:Lacoste"],
    "Спортивные-штаны": ["Штаны широкие:Corteiz", "Штаны:Nike"],
    "Жилетка": ["Жилетка:Polo x Italy"],
    "Поло": ["Поло:Corteiz", "Поло:polo ralph lauren", "Полузамок:Polo Ralph Lauren"],
    "Костюм": ["Костюм:Nike x Brazil", "Костюм:Nike Tn", "Спортивный костюм:Zarra Suvene"],
    "Джемпер": ["Джемпер:Polo Ralph Lauren", "Джемпер:Karl Lagerfeld"],
    "Куртка": ["Куртка:Lacoste"],
    "Кардиган": ["Кардиган:Maison margiela"],
    "Кроссовки": ["Кроссовки:Nike Initiator Custom", "Кроссовки:Raf Simons", "Кроссовки:Nike Air Jordan Retro 13", "Кроссовки:Adidas ozweego x Raf Simons", "Кроссовки:New Balance 9060", "Кроссовки:RAF Simons Antei Runner", "Кроссовки:New Balance 1906A", "Кроссовки:Adidas x Yeezy Boost 350 V2", "Кроссовки:Adidas Cp Company", "Низкие кроссовки:Nike Cortez", "Кроссовки:Balenciaga Track", "Кроссовки:New Balance 327", "Кроссовки:Nike air jordan 4", "Кроссовки:Nike Dunk Low", "Кроссовки:Nike Air Tailwind 4", "Кроссовки:Nike Air Jordan Low 1", "Кроссовки:New balance 574", "Кроссовки:Adidas Yeezy 700 V3", "Кроссовки:Nike Air Jordan Retro 13", "Кроссовки:Asics Gel pickax", "Мужские кроссовки:louis vuitton"],
    "Кеды": ["Кеды:Golden Goose", "Кеды:Golden Goose Stardan", "Кеды:Adidas Samba", "Кеды:Maison Margiela Replica Low", "Кеды:numeris", "Кеды:Golden Goose/DB", "Кеды:premiata"]
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
            [InlineKeyboardButton(text="🧥 Куртка", callback_data="Куртка")],
            [InlineKeyboardButton(text="🧥 Зип худи", callback_data="Зип-худи")],
            [InlineKeyboardButton(text="🧥 Жилетка", callback_data="Жилетка")],
            [InlineKeyboardButton(text="👕 Футболка", callback_data="Футболка")],
            [InlineKeyboardButton(text="👕 Поло", callback_data="Поло")],
            [InlineKeyboardButton(text="👕 Лонгслив", callback_data="Лонгслив")],
            [InlineKeyboardButton(text="👕 Свитшот", callback_data="Свитшот")],
            [InlineKeyboardButton(text="👕 Джемпер", callback_data="Джемпер")],
            [InlineKeyboardButton(text="👕 Кардиган", callback_data="Кардиган")],
            [InlineKeyboardButton(text="👕 Худи", callback_data="Худи")],
            [InlineKeyboardButton(text="👖 Джинсы", callback_data="Джинсы")],
            [InlineKeyboardButton(text="👖 Спортивные штаны", callback_data="Спортивные-штаны")],
            [InlineKeyboardButton(text="👖🧥 Костюм", callback_data="Костюм")],
            [inlineKeyboardButton(text="👟Кроссовки", callback_data="Кроссовки")],
            [inlineKeyboardButton(text="👟Кеды", callback_data="Кеды")]
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
    product_id = ":".join(callback.data.split(":")[1:])  
    index = user_photo_index.get(user_id, {}).get(product_id, 0)
    if index < len(PRODUCTS[product_id]["photos"]) - 1:
        index += 1
        user_photo_index[user_id][product_id] = index
        await update_product(callback, product_id, index)
    await callback.answer()

@router.callback_query(F.data.startswith("prev_photo:"))
async def prev_photo(callback: CallbackQuery):
    user_id = callback.from_user.id
    product_id = ":".join(callback.data.split(":")[1:])  
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

    await callback.message.delete()  

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

    if product["type"] == "clothes":
        caption = (
            f"🧥 {product['name']}\n"
            f"•📐размерная сетка:{product.get('sizes', '—')}\n"
            f"•🪽материал-{product.get('material', '—')}\n"
            f"•🎨 цвета:{product.get('colors', '—')}\n"
            f"•🏷️ бирки фирменные\n"
            f"•📌 логотип-{product.get('logo', '—')}\n"
            f"•💸 цена - {product.get('price', '—')}\n"
            f"•✅ писать @EYRoyul  @Emendgi_manager\n"
            f"•‼️ уточнять наличие\n"
            f"\n📸 {index+1}/{len(photos)}"
        )
        
    elif product["type"] == "shoes":
        box_text = f"•📦 {product['box']}\n" if product.get("box") else ""
        colors_text = f"•🎨 цвета: {product['colors']}\n" if product.get("colors") else "
        
        caption = (
            f"👟 {product['name']}\n"
            f"•📐размеры: {product['sizes']}\n"
            f"•🌸материал: {product['material']}\n"
            f"{colors_text}"
            f"{box_text}"
            f"•💸 цена: {product['price']}\n"
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
