# import os
# import telebot
# from gtts import gTTS
# from dotenv import load_dotenv
# # Замените 'YOUR_TELEGRAM_BOT_TOKEN' на токен вашего бота
# load_dotenv()
# TELEGRAM_BOT_TOKEN = os.getenv("API_KEY")
# bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
#
#
# @bot.message_handler(content_types=['text'])
# def handle_text_message(message):
#     # Получаем текст сообщения
#     text = message.text
#
#     # Создаем объект gTTS для преобразования текста в речь
#     tts = gTTS(text, lang='ru')  # Можете изменить язык на нужный вам
#     # Создаем временный файл для сохранения аудио
#     temp_file = "temp_audio.mp3"
#     tts.save(temp_file)
#
#     # Отправляем аудио-сообщение пользователю
#     with open(temp_file, 'rb') as audio:
#         bot.send_voice(message.chat.id, audio)
#
#     # Удаляем временный файл
#     os.remove(temp_file)
#
#
# if __name__ == '__main__':
#     bot.infinity_polling()

from gtts import gTTS


def speach_ai_answers(message):
    # Получаем текст сообщения
    text = message
    # Создаем объект gTTS для преобразования текста в речь
    tts = gTTS(text, lang='ru')  # Можете изменить язык на нужный вам
    # Создаем временный файл для сохранения аудио
    temp_file = "temp_audio.mp3"
    tts.save(temp_file)
    return temp_file
