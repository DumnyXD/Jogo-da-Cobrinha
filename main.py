import telas

while True:
    telas.jogo()
    opcao = telas.menu()
    if opcao == "Iniciar":
        telas.jogo()

    elif opcao == "Creditos":
        telas.creditos()
