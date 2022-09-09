import random

# Vectores auxiliares

titulos = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI', 'HIJ', 'IJK', 'JKL', 'KLM', 'LMN', 'MNÑ', 'NÑO', 'ÑOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXY', 'XYZ']
fechas = ['03-10-2001', '10-05-2002', '15-07-2003', '17-11-2004', '20-03-2005', '23-01-2006', '27-09-2007', '30-12-2008','31-06-2009', '05-03-2010', '12-04-2011', '08-02-2012', '19-05-2013']
anios = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]

# Clase Proyecto
class Proyecto:
    def __init__(self, num_p, tit, fecha, leng, cant):
        self.num = num_p
        self.titulo = tit
        self.fecha = fecha
        self.lenguaje = leng
        self.cantidad_cod = cant

    def __str__(self):
        s = "| {:<15} | {:<25} | {:<25} | {:<25} | {:<20}".format(self.num, self.titulo, self.fecha,
                                                                  cambiar_lenguajes(self.lenguaje), self.cantidad_cod)
        return s


# Menú de opciones -----------------------------------------------------------------------------------------------------
def mostrar_menu():
    print("-" * 160 + "|")
    print(" " * 60, "Gestión de Proyectos de Software.")
    print("-" * 160 + "|")
    print(" " * 60, "1. Cargar proyectos.")
    print(" " * 60, "2. Listar proyectos.")
    print(" " * 60, "3. Actualizar proyecto.")
    print(" " * 60, "4. Resumen por lenguaje.")
    print(" " * 60, "5. Resumen por año.")
    print(" " * 60, "6. Filtrar lenguaje.")
    print(" " * 60, "7. Productividad.")
    print(" " * 60, "8. Salir.")


# Generales ------------------------------------------------------------------------------------------------------------
def validate(inf):
    n = int(input('¿Cuántos proyectos quiere cargar? Valor (mayor a ' + str(inf) + ' por favor): '))
    while n <= inf:
        n = int(input('¡Error! debe ser mayor a ' + str(inf) + ', Cargue de nuevo: '))
    return n


def cambiar_lenguajes(lenguaje):
    leng = ['Python', 'Java', 'C++', 'Javascript', 'Shell', 'HTML', 'Ruby', 'Swift', 'C#', 'VB', 'Go']
    pos = lenguaje
    return leng[pos]

# OPCIÓN 1 ------------------------------------------------------------------------------------------------------------
def cargar_proyectos(n):
    proyectos = [None] * n
    for i in range(len(proyectos)):
        num = i + 1
        tit = random.choice(titulos)
        fecha = random.choice(fechas)
        leng = random.randint(0, 10)
        cant_cod = random.randint(10, 10000)
        proyectos[i] = (Proyecto(num, tit, fecha, leng, cant_cod))
    return proyectos


def cargar_nuevo(proyectos, n):
    for i in range(n):
        num = proyectos[-1].num + 1
        tit = random.choice(titulos)
        fecha = random.choice(fechas)
        leng = random.randint(0, 10)
        cant_cod = random.randint(10, 10000)
        proyectos.append((Proyecto(num, tit, fecha, leng, cant_cod)))


# OPCION 2 ------------------------------------------------------------------------------------------------------------
def mostrar_proyectos(proyectos):
    print("\n",  " " * 68, "Listado de Proyectos:")
    ordenamiento(proyectos)
    print("|" + "=" * 160 + "|")
    print("| {:^15} | {:^25} | {:^25} | {:^25} | {:^20}".format("Número", "Título", "Fecha", "Lenguaje",
                                                                "Líneas de Código"))
    print("|" + "=" * 160 + "|")
    for proyecto in proyectos:
        print(str(proyecto))
    print(" ")


# OPCION 3 -------------------------------------------------------------------------------------------------------------
# Validar fecha
def validar_fecha(inf=2000, sup=2022):
    fecha = input("- Ingrese la fecha en formato dd-mm-yyyy (sin espacios) a cambiar: ")
    dd = int(fecha[0:2])
    mm = int(fecha[3:5])
    yyyy = int(fecha[6:])
    while (dd >= 31) or (mm >= 13) or (yyyy < inf or yyyy > sup) or ((fecha[2] and fecha[5]) != "-"):
        fecha = input("¡ERROR! algunos de los datos están mal ingresados.\n- Fecha en formato dd-mm-yyyy (sin espacios): ")
        dd = int(fecha[0:2])
        mm = int(fecha[3:5])
        yyyy = int(fecha[6:])
    tiempo = fecha
    return tiempo


