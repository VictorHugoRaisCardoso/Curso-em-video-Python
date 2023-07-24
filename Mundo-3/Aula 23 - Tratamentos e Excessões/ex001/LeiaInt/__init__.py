def LeiaInt(mensagem):
    try:
        mensagem = int(input(mensagem))
        return mensagem
    
    except KeyboardInterrupt:
        mensagem = 0
        return f'O usuário preferiu não informar o valor. Valor definido como {mensagem}'
    
    except (TypeError, ValueError):
        while True:
            mensagem = str(input(f'ERRO: Isto não é um número!\nDigite apenas um valor interiro: '))
            if mensagem.isnumeric():
                int(mensagem)
                return f'Você digitou o valor: {mensagem}'
                break
    