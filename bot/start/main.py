"""Start Bot Telegram Module"""
import json
import requests

from start import option # noqa pylint: disable=import-error
from utils import constants # noqa pylint: disable=import-error


class TelegramBot:
    '''Class responsible for initializing and performing
       the main functions of the bot.'''
    def __init__(self):
        self.url_base = constants.TELEGRAM_URL
        print("Bot running...")

    def start(self):
        '''Start Bot'''
        update_id = None
        while True:
            try:
                update = self.get_new_messages(update_id)
                data = update["result"]
                if data:
                    for dado in data:
                        update_id = dado['update_id']
                        message = str(dado["message"]["text"])
                        chat_id = dado["message"]["from"]["id"]

                        primary_messase: bool = int(dado["message"]["message_id"]) == 1
                        response = self.generate_response(message, primary_messase)
                        self.reply(response, chat_id)

            except Exception as e:
                print(f"Problema no bot, error: {e}")

            finally:
                print("Bot OK")

    def get_new_messages(self, update_id):
        '''Get new messages sent to bot'''
        link_request = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_request = f'{link_request}&offset={update_id + 1}'

        result = requests.get(link_request) # noqa pylint: disable= missing-timeout
        return json.loads(result.content)

    def generate_response(self, message: str, primary_messase: bool):
        '''Send personalized responses to the bot,
           according to the request made.'''
        return option.response_coin(message, primary_messase)

    def reply(self, response, chat_id):
        '''Method responsible for sending responses to the bot user.'''
        link_request = f'{self.url_base}sendMessage?chat_id={chat_id}&text={response}'
        requests.get(link_request) # noqa pylint: disable= missing-timeout
