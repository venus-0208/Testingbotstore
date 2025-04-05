import os
import logging
import telegram
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters, CallbackContext

# Konfigurasi logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = os.getenv("7749916906:AAGoHK8GbCzTBdtHewPi8IuWuuPOC8TNzpQ")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")  # ID admin untuk menerima notifikasi

bot = telegram.Bot(7749916906:AAGoHK8GbCzTBdtHewPi8IuWuuPOC8TNzpQ)

# Produk yang dijual
PRODUCTS = {
    "1": {"name": "Produk A", "price": 50000},
    "2": {"name": "Produk B", "price": 75000},
    "3": {"name": "Produk C", "price": 100000}
}

def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    keyboard = [[InlineKeyboardButton(f"{p['name']} - Rp{p['price']}", callback_data=f"buy_{k}")] for k, p in PRODUCTS.items()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text(f"✨ Selamat datang di *Venus Store*! ✨\n\nSilakan pilih produk yang ingin kamu beli:", reply_markup=reply_markup, parse_mode="Markdown")

def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data.startswith("buy_"):
        product_id = query.data.split("_")[1]
        product = PRODUCTS.get(product_id)
        
        if product:
            qris_image_path = "qris.png"  # Pastikan file QRIS ada di server
            message = f"🛍 Kamu memilih *{product['name']}* seharga *Rp{product['price']}*.\n\n📸 Silakan scan QRIS di bawah untuk pembayaran."
            
            bot.send_photo(chat_id=query.message.chat_id, photo=open(qris_image_path, "rb"), caption=message, parse_mode="Markdown")
            bot.send_message(chat_id=ADMIN_CHAT_ID, text=f"📢 Pesanan baru dari @{query.message.chat.username}: {product['name']} - Rp{product['price']}")

def confirm_payment(update: Update, context: CallbackContext):
    if str(update.message.chat_id) != ADMIN_CHAT_ID:
        update.message.reply_text("❌ Hanya admin yang bisa mengonfirmasi pembayaran.")
        return
    
    update.message.reply_text("✅ Pembayaran telah dikonfirmasi! Pesanan sedang diproses.")
    bot.send_message(chat_id=context.args[0], text="🎉 Pembayaran berhasil! Pesanan kamu akan segera diproses.")

def main():
    updater = Updater(7749916906:AAGoHK8GbCzTBdtHewPi8IuWuuPOC8TNzpQ, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("konfirmasi", confirm_payment, pass_args=True))
    dp.add_handler(CallbackQueryHandler(button_handler))

    updater.start_polling()
    updater.idle()

if name == "main":
    main()
