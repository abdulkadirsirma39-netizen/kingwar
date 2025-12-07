async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in user_data:
        user_data[user_id] = {"balance": 100, "army": 10}
    
    keyboard = [[InlineKeyboardButton("🎮 SAVAŞ MEYDANINA GİR!", url="https://borsavadisi.com/oyun/index.html")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # İstediğin yeni savaşçı metin burası:
    await update.message.reply_text(
        f"⚔️ **KOMUTAN! SAVAŞA HAZIR MISIN?** ⚔️\n\n"
        f"Askerlerini topla, stratejini belirle ve haydi savaş meydanına!\n\n"
        f"🎖️ Mevcut Ordu Gücün: {user_data[user_id]['army']} Nefer\n"
        f"💰 Savaş Akçen: {user_data[user_id]['balance']} VadiCoin\n\n"
        "Aşağıdaki butona basarak cepheye gidebilirsin!",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )
