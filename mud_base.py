num = 1
print(70 * '_')
print('Passar de base (10) para base (2) - 0')
print(70 * '_')
print('Passar de base (2) para base (10) - 1')
print(70 * '_')
resp = int(input('0/1: '))
base = []
j = 0
while num != 0:
    if (resp == 0):
        print(70 * '=')
        print('Você selecionou passar de (2) para (10) - Pressione 0 para sair.')
        num = str(input('Número em base (2): '))

        reverse = num[::-1]

        for i in reverse:
            if(i == 0 or 1):
                j += 1
            print(j)
        print(i)
    if (resp == 1):
        print(70 * '=')
        print('Você selecionou passar de (10) para (2) - Pressione 0 para sair.')
        num = int(input('Número em base (10): '))
        print('{} em binário é igual a: {}'.format(num, bin(num)))
    if (num == 0):
        print('Saindo...')
        break
