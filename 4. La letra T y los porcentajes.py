def porcentaje(cp, cont_t):
    if cp == 0:
        porc = 0
    else:
        porc = (cont_t*100) / cp
    return porc


def test():
    #constantes
    clp = cp = 0
    clp_anterior = 0
    tiene_t = pal_solo_t = 0
    pal_ant_mas_letras = 0
    empieza_c = False
    cont_c = 0

    text = input('Insgresar el texto a analizar: ')

    for car in text:
        if car != ' ' and car != '.':
            clp += 1
            if car == 't':
                tiene_t += 1
            if clp == 1 and car == 'c':
                empieza_c = True
        else:
            if clp > 0:
                cp += 1
            if tiene_t == 1:
                pal_solo_t += 1
            if cp == 1:
                clp_anterior = clp
            else:
                if clp > clp_anterior:
                    pal_ant_mas_letras += 1
                clp_anterior = clp
            if empieza_c and clp % 2 == 0:
                cont_c += 1
            empieza_c = False
            tiene_t = 0
            clp = 0
    print('Palabras con una sola t: ', pal_solo_t)
    print('Palabras donde la cantidad de letras de la anterior es mas grande: ', pal_ant_mas_letras)
    print('Palabra con letras par y empieza con c: ', cont_c)
    print('Porcentaje Punto 1: ', porcentaje(cp, pal_solo_t), '%')
    print('Contador de palabras: ', cp)
    print('Contador de letras: ', clp)


if __name__ == '__main__':
    test()
