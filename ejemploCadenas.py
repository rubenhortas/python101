#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    EjemploCadenas.py
"""

"""
Breve ejemplo de las operaciones más utilizadas
al trabajar con cadenas
"""

def concatenar_cadenas():
    """
    Muestra varias formas de concatenar cadenas en python
    """
    cadena1 = "hola mundo"
    cadena2 = "hello world"

    print "Ejemplo de concatenación de cadenas"
    print

    # Esta forma es útil sobre todo cuando queremos imprimir
    # una colección (tuplas, listas, diccionarios...)
    print "3-", cadena1, "significa :", cadena2
    coordenadas = (1,2)
    print "4- Mis coordenadas (x,y) son:", coordenadas

    # Esta es la forma menos eficiente
    cadena_resultado = "1- " + cadena2 + " significa: " + cadena1
    print(cadena_resultado)

    # Formas más eficientes:

    # Con especificadores de formato
    print "2- %s significa: %s" % (cadena2, cadena1)

    # Con string.format
    cadena_resultado = ("5- {0} significa: {1}").format(cadena2, cadena1)

    print cadena_resultado
    print

def convertir_str_en_lista():
    """
    Muestra como convertir una cadena en una lista
    string.split(s[, sep[, maxsplit]])
    """
    cadena = "mi cadena es increiblemente larga y la quiero dividir"

    print "Ejemplo de convertir una cadena en una lista"

    # Separamos la cadena por los espacios
    lista_cadena = cadena.split(" ")

    print lista_cadena
    print

def eliminar_caracteres():
    """
    Muestra como eliminar caracteres al principio o al final de
    una cadena
    string.lstrip(s[, chars])
    string.rstrip(s[, chars])
    """

    print "Ejemplo de eliminar carácteres al principio o al final de una cadena"

    cadena = "Ahola mundoZ"
    # Borramos la 'A' de la izquierda
    # Si no se espicificase un carácter se borrarían los espacios
    cadena = cadena.lstrip('A')

    # Borramos la 'Z' de la derecha
    # Si no se espicificase un carácter se borrarían los espacios
    cadena = cadena.rstrip('Z')

    print cadena
    print

# Reemplazar caracteres
def reemplazar_caracteres():
    """
    Ejemplo de reemplazar carácteres en una cadena.
    string.replace(s, old, new[, maxreplace])
    """

    cadena  = "este es mi último programa en python"

    print "Ejemplo de reemplazar carácteres en una cadena"

    cadena = cadena.replace('último', 'primer')

    print(cadena)
    print

if __name__ == '__main__':
    concatenar_cadenas()
    convertir_str_en_lista()
    eliminar_caracteres()
