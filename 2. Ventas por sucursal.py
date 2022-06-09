# Datos y variables 

contador_ventas = 0 
acumulador_ventas = 0 
cont_acotado = 0 
cont_cuatro = 0 
cont_cinco = 0 
cont_seis = 0
inferior = False 

# Ciclo 

ventas = int(input('Ingrese la cantidad de ventas: '))

while ventas >= 0:
    #Procesos 
    #a)
    contador_ventas += 1

    #b) acumular ventas 

    acumulador_ventas += ventas

    #c) cantidad de ventas comprendido entre 100 y 300
    if 100 <= ventas <= 300:
        cont_acotado += 1 

    #d) ventas con 400 500 600 
    if ventas == 400:
        cont_cuatro += 1 
    if ventas == 500:
        cont_cinco += 1
    if ventas == 600:
        cont_seis += 1 
    #e) indicar venta menor a 50 
    if ventas < 50 :
        inferior = True 
    
    #Segunda carga 
    ventas = int(input('Ingrese la cantidad de ventas: '))

#Resultados 

print('Resultados')
print()
print('La cantidad de ventas fue de: ', contador_ventas)
print('Ventas totales: ', acumulador_ventas)
print('Ventas entre 100 y 300 unidades: ', cont_acotado)
print('Ventas con 400 unidades: ', cont_cuatro)
print('Ventas con 500 unidades: ', cont_cinco)
print('Ventas con 600 unidades: ', cont_seis)
if inferior:
    print('Hubo al menos una venta menor a 50 unidades.')
else:
    print('No hubo ventas menora 50 unidades.')
