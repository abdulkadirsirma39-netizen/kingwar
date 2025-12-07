import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# --- RENDER İÇİN SAHTE WEB SUNUCUSU (PORT HATASINI GİDERMEK İÇİN) ---
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot calisiyor!")

def run_health_check():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), HealthCheckHandler)
    server.serve_forever()

# Web sunucusunu arka planda başlat
threading.Thread(target=run_health_check, daemon=True).start()
# -----------------------------------------------------------------

TOKEN = os.getenv("TELEGRAM_TOKEN")
user_data = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in user_data:
        user_data[user_id] = {"balance": 100}
    
    keyboard = [[InlineKeyboardButton("🪙 Coin Topla!", callback_data='mine')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        f"Cüzdanın: {user_data[user_id]['balance']} VadiCoin\nToplamak için tıkla!",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    if query.data == 'mine':
        user_data[user_id]["balance"] += 1
        keyboard = [[InlineKeyboardButton("🪙 Devam Et!", callback_data='mine')]]
        await query.edit_message_text(
            text=f"Kazandın! Bakiyen: {user_data[user_id]['balance']} VadiCoin",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Port açıldı ve Bot çalışıyor...")
    app.run_polling()
