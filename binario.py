num = 1
print(70 *'_')
print('Passar de base (10) para base (2) - 0')
print(70*'_')
print('Passar de base (2) para base (10) - 1')
print(70*'_')
resp = bool(input('0/1: '))
while num != 0:
    if(resp == 1):
        print(70*'=')
        print('Você selecionou passar de (10) para (2) - Pressione 0 para sair')
        num = int(input('Número em base (10): '))
        if(num == 0):
            print('Saindo...')
            break

    