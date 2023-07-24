def LeiaFloat(mensagem):
    try:
        mensagem = float(input(f'{mensagem}'))
        return f'{mensagem:.2f}'
    
    except KeyboardInterrupt:
        mensagem = 0.0
        return f'O usuário preferiu não informar o valor. O valor foi definido como {mensagem}'
    
    except (ValueError, TypeError):
        while True:
            mensagem = str(input(f'ERRO: Isso não é um valor Real.\nTente novamente: '))
            if mensagem.isnumeric():
                float(mensagem)
                return mensagem
                break

    