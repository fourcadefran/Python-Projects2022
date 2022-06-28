def es_vocal(letra):
    vocales = 'aeiou'
    return letra in vocales


def test():
    clp = cp = 0
    tiene_m = tiene_b = False
    cont_mb = 0
    ant = ''
    cont_p = 0
    empieza_con = ''
    cont_fin = 0
    text = input('Ingrese el texto a analizar: ')

    for car in text:
        if car != ' ' and car != '.':
            clp += 1
            if clp >= 3:
                if car == 'm':
                    tiene_m = True
                if car == 'b':
                    tiene_b = True
            if clp == 2 and ant == 'p' and es_vocal(car):
                cont_p += 1
            if clp == 1:
                empieza_con = car
        else:
            if clp > 0:
                cp += 1
            if tiene_m and tiene_b:
                cont_mb += 1
            if empieza_con == ant:
                cont_fin += 1
            clp = 0
            tiene_b = tiene_m = False
        ant = car
    print('Cantidad de palabras que tienen m y b: ', cont_mb)
    print('Palabras que empiezan con p seguidas de una vocal: ', cont_p)
    print('palabras que empieza y termina con la misma letra: ', cont_fin)
    print('Contador de palabras: ', cp)
    print('Contador de letras: ', clp )


if __name__ == '__main__':
    test()
