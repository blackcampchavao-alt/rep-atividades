# um programa de peça um numero entre 0 e 10
# tem que ser um valor valido se nao ele nao avança e use comandos logicos 

numero = int(input("digite um numero entre 0 e 10:"))

while numero < 0 or numero > 10:
    print("numero invalido")
    numero = int(input("digite um numero valido"))

print("nuemro aceito")