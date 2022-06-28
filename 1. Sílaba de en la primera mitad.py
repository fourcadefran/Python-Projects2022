

def is_digit(letra):
    digit = '0123456789'
    return letra in digit


def test():

    have_digit_flag = False
    have_digit = 0
    clp = cp = 0
    cont_3 = cont_6 = cont_plus_6 = 0
    max_long = 0
    ant = ''
    have_de = 0
    middle = pos = 0




    text = input('Ingrese el texto a analizar: ')


    for car in text:

        if car != ' ' and car != '.':

            if is_digit(car):
                have_digit_flag = True
            else:
                clp += 1
            middle = clp // 2
            if car == 'd':
                pos = clp
            if ant == 'd' and car == 'e' and pos <= middle:
                have_de += 1
        else:
            if clp > 0:
                cp += 1
            if have_digit_flag:
                have_digit += 1
                have_digit_flag = False
            if clp <= 3:
                cont_3 += 1
            if 4 < clp < 6:
                cont_6 += 1
            if clp > 6:
                cont_plus_6 += 1
            if clp > max_long:
                max_long = clp
            clp = 0
        ant = car
    print('Palabras que contenian al menos un digito: ', have_digit)
    print('Palabras con 3 o menos letras: ', cont_3)
    print('Palabras entre 4 y 6 letras: ', cont_6)
    print('Palabras con mas de 6 letras: ', cont_plus_6)
    print('Palabra con la longitud mas larga: ', max_long)
    print('Palabras que contiene "de" en la primera mitad de la palabra: ', have_de)
    print('Contador de palabras: ', cp)
    print('Contador de letras: ', clp)


if __name__ == '__main__':
    test()
