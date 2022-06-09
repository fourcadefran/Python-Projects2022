#Datos y funciones


sal_valido = False


def validar_cuit(cuit):
    cuit_valido = False
    cont_num = 0
    if len(cuit) == 13:
        if cuit[2] == '-' and cuit[-2] == '-':
            for car in cuit:
                if car >= '0' and car <= '9':
                    cont_num += 1
            if cont_num == 11:
                print('Cuit Valido.')
                cuit_valido = True
        else:
            print('Cuit no valido.')
    else:
        print('Cuit no valido.')

    return cuit_valido


def validar_desc(descripcion):
    desc_valida = False
    cont_palabras = 0
    dos_mayuscula = False
    anterior = ''
    if len(descripcion)  <= 60:
        for car in descripcion:
            if car == ' ' or car == '.':
                cont_palabras += 1
            else:
                if es_may(car) and es_may(anterior):
                    dos_mayuscula = True
            anterior = car
        if dos_mayuscula is False and cont_palabras >= 3:
            desc_valida = True
    else:
        print('Descripcion incorrecta.')
    return desc_valida


def es_may(car):
    if car >= 'A' and car <= 'Z':
        return True
    return False


def validar_salario(salario):
    pass


#Procesos

op = 's'

while op == 's':

    cuit = input('Ingrese el Cuit(formato 00-000000000-0): ')


    if validar_cuit(cuit):
        pass
    else:
        print('Cuit invalido.')

    descripcion = input('Ingrese la Descripcion de la busqueda: ')



    if validar_desc(descripcion):
        pass
    else:
        print('Descripcion no valida.')

    salario = int(input('Ingrese el salario: '))

    validar_salario(salario)

    if sal_valido:
        pass
    else:
        print('Salario no es valido.')


    op = input('Desea realizar otra carga(si o no): ')
