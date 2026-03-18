
j = int(input("digite um valor: "))

for i in range(0,j):
    for x in range(0,j):
        if x >= i:
            print("@", end='')
        else:
            print("$", end='')
    print()

        
    
    