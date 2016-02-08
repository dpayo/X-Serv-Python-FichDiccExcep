#!/usr/bin/python
# -*- coding: utf-8 -*-

# hola, hola
dic={}

fd = open('/etc/passwd', 'r')

lineas = fd.readlines()
fd.close()

for linea in lineas:
    elementos = linea.split(':')
    usr=elementos[0]
    bash = elementos[-1][:-1]
    dic[usr]=bash;

print("Introduzca el usuario: ")
usuario = raw_input()

try:
    print dic[usuario]
except KeyError:
    print "Error user not found..."
