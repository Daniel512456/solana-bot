from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, CallbackQueryHandler, ContextTypes, filters

TOKEN = "8331539761:AAFWoSAkSZTWpCayukRV7BtUYWSBzgyXu7I"

WALLET = "AEk8J6coHJ6XDk3U1ib6jGYGPMY2L2qMKB3NmDbZJ8Dy"


# When someone sends a message
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    text = update.message.text.lower()

    if "anyone want some solana" in text:
        keyboard = [
            [InlineKeyboardButton("give lil bro solana", callback_data="give")],
            [InlineKeyboardButton("reject the offer", callback_data="reject")]
        ]

        await update.message.reply_text(
            "I want some solana🥰",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


# When a button is clicked
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "give":
        await query.message.edit_text(
            f"donate here:\n{WALLET}"
        )

    elif query.data == "reject":
        await query.message.edit_text("brokie")


# Start bot
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.add_handler(CallbackQueryHandler(button_click))

app.run_polling()