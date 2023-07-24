from logica.systema.layoutsystem import LayoutSystem

display = LayoutSystem()
display.arquivoInexiste()

while True:
    try:
        display.decorador("SYSTEMA DE CADASTRAMENTO")
        display.menu()
        opção = display.escolha()
        if opção == 1:
            display.novoCadastros()
        elif opção == 2:
            display.verCadastros()
        else:
            break
    except(KeyboardInterrupt):
        print(f'O usuário interrompeu o programa.')
        break
