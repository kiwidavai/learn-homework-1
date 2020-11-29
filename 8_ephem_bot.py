"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def planet(update,context):
    supinfo = {
        "Mars": ephem.Mars(), 'Neptune' : ephem.Neptune(),
        'Mercury' : ephem.Mercury(), 'Venus' : ephem.Venus(), 
        'Jupiter' : ephem.Jupiter(), 'Moon' : ephem.Moon(),
        'Saturn' : ephem.Saturn(), 'Uranus' : ephem.Uranus(), 
        'Pluto' : ephem.Pluto(), 'Sun' : ephem.Sun(),  
    }
    user_text = update.message.text
    user_text_planet = user_text.split(' ')
    print(user_text_planet[1])
    name_planet = user_text_planet[1]
    planet = supinfo.get(name_planet)
    planet.compute('2019/01/01')
    update.message.reply_text(planet.ra)
    print(ephem.constellation(planet))
    update.message.reply_text(ephem.constellation(planet))
   
    
# def  word_count():


def main():
    mybot = Updater("1487495874:AAEAwJ96Kr2hsCSqi7JLgTjX6CbpjdCgK6k", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    # dp.add_handler(CommandHandler('wordcount'))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
