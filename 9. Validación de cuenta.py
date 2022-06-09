#Datos
cuenta = input('Ingrese la cuenta con formato nombre@dominio: ')

dos_puntos = False


for i in cuenta:

    if i[0] == "." or i[len(cuenta)] == ".":
        print('Error!!! proceso terminado.')
        break

    if i == "." and anterior == ".":
        dos_puntos = True

    if i[0] == "@" or i[len(cuenta)] == "@":
        print('Error!!! proceso terminado.')
        break
    anterior = i 

if dos_puntos:
    print('Error!!! proceso terminado')
else:
    print('cuenta valida.')

    