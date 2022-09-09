from proyectos import *


def test():
    # Programa Principal
    proyectos = None
    p_por_anios = None
    flag = False

    # Menu principal
    opc = 0
    while opc != 8:
        mostrar_menu()
        opc = int(input('Ingrese su eleccion: '))
        print()

        if opc == 1:
            if proyectos is None:
                # Validar carga
                n = validate(0)
                # Cargar datos de los proyectos
                proyectos = cargar_proyectos(n)
                print('\n- Proyectos cargados correctamente.')
            else:
                # Validar nueva carga
                n = validate(0)
                # Cargar datos nuevos de los proyectos
                cargar_nuevo(proyectos, n)
                print('\n- Proyectos nuevos cargados correctamente.')

        elif 2 <= opc <= 7:
            if proyectos is not None:
                if opc == 2:
                    # Copia del arreglo proyecto
                    copia_de_proyectos = proyectos[:]
                    # Mostrar los datos de los proyectos
                    mostrar_proyectos(copia_de_proyectos)

                elif opc == 3:
                    # Numero del proyecto a buscar
                    x = int(input('- Ingrese número del proyecto a buscar: '))
                    # Buscar proyecto con dicho numero
                    buscar_proyecto(proyectos, x)

                elif opc == 4:
                    # Acumular las cantidades de lineas de codigo por lenguaje
                    acumular_codigo_por_lenguaje(proyectos)

                elif opc == 5:
                    # Contar la cantidad de proyectos por años
                    p_por_anios = contar_proyectos_anios(proyectos)
                    # Mostrar la cantidad de proyectos por año
                    mostrar_cant_proyectos_anio(p_por_anios)
                    flag = True

                elif opc == 6:
                    # Cargar vector de proyectos con el mismo lenguaje ingresado
                    v_por_lenguaje = generar_proyectos_por_lenguajes(proyectos)
                    # Ordenar lenguaje por numeros de proyecto
                    v_ordenado = ordenar_proyectos_lenguaje(v_por_lenguaje)
                    # Mostrar los proyectos
                    mostrar_proyectos(v_ordenado)

                elif opc == 7 and flag:
                    # Calcular los años con sus determinadas cantidades de proyectos
                    mayores = calcular_mayor_anio(p_por_anios)
                    # Mostrar los años y sus cantidades
                    mostrar_mayores(mayores)
            else:
                print("Error...No se encontraron datos cargados. Seleccione la opción 1.")

        elif opc == 8:
            print("|" * 160)
            print("\n\n", " " * 68, "PROGRAMA FINALIZADO", "\n\n")
            print("|" * 160)

        else:
            print("\n- Opción inválida. ")


# script principal...
if __name__ == '__main__':
    test()
