#EJERCICIO 1

x = input("ingreseel dia de la semana:  ", )
if x == "lunes":
    print("desayuno de manzanas y peras")
elif x == "martes":
    print("desayuno de jugo de leche,platano,fresa,leche")
elif x == "miercoles":
    print("desayuno de yogurt y cereales")
else:
    print("desayuno de papaya")



#EJERCICIO 2

import statistics
from collections import Counter
numeros = []
for i in range(20):
    numero = float(input("Ingrese el número {}: ".format(i+1)))
    numeros.append(numero)
media = statistics.mean(numeros)
print("La media es:", media)
mediana = statistics.median(numeros)
print("La mediana es:", mediana)
conteo = Counter(numeros)
frecuencia = conteo.most_common(1)[0][0]
print("Su frecuencia es:", frecuencia)



