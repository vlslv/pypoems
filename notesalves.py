#!/usr/bin/python
# -*- coding: utf-8 -*-
#title                  :notesalves.py
#description            :poema "No te salves" de Mario Benedetti
#author                 :vlslv
#date                   :20140523
#version                :0.1
#usage                  :python notesalves.py
#notes                  :
#python_version         :2.7.5
#==============================================================================

titulo = 'NO TE SALVES'
verso1 = ['te quedes inmovil \nal borde del camino',\
        'congeles el júbilo',\
        'quieras con desgana',\
        'te salves ahora \nni nunca',\
        'te salves',\
        'te llenes de calma',\
        'reserves del mundo \nsólo un rincón tranquilo',\
        'dejes caer los párpados \npesados como juicios',\
        'te quedes sin labios',\
        'te duermas sin sueño',\
        'te pienses sin sangre',\
        'te juzgues sin tiempo\n']
condicion = 'pero si \npese a todo \nno puedes evitarlo'
verso2 = ['congelas el júbilo',\
        'quieres con desgana',\
        'te salvas ahora',\
        'te llenas de calma',\
        'reservas del mundo \nsólo un rincón tranquilo',\
        'dejas caer los párpados \npesados como juicios',\
        'te secas sin labios',\
        'te duermes sin sueño',\
        'te piensas sin sangre',\
        'te juzgas sin tiempo',
        'te quedas inmóvil \nal borde del camino',\
        'te salvas']

final = 'entonces \nno te quedes conmigo\n'
if (titulo == 'NO TE SALVES'):
    print titulo
    for i in range(len(verso1)):
        print 'no',verso1[i]
if (condicion == 'pero si \npese a todo \nno puedes evitarlo'):
    print condicion
    for i in range(len(verso2)):
        print 'y',verso2[i]
if (verso2[len(verso2)-1] == 'te salvas'):
    print final                                                                                              15,1          B
