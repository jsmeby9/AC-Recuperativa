# -*- coding: utf-8 -*-
import random
"""
# Parte 2

Generamos el data
"""

data= [b'_/\xef\xb9\x8b\\_ \n(\xd2\x82`_\xc2\xb4)\n<,\xef\xb8\xbb\xe2\x95\xa6\xe2\x95\xa4\xe2\x94\x80 \xd2\x89 - -\n_/\xef\xb9\x8b\\_',
       b'(\xe2\x95\xad\xe0\xb2\xb0_\xe2\x8a\x99)',
       b'(\xc2\xa6\xea\x92\x89[\xe2\x96\x93\xe2\x96\x93]',
       b'\xef\xbc\xbc\xef\xbc\x88\xef\xbc\xbe\xe2\x96\xbd\xef\xbc\xbe\xef\xbc\x89\xef\xbc\x8f']

"""Intentamos decodificar la información"""

def enumerar(string):
  return "{} - {}".format(0, string)


with open("output_2.txt", "w", encoding="UTF-8") as file:
  file.write(enumerar(data[random.randint(0,3)].decode("UTF-8")))

print('Esto fue creado un día')