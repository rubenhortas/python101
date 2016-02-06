#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    clase.py
"""

"""
Ejemplo de clase en python
"""


class SuperHeroe:
    nombre = None
    batmovil_disponible = True
    batcoptero_disponible = False

    def __init__(self):
        self.nombre = 'Batman'
        print 'Mi nombre es %s' % self.nombre
        self.compi = 'Robin'

    def desvelar_compi(self):
        print 'Mi compañero es %s' % self.compi

    def conducir(self):
        if self.batcoptero_disponible:
            print "Al batcóptero!"
        else:
            if self.batmovil_disponible:
                print "Al batmóvil!"
            else:
                print "A batpatas!"

    @staticmethod
    def __identidad_secreta():
        print 'Soy Bruce Wayne :('


if __name__ == '__main__':
    mi_batman = SuperHeroe()
    mi_batman.desvelar_compi()
    mi_batman.conducir()

    # Name mangling para acceder a métodos "privados"
    mi_batman._SuperHeroe__identidad_secreta()
