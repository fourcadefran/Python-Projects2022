# Datos

cant_espec = int(input('Ingrese la cantidad de espectadores(con 0(cero) termina): '))
total = 0
cont_desc = 0
cont_funciones = 0

#Procesos

while cant_espec != 0:
    #Cargar descuesto
    descuento = input("Ingrese el descuento(S -> tiene descuento ; N -> No tiene descuento)")
    #definir precio
    if descuento == 'S':
        precio = 50
    else:
        precio = 75
    #Acumular monto total
    total = total + (cant_espec * precio)

    #Contar funciones
    if descuento == 'S':
        cont_desc += 1
    cont_funciones += 1
    #Nueva carga de datos
    cant_espec = int(input('Ingrese la cantidad de espectadores(con 0(cero) termina): '))


if cont_funciones != 0:
    porcentaje = (cont_desc * 100) / cont_funciones
else:
    porcentaje = 0

#Resultados

print('la recaudación total del complejo: ', total)

print('Se efectuaron ', cont_desc, ' funciones con descuento. ')

print('Representa un ', porcentaje, ' % del total de las funciones. ')
