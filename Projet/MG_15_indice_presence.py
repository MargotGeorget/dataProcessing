"""
GEORGET Margot
Fichier 15
Ce fichier contient :
    - Une fonction qui retourne l'indice d'une valeurs parmis les valeur de l'année
    2016 d'une liste de type FR_etrangers
    - Une fonction qui retourne le plus petit indice d'une valeur parmis les valeurs
    de l'année 2016 d'une liste de type FR_etrangers
    - Une fonction qui retourne le plus grand indice d'une valeur parmis les valeurs
    de l'année 2016 d'une liste de type FR_etrangers
"""

from MG_1_def_FR_etrangers import*
from MG_3_liste_FR_etrangers import*
from MG_6_calcul_indicateurs_statistiques import*

def indice_presence (valeur, lis_FR_etrangers):
    """
    Données: lis_FR_etrangers : une liste de valeurs de type FR_etrangers
             valeur : un entier
    Rôle: retourne l'indice de 'valeur' si valeur est dans lis_FR_etrangers
    (pour l'année1),
          retourne -1 sinon
    Resultat : un entier
    Précondition : lis_FR_etrangerstriée par ordre croissant 
    """
    g = 0
    d = len(lis_FR_etrangers)-1
    trouve = False
    a=-1
    while (g<=d) and not trouve:
        m= (g+d)//2
        if lis_FR_etrangers[m].annee1 == valeur :
            trouve = True
            a=m
        else:
            if valeur < lis_FR_etrangers[m].annee1:
                d= m-1
            else :
                g = m+1
    return a

def plus_petit_indice_presence (valeur, lis_FR_etrangers):
    """
    Données: lis_FR_etrangers : une liste de valeurs de type FR_etrangers
             valeur : un entier
    Rôle: retourne le plus petit indice de 'valeur' si valeur est dans lis_FR_etrangers
    (pour l'année1),
          retourne -1 sinon
    Resultat : un entier
    Précondition : lis_FR_etrangers triée par ordre croissant 
    """
    g = 0
    d = len(lis_FR_etrangers)-1
    trouve = False
    a=-1
    while (g<=d) and not trouve:
        m= (g+d)//2
        if lis_FR_etrangers[m].annee1 == valeur and lis_FR_etrangers[m-1].annee1!=valeur :
            trouve = True
            a=m
        else:
            if valeur < lis_FR_etrangers[m].annee1 or valeur==lis_FR_etrangers[m].annee1:
                d= m-1
            else :
                g = m+1
    return a

def plus_grand_indice_presence (valeur, lis_FR_etrangers):
    """
    Données: lis_FR_etrangers : une liste de valeurs de type FR_etrangers
             valeur : un entier
    Rôle: retourne le plus grand indice de 'valeur' si valeur est dans lis_FR_etrangers
    (pour l'année1),
          retourne -1 sinon
    Resultat : un entier
    Précondition : lis_FR_etrangers triée par ordre croissant
    """
    g = 0
    d = len(lis_FR_etrangers)-1
    trouve = False
    a=-1
    while (g<=d) and not trouve:
        m= (g+d)//2
        if m==len(lis_FR_etrangers)-1:
            trouve=True
            a=m
        elif lis_FR_etrangers[m].annee1 == valeur and lis_FR_etrangers[m+1].annee1!=valeur:
            trouve = True
            a=m
        else:
            if valeur < lis_FR_etrangers[m].annee1:
                d= m-1
            else :
                g = m+1
    return a

def nombre_occurence (valeur,lis_FR_etrangers):
    """
    Données: lis_FR_etrangers : liste de valeur de type FR_etrangers
             valeur : un entier
    Résultat: un entier
    Rôle : retourne le nombre d'occurence de 'valeur' dans lis_FR_etrangers
    Préconditions : liste triée par ordre croissant et non vide
    """
    a= plus_grand_indice_presence(valeur,lis_FR_etrangers)
    b= plus_petit_indice_presence(valeur,lis_FR_etrangers)
    if(a==-1):
        nb= a-b
    else:
        nb=(a+1)-b
    return nb
