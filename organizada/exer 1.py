# imprimir numeros pares entre o 0 e um numero que o usuario digitar

# while

x = 1
numero = int(input("digite um numero"))
while x < numero:
    #verificar se e par
    if x % 2 ==0:
        print(x)
    x = x +1 

#for
numero = int(input("digite um numero"))
for x in range(1,numero):
    if x % 2 == 0:
      print(x)