import telebot
import time

# Твои данные
TOKEN = '8646449140:AAHjn1qE2RfeWQhF7nzUCJkCKhKrTzKCyxA'
ADMIN_ID = 2012037330

bot = telebot.TeleBot(TOKEN)

# ФУНКЦИЯ ОЧИСТКИ: удаляем вебхук Livegram и очищаем очередь сообщений
def clear_webhook():
    print("Удаляю вебхук Livegram...")
    bot.remove_webhook()
    time.sleep(1) # Даем Telegram секунду «продышаться»
    print("Вебхук удален. Запускаю бота...")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "ⲡⲣυⲃⲉⲧ, ⲥⲕυⲇыⲃⲁύ ⲧⲉύⲕυ ⲥюⲇⲁ.")

@bot.message_handler(content_types=['text', 'photo', 'video', 'sticker', 'document'])
def forward_to_admin(message):
    try:
        bot.send_message(ADMIN_ID, "🔔 ⲏⲟⲃыύ ⲧⲉύⲕ:")
        bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "ⲡⲣυⲏяⲧⲟ, ⲟⲿυⲇⲁύ ⲡⲩⳝⲗυⲕⲁⳡυυ.")
    except Exception as e:
        print(f"Ошибка при пересылке: {e}")

if __name__ == "__main__":
    clear_webhook()
    # Запуск с игнорированием старых ошибок
    bot.polling(none_stop=True, skip_pending=True)
