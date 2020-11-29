#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 15:54:40 2020

@author: axel
"""

def fConjectureSyracuseSuite(pNombre):
    """Fonction qui retourne la suite de la conjecture de Syracuse pour un nombre n"""
    suite=[pNombre]
    while pNombre != 1:
        if pNombre % 2 == 0:
            pNombre = pNombre/2
        else:
            pNombre = pNombre*3 +1
        suite.append(int(pNombre))
    return suite

def fConjectureSyracuseAltitudeMax(pNombre):
    """Fonction qui retourne l'altitude maximum dans la suite de la conjecture de Syracuse pour un nombre n"""
    liste = fConjectureSyracuseSuite(pNombre)
    return max(liste)

def fConjectureSyracuseTpsVol(pNombre):
    """Fonction qui retourne la durée de vol dans la suite de la conjecture de Syracuse pour un nombre n"""
    liste = fConjectureSyracuseSuite(pNombre)
    return len(liste)

print(fConjectureSyracuseSuite(500))
print(fConjectureSyracuseAltitudeMax(500))
print(fConjectureSyracuseTpsVol(500))

maxtempsvol = 1
maxalt = 1
for i in range(1,1001):
    if fConjectureSyracuseTpsVol(i) > fConjectureSyracuseTpsVol(maxtempsvol):
        maxtempsvol = i
    if fConjectureSyracuseAltitudeMax(i) > fConjectureSyracuseAltitudeMax(maxalt):
        maxalt = i
        
print(maxtempsvol, maxalt)
        