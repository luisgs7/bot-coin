"""Start Bot Telegram Module"""
import os
import json
import requests
from decouple import config

from query_response import app # noqa pylint: disable=import-error


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

                    primeira_message = int(dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(message, primeira_message)
                    self.responder(resposta, chat_id)

    def obter_novas_mensagens(self, update_id):
        '''Get new messages sent to bot'''
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'

        resultado = requests.get(link_requisicao) # noqa pylint: disable= missing-timeout
        return json.loads(resultado.content)

    def criar_resposta(self, message, primeira_message):
        '''Send personalized responses to the bot,
           according to the request made.'''
        if primeira_message or message.lower() in 'menu': #noqa pylint: disable=no-else-return
            return 'Bem vindo ao menu...' 
        else:
            match message:
                #TODO Dollar Option
                case '1':
                    return 'Dollar Option'
                #TODO Euro Option
                case '2':
                    return 'Euro Option'
                #TODO Canadian Dollar
                case '3':
                    return 'Canadian Dollar'
                #TODO Japanese Yen
                case '4':
                    return 'Japanese Yen'
                #TODO Mercado Bitcoin
                case '5':
                    return 'Mercado Bitcoin'
                case _:
                    return 'Opção inválida, digite "menu" e volte ao MENU do Bot :)'

    def responder(self, resposta, chat_id):
        '''Method responsible for sending responses to the bot user.'''
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao) # noqa pylint: disable= missing-timeout
