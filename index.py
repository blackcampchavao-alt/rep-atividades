from math import *
x = 3
y = x**3 - abs(log(x))
print(y)

#6
x = 3
w = 3
k = 3
v = x**2 - w**k
print(v)

#7
x = 3
y = 3
Y = (exp(2) + sqrt(x + y))/3
print(Y)

#8
x = 3
y = (x**2 - log10(x) + sin(x)) / (x - cos(2)**3)

print(y)




# aula 2 
n1 = int(input("ler o primeiro valor: "))
n2 = int(input("ler o segundo valor: "))
if n1 > n2: 
    print(n1) 

if n2 > n1:
    print(n2)

if n1 == n2: 
    print("iguais")


# 2

n1 = int(input("ler o valor: "))
if n1 >= 0:
    print("positivo")

if n1 <= 0:
    print("negativo")
