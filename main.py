import telebot
import os
from flask import Flask
from threading import Thread

# نظام البقاء حياً للسحابة
app = Flask('')
@app.route('/')
def home(): return "Bot is Online! ✅"
def run(): app.run(host='0.0.0.0', port=8080)
def keep_alive(): Thread(target=run).start()

# التوكن الخاص بك
TOKEN = '7760390452:AAFfS1azdUBlT49TDq_MvOpD5dRtTvGEmqg'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🚀 البوت يعمل الآن من السحابة بنجاح!")

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
