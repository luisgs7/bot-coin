'''Present Messages for Bot'''
import os
from typing import Tuple
from query_response import app  # noqa pylint: disable=import-error
from utils import constants # noqa pylint: disable=import-error


def welcome() -> str:
    '''Message welcome User Bot'''
    text_menu = f'''Olá bem vindo ao BotCoin, digite a opção da cotação desejada:{os.linesep}
      1 - Cotação do Dollar Americano {os.linesep}
      2 - Cotação do Euro {os.linesep}
      3 - Cotação do Dollar Canadense {os.linesep}
      4 - Cotação do Yen Japonês {os.linesep}
      5 - Cotação do Bitcoin(Mercado Bitcoin) {os.linesep}
      6 - Sobre o Bot
      '''
    return text_menu


def format_query(_id: int) -> str:
    '''Performs data search, according to the informed id'''
    result: Tuple = app.DataConnect(_id).select_coin_id()
    data_format = _format_response(result)
    return data_format


def _format_response(query: Tuple) -> str:
    '''Return messase response formated'''
    return f'''Cotação:
    - {query[0]}: R$ {round(query[1], 3)}{os.linesep}\
    - Variação: {query[2]}%{os.linesep}\
    - Dados salvos em: {query[3]}'''


def about():
    '''Message about Bot'''
    text_menu = f'''Sobre o BotCoin:{os.linesep}
    {constants.MESSAGE_ABOUT}'''
    return text_menu
