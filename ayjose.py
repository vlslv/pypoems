#!/usr/bin/python
# -*- coding: utf-8 -*-
#title                  :ayjose.py
#description    :poema  ¡Ay, José, así no se puede! de Cabrera Infante
#author                 :vlslv
#date                   :20140524
#version                :0.1
#usage                  :python ayjose.py
#notes                  :
#python_version :2.7.5
#==============================================================================

titulo = '¡Ay, José, así no se puede!'
serie=reversed([4,11,17,20,23,29])
print '\n'+titulo+'\n'
for i in serie:
    if (i == 23):
        print titulo[0:21]+titulo[8:11]+titulo[len(titulo)-1]
    else:
        print titulo[0:i]+titulo[len(titulo)-1]
print '\n'
