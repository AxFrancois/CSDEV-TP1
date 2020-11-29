#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:35:28 2020

@author: axel
"""

def multiplication(pA, pB):
    """calulateur d'un produit de matrice AB"""
    if len(pB) == len(pA[0]):
        print("dimensions compatibles")
    else:
        print("dimensions incompatibles")
        return -1
    #NombreTermes = len(pA) * len(pB[0])
    NombreTermesParLigne = len(pB[0]) 
    NombreColonnes = len(pA)
    
    valren = []
    for j in range(NombreColonnes):
        ligne = []
        for i in range(NombreTermesParLigne):
            somme = 0
            for k in range(len(pB)):
                somme += pA[j][k] * pB[k][i]
            ligne.append(somme)
        valren.append(ligne)
    return valren
                
    
"""batch test"""
B = [[0,1,2],
     [1,0,1],
     [2,1,0]]
A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

C = multiplication(A,B)
print(C)