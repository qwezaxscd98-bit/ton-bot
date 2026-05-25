import requests
import time
from telegram import Bot

TOKEN = "8866838883:AAFuegk-OLifAa8ytAsdNOrGCt4kX87WfQY"
CHANNEL_ID = "@ton_price_news"

bot = Bot(token=TOKEN)

while True:
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=the-open-network&vs_currencies=usd"

        data = requests.get(url).json()

        ton_usd = data["the-open-network"]["usd"]

        usd_to_toman = 83000

        ton_toman = int(ton_usd * usd_to_toman)

        text = f"""
💎 قیمت TON

💵 دلار: {ton_usd} $
🇮🇷 تومان: {ton_toman:,} تومان
"""

        bot.send_message(
            chat_id=CHANNEL_ID,
            text=text
        )

    except Exception as e:
        print(e)

    time.sleep(60)
