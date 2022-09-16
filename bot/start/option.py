def response_coin(message: str, first_message):
    if first_message or message.lower() in 'menu': #noqa pylint: disable=no-else-return
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