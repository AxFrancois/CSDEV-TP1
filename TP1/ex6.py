#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:14:23 2020

@author: axel
"""

def tricolore(n):
    """Fonction qui retourne si un nombre n est tricolore ou pas"""
    valren = True
    nsquare = str(n**2)
    for i in nsquare:
        if i not in ["1","4","9"]:
            valren = False
    return valren

def tous_les_tricolores(N):
    """Fonction qui retourne l'ensemble des nombres tricolores d'une liste N"""
    valren = []
    for i in N:
        if tricolore(i) == True:
            valren.append(i)
    return valren
    
print(tricolore(16))
print(tous_les_tricolores(list(range(1,1001))))
    