#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    funciones.py
"""

"""
Ejemplo de uso de funciones
"""

def hola_mundo():
    print 'hola mundo'

# En python una funcion puede devolver varios valores
def devuelve_valores():
    return 1, 3

# Funciones con número variable de parámetros
def parametros_variables(argumento1, argumento2, *varios):
    # Los parámetros *varios serán una tupla
    print 'Tupla de parámetros:', varios
    print 'Argumentos:'
    for argumento in varios:
        print argumento

# Funciones con número variable de parámetros *con nombre*
def kwargs(argumento1, argumento2, **varios):
    # Los parámetros **varios será un diccionario
    # y serán identificados por su nombre (o clave)
    print 'Diccionario de parámetros:', varios
    print 'Argumentos:'
    for item in varios.items():
        print item

if __name__ == '__main__':
    hola_mundo()

    x,y = devuelve_valores()
    print 'x vale %s, y vale %s' % (x,y)

    parametros_variables(1, 2, 3)
    parametros_variables(1, 2, 100, 200, 300)

    kwargs(1, 2, tres=3, cuatro=4)
