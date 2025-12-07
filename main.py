# main.py dosyasındaki start fonksiyonunu bu şekilde güncelleyebilirsin
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    army_count = user_data[user_id]['army']
    
    # Görsel bir ordu gücü çubuğu oluşturalım
    bar_length = 10
    filled = min(army_count // 10, bar_length)
    army_bar = "█" * filled + "░" * (bar_length - filled)

    dashboard = (
        f"🏰 **VADİ KARARGAHI** 🏰\n"
        f"----------------------------\n"
        f"💰 **Bakiye:** {user_data[user_id]['balance']} 🪙\n"
        f"🎖️ **Ordu Gücü:** {army_count} Nefer\n"
        f"📊 **Kapasite:** [{army_bar}]\n"
        f"----------------------------\n"
        f"📡 *VaultVadi Durumu:* Güvenli ✅\n"
    )

    keyboard = [
        [InlineKeyboardButton("🪙 Coin Topla", callback_data='mine')],
        [InlineKeyboardButton("🛡️ Orduyu Eğit", callback_data='buy_army')],
        [InlineKeyboardButton("⚔️ Savaş Meydanı", callback_data='battle')]
    ]
    
    await update.message.reply_text(dashboard, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")
