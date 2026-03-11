# imprimir a tabuada de um numero escolhido 

#numero do usuario para contador
tabuada = int(input("digite um valor para a tabuada"))

contador = 0
while contador <= 10:
    print(contador * tabuada)
    contador = contador + 1


#correção

tabuada = int(input("digite a tabuada desejada"))

for x in range(1,11):
    print(tabuada * x)