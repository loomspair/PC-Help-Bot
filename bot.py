from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import BOT_TOKEN


# ==================================================
# НАСТРОЙКИ
# ==================================================

MASTER_ID = 8145950317
MASTER_USERNAME = "@Invincible_fanfan"


# ==================================================
# ТЕКСТЫ
# ==================================================

TEXTS = {

    # ==================================================
    # 🇷🇺 РУССКИЙ
    # ==================================================

    "ru": {
        "start":
            "👋 Привет!\n\n"
            "Добро пожаловать в PC Help!\n\n"
            "Мы поможем решить проблему с вашим компьютером.",

        "start_button": "🚀 Начать",

        "choose_language":
            "🌍 Выберите язык:",

        "ultraviewer_question":
            "🖥 Установлена ли у вас программа UltraViewer?",

        "yes": "✅ Да",
        "no": "❌ Нет",

        "download":
            "🌐 Скачать UltraViewer",

        "installed":
            "✅ Я установил",

        "ultraviewer_no":
            "❌ Похоже, UltraViewer ещё не установлен.\n\n"
            "Пожалуйста, скачайте и установите программу.\n"
            "После установки нажмите «Я установил».",

        "describe":
            "📝 Отлично!\n\n"
            "Теперь подробно опишите вашу проблему с компьютером.",

        "sent":
            "⏳ Спасибо!\n\n"
            "Ваш запрос отправлен мастеру.\n"
            "Пожалуйста, подождите, пока мастер рассмотрит проблему.",

        "accepted":
            "✅ Мастер принял ваш запрос!\n\n"
            "👨‍💻 Свяжитесь с мастером: "
            f"{MASTER_USERNAME}",

        "rejected":
            "❌ К сожалению, мастер не может исправить эту проблему.",

        "accept":
            "✅ Принять",

        "reject":
            "❌ Отказать",

        "order_accepted":
            "✅ ЗАКАЗ ПРИНЯТ",

        "order_rejected":
            "❌ ЗАКАЗ ОТКЛОНЁН",

        "new_order":
            "🆕 НОВЫЙ ЗАКАЗ",

        "user":
            "👤 Пользователь",

        "user_id":
            "🆔 ID",

        "language":
            "🌍 Язык",

        "problem":
            "📝 Проблема",
    },


    # ==================================================
    # 🇬🇧 ENGLISH
    # ==================================================

    "en": {
        "start":
            "👋 Hello!\n\n"
            "Welcome to PC Help!\n\n"
            "We will help you solve your computer problem.",

        "start_button":
            "🚀 Start",

        "choose_language":
            "🌍 Choose your language:",

        "ultraviewer_question":
            "🖥 Is UltraViewer installed on your computer?",

        "yes":
            "✅ Yes",

        "no":
            "❌ No",

        "download":
            "🌐 Download UltraViewer",

        "installed":
            "✅ I installed it",

        "ultraviewer_no":
            "❌ It looks like UltraViewer is not installed yet.\n\n"
            "Please download and install the program.\n"
            "After installation, press «I installed it».",

        "describe":
            "📝 Great!\n\n"
            "Now describe your computer problem in detail.",

        "sent":
            "⏳ Thank you!\n\n"
            "Your request has been sent to the technician.\n"
            "Please wait while the technician reviews your problem.",

        "accepted":
            "✅ The technician accepted your request!\n\n"
            "👨‍💻 Contact the technician: "
            f"{MASTER_USERNAME}",

        "rejected":
            "❌ Unfortunately, the technician cannot fix this problem.",

        "accept":
            "✅ Accept",

        "reject":
            "❌ Reject",

        "order_accepted":
            "✅ REQUEST ACCEPTED",

        "order_rejected":
            "❌ REQUEST REJECTED",

        "new_order":
            "🆕 NEW REQUEST",

        "user":
            "👤 User",

        "user_id":
            "🆔 ID",

        "language":
            "🌍 Language",

        "problem":
            "📝 Problem",
    },


    # ==================================================
    # 🇩🇪 DEUTSCH
    # ==================================================

    "de": {
        "start":
            "👋 Guten Tag!\n\n"
            "Willkommen bei PC Help!\n\n"
            "Wir helfen Ihnen, Ihr Computerproblem zu lösen.",

        "start_button":
            "🚀 Starten",

        "choose_language":
            "🌍 Wählen Sie Ihre Sprache:",

        "ultraviewer_question":
            "🖥 Ist UltraViewer auf Ihrem Computer installiert?",

        "yes":
            "✅ Ja",

        "no":
            "❌ Nein",

        "download":
            "🌐 UltraViewer herunterladen",

        "installed":
            "✅ Ich habe es installiert",

        "ultraviewer_no":
            "❌ UltraViewer scheint noch nicht installiert zu sein.\n\n"
            "Bitte laden Sie das Programm herunter und installieren Sie es.\n"
            "Drücken Sie danach «Ich habe es installiert».",

        "describe":
            "📝 Großartig!\n\n"
            "Beschreiben Sie jetzt Ihr Computerproblem ausführlich.",

        "sent":
            "⏳ Vielen Dank!\n\n"
            "Ihre Anfrage wurde an den Techniker gesendet.\n"
            "Bitte warten Sie, während der Techniker Ihr Problem überprüft.",

        "accepted":
            "✅ Der Techniker hat Ihre Anfrage angenommen!\n\n"
            "👨‍💻 Kontaktieren Sie den Techniker: "
            f"{MASTER_USERNAME}",

        "rejected":
            "❌ Leider kann der Techniker dieses Problem nicht beheben.",

        "accept":
            "✅ Annehmen",

        "reject":
            "❌ Ablehnen",

        "order_accepted":
            "✅ ANFRAGE ANGENOMMEN",

        "order_rejected":
            "❌ ANFRAGE ABGELEHNT",

        "new_order":
            "🆕 NEUE ANFRAGE",

        "user":
            "👤 Benutzer",

        "user_id":
            "🆔 ID",

        "language":
            "🌍 Sprache",

        "problem":
            "📝 Problem",
    },


    # ==================================================
    # 🇬🇪 ქართული
    # ==================================================

    "ka": {
        "start":
            "👋 გამარჯობა!\n\n"
            "კეთილი იყოს თქვენი მობრძანება PC Help-ში!\n\n"
            "ჩვენ დაგეხმარებით კომპიუტერთან დაკავშირებული "
            "პრობლემის მოგვარებაში.",

        "start_button":
            "🚀 დაწყება",

        "choose_language":
            "🌍 აირჩიეთ ენა:",

        "ultraviewer_question":
            "🖥 თქვენს კომპიუტერში UltraViewer დაყენებულია?",

        "yes":
            "✅ დიახ",

        "no":
            "❌ არა",

        "download":
            "🌐 UltraViewer-ის ჩამოტვირთვა",

        "installed":
            "✅ დავაყენე",

        "ultraviewer_no":
            "❌ როგორც ჩანს, UltraViewer ჯერ არ არის დაყენებული.\n\n"
            "გთხოვთ, ჩამოტვირთოთ და დააყენოთ პროგრამა.\n"
            "დაყენების შემდეგ დააჭირეთ «დავაყენე».",

        "describe":
            "📝 შესანიშნავია!\n\n"
            "ახლა დეტალურად აღწერეთ თქვენი კომპიუტერის პრობლემა.",

        "sent":
            "⏳ გმადლობთ!\n\n"
            "თქვენი მოთხოვნა გაიგზავნა სპეციალისტთან.\n"
            "გთხოვთ, დაელოდოთ სანამ სპეციალისტი თქვენს პრობლემას განიხილავს.",

        "accepted":
            "✅ სპეციალისტმა მიიღო თქვენი მოთხოვნა!\n\n"
            "👨‍💻 დაუკავშირდით სპეციალისტს: "
            f"{MASTER_USERNAME}",

        "rejected":
            "❌ სამწუხაროდ, სპეციალისტს ამ პრობლემის მოგვარება არ შეუძლია.",

        "accept":
            "✅ მიღება",

        "reject":
            "❌ უარყოფა",

        "order_accepted":
            "✅ შეკვეთა მიღებულია",

        "order_rejected":
            "❌ შეკვეთა უარყოფილია",

        "new_order":
            "🆕 ახალი მოთხოვნა",

        "user":
            "👤 მომხმარებელი",

        "user_id":
            "🆔 ID",

        "language":
            "🌍 ენა",

        "problem":
            "📝 პრობლემა",
    }
}


