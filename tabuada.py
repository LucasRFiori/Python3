num = 0
i = 0
respos = 's'
while respos == 's':
    num = int(input())
    i = 1
    while(i<10):
        res = num * i
        print("{} X {} = {}".format(num, i, res))
        i += 1
    respos = str(input('Deseja continuar? s/n'))