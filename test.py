from registro import *
import random
import pickle
import os


def menu():
    print('\n === Menu ===')
    print('1) Opcion 1: Cargar vector.')
    print('2) Opcion 2: Mostrar vector.')
    print('3) Opcion 3: Det. cantidad de alumnos por curso y aula.')
    print('4) Opcion 4: Generar archivo. ')
    print('5) Opcion 5: Mostrar archivo. ')
    print('0) Salir.')


def validate():
    n = int(input('Ingrese la cantidad de estudiantes a cargar: '))
    while n <= 0:
        n = int(input('Error! Tiene que ser un nro mayor a cero: '))
    return n


def cargar_vector(v, n):
    nombres = ('fran', 'carlos', 'marcelo', 'juan', 'lionel', 'diego')
    for i in range(n):
        leg = random.randint(1, 999)
        nom = random.choice(nombres)
        cur = random.randint(1, 17)
        aula = random.randint(540, 555)
        cca = random.randint(0, 30)
        reg = Estudiante(leg, nom, cur, aula, cca)
        add_in_order(v, reg)
    print('Vector Cargado.')
    return v


def add_in_order(v, reg):
    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].legajo == reg.legajo:
            pos = c
            break
        if reg.legajo < v[c].legajo:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [reg]


def mostrar_vector(v):
    for i in range(len(v)):
        print(v[i])


def generar_matriz(v):
    fila = 17
    col = 16
    mat = [[0] * col for f in range(fila)]
    for i in range(len(v)):
        f = v[i].curso - 1
        c = v[i].aula - 540
        mat[f][c] += 1
    print('\nMatriz generada.')
    return mat


def mostrar_matriz(matriz):
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if c >= 5:
                print('Pára el curso: 1k', f + 1, ', en el aula: ', c + 540, ', hay: ', matriz[f][c], ' alumnos.')


def generar_archivo(v, fd):
    m = open(fd, 'wb')
    for i in range(len(v)):
        if v[i].cuestionarios >= 10:
            pickle.dump(v[i], m)
    m.close()
    print('\nArchivo generado.')


def calcular_prom(suma, cant):
    if cant == 0:
        print('\nEl promedio es de: ', 0)
    else:
        prom = suma / cant
        print('\nEl promedio de cuestionarios aprobados por los alumnos es de: ', round(prom, 2))


def mostrar_archivo(fd):
    suma, cant = 0, 0
    if os.path.exists(fd):
        m = open(fd, 'rb')
        tam = os.path.getsize(fd)
        while m.tell() < tam:
            reg = pickle.load(m)
            print(reg)
            cant += 1
            suma += reg.cuestionarios
        m.close()
        calcular_prom(suma, cant)
    else:
        print('El archivo ', fd, ' no existe.')


def principal():
    op = -1
    v = []
    fd = 'archivo.dat'
    while op != 0:
        menu()
        op = int(input('Ingrese la opcion que desea: '))

        if op == 1:
            n = validate()
            v = cargar_vector(v, n)
        elif op == 2:
            if len(v) == 0:
                print('\nPrimero cargue el vector. (op 1)')
            else:
                mostrar_vector(v)
        elif op == 3:
            if len(v) == 0:
                print('\nPrimero cargue el vector. (op 1)')
            else:
                matriz = generar_matriz(v)
                mostrar_matriz(matriz)
        elif op == 4:
            if len(v) == 0:
                print('\nPrimero cargue el vector. (op 1)')
            else:
                generar_archivo(v, fd)
        elif op == 5:
            if len(v) == 0:
                print('\nPrimero cargue el vector. (op 1)')
            else:
                mostrar_archivo(fd)
        elif op == 0:
            print('Programa terminado. ')
        else:
            print('Opcion Invalida.')


if __name__ == '__main__':
    principal()
