import telepot
import time

# Replace YOUR_TOKEN with the API token provided by BotFather
bot = telepot.Bot('6250643198:AAE585Pnl_xKH7xkFpC-P9t14uQTAqYVLgg')

def send_message():
    # Replace YOUR_CHAT_ID with the ID of the chat you want to send the message to
    bot.sendMessage(chat_id='-1001978484301', text='sinal 01\n1 ')

while True:
    send_message()
    time.sleep(1)
