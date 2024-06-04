#!/usr/bin/python
# -*- coding: utf-8 -*-
#title                  :ayjose.py
#description    :poema  Canción Cubana de Guillermo Cabrera Infante
#author                 :vlslv
#date                   :20140524
#version                :0.1
#usage                  :python ayjose.py
#notes                  :
#python_version :2.7.5
#==============================================================================
##########0123456789ABCDEFG
titulo = '¡Ay, José, así no se puede!'
serie=reversed([3,9,17,21,26])
print('\n'+titulo+'\n')
for i in serie:
    if (i == 21):
        print(titulo[0:19]+titulo[8:9]+titulo[-1])
    else:
        print(titulo[0:i]+titulo[-1])
print('\n')
