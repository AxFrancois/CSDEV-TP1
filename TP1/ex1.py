#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 13:35:22 2020

@author: axel
"""

def fIsBissextile(pYear):
    """Vérife que pYear est une année bissextile, return True ou False"""
    if ((str(pYear)[-2:] != "00") and (int(pYear) % 4 == 0)) or (int(pYear) % 400 == 0):
        valren = True
    else:
        valren = False
    return valren

def fNbJourMois(pMois, pYear):
    """retourne le nombre de jour dans un mois pMois donné d'une année pYear donné"""
    mois31j = ["01","03","05","07","08","10","12"]
    mois30j = ["04","06","09","11"]
    valren = 0
    if str(pMois) == "02":
        if fIsBissextile(pYear) == True:
            valren = 29
        else:
            valren = 28
    elif str(pMois) in mois31j:
        valren = 31
    elif str(pMois) in mois30j:
        valren = 30
    return valren
        
def fIsDateValide(pJour, pMois, pYear):
    """vérifie qu'une date soit valide, return True ou False"""
    valren = False
    if int(pMois) <= 12 and int(pMois) >= 1:
        NbJour = fNbJourMois(pMois, pYear)
        if int(pJour) <= NbJour and int(pJour) >= 1:
            valren = True
        else:
            valren = False
    else:
        valren = False
    return valren

print("Entrez la date avec le format JJ/MM/AAAA")
date = str(input())
result = fIsDateValide(date[:2], str(date[3:5]), date[6:10])
if result == True:
    print("Date valide")
else:
    print("Date non valide")

"""#Batch de test    
print(fIsBissextile(2000))
print(fIsBissextile(2020))
print(fIsBissextile(1900))
print(fNbJourMois("02",1900))
print(fNbJourMois("02",2000))
print(fNbJourMois("08",1900))
print(fNbJourMois("10",2000))
print(fIsDateValide(25,"12",2000))
print(fIsDateValide(31,"12",2000))
print(fIsDateValide(1,"01",2000))
print(fIsDateValide(29,"02",2000))
print(fIsDateValide(10,"13",2000))
"""