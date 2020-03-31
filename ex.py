dezena10 = 0
centena100 = 0

print("Escreva um número de até 3 digitos")
abc = int(input())
centena = int(abc/100)
perdido = (abc-(centena100))
dezena = int(perdido/10)
unidade = (perdido-(dezena10))
print("centena=", centena, "dezena", dezena, "unidade", unidade)