def buscar_proyecto(proyectos, x):
    for proyecto in proyectos:
        if proyecto.num == x:
            print("\n",  " " * 68, "¡Proyecto encontrado!")
            print("|" + "=" * 160 + "|")
            print("| {:<15} | {:<25} | {:<25} | {:<25} | {:<20}".format("Número", "Título", "Fecha", "Lenguaje",
                                                                        "Líneas de Código"))
            print("|" + "=" * 160 + "|")
            print(str(proyecto))
            proyecto.cantidad_cod = int(input('\n- Ingrese la cantidad de líneas de código a cambiar: '))
            proyecto.fecha = validar_fecha()
            print("\n",  " " * 68, "¡Proyecto actualizado con éxito!")
            print("|" + "=" * 160 + "|")
            print("| {:<15} | {:<25} | {:<25} | {:<25} | {:<20}".format("Número", "Título", "Fecha", "Lenguaje",
                                                                        "Líneas de Código"))
            print("|" + "=" * 160 + "|")
            print(str(proyecto))
            print()
            return
    return print('Error...No se encontró ningún proyecto con los datos ingresados.')


# OPCION 4 -------------------------------------------------------------------------------------------------------------
# Ordenar por títulos
def ordenamiento(proyectos):
    n = len(proyectos)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if proyectos[i].titulo > proyectos[j].titulo:
                proyectos[i], proyectos[j] = proyectos[j], proyectos[i]


def acumular_codigo_por_lenguaje(v):
    v_acum = [0] * 11
    for i in range(len(v)):
        pos = v[i].lenguaje
        v_acum[pos] += v[i].cantidad_cod

    for i in range(len(v_acum)):
        if v_acum[i] > 0:
            print("- Lenguaje: ", cambiar_lenguajes(i), "- Cantidad: ", v_acum[i],"\n")


# OPCION 5 -------------------------------------------------------------------------------------------------------------
def contar_proyectos_anios(proyectos):
    cant_anios = [0] * 23
    n = len(proyectos)
    for i in range(n):
        fecha = proyectos[i].fecha
        anio = int(fecha[6:])
        for j in range(len(anios)):
            if anio == anios[j]:
                cant_anios[j] += 1
    return cant_anios


def mostrar_cant_proyectos_anio(cant_proy):
    for i in range(len(cant_proy)):
        if cant_proy[i] > 0:
            print('En el año ', anios[i], ' hubo: ', cant_proy[i], ' proyectos.\n')


# OPCION 6 -------------------------------------------------------------------------------------------------------------
def generar_proyectos_por_lenguajes(vp):
    v = []
    ln = input("Ingrese el lenguaje que desee ordenar: ")
    for i in range(len(vp)):
        if cambiar_lenguajes(vp[i].lenguaje) == ln:
            v.append(vp[i])
    return v


def ordenar_proyectos_lenguaje(vector):
    tam = len(vector)
    for i in range(0, tam - 1):
        for j in range(i + 1, tam):
            if vector[i].num > vector[j].num:
                vector[i], vector[j] = vector[j], vector[i]
    return vector


# OPCION 7--------------------------------------------------------------------------------------------------------------
# Calcular el mayor de las cantidades
def calcular_mayor_anio(v_cantidad_anios):
    mayores = []
    mayor = -1
    for i in range(len(v_cantidad_anios)):
        if v_cantidad_anios[i] > mayor:
            mayor = v_cantidad_anios[i]


    for j in range(len(v_cantidad_anios)):
        if v_cantidad_anios[j] >= mayor:
            mayores.append([j, v_cantidad_anios[j]])
    return mayores


# Convertir el indece en el año determinado
def convertir_indice_anio(a):
    for i in range(len(anios)):
        if a == i:
            return anios[i]


def mostrar_mayores(mayores):
    n = len(mayores)
    for i in range(n):
        print('Año: ', convertir_indice_anio(mayores[i][0]), 'Cantidad de proyecto: ', mayores[i][1])
# ------------------------------------------------------------------------------------------------------------------------
