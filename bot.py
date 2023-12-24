import config
import telebot
from requests import get
import webbrowser
import pyautogui
import time

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["start"])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row("Сделать хорошо✨", "Сделать плохо⚡")
    bot.send_message(message.chat.id, "Выбери действие", reply_markup=keyboard)


@bot.message_handler(content_types=["text"])
def using_power(message):
    if message.text == "Сделать хорошо✨":
        r = get("https://godville.net/gods/api/Abendsonnenschein/fcc1eac28af1")
        count_of_clicks = r.json()["godpower"] // 25
        if count_of_clicks == 0:
            bot.send_message(message.chat.id, "Нет энергии")
        else:
            bot.send_message(
                message.chat.id, "Процесс пошел. Всего зарядов:" + str(count_of_clicks)
            )
            webbrowser.open("https://godville.net/superhero")
            pyautogui.moveTo(1739, 374)
            time.sleep(5)
            for _ in range(count_of_clicks):
                pyautogui.click()
                time.sleep(2)
            pyautogui.click(3792, 30)
            pyautogui.moveTo(2009, 1027)
            bot.send_message(message.chat.id, "Готово")
    elif message.text == "Сделать плохо⚡":
        bot.send_message(message.chat.id, "Мы не делаем герою плохо!")


bot.polling(none_stop=True)
