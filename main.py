from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8875449331:AAHGOb1PP_uDHqmnICiT_X0fmEWYfUK9Tdg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(
            "💳 Карту можна зробити тут",
            url="https://www.privat24.ua/invite/kcxlx"
        )]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Вітаю!\n\n"
        "💳 Карту можна зробити тут:",
        reply_markup=reply_markup
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Бот запущений...")
    app.run_polling()


if __name__ == "__main__":
    main()
