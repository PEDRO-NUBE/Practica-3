# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:08:19 2024

@author: HP
"""

"""
Práctica 03 - Introducción a Listas y Operadores Condicionales
Alumno: Quispe Yncarroque
"""

#===========================================
# 1. INTRODUCCIÓN A LISTAS
#===========================================
# Las listas son colecciones ordenadas de valores
# Los valores pueden ser de cualquier tipo: enteros, cadenas, booleanos, listas, etc.

# Ejemplo de cadena de texto y acceso a un carácter específico
texto = "Hola mundo Python"
primer_caracter = texto[0]
print("Primer caracter:", primer_caracter)

# Método split: convierte una cadena en una lista de palabras
lista_palabras = texto.split()
print("Lista de palabras:", lista_palabras)

# Ejemplo de una lista con elementos de diferentes tipos de datos
lista_mixta = [1, "Python", 3.14, True, [1, 2, 3]]
print("Lista con diferentes tipos:", lista_mixta)

#===========================================
# 2. OPERADORES Y CONDICIONALES
#===========================================
# Operadores de comparación y uso en condiciones:
# == : Igual a
# != : Diferente
# <  : Menor que
# >  : Mayor que
# <= : Menor igual que
# >= : Mayor igual que

# Condicional simple (if): Verifica si el número es positivo
numero = 10
if numero > 0:
    print("El número es positivo")

# Condicional if-else: Verifica si el número es par o impar
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# Condicional if-elif-else: Verifica si el número es negativo, cero, o positivo
if numero < 0:
    print("El número es negativo")
elif numero == 0:
    print("El número es cero")
else:
    print("El número es positivo")
