def es_vocal(letra):
    vocales = 'aeiou'
    return letra in vocales


clp = cp = 0
primera_vocal = False


text = input('Ingrese un texto a analizar: ')

for car in text:
    if car != ' ' and car != '.':
        clp += 1
        if es_vocal(car):
            primera_vocal = True
    else:
        if clp > 0:
            cp += 1
