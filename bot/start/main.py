"""Start Bot Telegram Module"""
import os
import json
import requests
from decouple import config

from query_response import app # noqa pylint: disable=import-error
from start import option # noqa pylint: disable=import-error


TOKEN: str = config("TELEGRAM_BOT_TOKEN")


class TelegramBot:
    '''Class responsible for initializing and performing
       the main functions of the bot.'''
    def __init__(self):
        self.url_base = f'https://api.telegram.org/bot{TOKEN}/'
        print("Bot running...")

    def iniciar(self):
        '''Start Bot'''
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao["result"]

            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    message = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]

                    primeira_message: bool = int(dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(message, primeira_message)
                    self.responder(resposta, chat_id)

    def obter_novas_mensagens(self, update_id):
        '''Get new messages sent to bot'''
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'

        resultado = requests.get(link_requisicao) # noqa pylint: disable= missing-timeout
        return json.loads(resultado.content)

    def criar_resposta(self, message: str, primeira_message: bool):
        '''Send personalized responses to the bot,
           according to the request made.'''
        return option.response_coin(message, primeira_message)

    def responder(self, resposta, chat_id):
        '''Method responsible for sending responses to the bot user.'''
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao) # noqa pylint: disable= missing-timeout
