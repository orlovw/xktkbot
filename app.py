"""
Launch from here 
No telegram imports, only this bot modules

specify this environs pls
BOT_TOKEN
BOT_PORT (default = 5000)
BOT_URL (default = '')
"""
import handlers

from os import environ
from telegram.ext import Updater

token = "518550964:AAH8REFTL-_vH0ijF-7u5rShQC2PB9DjKqM"
#port = int(environ.get('PORT', 5000))
#token = environ.get('BOT_TOKEN')
#url = environ.get('BOT_URL', '')

bot_updater = Updater(token)


def start_listen():
    """Begin listening"""
    #bot_updater.start_webhook(url_path=url,
    #                          port=port,
    #                          listen='0.0.0.0')
    #bot_updater.bot.set_webhook("https://xktkbot.herokuapp.com/")
    
    bot_updater.start_polling(poll_interval=0.0, timeout=10, clean=False, bootstrap_retries=-1,
                              read_latency=2.0, allowed_updates=None)
    bot_updater.idle()


def main():
    Dispatcher = bot_updater.dispatcher
    Handlers = handlers.bot_handlers

    for handler in Handlers:
        Dispatcher.add_handler(handler)

    start_listen()

if __name__ == '__main__':
    main()
