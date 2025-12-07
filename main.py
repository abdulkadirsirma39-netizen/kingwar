import os
import sys
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Token'ı Render üzerinden alıyoruz
TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    print("HATA: TELEGRAM_TOKEN bulunamadı! Lütfen Environment sekmesinden ekleyin.")
    sys.exit(1)

async def baslat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Borsa Vadisi Oyununa Hoş Geldin! 📈\n"
        "Çok yakında borsavadisi.com verileriyle coin toplayabileceksin."
    )

if __name__ == '__main__':
    try:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", baslat))
        print("Bot çalışıyor...")
        app.run_polling()
    except Exception as e:
        print(f"Bot başlatılırken hata oluştu: {e}")
