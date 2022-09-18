'''Option Module For Bot'''
from start.messages import welcome, format_query, about # noqa pylint: disable=import-error


def response_coin(message: str, first_message): # noqa pylint: disable=too-many-return-statements
    '''Response data for user'''
    if first_message or message.lower() in 'menu': # noqa pylint: disable=no-else-return
        return welcome()
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
            case '6':
                return about()
            case _:
                return 'Opção inválida, digite "menu" e volte ao MENU do Bot :)'
