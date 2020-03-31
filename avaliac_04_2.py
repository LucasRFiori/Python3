n1 = int(input())
conv = str(n1)

if (int(conv[3]) in range(0,3)):
    print("Segunda")
elif (int(conv[3]) in range(2,5)):
    print("Terça")
elif (int(conv[3]) in range(4,7)):
    print("Quarta")
elif (int(conv[3]) in range(6,9)):
    print("Quinta")
else:
    print("Sexta")