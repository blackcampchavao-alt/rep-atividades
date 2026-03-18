
tamanho = int(input("digite um tamanho: "))

for i in range(0,tamanho):
    for j in range(0,tamanho):
        if j % 2 == 0:
            print("0", end='')
        else:
            print("*", end='')
    print();