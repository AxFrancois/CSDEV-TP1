#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:23:31 2020

@author: axel
"""


def fListeDiviseurs(pNombre):
    """Fonction qui retourne la liste des diviseurs d'un nombre pNombre"""
    valren = []
    liste = list(range(1,pNombre+1))
    for i in liste:
        if pNombre%i == 0:
            valren.append(i)
    
    return valren

nombre1 = 66928
nombre2 = 66992

diviseurs1 = fListeDiviseurs(nombre1)
diviseurs2 = fListeDiviseurs(nombre2)

if sum(diviseurs1) == sum(diviseurs2) and sum(diviseurs1) == (nombre1+nombre2):
    print('{} et {} sont des nombres amicaux'.format(nombre1,nombre2))
else:
    print('non')