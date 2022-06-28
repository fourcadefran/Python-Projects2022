def es_vocal(letra):
    vocales = 'aeiou'
    return letra in vocales


def porcentaje(total_palabras, palabras_impares):
    if total_palabras == 0:
        porc = 0
    else:
        porc = (palabras_impares * 100) / total_palabras
    return porc


clp = cp = 0
empieza_con = ant = ''
empieza_con_si = 0
cont_impar = 0
tiene_vocal = 0
cont_sola_vocal = 0
cont_ini_fin = 0
cont_cc = 0
menor = 0
acum_letras = 0


text = input('Ingrese el texto a analizar: ')


for car in text:
    if car != ' ' and car != '.':
        clp += 1
        if ant == 's' and car == 'i' and clp == 2:
            empieza_con_si += 1
        if es_vocal(car):
            tiene_vocal += 1
        if clp == 1:
            empieza_con = car
        if ant == 'c' and car == 'c':
            cont_cc += 1
    else:
        if clp > 0:
            cp += 1
            if (car == ' ' or car == '.') and es_vocal(ant) and clp % 2 != 0:
                cont_impar += 1
            if tiene_vocal == 1:
                cont_sola_vocal += 1
            if car == " " or car == '.':
                if empieza_con == ant:
                    cont_ini_fin += 1
            if cp == 1:
                menor = clp
            else:
                if menor > clp:
                    menor = clp
            acum_letras += clp
        clp = 0
        tiene_vocal = 0
    ant = car

print('Palabras que empiecen con si: ', empieza_con_si)
print('Cantidad de palabras que terminan con vocal y tienen una cantidad impar de letras: ', cont_impar)
print('Palabras con una sola vocal: ', cont_sola_vocal)
print('Palabras que empiezan y terminan con la misma letra: ', cont_ini_fin)
print('Palabras que contienen cc: ', cont_cc)
print('Porcentaje que representa el punto b en todas las palabras: ', porcentaje(cp, cont_impar), '%')
print('Longitud mas chica de palabra: ', menor)
if cp == 0:
    promedio = 0
    print('El promedio es igual a: ', 0)
else:
    promedio = acum_letras / cp
    print('El promedio de letras por palabras es igual a: ', promedio)
print('Contador de palabras: ', cp)
