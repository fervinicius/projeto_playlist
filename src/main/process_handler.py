from src.view.first_view import introduction_page

def start() -> None:
    while True:

        command = introduction_page()
        if command == '1': print("Inserindo música")
        elif command == '2': print("Criando playlist")
        elif command == '5': exit()
        else: print("\n Comando não encontrado, tente novamente! \n\n")