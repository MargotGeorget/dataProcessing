"""
GEORGET Margot
Fichier 6
Ce fichier contient des fonctions permettant de calculer, pour une liste de
valeurs de type FR_etrangers les indicateurs statistiques suivant :
    - le minimum
    - le maximum
    - la moyenne
    - l'écart type
    - la médiane
    - les modalités
    - le(s) mode(s)
    - (J'ai ajouté une fonction maxi qui calcul et retourne le maximum dans une
    liste d'entier pour créer ma fonction mode_liste_FR_etrangers)
"""

from math import*
from MG_1_def_FR_etrangers import*

def valeur_min_liste_FR_etrangers (lis_FR_etrangers):
    """
    Donnée: lis_FR_etrangers: listes de valeur de types FR_etrangers
    Résultat : entier
    Rôle: la fonction recherche et retourne la plus petite valeur de l'annee1
    (2016) parmi les éléments de lis_FR_etrangers
    Préconditions : liste non vide 
    """
    mini = lis_FR_etrangers[0].annee1
    for i in range (1,len(lis_FR_etrangers),1):
        if (lis_FR_etrangers[i].annee1 < mini):
            mini = lis_FR_etrangers[i].annee1
    return mini


def valeur_max_liste_FR_etrangers (lis_FR_etrangers):
    """
    Donnée: lis_FR_etrangers: listes de valeur de types FR_etrangers
    Résultat : entier
    Rôle: la fonction recherche et retourne la plus grande valeur de l'annee1
    (2016) parmi les éléments de lis_FR_etrangers
    Préconditions : liste non vide 
    """
    maxi = lis_FR_etrangers[0].annee1
    for i in range (1,len(lis_FR_etrangers),1):
        if (lis_FR_etrangers[i].annee1 > maxi):
            maxi = lis_FR_etrangers[i].annee1
    return maxi

def moyenne_liste_FR_etrangers (lis_FR_etrangers):
    """
    Donnée: lis_FR_etrangers: listes de valeur de types FR_etrangers
    Résultat : entier
    Rôle: la fonction recherche et retourne la moyenne des éléments de l'annee1
    (2016) de lis_FR_etrangers
    Préconditions : liste non vide 
    """           
    moy = 0
    for i in range (0,len(lis_FR_etrangers),1):
        moy += lis_FR_etrangers[i].annee1
    moy/= len(lis_FR_etrangers)
    return moy

def ecart_type_liste_FR_etrangers (lis_FR_etrangers) :
    """
    Donnée: lis_FR_etrangers: listes de valeur de types FR_etrangers
    Résultat : entier
    Rôle: la fonction calcule et retourne l'écart type des éléments de
    l'annee1(2016) de lis_FR_etrangers
    Préconditions : liste non vide
    """
    m = moyenne_liste_FR_etrangers(lis_FR_etrangers)
    a = 0
    for i in range (0,len(lis_FR_etrangers),1):
        a += (lis_FR_etrangers[i].annee1-m)**2
    a = a/len(lis_FR_etrangers)
    e = sqrt(a)
    return e

def mediane_liste_FR_etrangers (lis_FR_etrangers):
    """
    Donnée: lis_FR_etrangers: liste de valeur de type FR_etrangers
    Résultats: un entier
    Rôle: la fonction recherche et retourne la médiane pour les
    valeurs de l'annee1 de la liste de type FR_etrangers
    Précondition : liste triée et non vide  
    """
    a = len(lis_FR_etrangers)//2
    if (len(lis_FR_etrangers)%2!=0):
        mediane = lis_FR_etrangers[a].annee1
    else:
        mediane = int((lis_FR_etrangers[a-1].annee1 + lis_FR_etrangers[a].annee1)/2)
        #j'utilise la fonction int() afin que la médiane soit une modalité observable
        #c'est à dire un nombre entier puisqu'il s'agis d'un nombre de personne
        #je prend donc la valeur directement inférieur à la mediane 
    return mediane

def modalites_liste_FR_etrangers (lis_FR_etrangers):
    """
    Donnée: lis_FR_etrangers: liste de valeur de type FR_etrangers
    Résultats: liste 
    Rôle: la fonction recherche et retourne les modalités pour les valeurs
    de l'annee1 de la liste de type FR_etrangers
    Précondition : liste triée et liste non vide 
    """
    modalite= []
    modalite.append(lis_FR_etrangers[0].annee1)
    for i in range (1,len(lis_FR_etrangers),1):
        if (lis_FR_etrangers[i].annee1 != lis_FR_etrangers[i-1].annee1) :
            modalite.append(lis_FR_etrangers[i].annee1)
    return modalite

def maxi(lis):
    """
    (fonction créer pour être réutilisé dans la fonction mode)
    Donnée: lis: listes d'entiers
    Résultat : entier
    Rôle: la fonction recherche et retourne la plus grande valeur de lis
    Préconditions : liste non vide 
    """
    maxi = lis[0]
    for i in range (1,len(lis),1):
        if (lis[i] > maxi):
            maxi = lis[i]
    return maxi

def mode_liste_FR_etrangers (lis):
    """
    Donnée: lis : liste de valeur de type FR_etrangers
    Résultat: liste d'entier
    Rôle: calcul et retourne le(s) mode(s) de lis
    Précondition : lis non vide et triée par ordre croissant 
    """
    repe=[]
    rep=1
    
    #je parcours la liste lis et j'ajoute dans la liste repe le nombre de
    #répétitions de chaque valeurs
    for i in range (0,len(lis)-1,1):
        if lis[i].annee1==lis[i+1].annee1:
            rep+=1
        else :
            repe.append(rep)
            rep=1
    repe.append(rep)

    #je créé une liste avec toutes les modalités de lis en utilisant la fonction
    #créée précedement (modalites_liste_FR_etrangers)
    modalites = modalites_liste_FR_etrangers (lis)
    mode=[]
    
    #je prends le maximum des répétitions (liste repe) observées et je recopie dans
    #la liste mode les modalités associées    
    m = maxi(repe)
    for k in range (0,len(repe),1):
        if repe[k]==m:
            mode.append(modalites[k])
    return mode 

                    
