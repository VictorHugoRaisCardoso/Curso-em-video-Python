def maior(*num):
    mai = 0
    print('=' * 50)
    for pos, n in enumerate(num):
        print(f'{n} ', end='')
        if pos == 0:
            mai = n
        else:
            if n > mai:
                mai = n
    print(f'Ao todo foram analisados {len(num)} números.')
    print(f'O maior numero foi {mai}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()