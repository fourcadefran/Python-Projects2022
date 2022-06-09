#Datos

total_velero = 0
total_lanchas = 0
mas_paga = 0
prom = 0
porcentaje = 0
primer_velero = True

# Procesos

n = int(input("Ingrese la cantidad de barcos: "))

for i in range(n):
    #inicializar los datos
    tipo = int(input("Ingrese el tipo (1 velero 2 lancha): "))
    monto = int(input("Ingrese el monto mensual: "))
    nombre = input("Ingrese el nombre: ")

    #Procesar datos

    if tipo == 1:
        total_velero += monto

        if primer_velero:
            mas_paga = monto
            mas_paga_nombre = nombre
            primer_velero = False
        elif monto > mas_paga:
            mas_paga = monto
            mas_paga_nombre = nombre
    else:
        total_lanchas += monto

if n > 0:
    total_anual_velero = total_velero * 12
    total_anual_lanchas = total_lanchas * 12

    total = total_anual_lanchas + total_anual_velero
    pv = ( total_velero / total ) * 100
    pl = ( total_lanchas * 100 ) / total

    promedio = total / n
    print("total de lanchas:", total_lanchas, "total de veleros: ", total_velero)

    if primer_velero == False:
        print("Cuota mas alta: ", mas_paga,"Nombre mas cuota mas alta: ", mas_paga_nombre)
    else:
        print("No hubo valores")

else:
    print("Error")

print("Promedio: ", promedio,"Porcentaje veleros: ", pv,"Porcentaje lanchas", pl)