# ==================================================
# ПОЛУЧЕНИЕ ЯЗЫКА
# ==================================================

def get_language(context):

    language = context.user_data.get("language", "ru")

    if language not in TEXTS:
        language = "ru"

    return language


# ==================================================
# /START
# ==================================================

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    # Сбрасываем предыдущую сессию
    context.user_data.clear()

    keyboard = [
        [
            InlineKeyboardButton(
                "🚀 Начать / Start / Starten / დაწყება",
                callback_data="start_service"
            )
        ]
    ]

    await update.message.reply_text(
        "👋 Привет / Hello / Guten Tag / გამარჯობა!\n\n"
        "🖥 PC Help\n\n"
        "🇷🇺 Русский • "
        "🇬🇧 English • "
        "🇩🇪 Deutsch • "
        "🇬🇪 ქართული",

        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ==================================================
# /MYID
# ==================================================

async def myid(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        f"🆔 Ваш Telegram ID:\n\n"
        f"{update.effective_user.id}"
    )


# ==================================================
# ВЫБОР ЯЗЫКА
# ==================================================

async def choose_language(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query
    await query.answer()

    keyboard = [
        [
            InlineKeyboardButton(
                "🇷🇺 Русский",
                callback_data="lang_ru"
            ),

            InlineKeyboardButton(
                "🇬🇧 English",
                callback_data="lang_en"
            )
        ],

        [
            InlineKeyboardButton(
                "🇩🇪 Deutsch",
                callback_data="lang_de"
            ),

            InlineKeyboardButton(
                "🇬🇪 ქართული",
                callback_data="lang_ka"
            )
        ]
    ]

    await query.edit_message_text(
        "🌍 Выберите язык / "
        "Choose language / "
        "Sprache / "
        "აირჩიეთ ენა:",

        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ==================================================
# ЯЗЫК ВЫБРАН
# ==================================================

async def language_selected(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query
    await query.answer()

    language = query.data.replace(
        "lang_",
        ""
    )

    context.user_data["language"] = language

    keyboard = [
        [
            InlineKeyboardButton(
                TEXTS[language]["yes"],
                callback_data="uv_yes"
            ),

            InlineKeyboardButton(
                TEXTS[language]["no"],
                callback_data="uv_no"
            )
        ]
    ]

    await query.edit_message_text(
        TEXTS[language]["ultraviewer_question"],
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ==================================================
# ULTRAVIEWER YES
# ==================================================

async def ultraviwer_yes(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query
    await query.answer()

    language = get_language(context)

    context.user_data["ultraviewer"] = True
    context.user_data["waiting_problem"] = True

    await query.edit_message_text(
        TEXTS[language]["describe"]
    )


# ==================================================
# ULTRAVIEWER NO
# ==================================================

async def ultraviwer_no(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query
    await query.answer()

    language = get_language(context)

    keyboard = [
        [
            InlineKeyboardButton(
                TEXTS[language]["download"],
                url="https://www.ultraviewer.net/"
            )
        ],

        [
            InlineKeyboardButton(
                TEXTS[language]["installed"],
                callback_data="uv_ready"
            )
        ]
    ]

    await query.edit_message_text(
        TEXTS[language]["ultraviewer_no"],
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ==================================================
# ULTRAVIEWER READY
# ==================================================

async def ultraviwer_ready(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query
    await query.answer()

    language = get_language(context)

    context.user_data["ultraviewer"] = True
    context.user_data["waiting_problem"] = True

    await query.edit_message_text(
        TEXTS[language]["describe"]
    )


# ==================================================
# ПОЛУЧЕНИЕ ПРОБЛЕМЫ
# ==================================================

async def receive_problem(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    if not context.user_data.get(
        "waiting_problem"
    ):
        return

    language = get_language(context)

    problem = update.message.text

    user_id = update.effective_user.id

    first_name = (
        update.effective_user.first_name
        or "Unknown"
    )

    context.user_data["problem"] = problem
    context.user_data["waiting_problem"] = False

    # ==================================================
    # СОХРАНЯЕМ ЗАКАЗ
    # ==================================================

    if "orders" not in context.application.bot_data:

        context.application.bot_data[
            "orders"
        ] = {}

    context.application.bot_data[
        "orders"
    ][user_id] = {

        "language": language,

        "problem": problem,

        "name": first_name
    }

    # ==================================================
    # ПОЛЬЗОВАТЕЛЮ
    # ==================================================

    await update.message.reply_text(
        TEXTS[language]["sent"]
    )

    # ==================================================
    # КНОПКИ МАСТЕРА
    # ==================================================

    keyboard = [
        [

            InlineKeyboardButton(
                TEXTS[language]["accept"],
                callback_data=f"accept_{user_id}"
            ),

            InlineKeyboardButton(
                TEXTS[language]["reject"],
                callback_data=f"reject_{user_id}"
            )

        ]
    ]

    # ==================================================
    # НАЗВАНИЕ ЯЗЫКА
    # ==================================================

    language_name = {

        "ru": "🇷🇺 Русский",

        "en": "🇬🇧 English",

        "de": "🇩🇪 Deutsch",

        "ka": "🇬🇪 ქართული"
    }

    # ==================================================
    # ОТПРАВКА МАСТЕРУ
    # ==================================================

    try:

        await context.bot.send_message(

            chat_id=MASTER_ID,

            text=(

                "🆕 НОВЫЙ ЗАКАЗ\n\n"

                f"👤 Пользователь: "
                f"{first_name}\n"

                f"🆔 ID: "
                f"{user_id}\n"

                f"🌍 Язык: "
                f"{language_name[language]}\n\n"

                f"📝 Проблема:\n"
                f"{problem}"
            ),

            reply_markup=InlineKeyboardMarkup(
                keyboard
            )
        )

        print(
            f"✅ Заказ пользователя "
            f"{user_id} отправлен мастеру."
        )

    except Exception as error:

        print(
            "❌ ОШИБКА ОТПРАВКИ МАСТЕРУ:"
        )

        print(error)


# ==================================================
# РЕШЕНИЕ МАСТЕРА
# ==================================================

async def master_decision(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    # ==================================================
    # ПРОВЕРКА МАСТЕРА
    # ==================================================

    if update.effective_user.id != MASTER_ID:

        await query.answer(
            "❌ У вас нет доступа.",
            show_alert=True
        )

        return

    await query.answer()

    data = query.data

    user_id = int(
        data.split("_")[1]
    )

    # ==================================================
    # ПОЛУЧАЕМ ЗАКАЗ
    # ==================================================

    orders = context.application.bot_data.get(
        "orders",
        {}
    )

    order = orders.get(
        user_id
    )

    if order:

        language = order["language"]

    else:

        language = "ru"

    # ==================================================
    # ПРИНЯТЬ
    # ==================================================

    if data.startswith(
        "accept_"
    ):

        await context.bot.send_message(

            chat_id=user_id,

            text=TEXTS[
                language
            ][
                "accepted"
            ]
        )

        await query.edit_message_text(

            query.message.text
            + "\n\n"
            + TEXTS[
                language
            ][
                "order_accepted"
            ]
        )

    # ==================================================
    # ОТКАЗАТЬ
    # ==================================================

    elif data.startswith(
        "reject_"
    ):

        await context.bot.send_message(

            chat_id=user_id,

            text=TEXTS[
                language
            ][
                "rejected"
            ]
        )

        await query.edit_message_text(

            query.message.text
            + "\n\n"
            + TEXTS[
                language
            ][
                "order_rejected"
            ]
        )


# ==================================================
# ЗАПУСК
# ==================================================

def main():

    app = (
        Application
        .builder()
        .token(BOT_TOKEN)
        .build()
    )

    # ==================================================
    # /START
    # ==================================================

    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    # ==================================================
    # /MYID
    # ==================================================

    app.add_handler(
        CommandHandler(
            "myid",
            myid
        )
    )

    # ==================================================
    # КНОПКА НАЧАТЬ
    # ==================================================

    app.add_handler(
        CallbackQueryHandler(
            choose_language,
            pattern="^start_service$"
        )
    )

    # ==================================================
    # ВЫБОР ЯЗЫКА
    # ==================================================

    app.add_handler(
        CallbackQueryHandler(
            language_selected,
            pattern="^lang_"
        )
    )

    # ==================================================
    # ULTRAVIEWER YES
    # ==================================================

    app.add_handler(
        CallbackQueryHandler(
            ultraviwer_yes,
            pattern="^uv_yes$"
        )
    )

    # ==================================================
    # ULTRAVIEWER NO
    # ==================================================

    app.add_handler(
        CallbackQueryHandler(
            ultraviwer_no,
            pattern="^uv_no$"
        )
    )

    # ==================================================
    # ULTRAVIEWER READY
    # ==================================================

    app.add_handler(
        CallbackQueryHandler(
            ultraviwer_ready,
            pattern="^uv_ready$"
        )
    )

    # ==================================================
    # ПРИНЯТЬ / ОТКАЗАТЬ
    # ==================================================

    app.add_handler(
        CallbackQueryHandler(
            master_decision,
            pattern="^(accept|reject)_"
        )
    )

    # ==================================================
    # СООБЩЕНИЕ С ПРОБЛЕМОЙ
    # ==================================================

    app.add_handler(
        MessageHandler(
            filters.TEXT
            & ~filters.COMMAND,
            receive_problem
        )
    )

    # ==================================================
    # ЗАПУСК
    # ==================================================

    print(
        "================================"
    )

    print(
        "PC Help Bot запущен!"
    )

    print(
        "MASTER ID:",
        MASTER_ID
    )

    print(
        "MASTER USERNAME:",
        MASTER_USERNAME
    )

    print(
        "LANGUAGES: RU / EN / DE / KA"
    )

    print(
        "================================"
    )

    app.run_polling()


# ==================================================
# START PROGRAM
# ==================================================

if __name__ == "__main__":

    main()