#datos
import random

n = 20000
inicio = 1
fin = 45000
random.seed(49)
cont5 = cont7 = cont9 = 0
cont_par_menor = 0
porcentaje = 0
may = 0
# procesos

for i in range(n):
    #procesos

    num = random.randint(inicio, fin)
    #1)
    if num % 5 ==0:
        cont5 += 1
    if num % 7 == 0:
        cont7 += 1
    if num % 9 == 0:
        cont9 += 1
    #2)
    car = str(num)
    ultimo_digito = int(car[-1])

    if i == 0 and 5 <= ultimo_digito <= 8 :
        may = num
    else:
        if 5 <= ultimo_digito <= 8:
            if may < num:
                may = num
    #3)
    if num % 2 == 0 and num < 15000:
        cont_par_menor += 1
    #4)
    porcentaje = (cont_par_menor * 100) // n

#Resultados
print()
print("Indicar cuantos números eran múltiplos de 5, cuántos eran múltiplos de 7 y cuántos eran múltiplos de 9." "\n"
      "5: ", cont5, "7: ", cont7, "9: ", cont9)
print()
print("Indicar el mayor entre todos aquellos números cuyo último dígito sea mayor o igual a 5 pero menor o igual a 8." "\n"
      "Mayor: ", may)
print()
print("Indicar cuantos números generados son pares menores a 15000.", cont_par_menor)
print()
print("Porcentaje: ", porcentaje)