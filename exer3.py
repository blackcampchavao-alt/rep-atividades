n1 = int(input("ler o numero: "))
if n1 == 1:
    print("domingo")

if n1 == 2:
    print("segunda")

if n1 == 3:
    print("terça")

if n1 == 4:
    print("quarta")

if n1 == 5:
    print("quinta")

if n1 == 6:
    print("sexta")

if n1 == 7:
    print("sabado")



#exer 4
s = int(input("informe o salário "))

if s > 1250:
    aumento = s* 0.1
    s = s + aumento
    print(s)

if s <= 1250:
    aumento = s* 0.15
    s = s + aumento
    print(s)

    
#5
i = int(input("idade do carro" ))

if i <= 3:
    print("velho")
else:
    print("novo")
