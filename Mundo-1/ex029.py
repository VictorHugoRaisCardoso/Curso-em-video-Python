from time import sleep
velocidade = int(input('Digite a velocidade do seu carro na rodovia: '))
sleep(2)
km = velocidade - 80
multa = float(km * 7)
if velocidade > 80:
    print(f'O limite de velocidade permitido neste trecho da rodovia é de 80km/h.')
    sleep(2)
    print(f'A velocidade registrada na rodovia foi de {velocidade}km/h.')
    sleep(2)
    print(f'Por ter ultrapassado este limite você será multado em R${multa:.2f}.')
    sleep(2)
    print(f'____________RESPEITE AS LEIS DE TRÂNSITO____________')
else:
    print(f'A velocidade registrada foi de {velocidade}km/h.')
    sleep(2)
    print(f'Continue sempre assim, sendo um exemplo no trânsito!')
    sleep(2)
    print('___________________FIM DO RELATÓRIO___________________')
