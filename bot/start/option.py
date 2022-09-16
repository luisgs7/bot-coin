'''Option Module For Bot'''
from query_response import app  # noqa pylint: disable=import-error


def response_coin(message: str, first_message): # noqa pylint: disable=too-many-return-statements
    '''Response data for user'''
    if first_message or message.lower() in 'menu': # noqa pylint: disable=no-else-return
        return 'Bem vindo ao menu...'
    else:
        match message:

            case '1':
                response = format_query(1)
                return response

            case '2':
                response = format_query(2)
                return response

            case '3':
                response = format_query(3)
                return response

            case '4':
                response = format_query(4)
                return response

            case '5':
                response = format_query(5)
                return response
            case _:
                return 'Opção inválida, digite "menu" e volte ao MENU do Bot :)'


def format_query(_id: int):
    '''Performs data search, according to the informed id'''
    return app.DataConnect(_id).select_coin_id()
