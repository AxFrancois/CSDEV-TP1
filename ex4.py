#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 15:08:14 2020

@author: axel
"""

def fTourHanoï(pNetage, pPlotInit, pPlotFinal, pPlotInterMédiaire):
    """Fonction qui indique les coups pour résoudre le casse tête de la tour de Hanoï"""
    if pNetage == 1:
        print('Déplacer le disque du plot {} vers le plot {}'.format(pPlotInit, pPlotFinal))
    else:
        fTourHanoï(pNetage-1, pPlotInit, pPlotInterMédiaire, pPlotFinal)
        print('Déplacer le disque du plot {} vers le plot {}'.format(pPlotInit, pPlotFinal))
        fTourHanoï(pNetage-1, pPlotInterMédiaire, pPlotFinal, pPlotInit)
        
        
fTourHanoï(4,1,3,2)



"""
def fTourHanoï(pNetage,pEtat):
    if pNetage == 1:
        print("Déplacer le disque du plot 1 vers le plot 3")
        pEtat[2].append(pEtat[0][0])
        pEtat[0].remove(pEtat[0][0])
        print(pEtat)
    elif pNetage%2 ==0 :
        print("Déplacer le disque du plot 1 vers le plot 2")
        pEtat[1].append(pEtat[0][0])
        pEtat[0].remove(pEtat[0][0])
        print(pEtat)
        fTourHanoï(pNetage-1,pEtat)
        print("Déplacer le disque du plot 2 vers le plot 3")
        pEtat[2]= [pEtat[1][0]] + pEtat[2]
        pEtat[1].remove(pEtat[1][0])
        print(pEtat)
    else:
        print("Déplacer le disque du plot 1 vers le plot 3")
        pEtat[2].append(pEtat[0][0])
        pEtat[0].remove(pEtat[0][0])
        print(pEtat)
        fTourHanoï(pNetage-1,pEtat)
        print("Déplacer le disque du plot 3 vers le plot 2")
        pEtat[1].append(pEtat[2][0])
        pEtat[2].remove(pEtat[2][0])
        print(pEtat)

Etage = 3
Etat = [list(range(1,Etage+1)), [],[]]
print(Etat)
fTourHanoï(Etage, Etat)
"""