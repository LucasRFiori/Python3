#Lucas Rodrigues Fiori 600687 1 B
n, oper, n2 = input("Digite em uma linha, ex: 5 + 4: ").split()

if(str(oper) == "+"):
    res = int(n) + int(n2)

if(str(oper) == "-"):
    res = int(n) - int(n2)

if(str(oper) == "*"):
    res = int(n) * int(n2)

if(str(oper) == "/"):
    res = int(n) / int(n2)

print("Resultado:", res)

#DE OUTRA FORMA

'''
n1 = float(input())
oper = str(input())
n2 = float(input())

if (oper == "+"):
    r = n1 + n2
if (oper == "-"):
    r = n1 - n2
if (oper == "/"):
    r = n1 / n2
if (oper == "*"):
    r = n1 * n2
print(r)

'''

