import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Token Render'dan çekiliyor
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Geçici veri saklama (Kullanıcı verileri)
user_data = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in user_data:
        user_data[user_id] = {"balance": 100} # Hoş geldin bonusu
    
    keyboard = [[InlineKeyboardButton("🪙 Coin Topla!", callback_query_data='mine')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"Hoş geldin! 📈\nCüzdanında şu an {user_data[user_id]['balance']} VadiCoin var.\n\n"
        "Aşağıdaki butona basarak coin toplayabilirsin!",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()

    if query.data == 'mine':
        user_data[user_id]["balance"] += 1
        
        keyboard = [[InlineKeyboardButton("🪙 Bir Daha Tıkla!", callback_query_data='mine')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            text=f"Harika! 🪙 Kazandın.\nGüncel Bakiyen: {user_data[user_id]['balance']} VadiCoin",
            reply_markup=reply_markup
        )

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Oyun motoru çalışıyor...")
    app.run_polling()
