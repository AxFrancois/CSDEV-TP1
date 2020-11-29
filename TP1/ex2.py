#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:11:38 2020

@author: axel
"""
import math

def mesImpots(revenu):
    """calculateur impots sur le revenu"""
    valren = 0
    Tranche = [[0,9964,0],[9964,27519,14],[27519,73779,30],[73779,156244,41],[156244,math.inf,45]]
    for i in range(len(Tranche)):
        if revenu > Tranche[i][0] and revenu < Tranche[i][1] :
            valren += (revenu-Tranche[i][0]) * Tranche[i][2] /100
        elif revenu >= Tranche[i][1]:
            valren += (Tranche[i][1]-Tranche[i][0]) * Tranche[i][2] /100
    return valren

"""Batch de test
print(mesImpots(50000))
"""
print(mesImpots(int(input("vos revenus"))))