a = 's'
while a != 'n':
    n, oper, n2 = input("Digite em uma linha, ex: 5 + 4 ").split()

    if(str(oper) == "+"):
        res = int(n) + int(n2)

    if(str(oper) == "-"):
        res = int(n) - int(n2)

    if(str(oper) == "*"):
        res = int(n) * int(n2)

    if(str(oper) == "/"):
        res = int(n) / int(n2)
    a = str(input('Deseja continuar? s/n '))
    print("Resultado:", res)