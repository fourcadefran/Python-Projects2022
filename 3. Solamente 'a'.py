def porcentaje(cp, cont_a):
    if cp == 0:
        porc = 0
    else:
        porc = (cont_a * 100) / cp
    return porc


def test():
    #Constastes
    max_long = clp = cp = 0
    tiene_a = tiene_vocal = False
    cont_solo_a = 0


    text = input('Ingrese el texto a analizar: ')

    for car in text:
        if car != ' ' and car != '.':
            clp += 1
            if car == 'a':
                tiene_a = True
            if car in 'eiou':
                tiene_vocal = True
        else:
            if clp > 0:
                cp += 1
            if clp > max_long:
                max_long = clp
            if tiene_a and not tiene_vocal:
                cont_solo_a += 1
            tiene_a = tiene_vocal = False
            clp = 0
    print('Palabras con solo a: ', cont_solo_a, ' Palabras')
    print('Porcentaje que representan en el total de palabras: ', porcentaje(cp, cont_solo_a), '%')
    print('Palabra mas larga: ', max_long, ' Letras')
    print('Contador de palabras: ', cp)
    print('Contador de Letras: ', clp)


if __name__ == '__main__':
    test()
