import telebot
import os
from dotenv import load_dotenv
from openai import OpenAI
import speach_bot
load_dotenv()
API_KEY_bot = os.getenv("API_KEY")
bot = telebot.TeleBot(API_KEY_bot)
# Инициализация клиента API OpenAI с вашим API ключом
client = OpenAI(
    api_key="sk-ocZsDK2UM23MfVob1ncrgijjrEytVdeU", base_url="https://api.proxyapi.ru/openai/v1",
)
conversation_histories = {}
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я простой бот, создвнный для демонстрации команд /start и /help")
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "Список доступных команд:\n/start - Начать работу с ботом\n/help - Показать справку")
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.chat.id
    user_input = message.text
    if user_id not in conversation_histories:
        conversation_histories[user_id] = []
    conversation_history = conversation_histories[user_id]
    conversation_history.append({"role": "user", "content": user_input})
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=conversation_history
    )
    ai_response_content = chat_completion.choices[0].message.content
    temp_file = speach_bot.speach_ai_answers(ai_response_content)
    with open(temp_file, 'rb') as audio:
        bot.send_voice(message.chat.id, audio)
        bot.reply_to(message, ai_response_content)
    os.remove(temp_file)
    conversation_history.append({"role": "system", "content": ai_response_content})
if __name__ == '__main__':
    bot.polling(none_stop=True)



# @bot.message_handler(commands=['help'])
# def handle_help(message):
#     bot.send_message(message.chat.id, "Список доступных команд:\n/start - Начать работу с ботом\n/help - Показать справку"
#                                       "\n/perevorot - Переворачивает строку\n/caps - Переводит строку в верхний регистр\n/cut - Удаляет гласные буквы из строки"
#                                       "\n/count - Считает количество символов")
# @bot.message_handler(commands=['perevorot'])
# def handle_perevorot(message):
#     orig_txt = message.text[len('/perevorot '):]
#     rev_txt = orig_txt[::-1]
#     bot.reply_to(message, rev_txt)
# @bot.message_handler(commands=['caps'])
# def handle_caps(message):
#     orig_txt = message.text[len('/caps '):]
#     rev_txt = orig_txt.upper()
#     bot.reply_to(message, rev_txt)
# def remove_vowels(input_text):
#     vowels = "AEIOUaeiouАЕИОУаеиоуЫыЭэЮюЯя"
#     txt = ''.join([char for char in input_text if char not in vowels])
#     return txt
# @bot.message_handler(commands=['cut'])
# def handle_cut(message):
#     orig_txt = message.text[len('/cut '):]
#     rev_txt = remove_vowels(orig_txt)
#     bot.reply_to(message, rev_txt)
# def count_char(input_text):
#     vowels = "AEIOUaeiouАЕИОУаеиоуЫыЭэЮюЯя"
#     consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyzБВГДЖЗКЛМНПРСТФХЦЧШЩЪЬбвгджзклмнпрстфхцчшщъь"
#     num_vowels = len([char for char in input_text if char in vowels])
#     num_consonants = len([char for char in input_text if char in consonants])
#     total_chars = len(input_text)
#     num_symbols = len([char for char in input_text if char != ' '])
#     result_str = f"Общее количество символов в строке с пробелами: {total_chars}.\n" \
#                  f"Общее количество символов в строке без пробелов: {num_symbols}.\nГласных в строке: {num_vowels}\nСогласных в строке: {num_consonants}"
#     return result_str
# @bot.message_handler(commands=['count'])
# def handle_count(message):
#     orig_txt = message.text[len('/count '):]
#     rev_txt = count_char(orig_txt)
#     bot.reply_to(message, rev_txt)
# Обработчик текстовых сообщений
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#
#     bot.reply_to(message, message.text)