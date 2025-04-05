import os
from telegram.ext import Updater, CommandHandler

TOKEN = os.environ.get("7749916906:AAGoHK8GbCzTBdtHewPi8IuWuuPOC8TNzpQ")

produk_list = [
    "° Blockmesh - 1.000/pcs",
    "° Xenea wallet - 1.200/pcs",
    "° Arichain wallet - 1.300/pcs",
    "° Nodepay - 700p/pcs (tidak running)",
    "° Klokapp - 1.000/pcs",
    "° Walme.io - 800p/pcs"
]

def start(update, context):
    pesan = "Selamat datang di Venus Store!\n\nProduk:\n"
    for item in produk_list:
        pesan += f"{item}\n"
    update.message.reply_text(pesan + "\n\nHubungi admin @vee_0208")

updater = Updater(7749916906:AAGoHK8GbCzTBdtHewPi8IuWuuPOC8TNzpQ, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
updater.start_polling()
updater.idle()
