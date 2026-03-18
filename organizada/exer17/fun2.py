def par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
print(par(2))
print(par(3))
print(par(27))

def par_ou_impar(numero):
    if par(numero):
        return "par"
    else:
        return "impar"

print(par_ou_impar(2))
print(par_ou_impar(3)) 

def maior(x,y):
    if x > y:
        return x
    else:
        return y
    
print(maior(5,9))