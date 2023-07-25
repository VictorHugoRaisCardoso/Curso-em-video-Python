distancia = float(input('Seja muito bem vindo prezado cliente! informe qual a distância da viagem: '))
if distancia > 200.0:
    print(f'Sua viagem vai ser de {distancia}Km, seu custo total será de R${distancia * 0.45}.')
    resposta = str(input('Confirme ou rejeite digitando SIM ou NAO: ')).upper().strip()
    if resposta == 'SIM':
        print('Passagem comprada com sucesso! Boa viagem!')
    else:
        print('Lamentamos que não tenha fechado negócio, mas esperamos te ver em breve!')

else:
    print(f'Sua viagem vai ser de {distancia}Km, seu custo total será de R${distancia * 0.50}.')
    resposta = str(input('Confirme ou rejeite digitando SIM ou NAO: ')).upper().strip()
    if resposta == 'SIM':
        print('Passagem comprada com sucesso! Boa Viagem!')
    else:
        print('Lamentamos que não tenha fechado negócio, mas esperamos te ver em breve!')
