#!/usr/bin/python3
# -*- coding: utf-8 -*-
#title                  :gastronomia.py
#description            :Reconstrucción del poema Gastronomia de Juan Gonzalo Rose usando un codigo genetico para descubrir passwords, ver el libro Genetic Algorithms de Clinton Sheppard
#author                 :vlslv
#date                   :20220420
#version                :0.1
#usage                  :python3 gastronomia.py
#notes                  :
#python_version :3.8.5
#==============================================================================

geneSet = " aábcdeéfghiíjklmnoópqrstuúvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?.:,;\n"
target = " Para comerse un hombre en el Perú\n hay que sacarle antes las espinas,\n las vísceras heridas,\n los residuos de llanto y de tabaco.\n Purificarlo a fuego lento.\n Cortarlo en pedacitos\n y servirlo a la mesa con los ojos cerrados,\n mientras se va pensando\n que nuestro buen gobierno nos protege.\n Luego:\n afirmar que los poetas exageran.\n Y como buen final:\n tomarse un trago."

import random
import datetime

def generate_parent(length):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    return ''.join(genes)

def get_fitness(guess):
    return sum(1 for expected, actual in zip(target, guess) if expected == actual)

def mutate(parent):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate \
        if newGene == childGenes[index] \
        else newGene
    return ''.join(childGenes)
    
def display(guess):
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(guess)
    #print("\n")
    print("{0}\n\n{1}\t{2}\n".format(guess, fitness, str(timeDiff)))
    #print("\n")

random.seed()
startTime = datetime.datetime.now()
bestParent = generate_parent(len(target))
bestFitness = get_fitness(bestParent)
display(bestParent)

while True:
    child = mutate(bestParent)
    childFitness = get_fitness(child)
    if bestFitness >= childFitness:
        continue
    display(child)
    if childFitness >= len(bestParent):
        break
    bestFitness = childFitness
    bestParent = child
