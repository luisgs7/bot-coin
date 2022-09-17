'''Present Messages for Bot'''
import os


def welcome() -> str:
    '''Message welcome User Bot'''
    text_menu = f'''Olá bem vindo ao BotCoin, digite a opção da cotação desejada:{os.linesep}
      1 - Cotação do Dollar Americano {os.linesep}
      2 - Cotação do Euro {os.linesep}
      3 - Cotação do Dollar Canadense {os.linesep}
      4 - Cotação do Yen Japonês {os.linesep}
      5 - Cotação do Bitcoin(Mercado Bitcoin)
      '''
    return text_menu
