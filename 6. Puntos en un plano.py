#Datos 
n = int(input('Ingrese la cantidad de puntos a procesar: '))
contador_primer = contador_tercer = 0 

for i in range(n):
    #Procesos
    x = float(input('Ingrese la coordenada en X: '))
    y = float(input('Ingrese la coordenada en Y: '))

    if x > 0 and y > 0:
        print('Se encuentra en el primer cuadrante.')
        contador_primer += 1
    elif x > 0 and y < 0:
        print('Se encuentra en el segundo cuadrante.')
    elif x < 0 and y < 0:
        print('Se encuentra en el tercer cuadrante.')
        contador_tercer += 1 
    elif x < 0 and y > 0: 
        print('Se encuentra en el cuarto cuadrante.')

    d = (x**2 + y**2)**1/2

    if i == 0:
        may = d 
    elif d > may:
        may = d


# Resultados
print()
print('En el 1er cuadrante se encuentran: ', contador_primer, ' puntos.')
print('En el 3er cuadrante se encuentran: ', contador_tercer, ' puntos.')
print()
print('Distancia mayor al punto al origen: ', may) 
