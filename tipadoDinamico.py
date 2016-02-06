#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    tipadoDinamico.py
"""

"""
Ejemplo de tipado dinámico.
Una variable puede tomar distintos valores en distintos momentos.
"""


def tipado_dinamico():
    # Inicializamos la variable
    x = None
    print '\'x\' vale: %s' % x

    # Ahora es un entero
    x = 1
    print '\'x\' vale: %s' % x

    # Ahora es un string
    x = "uno"
    print '\'x\' vale: %s' % x

    # Tipado dinámico, pero fuertemente tipado.
    # *NO* se puede hacer:
    # x = "uno" + 2
    # TypeError: cannot concatenate 'str' and 'int' objects


if __name__ == '__main__':
    tipado_dinamico()
