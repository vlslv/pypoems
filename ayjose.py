#!/usr/bin/python
# -*- coding: utf-8 -*-
#title                  :ayjose.py
#description            :poema  Canción Cubana de Guillermo Cabrera Infante
#author                 :vlslv
#date                   :20140524/20240604
#version                :0.5
#usage                  :python3 ayjose.py
#notes                  :
#python_version         :3.10
#==============================================================================
##########012345678901234567890123456##############
titulo = '¡Ay, José, así no se puede!'
serie=reversed([3,9,17,21,26])
print('\n'+titulo+'\n')
for i in serie:
    if (i == 21):
        print(titulo[0:19]+titulo[8:9]+titulo[-1])
    else:
        print(titulo[0:i]+titulo[-1])
print('\n')
