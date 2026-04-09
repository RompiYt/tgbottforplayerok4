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
            "AgACAgIAAxkBAAIBGGnW4Z3xkfE-bbxiSa0bfsu5yXEgAALNFGsbU5PoSTRAMZOJUabEAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBGWnW4Z3DTT7-Yw7XkVOHTrbaZUAuAALOFGsbU5PoSW2MM00vMmb_AQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBHWnW4Z01i5qbq6u7P69A-addRwsuAALUFGsbU5PoSdbm94GcXoCOAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBF2nW4Z1uJFd8yR2hlKDKkQixjgL3AALMFGsbU5PoSWrt4_zJK01mAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBGmnW4Z3wtMny6OmwCK5zcdk4PKooAALPFGsbU5PoSc8qPGB8JFdAAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBG2nW4Z3acO2hh18eBYosvZVBwdsuAALQFGsbU5PoSQK_H6vLnrvSAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBHGnW4Z0XdAeLScKOqA4pgvfhmm2EAALTFGsbU5PoSfCHiiyLt85pAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBKmnW4fRrPj0cJU8xiNlcAjM3cIhGAAJQFmsbU5PgSWbRiPxsQAYzAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBKWnW4fSec-fS3zH4P1-7_REdNmIuAAJPFmsbU5PgSZqWnqLo7M5DAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBJWnW4fRv4ylfuMrKnixSeyFz-GNcAAJMFmsbU5PgSab_dKM8eXF2AQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBJ2nW4fT0gT0I34P1Ahe2dIofnYEfAAJOFmsbU5PgSVrNLz1ypOXXAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBJmnW4fQbfp6NYeD-OA9ma8jmYzRmAAJNFmsbU5PgSQbivcfITVAKAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBK2nW4fTJSROF5PnheJB-cl0OcvlAAAJRFmsbU5PgSabKBJOqHySvAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBJ2nW4fT0gT0I34P1Ahe2dIofnYEfAAJOFmsbU5PgSVrNLz1ypOXXAQADAgADeQADOwQ"
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
            "AgACAgIAAxkBAAICmmnXfEch2s8iaI-in7SX6BKxczErAAJzFmsbqGKZSYYpINBU1QqVAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICm2nXfEdBWHD-llH6HMYqrIdM60mRAAJ1FmsbqGKZSVN2Lc3b_vhIAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICmWnXfEekuqc7yDUX6nCu3s337qAuAAJyFmsbqGKZSe_hZEoHqj5FAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIComnXfEf4z0LNT3tGZW6qKofm-gQYAAJ8FmsbqGKZSRluj93rq9KhAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICnGnXfEevnfYPdP4zWgiawv1i_9hLAAJ2FmsbqGKZSbBcAAG92tQ1egEAAwIAA3kAAzsE",
            "AgACAgIAAxkBAAICnWnXfEeHgKTrimqCCMUC1juEBBhpAAJ3FmsbqGKZSbfQevuYbGbrAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICoWnXfEcZnmGxL6-qlQWaEehuUkj6AAJ7FmsbqGKZSR8iFICTrMbwAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICn2nXfEdHN5IG9B0Jf1bz1EoCQKdfAAJ5FmsbqGKZSVO4E6R_fngoAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICnmnXfEerh2wWcPOTwhNvyR60GhkZAAJ4FmsbqGKZSQYnxo_8yyyyAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICoGnXfEd-k2va_CU29sPTqBpxwqyWAAJ6FmsbqGKZSfzH345JgDRnAQADAgADeQADOwQ"
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
            "AgACAgIAAxkBAAICsmnXfL-jNxILMv3Pv0OEj9N3kU0MAAIXEmsbnGmgSQkmp-nvkTToAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICsWnXfL-nacaLsWVup8avxMXSxIAtAAIWEmsbnGmgSY3lsompXvNAAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICrmnXfL-Fj8qYvpGXutmNuxG7ZEaMAAITEmsbnGmgSQ2iEv0COjoiAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICs2nXfL8cLGG3uH6a15qYnaODXWm_AAIYEmsbnGmgSTdCiEza0q5EAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICrWnXfL9zihmBKXJXgQcirA21TFZzAAISEmsbnGmgSWXc5t2dIsv4AQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICr2nXfL-Sw74tHV8zPaRfS53HxNmbAAIUEmsbnGmgSdHsOcrwNnHqAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICsGnXfL_lKHdVK4hzoDdLMXEONltuAAIVEmsbnGmgSc2WZWtvHKGUAQADAgADeQADOwQ"
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
            "",
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
            "",
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
            "",
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
            "",
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
            "",
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
            "",
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
            "",
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
            "AgACAgIAAxkBAAIBV2nXcpkCMA6ivR_YYDcmEHN0KwIdAAIRFGsbfs_QSem68jcPf6_aAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBWmnXcpm82ID0lB8knqfD8CJmUKDoAAIUFGsbfs_QSQ03QNQONx-yAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBW2nXcpnmiJcdg9VWVN9spgqDR3K4AAIVFGsbfs_QSb4nZgpmqU_wAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBXmnXcpnz0UfyQr363AxM-E2bTnLCAAIbFGsbfs_QSY2sCVOG564BAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBWGnXcpnvrc46Di6CCvX4n3gfCViEAAISFGsbfs_QSd2IX9q8mjxeAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBXGnXcplzXz329Ls10pmMk3bk7Wp-AAIXFGsbfs_QSU5xN0n9WVmwAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBXWnXcpnJ8FlCXSwSIRdlcqkUW3oPAAIaFGsbfs_QSUQSSGQ45gNvAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBX2nXcpmpcIjG5DTGnjUu7UuKjIKLAAIcFGsbfs_QSXXVR04L4zj5AQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBWWnXcplpMeg4FqB2E-9dZc46vm3jAAITFGsbfs_QSZ-Jmd2Do1mcAQADAgADeQADOwQ"
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
            "AgACAgIAAxkBAAIBeWnXc68eZ7SeYcvGGgRllDG26laXAAJNEmsbfs_QSfo8PDRgVTjwAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBf2nXc68WmcERzBtVC0BxkYAX6F7ZAAJTEmsbfs_QSTIzC_gxH9EgAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBgGnXc6_NeFMMgIJ63szMxoa3QOphAAJUEmsbfs_QSYiNpOpT6Hp9AQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBfmnXc68mh8qZThO_1ln0q7waptDwAAJSEmsbfs_QSfhgqFkivMapAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBemnXc6_rbzCqP9a8CTaZPl77dO2wAAJOEmsbfs_QSYsOkByJFnEpAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBe2nXc6_Ts269kQABMUvN3aitrfmIDwACTxJrG37P0Em4BsAso_0GUQEAAwIAA3kAAzsE",
            "AgACAgIAAxkBAAIBfGnXc6_vJXrQmv5OJILmen0wnbLGAAJQEmsbfs_QSdDQIspFspxyAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBfWnXc698R_P4Y3xPAAHuER7cPd488wACURJrG37P0EmL-Z4QIG1gswEAAwIAA3kAAzsE"
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
            "AgACAgIAAxkBAAIBaWnXczfCAAEtHBn5UebWeYI6ybFrNQACBBRrG37P0EkwM6mMqe0-4wEAAwIAA3kAAzsE",
            "AgACAgIAAxkBAAIBamnXczdrC6v8z0hgmes5xC7c3Is9AAIFFGsbfs_QSZN3tKJSj0CAAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBa2nXczcLQ7RMTDbDBFfkzk3vzbB0AAIGFGsbfs_QSRjo6zyVWu-KAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBbmnXczebBDXhxhhUJYdNumCqZFmkAAIJFGsbfs_QSQ83o3Qg_5b6AQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBb2nXczez_cRvf-iCg0aEwEM2s4LaAAIKFGsbfs_QSWBSHo2EkGKIAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBbWnXczcKi5N0mo1aDNBYYZdbJpVPAAIIFGsbfs_QSULZTeLO0r0vAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBbGnXczemeQ90K8BNk7TvhKJti7vEAAIHFGsbfs_QSeTWIe1P5gToAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBcGnXczdjqYBZP7csDyFPXluBa48GAAILFGsbfs_QSTRIQJntgTbDAQADAgADeQADOwQ"
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
            "AgACAgIAAxkBAAIBqWnXdUY0J4JIJjHK6dnvuNny-YkVAAKMFmsb81vASXJt3KeOKbHBAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBqGnXdUav6JcwSLsOtrKhWsH5UjphAAKLFmsb81vASQ4bYkdFXR0-AQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBrGnXdUZF-N26nGiad2d9jj0wNj-8AAKQFmsb81vAScx4HCNehI7YAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBq2nXdUZEr5AjovFSEzzeynCAm43mAAKPFmsb81vASaGpBNDypI1xAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBr2nXdUaq47EdOgxfTIoaMR8em_D0AAKTFmsb81vASfo958vhg16OAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBp2nXdUYf8cNJ3FKoBGAEubo5F6poAAKKFmsb81vASfdBklVxbXidAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBsGnXdUbcVQSMccg2ER9do_9dTBPfAAKUFmsb81vASf4uiiyCaUu6AQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBrmnXdUZO6AJ9BWPdfniABisVd9rsAAKSFmsb81vASVakgnG0nE08AQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBrWnXdUacQ4G5Q5LdFiT-WpU3wNHWAAKRFmsb81vASeWPx-lmqgnNAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBqmnXdUbcaXH8x_Stae-NiVhSBHZLAAKOFmsb81vASazXkMC7qtW5AQADAgADeQADOwQ"
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
            "AgACAgIAAxkBAAIB0mnXd0DZucBFt0zgmQ8VjK-XRC8pAALPG2sbmMFQShCVYZVKgr6EAQADAgADdwADOwQ",
            "AgACAgIAAxkBAAIB0WnXd0DEUgn2Nw0fYHvW5OEp2_yGAALOG2sbmMFQSu3AXDvTQAY2AQADAgADdwADOwQ",
            "AgACAgIAAxkBAAIBz2nXd0BeJ1q52CYdBuLXlP-X27zvAALMG2sbmMFQStOFtmn32bruAQADAgADdwADOwQ",
            "AgACAgIAAxkBAAIB0GnXd0CNQsuxShOPBFAeb6Sma9DBAALNG2sbmMFQSq09DSka5mPBAQADAgADdwADOwQ",
            "AgACAgIAAxkBAAIBzmnXd0CQXaZwX6CqlTbEw-VVo5-hAALLG2sbmMFQSsd5Pht1W6h9AQADAgADdwADOwQ",
            "AgACAgIAAxkBAAIBzWnXd0A3vDTemz52GoYXbNYKVF5ZAALKG2sbmMFQSqDB_VM74TZmAQADAgADdwADOwQ"
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
            "AgACAgIAAxkBAAIBv2nXdt-HteVPek0dlDRWKj74asu-AAKCFGsbPOxpSqwUpxcLi1UCAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBwGnXdt_7H4udwnqdHBOARBLRvr-uAAKDFGsbPOxpSu96qvPYfh29AQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBw2nXdt_evsKmJZ1HFPaYuSQVa1_-AAKIFGsbPOxpSox8wfqju1_IAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBu2nXdt9SvHJZRF-otWprX4-EzTl4AAJ-FGsbPOxpSsv-tBRFzEeXAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBwWnXdt9VtLismzXiXsWu0SNl2FfYAAKEFGsbPOxpSvsQyLF_pND8AQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBvGnXdt8ZK4c917p7ujs7X5Sk9WqyAAJ_FGsbPOxpSiCBKY00zc31AQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBwmnXdt8XakMtS_29AR7ywc5NUtMBAAKHFGsbPOxpSrUrUXJ3y9M-AQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBvmnXdt_cSkTmQSNVC6r7qHh_oqHwAAKBFGsbPOxpSjb007p_sMftAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIBvWnXdt_RVU0nQoksGo8RCF0htb88AAKAFGsbPOxpSh3Nigq0rdUYAQADAgADeQADOwQ"
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
            "AgACAgIAAxkBAAIB9WnXeC-LWMvaf5id53jIUNh8LAllAAKdFWsbf5s4Sqc8mpLCe42aAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIB8WnXeC87bANnDNLE2tFNXvz7g68HAAKZFWsbf5s4SljL1VyFNyssAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIB9GnXeC_41Kjk9Ly2P_4qJEZMAnKsAAKcFWsbf5s4SqfmxMXNbBavAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIB82nXeC8n4RfdVYzXRvvn8mcNqthpAAKbFWsbf5s4Spa1u6_oQKzpAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAIB8mnXeC9HltPiUrxxKbt08oQBU7dJAAKaFWsbf5s4SshY8cXwNL9WAQADAgADeQADOwQ"
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
            "AgACAgIAAxkBAAICD2nXeOyzg_l18F7nrX5__8fPXdzyAALyEmsb3G0gSuSkpzgrdgdxAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICDmnXeOzBF5EYfRvbkf--vbr_rkhlAALxEmsb3G0gSowH8Qaci8HeAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICEmnXeOyzUL2YcE0AAVPhm2c7d2uVeAAC9RJrG9xtIEr3xwXbm22nTQEAAwIAA3kAAzsE",
            "AgACAgIAAxkBAAICEGnXeOzn8AwqxWiqOnUdDPO8i9YfAALzEmsb3G0gSiizPTWDkZcjAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICDWnXeOwpXbKlYo64Xnh_A2mGGgABGQAC8BJrG9xtIEqETj7f8bxfOQEAAwIAA3kAAzsE",
            "AgACAgIAAxkBAAICFGnXeOxRaN18Cb7qvw6GOOlwaI2FAAL2Emsb3G0gSioHxD0pjusmAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICEWnXeOyW3AoRLNO1xxHEPngGojTZAAL0Emsb3G0gSlasIgYdK9TRAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICE2nXeOwocRWUnNn85jaweRuZ7erGAAKfF2sb688ZSu9c0VeBuGbvAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICHmnXeUkrZ2VY_CLClu1gqIU3QHFeAALoEmsb3G0gSteMtJF3KBOMAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICH2nXeUnpoPbif9JjnT7qPO0IqN4BAALpEmsb3G0gSr4GHQuQlQwLAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICIGnXeUkozVP-GvEclPc_73qA16lWAALqEmsb3G0gSkvmM3aGxnwIAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICI2nXeUlTlPHE7EAhMjoboTyTWc73AALtEmsb3G0gSl1uWqe_kr7kAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICHWnXeUmGGbDXMHQttnrSsRrrtiQFAAKeF2sb688ZSs-oNDdDTzFUAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICImnXeUm0DybjG9lA0kPvufwzraxyAALsEmsb3G0gSg948q91lIhhAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICJGnXeUn952s0ga2CrjAEBUZiYpiWAALuEmsb3G0gSn6YV9Gm3LPCAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICIWnXeUmUTiu63-JPBpgbvsLrIRORAALrEmsb3G0gSnJ7J420T4OLAQADAgADeQADOwQ"
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
            "AgACAgIAAxkBAAICL2nXebFexkgkZWDmdKGY-RomIMoTAALKEmsb3G0gSpLNzU3mv01MAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICMmnXebFW_QmJs9YmtDeQQWoAAeXu3gACzRJrG9xtIEo454ULZBBfowEAAwIAA3kAAzsE",
            "AgACAgIAAxkBAAICM2nXebF7GKScVlsrGGkB04KtaxoFAALOEmsb3G0gSt9WP1OQzweBAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICLWnXebFImnjR8k1_sOjPZmWQhasnAALIEmsb3G0gSgpU_HaqeFFtAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICLmnXebGSENSooZUHKg9pwevzNzrQAALJEmsb3G0gSiE6La8kNIsOAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICNWnXebEIlHcbEbhoTXVBFoIpt5N8AALQEmsb3G0gSq94hWYHKmcvAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICMGnXebHcscX76cc5Jxx53bKrPevNAALLEmsb3G0gSuCM4mZzfWYWAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICMWnXebEh-uW5j3F_4qveNuY6dBiSAALMEmsb3G0gSvcRnMhuMSLhAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICNGnXebEt1kVCQR1kfoN41IXNzePlAALPEmsb3G0gSsoF7Zqb2O1ZAQADAgADeQADOwQ"
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
            "AgACAgIAAxkBAAICP2nXehkxvXkZpDLMlZvfX5s03AfuAAKAFGsb3G0YSn7ZaW-om49YAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICRGnXehkszDSLsn-pMlmYa3D7Np_fAAKFFGsb3G0YSk7CqRuAok_5AQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICQ2nXehm4QUxETMLg2YG0SKTCfIvdAAKEFGsb3G0YSkkSjXpULm1OAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICQWnXehnSuTJyrLV23HLtCGSKiFFPAAKCFGsb3G0YSiRjPxKcVYTgAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICQGnXehnePLpH_yX16bQ4LfMlIZrnAAKBFGsb3G0YSkOndEHDAuR5AQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICRmnXehns3iJMJl2yPhI0M16aiWOrAAKHFGsb3G0YSptBv3yxl7zPAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICQmnXehnVItn8WEO43WjC3eoa9WmUAAKDFGsb3G0YSiF-RRW1CfPsAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICR2nXehlIO3VMX4wp69dq3KEOjWiIAAKIFGsb3G0YSsXoAwABSi5OxgEAAwIAA3kAAzsE",
            "AgACAgIAAxkBAAICSGnXehmJ--zA2W5E7uaCRH0Yd3n5AAKJFGsb3G0YSj_gykpp0Y0qAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICRWnXehky4AHkgz3ryO4JkXYmy9J1AAKGFGsb3G0YSm7FcgqsT-a4AQADAgADeQADOwQ"
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
            "AgACAgIAAxkBAAICVGnXeo2W3ri3HmZfmU8gtcq66Q1EAAJuGGsbjPEJSvwt50y3dFZkAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICU2nXeo1EeobMQ8SAqzNro1Z9vdwNAAJtGGsbjPEJSjMeRofhZ9zcAQADAgADeQADOwQ"
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
            "AgACAgIAAxkBAAICbWnXezDZnHk4o7JwIRcxjlKat_FMAALmFmsblsf5SS3DNpaSmrvHAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICb2nXezDgotauPHcgw5Xnlx724O-7AALoFmsblsf5SUx8B6eVjGUBAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICa2nXezCsf2DVQStdXzi0XS_ZrIYIAALkFmsblsf5SbiM9J2QZLRCAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICcmnXezC1U5l85pPjrKx5klC0NEz7AALrFmsblsf5Sf9Rm4SeufypAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICc2nXezBVvIh43b7EfDoKuxDzFPa6AALtFmsblsf5SdZH5N0dCJ47AQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICbGnXezDd_sexHaZEGSURLFP739XlAALlFmsblsf5SYGMunn_X6T-AQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICbmnXezC8GWwEVIIzsbKtYrkGLmGrAALnFmsblsf5SZyMhGmfiYrjAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICcGnXezBXAAEQUJIPTEIWD4NRfRcOKQAC6RZrG5bH-Ukf5huku-gWAgEAAwIAA3kAAzsE",
            "AgACAgIAAxkBAAICcWnXezAzbZgyNFPLrvRV8AsbZsCWAALqFmsblsf5SSFNmujxyzy_AQADAgADeQADOwQ"
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
            "AgACAgIAAxkBAAICyWnXfUjSaBMfLcPpTEli47gEq2w7AALRFGsbLkyISWlnIAstJvhWAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICy2nXfUhQzQyueLRUZq43Ccwhg-2oAALTFGsbLkyISVIQLqDFmVexAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICzWnXfUgEs24fxb9nRV4h7J56B1lmAALVFGsbLkyISc9gA2pge2jvAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICzGnXfUjzNLJl8vLGg7_Roi3Nwad8AALUFGsbLkyISeCZH6-uDDymAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICymnXfUj7f_pu5GvZnw5AOLSc15QPAALSFGsbLkyISal6CS3iKLAaAQADAgADeQADOwQ",
            "AgACAgIAAxkBAAICzmnXfUhleZaVtYsDzb5vDgAB1FiGKQAC1hRrGy5MiElo3trkU1fXuQEAAwIAA3kAAzsE"
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
           "AgACAgIAAxkBAAICvGnXfP6Njy2tkQJonE0xokUhmJI0AAKeFGsbnGmYSXGH6OGygNhyAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICwGnXfP449WXp-dPS-wI30OZu-wqaAAKkFGsbnGmYSWi462Jzubo0AQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICu2nXfP5WjIKX4ezUnyTdOBPQ7uyhAAKdFGsbnGmYSX6P8U731kJAAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICvWnXfP7nqzMnxCOgwAR_tkg72pDuAAKfFGsbnGmYSf4AAbdI8JPMugEAAwIAA3kAAzsE",
           "AgACAgIAAxkBAAICv2nXfP4xcRcGaR0m-w0Tyk-h8kgcAAKiFGsbnGmYScXsxXDLcxVqAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICwWnXfP4ecW35RQoQMW3ju1ADhw6uAAKlFGsbnGmYSeUe-4vi4lTWAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICvmnXfP5QMknxrxvEwHdzIlnhWtmHAAKhFGsbnGmYSUVVbXvSbQHoAQADAgADeQADOwQ"
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
           "AgACAgIAAxkBAAIC_GnXfmfftWUvuSYv6dG_6Tp6R5KyAAJQE2sb3sxxSSIVRauQTi-5AQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIC-2nXfmdtdMeF4y5hDUox0f4NqxZEAAJME2sb3sxxSUfzyz8B0A6XAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIC-mnXfmcy8wh5RP9zq7PsyKndNnpSAAJLE2sb3sxxSVVp9_hd66OEAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIC-WnXfmefkGzb-qOF_aVS7n6GkCUOAAJJE2sb3sxxSVCefD_YN7CYAQADAgADeQADOwQ"
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
           "AgACAgIAAxkBAAIDE2nXfv07AwUHbJBx1bV3YdG2D2xjAAKHFGsbQtVwSXum-0wwHf54AQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDEmnXfv3f8vwcCGNFpox7ssQRSqkuAAKGFGsbQtVwSWmy6AqVK6KeAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDFGnXfv03WNzn5qYIQe_lbnj_GbJ8AAKIFGsbQtVwSYnie5z4bC80AQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDFmnXfv20f7V8xDXE4JjkwcfLEDvAAAKKFGsbQtVwSX6GUHoxmBg_AQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDEWnXfv0J0G9z-QRYsIOaDZ6U3ldjAAKEFGsbQtVwSQO62dUfFs-vAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDFWnXfv3WX_nDAAFT3hvNb0WcFZ4l0AACiRRrG0LVcEmFMmQ3CygWHgEAAwIAA3kAAzsE"
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
           "AgACAgIAAxkBAAIDJmnXfzuII78jR_uasP4ZCiX_S8DSAAJfFGsbQtVwSa1DG_zJ-M6IAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDH2nXfzsepwtpquh-DdCd36u9ejxvAAKNE2sbQtVoSSYqUZEAAdBSXgEAAwIAA3kAAzsE",
           "AgACAgIAAxkBAAIDHmnXfzt3hqHx79Qgl2wpPizzz7ySAAKME2sbQtVoSRLjDTpy2zJ4AQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDHWnXfzsVJ7SW_9rK_n7AtNECK9bjAAKLE2sbQtVoSR-K8S2oKfogAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDIGnXfzuUVN-zHZrTobb1lTaAuVYoAAKOE2sbQtVoSfR-9g-P6n8tAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDIWnXfzs3lgxFXX70ueGvT1t9AAF_zQACjxNrG0LVaEnYjkAqnIth7AEAAwIAA3kAAzsE",
           "AgACAgIAAxkBAAIDI2nXfzsskSJtJrHf8R0R_-OTtHWEAAJcFGsbQtVwScuH-Aia7_NnAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDImnXfzt6YVd8Qmti5JqUDVtYAAGfogACWxRrG0LVcElfMrYyvRmNkwEAAwIAA3kAAzsE",
           "AgACAgIAAxkBAAIDJGnXfzu_owPnu6MYQ9MIN89b3FvUAAJdFGsbQtVwSeofQi2jUZcbAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDJWnXfztI8DplOh_23P8LGM54MV1yAAJeFGsbQtVwSZjZ1hvZM7fSAQADAgADeQADOwQ"
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
           "AgACAgIAAxkBAAIDMWnXf7L4TZYxnAKIKlUAAYsID8lBQwAC3hVrGx9HkEp6HHw79124DgEAAwIAA3kAAzsE",
           "AgACAgIAAxkBAAIDM2nXf7JHT1R4Bk867GLoEqnAESnvAALgFWsbH0eQStbR9OFFGzrzAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDNGnXf7Lw84LHG4i07TxmoV8_IaKMAALhFWsbH0eQSiqIwuADfXpdAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDMmnXf7JtsVIyPUwv_M4XHti-RF-RAALfFWsbH0eQSoNWdJOnlWLcAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDNWnXf7J8oRP8SRdTsGN9nJgug87MAALiFWsbH0eQSvRAnoK6QcpIAQADAgADeQADOwQ"
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
           "AgACAgIAAxkBAAIDU2nXgJS-hAPjl3EI-4z_xs6d9OgNAAJhFWsbv_x4SqJ5gPpqGIUrAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDVmnXgJRS8wyLIwvKFutkN_5J_7LCAAJkFWsbv_x4Sh5lOpQqRd5HAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDWGnXgJRCj1Mk_QABt4IhMiOlm1XFDwACZhVrG7_8eEqGQYzpp-PXGAEAAwIAA3kAAzsE",
           "AgACAgIAAxkBAAIDWWnXgJSwrHxIZ_WwShSAnjWWAWVmAAJnFWsbv_x4Sg6FiBquozTNAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDVWnXgJTZSPoPMdYlD8E90DWlHMosAAJjFWsbv_x4SmNY_PegTkjbAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDVGnXgJSwmGRMxd8u9PhmD-ST71aYAAJiFWsbv_x4SjgZjf1n7OUAAQEAAwIAA3kAAzsE",
           "AgACAgIAAxkBAAIDV2nXgJSwjDW7j5phGUND5dpaUcy7AAJlFWsbv_x4SijjOZbVByPsAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDWmnXgJRuKcbWuffbJdrnKapocxBLAAJoFWsbv_x4SkILFs9eK6RKAQADAgADeQADOwQ"
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
           "AgACAgIAAxkBAAPNadbfW3WINID5sV8Ffnz7t0fe3_IAAtcRaxtRlfBJglV9GUyg2akBAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAPQadbfW9GgfIXTFBUS8IB3TzhpXRkAAtoRaxtRlfBJI9CCHz57e-4BAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAPTadbfWyHa3ZxHhDkbosLOBFO5VCgAAt0RaxtRlfBJBOcH84Nx0P8BAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAPPadbfWyEzhc4QkTUXgMO8jin3LOgAAtkRaxtRlfBJbwYNStiKHvoBAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAPOadbfWymS32TjahyzKWu8EvAvEMIAAtgRaxtRlfBJevkw2ciW43MBAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAPRadbfW52hxOu4sGBXvmra74a8RRAAAtsRaxtRlfBJgMEa4zfbi7kBAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAPSadbfW4JXWOlMsjqlBuGPsv3g0v0AAtwRaxtRlfBJadfx4mvJkJwBAAMCAAN5AAM7BA"
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
           "AgACAgIAAxkBAAPfadbfwprrgjYi0LnpNtxWB5_8og0AAn0VaxvUb7FJC3V_p-oFZY4BAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAPbadbfwm5AwENTMMf4GvX-Jv6Nr2AAAjEbaxuG_7FJh3L-UbywE-UBAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAPeadbfwiVOUHoq2IHLTUnP1OEWYwcAAnwVaxvUb7FJ1t8MnJOcx7ABAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAPkadbfwl29PWb3YRC2X1JaM3aObjMAAoIVaxvUb7FJ1t8I7MWGqDkBAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAPcadbfwoRiThK6qRos5Pp0o04ZhksAAjIbaxuG_7FJFXNWJHDZLl8BAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAPgadbfwqDrAciZwqcjLF3IVWvyD0MAAn4VaxvUb7FJzjjpbn8QmGcBAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAPiadbfwmSBhn7OA7MFPG03GZvZDdgAAoAVaxvUb7FJLq-2ZjZLLbEBAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAPjadbfwv9u9CCvVZQupdlX2mGx4S4AAoEVaxvUb7FJFpuPhs2CN-MBAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAPhadbfwjhPN2062DA91l08TOUxgxYAAn8VaxvUb7FJGytE9komCRIBAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAPdadbfws8IyqLN2rTegEOgfvFT17UAAjAbaxuG_7FJK0uujGyv5_kBAAMCAAN5AAM7BA"
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
           "AgACAgIAAxkBAAPwadbgTz6tGSVlvKNG2ovgtBbG18YAAn8Vaxty9DBJA1-Tv1n-S10BAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAPzadbgTwz7-DPJD7MdH-eMLlX0ylUAAoIVaxty9DBJcU5ogXjhaDIBAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAPvadbgT15m5O7tHcVucJGlkWZ7JUkAAn4Vaxty9DBJti8JRgRagP4BAAMCAAN3AAM7BA",
           "AgACAgIAAxkBAAPxadbgT_tOXYEkGUIUV5uVWGhFyYQAAoAVaxty9DBJwovwcuoxuKgBAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAPyadbgT-LIlycpsD5QM0wnscN92r4AAoEVaxty9DBJ6OHxNPeNb2wBAAMCAAN5AAM7BA"
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
           "AgACAgIAAxkBAAP8adbgkg-lMXWJYLDXdFwqzU6UdNoAAtASaxve6vBJaQFWoYb3TpUBAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAP_adbgkiBl4K6PKDxf78-s2kV5RywAAtMSaxve6vBJdQLSS9fNwscBAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAP7adbgkteS7GSzYwvh7R_pjGmtDk0AAs4Saxve6vBJstlWgZWeBjQBAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAP5adbgkj_9rcSK9GcejcyMoGnJCV8AAswSaxve6vBJytH_ExiZIQUBAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAP6adbgkme-MWzKKbOzGtUfynENJjAAAs0Saxve6vBJbW4dcRDUjcQBAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAP9adbgkj--RUlYBEhJr-hJu4WB9kgAAtESaxve6vBJFDUxDqoRFvEBAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAP-adbgkheT5TUlohfrrQaw3TP69u8AAtISaxve6vBJtwTZMda_pEgBAAMCAAN5AAM7BA"
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
           "AgACAgIAAxkBAAIBCGnW4N-uSOYTSuGmV2v49MUy9xO2AALDEmsb3urwSZHXRAPxnj-zAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBB2nW4N8Y3BZLhbmXScbpQwABNij_jgACwhJrG97q8Ennq883rWnkAAEBAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAIBCmnW4N8zQfOSOuNQR97BBdgRfe5iAALFEmsb3urwSZOC94XyT-uMAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBDGnW4N9G2tNgvS0L939bea_BxLeRAALHEmsb3urwSee5-HMibhO-AQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBCWnW4N_n-da7tBUqinza8UI4296bAALEEmsb3urwSUjBeUC_6h1yAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBC2nW4N9vVBljNExcgCWZBpMAARkr3AACxhJrG97q8ElsYc86XY7N-AEAAwIAA3kAAzsE",
           "AgACAgIAAxkBAAIBDmnW4N8dMeTUNz-SJWkha-uwqRvGAALJEmsb3urwScG1BFC9PB9QAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBDWnW4N8_J3BWwplqhexkZFTjtlaaAALIEmsb3urwSaBws-6yhTYwAQADAgADeQADOwQ"
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
           "AgACAgIAAxkBAAIBM2nW4j98fyjK4kFEEWpO_BiZ65KpAAIzFmsbU5PgSXCB-TX4isNhAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBNGnW4j8wks6jexRvp1xnxkPtQnRkAAI0FmsbU5PgSZA9hyHDcsYbAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBNWnW4j-P6j6bubdEaR_6GnhLS00AAzUWaxtTk-BJcmeySSwQp-wBAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAIBOmnW4j9Ndgq5PzUQ71nSAwAB5oI-qgACOhZrG1OT4EkrPgosSk3aBAEAAwIAA3kAAzsE",
           "AgACAgIAAxkBAAIBNmnW4j_bnHbBimfQ4dsOvDaqTQX4AAI2FmsbU5PgSVhSiYR1cDDvAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBOGnW4j_SsiOMvjNTUYPeY72Jgb9MAAI4FmsbU5PgSWhxjrmmFfnWAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBN2nW4j9ZvM_rP1GD_dwQxoNHPC57AAI3FmsbU5PgScwxyCAVmxeuAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBPGnW4j8NAAEz6t6Odu361tTGNdnvTwACPRZrG1OT4Elq72bTApe2OAEAAwIAA3kAAzsE",
           "AgACAgIAAxkBAAIBO2nW4j-mix_nTByjV9NB9bDnsUGEAAI7FmsbU5PgSTkB4Dq_ULeKAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBOWnW4j8GrA6K7QSKywrxadT_v53TAAI5FmsbU5PgSTCDKi4MjtVhAQADAgADeQADOwQ"
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
           "AgACAgIAAxkBAAIBR2nW4tCq4Li4evBK2zWZDpJ_sd23AAJgFmsbm-ThScxJKEhPbFdvAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBTWnW4tAAATXcs3vxYG61aZK1UBoAAQcAAmYWaxub5OFJGdKmWJtsJSMBAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAIBSWnW4tCLFSZH6HSu_kuevMIdMr8tAAJiFmsbm-ThSS0ZmFxWUktTAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBSGnW4tCeJjwlKynVpshLKE83dckvAAJhFmsbm-ThSTJbmEbxn4KrAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBS2nW4tBmLOs0wDgqVWF_XWP_FsdnAAJkFmsbm-ThScGcnkUsjfQuAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBTmnW4tDZDNEp8Qg0nHR1R98YLZiwAAJnFmsbm-ThScV2byj3nMdXAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBSmnW4tAS_OS21ssCH0BoEF6p6xpPAAJjFmsbm-ThSf_SAAEUgCrtjQEAAwIAA3kAAzsE",
           "AgACAgIAAxkBAAIBTGnW4tDddhaIosv0m1zOWokhmEyvAAJlFmsbm-ThSdYy0vLAyT8RAQADAgADeQADOwQ"
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
           "AgACAgIAAxkBAAIBimnXdC44I6knV-BNEujP0l6lMb8hAAIiEmsb81vISdWy73AenWVFAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBjGnXdC4SiuGOAjThWo3AQwtfMoaOAAIkEmsb81vISWh6Jagjo1PbAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBiWnXdC6voJ7IsbLTh-8N9ms81XNsAAIhEmsb81vISd-bSz6Y_OiHAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBj2nXdC59iSJTm9ZgUlsWv7NsdzTGAAInEmsb81vISW1e9LGMTzcyAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBkWnXdC7Hk2VzMAyJfH_svo1Vi2CRAAIpEmsb81vISZrWBD8n4bMlAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBi2nXdC6gnGBQiuqCv14X8e5FK2r8AAIjEmsb81vISTCHx8bBhgJhAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBjWnXdC7WUMslNe4U0eE-UjWb1RMcAAIlEmsb81vISc3TKhL7uduiAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBjmnXdC6de2LybAOPaW0k_YB1nMyuAAImEmsb81vISbt-DWzak3mqAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBkGnXdC7b7wcRcxH4Mfb5OUXUNxSdAAIoEmsb81vISVlkzsPk8clGAQADAgADeQADOwQ"
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
           "AgACAgIAAxkBAAIBm2nXdJmwmXAfOR46nraF84veF6dBAAIXEmsb81vISavCMZCgZPQTAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBnmnXdJmh06qzAAGkBBrnl-AURaATxAACGhJrG_NbyEl73D2TUWYucAEAAwIAA3kAAzsE",
           "AgACAgIAAxkBAAIBnGnXdJlNF9nY9-ql0bYxEFch3PE2AAIYEmsb81vISYmGZS8C2s2mAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBoGnXdJmfi1xKUKX9pMX1UlI5GgbwAAIeEmsb81vISfMBoRv4udcVAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBn2nXdJlhvP_PiBqwaglGNFCwfymSAAIbEmsb81vISTbn6i-a6LSAAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIBnWnXdJntDoeh99L7vzd0qkqjfkumAAIZEmsb81vISRZPcBz4mWN4AQADAgADeQADOwQ"
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
           "AgACAgIAAxkBAAIB22nXd4-Agn16vIS-CcFEWwJNUruHAALDFWsbomMxSn1NEJHwHrlFAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIB32nXd4_VMuCqUXl1KgTjAXBYVTUQAALHFWsbomMxSoCDcQ7xCF22AQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIB3mnXd4-G_jDXLLqKZs4P2vhAtj-cAALGFWsbomMxSq-5Jkp7TxdgAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIB2WnXd48AAYmUz5t8KtwDa-uCJpj96gACwRVrG6JjMUry1feixhgxgQEAAwIAA3kAAzsE",
           "AgACAgIAAxkBAAIB3GnXd49YmHMiLiQy31-iCWKnQxnZAALEFWsbomMxSqiRyiMI5riRAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIB2mnXd4-B_Ijtzvf7bi7_J-JzwPSNAALCFWsbomMxSkjFV3k5YDNOAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIB3WnXd4_HsiYHPVp3ibj1XP3yXJTPAALFFWsbomMxSpM693bKKXfnAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIB52nXd_KXxtYkeIKLQJpRDMiClk8wAALIFWsbomMxSnKgl_eyubMcAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIB6WnXd_KhylG4TeP_W7YN_RRh57nDAALKFWsbomMxSgbzvIc4EJlPAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIB6GnXd_JO_qEO7W7-WJkCNxv35kwAA8kVaxuiYzFKVQiEvlgOgtkBAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAIB62nXd_J7muXjq7wiv6qIa_ssib27AALMFWsbomMxSiXwWgEcKJy9AQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIB6mnXd_IdtGA4exECad5AqdTg8U-aAALLFWsbomMxSj4lUe0FBbfzAQADAgADeQADOwQ"
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
           "AgACAgIAAxkBAAIB_WnXeHZlL01gihCzlmL7zfah5SGoAAIpE2sb5HwoSpxKVTjN60DbAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICAAFp13h25YHzVghDbFaVPsdFZG0amAACJhNrG-R8KEoPR-ohayEu2QEAAwIAA3kAAzsE",
           "AgACAgIAAxkBAAIB_GnXeHbKvwkz8Wm7wgUxYbWA4EnrAAIoE2sb5HwoSpTaFmUt3MQUAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICAmnXeHaX3cNBdSWYZPWeE_DVR3CpAAItE2sb5HwoStQV7kQgnvw5AQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICA2nXeHavNVdR-mxgVf1iN7JykQ8CAAIuE2sb5HwoSjBeyW6mcpjyAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIB_mnXeHY4OegcIpp2V82o5QJYL3jSAAIqE2sb5HwoSkCh49LTm02aAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIB-2nXeHYaY3vLTPH3h6mkvMBDm1xcAAInE2sb5HwoSlSXNc5p_8gIAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICAWnXeHZFZAYnCzTu8qJP4YGd1LedAAIsE2sb5HwoStcc7GD3_0vEAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIB_2nXeHatv5-ok0rqLEaHFrllSPPYAAIrE2sb5HwoSiv8Oda9JtkVAQADAgADeQADOwQ"
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
           "AgACAgIAAxkBAAICV2nXerAq3K9ur_Xl6xjclV8nundBAALqFWsbUZX4SR-6aJn7dlZYAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICXGnXerDgMD_DGwg4qwc6m6r5AzXfAALtFWsbUZX4Se9ZuKf0NW7kAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICXmnXerDyWt68nr_bKw3-S7oJh5Y6AALwFWsbUZX4SU5_MQeTrug4AQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICWWnXerDngO86_vtI-JHAhmb_ZdjPAAL1FWsbUZX4Sc7U6F8Y_VMVAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICWmnXerBp8XVTE-ItvAt263bqTUCVAALxFWsbUZX4SUgeuNQ-DsXAAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICWGnXerBna0cmeVoVQMehI5Lk-dpTAAL3FWsbUZX4SYUp1cdtViOCAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICW2nXerBnOJG7pbZfIecpcHRVCd9TAAL4FWsbUZX4SfO_Wjn6bGbTAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICX2nXerBnexA2yx5i7LH5wRvBeonnAALyFWsbUZX4SeLkDiYa4k43AQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICXWnXerAd64Cjz1iZVtGY3uuH1XZ0AALzFWsbUZX4SUBCFWy812gXAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICYGnXerAV2JQJE5vecfm-GklI5lqrAALvFWsbUZX4SRsixFYtKyldAQADAgADeQADOwQ"
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
           "AgACAgIAAxkBAAICfWnXe6F-4swHdPOy65T3G4bGewgDAAKEFmsb_TqwSTkkYzw5a-oCAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICf2nXe6FipybvnU-S4o2jPmcXnkmbAAKHFmsb_TqwSQkK0pTdiPozAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICgWnXe6FzFycAAdW53_K_l1ethOJwcAACiRZrG_06sEnKRIhQDe8ifwEAAwIAA3kAAzsE",
           "AgACAgIAAxkBAAICfmnXe6HA_lT_JRjMx7hSTddv0yPzAAKGFmsb_TqwSagZ8c2DsXEyAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICg2nXe6EqUx2Y7OdJjV1rPAX33vUaAAKLFmsb_TqwSRnuzyCBsDfiAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICgmnXe6HiOre8rWU07TNF0EYcgWY7AAKKFmsb_TqwSW1FQePXQLF5AQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICgGnXe6FyJu-IHC_dB8YhG2dEkfjeAAKIFmsb_TqwSaZ-t7g8hMwRAQADAgADeQADOwQ"
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
           "AgACAgIAAxkBAAICi2nXfAycVNY71GFO6_8C_PI9Mr_1AAIwFWsb1G-pSaj9pi5-97_bAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICjmnXfAz_xfaboaJ88D248ylx6rYqAAIzFWsb1G-pSW7jmi525mA9AQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICjGnXfAz8bQeiRhxRBjl8l4v-h7IgAAIxFWsb1G-pSYuyyvdCcDppAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICkGnXfAyfR4ArLcPTP9fRVIeNHcndAAI1FWsb1G-pSdTF4qUSBk_BAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICkWnXfAzIr0BPveBXviwjdUEUOzq9AAI2FWsb1G-pSVwcZRjEVWqKAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICjWnXfAy90iETVduP6dI51XaRuF32AAIyFWsb1G-pSbseD66foSexAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAICj2nXfAxfRY5uJXLh5T7RzkScvd6PAAI0FWsb1G-pSQOWMizlvVqoAQADAgADeQADOwQ"
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
           "AgACAgIAAxkBAAIC1WnXfbP4B_aZRv3sdeUlh4Ed1My-AALqGWsbLkyASaWJL9E3V0rkAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIC2GnXfbPMK_pjJaodsvcMnbhj_XpkAALuGWsbLkyASXk6zzV-C1axAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIC22nXfbMEm-Vic8jAZ6GocfEeDgABrQAC8RlrGy5MgEknCBuw4s1LwwEAAwIAA3kAAzsE",
           "AgACAgIAAxkBAAIC3GnXfbMF29ecsN3De0uaTG6ak_7mAALyGWsbLkyAScjF4lwTZ8goAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIC3mnXfbMHxUXFTmqSsBeCifn87wd5AAL1GWsbLkyASW3StCfbxxwzAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIC1mnXfbPEPHCV1IQen6lGdiv0Q4-6AALrGWsbLkyASWfu9QHCJHJyAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIC12nXfbPz83Nar1nIfDnxWhI8-pskAALtGWsbLkyASXZ1Kpr1VxN2AQADAgADeQADOwQ",
           AgACAgIAAxkBAAIC2mnXfbPGgPfNNQrPotXAhJsd8EptAALwGWsbLkyASXs_FGXPkdhBAQADAgADeQADOwQ"",
           "AgACAgIAAxkBAAIC2WnXfbM8S_-9dTS55rDCqGwdXTXJAALvGWsbLkyASR8s-cFrlIvwAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIC3WnXfbP5-CxSw7yLcXllFpZnaiSMAALzGWsbLkyASZr7q_ha2h29AQADAgADeQADOwQ"
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
           "AgACAgIAAxkBAAIC7WnXfh2yD9b0sy_h3XKVMWxk-ZYpAALQGWsbgoWASeGCmDnZRIUnAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIC72nXfh3xIrWc20GY8cp28Mc5DNaWAALSGWsbgoWASXGc_sq4BqvGAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIC7GnXfh1PfEn-1x9zVbDgfuvz1YDqAALPGWsbgoWASS_DmM9nbLaTAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIC6WnXfh1P6HPoDtPWhhmW4CjCdcqEAALMGWsbgoWASY0Ltpgd7GgGAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIC7mnXfh07eaSeqlcKwQzc8_WKcdtmAALRGWsbgoWASTJWQPx2P7M7AQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIC6mnXfh1s4vHmJ4q4ZJtEH0-7I_e1AALNGWsbgoWASbYXoUMTw6O7AQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIC8GnXfh0KM7GxDQUNZHfWF1KvatrqAALTGWsbgoWASZHIjS_oC6qLAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIC62nXfh0fa8WMrzoV0rdCYuZ1jPiGAALOGWsbgoWASXW8Pagr1Pz5AQADAgADeQADOwQ"
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
           "AgACAgIAAxkBAAIDBWnXfpwYu-j8mQfSZsvPH4JCMV2xAAK2HGsb0dlxSZuUa1iXg4dMAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDAmnXfpwlO9JbG98Iqo7pLzfGE0V8AAKyHGsb0dlxSaHioLfBAAF5ewEAAwIAA3kAAzsE",
           "AgACAgIAAxkBAAIDB2nXfpwqojSYYZmVFd4ZWukP6sObAAK4HGsb0dlxSf6cT4ltKLkAAQEAAwIAA3kAAzsE",
           "AgACAgIAAxkBAAIDAWnXfpzdos3gnutrwC0NBbnu-3gOAAKxHGsb0dlxSbop6nUNIjv7AQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDBGnXfpyDo182ne3hjK4eO-cCNRgDAAK0HGsb0dlxSeBE1cLhP6rPAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDBmnXfpwNQviPqcmLhAiJ4499p5SMAAK3HGsb0dlxSbclA5tH1bdcAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDA2nXfpz_swwRb6g1Fo5aw3ZXUlzuAAKzHGsb0dlxSeWQIvZs3JP3AQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDCGnXfpxkCLAGs--L5T4PS7xxZbZzAAK5HGsb0dlxSQABe75SuQNqLwEAAwIAA3kAAzsE"
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
           "AgACAgIAAxkBAAIDO2nXf-MOy-8oLRGOnb84bQABVIGdmgACohdrG93hYUow3iwkU6uURAEAAwIAA3kAAzsE",
           "AgACAgIAAxkBAAIDQGnXf-NFsFpOC6f2geo-zTVGNg44AAKnF2sb3eFhSjWm8sDF24aRAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDPGnXf-MRCtJhdJS7LozVGdNo1XksAAKjF2sb3eFhSkHtyzErOHSdAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDPWnXf-Nyk2GOPcYKLHmOiE_MVpAjAAKkF2sb3eFhSkLin_IK1C-JAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDPmnXf-O8gGA9llHNOeS_8MUxMUmsAAKlF2sb3eFhSqW-Fr40m03xAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDQWnXf-MECNGNanY_F7c2lwtt6PywAAKoF2sb3eFhSijHHD-yLbdkAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDQmnXf-PiX1g-xOmNYvU6_EBGOe1xAAKpF2sb3eFhSsOBQwYX2vONAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDP2nXf-OyutWW_c1-PmHbwXxCuLQMAAKmF2sb3eFhSpgmMJcv1j_xAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDTWnXgEwkHRSfg3tcG9C7tAQxxWpWAALTE2sbsmyISleMoz_wBIuyAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDTGnXgEyeSIX8F31asfC-z2zyYBRCAALSE2sbsmyISt4OeZBQ-Nn-AQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDS2nXgExl2G0jC68BR97EYRmsE4coAALRE2sbsmyISuW1D4v47LSRAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDTmnXgEzRx0CWM-4lftOdZSlNEKnpAALUE2sbsmyISgMCeXziycJIAQADAgADeQADOwQ"
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
           "AgACAgIAAxkBAAIDZGnXgPZYvtC5qzZ3hshy-l6n8WKSAAJgF2sb3eFhStqxFkVHkSbqAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDZmnXgPZ57ug8yvJYHDGhdiG63cwmAAJiF2sb3eFhSjfFRI7AXlWXAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDY2nXgPbqlpwt2rFz8is6hK_cYIAZAAJfF2sb3eFhSlhGbqg-K_2hAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDZWnXgPYUW6BEoW5nDR9rdJ9bMZu8AAJhF2sb3eFhSvmEydLmU9MjAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDZ2nXgPb8f18gCuAzbJVZ9HevueTIAAJjF2sb3eFhSoZOTly5gSHLAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDaGnXgPZjtRwjgr8MMdYlWvqFVtytAAJkF2sb3eFhSlhUdkB2bMoAAQEAAwIAA3kAAzsE",
           "AgACAgIAAxkBAAIDaWnXgPZ4yDYu_Gd8MlsZWsHOeIRUAAJlF2sb3eFhSlaNdPbVXa-bAQADAgADeQADOwQ"
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
           "AgACAgIAAxkBAAIDcmnXgT8N9o2gRqkFoLkw2-gZ8RUNAAJoGGsb5YBISezqShc4F1E_AQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDc2nXgT9_FvkGZ87apudYLQABe11nEAACaRhrG-WASEnY5yLi8-PW3QEAAwIAA3kAAzsE",
           "AgACAgIAAxkBAAIDeGnXgT-B5OECNis9dKjOvw8lQqU-AAJtE2sb_CBYSQfddcAGCGSlAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDcWnXgT9xVwLkNiZOAyDRfKX4Vs_rAAJnGGsb5YBISbYjujcT0AKOAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDdmnXgT_93LrU9XbZihIZ6fgM1tOrAAJrE2sb_CBYSdKdCukGvIfqAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDdGnXgT9RabLL9LE0Fvrc35hR1-s-AAJpE2sb_CBYScNTjMFf78WTAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDd2nXgT-_lFNz6g1Wwsvt77mxuz0AA2wTaxv8IFhJvODNe6OAp4oBAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAIDdWnXgT_VLuTpf8sG2tLOD_lQfp92AAJqE2sb_CBYSfQ3xMYk4ZWyAQADAgADeQADOwQ"
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
           "AgACAgIAAxkBAAIDgWnXgYTFYQERIFAI61suuLt3kxPLAAKDJGsbagxISQSVdmO-IeLSAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDgmnXgYQF5uXuHOn1h-H1KqopVJiuAAKEJGsbagxISRKuXbOYhv2HAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDg2nXgYS-rpOJjn9MyQABU9v_gJb-FwAChiRrG2oMSEnYoO9Rs8U51wEAAwIAA3kAAzsE",
           "AgACAgIAAxkBAAIDhWnXgYQvem8W4np6x1cf6VXkDbB4AAKIJGsbagxISeRmrjJDbunQAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDhGnXgYTW3AMw_sm1-ah5afKii-y9AAKHJGsbagxIScVbwcXOEMIDAQADAgADeQADOwQ"
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
           "AgACAgIAAxkBAAIDi2nXgb6SCUSCC3dY_SIU3MxKcEwmAAKXI2sbagxISdq3oD4V1B_eAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDjGnXgb7VWqmaIDUdH-RurZUsR_ChAAKSI2sbagxISaq6FcldmXSeAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDjWnXgb6jDN6FCVjv2iiNrgr1hPRAAAKaI2sbagxISU4-QDiOXEewAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDk2nXgb6Vbh_03_hYQvYXLJKVmMjFAAKWI2sbagxISbXiWTpKoQS5AQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDkmnXgb6FN1ciOuub25kAAfZLH5rNIgAClCNrG2oMSEl7xlCtNxiVkAEAAwIAA3kAAzsE",
           "AgACAgIAAxkBAAIDkGnXgb6lKLACen4aZybrYeISlVP_AAKTI2sbagxISen1gNbSEwTmAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDkWnXgb7_LYKKAjoMav6lEAT-ecaaAAKcI2sbagxISROUeLP5qjEWAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDlGnXgb6Z14JvIqUzT7ut6P6b1MivAAKeI2sbagxISTGiR6OzfHfgAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDj2nXgb4omauqJNaIouUCpuWSAaNzAAKpI2sbagxISRzgMG1hc4_aAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAIDjmnXgb4aef9bjmrG01qTbYGbDRA1AAKnI2sbagxISdPhKVP_cVQ_AQADAgADeQADOwQ"
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
           "AgACAgIAAxkBAAO-adbcyDkE77Ag6XbAYcjfD7vFhV4AAsoUaxu2WRhJhewRsQmRC54BAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAPBadbcyKwAAR9hE_WcDtFFDvj8EbZVAALNFGsbtlkYSWYZF_BKHunZAQADAgADeQADOwQ",
           "AgACAgIAAxkBAAO_adbcyF_2Pru27LFspvitk06eVvQAAssUaxu2WRhJY_wWqtPsW1cBAAMCAAN5AAM7BA",
           "AgACAgIAAxkBAAPAadbcyCLrVxtYeuTesB_3chVYZcwAAswUaxu2WRhJkMdZgYCDLioBAAMCAAN5AAM7BA"
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
