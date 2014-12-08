#!/usr/bin/env python
# _*_ coding:utf-8 _*

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
