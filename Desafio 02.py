# Datos

n = int(input('Ingrese el valor de N: '))

print('Valor de N: ', n)

orbita = None,
longitud = 0
promedio = acum = cont = 0
mayor = 0

# Procesos
# si n es par -> n / 2
# si n es impar -> 3n + 1
resultado = []

while n != 1:

    resultado.append(n)
    acum += n
    cont += 1

    if n % 2 == 0:
        n = n / 2

    elif n % 2 != 0:
        n = 3 * n + 1

    print(acum, cont)

resultado.append(n)
acum += n
cont += 1

print(acum, cont)

# Resultados

print('Orbita de n (sin incluir a n):', resultado)
print('Longitud de la Orbita de n: ', len(resultado))
if cont > 0:
    promedio = acum / cont
    print('Promedio de los valores de la orbita: ', promedio)
else:
    print('No se pudo realizar el calculo del promedio ya que no se ingresaron numeros. ')

print('el mayor es: ', max(resultado))
