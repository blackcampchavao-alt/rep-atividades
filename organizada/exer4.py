# leia 6 numeros inteiros positivos do usuario e exiba o maior
contador = 0
maior = 0 

while contador < 6:
    numero = int(input("digite um valor"))
    if maior < numero:
        maior = numero
    contador = contador + 1 

print(maior)