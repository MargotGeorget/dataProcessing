""""
GEORGET Margot
Fichier 3
Gestion de liste de valeur de type FR_etrangers
Ce fihier contient :
    - une fonction de lecture d'un fichier retournant une liste de valeurs de
    type FR_etrangers pour laquelle je me suis aidée des fonctions présentes sur
    Moodle (prog_exemple_lecture_csv) 
    - une fonction permettant d'afficher une liste de valeur de type
    FR_etrangers, pour cette fonction j'appelle la fonction affiche_FR_etrangers
    presente dans le fichier 1 (MG_1_def_FR_etrangers).
    - BONUS : une fonction permettant de sauvegarder une liste de type
    FR_etrangers, écrite manuellement, dans un fichier csv (Prise à partir des
    documents déposés sur Moodle par M.Richomme) 
    - une fonction permmettant de créer et d'afficher une liste comportant 
    toutes les valeurs de l'année 1 (2016) pour les pays d'une liste de type
    FR_etrangers. (ajout personnel)
    - Une fonction permettant de retourner le plus grand indice de la plus grande
    valeur de l'annee 2016 d'une liste de valeur de type FR_etrangers 
    - Une fonction permmettant de trier par ordre croissant des valeurs de l'annee
    2016 d'une lis_FR_etrangerste de type FR_etrangers
"""

from MG_1_def_FR_etrangers import*
import csv

def lecture_dans_fichier( nom_fichier ) :
    """
    Données : nom_fichier : chaîne de caractères
    Rôle : le fichier dont le nom est fourni en paramètre
        est supposé être un fichier au format csv
        avec des ; comme séparateur.
        Chaque ligne du fichier contient un nom de pays, un entier qui désigne
        le nombre de français inscrits dans un pays étranger en 2016 et un autre
        entier pour l'année 2017 et enfin un flottant pour l'évolution entre les
        deux années.
        La fonction lit le fichier et retourne l'information contenue
        sous forme d'une liste de valeur de type FR_etrangers
    """
    
    fichier = open(nom_fichier,"r")
    cr = csv.reader(fichier,delimiter=";")

    fr_etrangers = []
    for ligne in cr:
        pays = ligne[0]
        annee1 = int(ligne[1])
        annee2 = int( ligne[2] )
        evolution = float(ligne[3])
        p = FR_etrangers( pays, annee1, annee2, evolution)
        fr_etrangers.append( p )

    fichier.close()
    return fr_etrangers

def affiche_liste_FR_etrangers (liste_f):
    """
    Données : liste_FR_etrangers : Liste de valeur de type FR_etrangers
    Rôle : Permet d'afficher les caratéristiques de fr_etrangers_pays
    """
    for i in range (0,len(liste_f),1):
        affiche_FR_etrangers(liste_f[i])

def affiche_liste_FR_etrangers_annee1 (liste_f):
    """
    Données : liste_FR_etrangers : Liste de valeur de type FR_etrangers
    Rôle : Permet d'afficher une liste des valeurs de l'annnée 1 (2016) pour
    tout les pays de la liste liste_FR_etrangers
    """
    l=[]
    for i in range (0,len(liste_f),1):
        l+= [liste_f[i].annee1]
    print(l)
             
def sauvegarde_dans_fichier( nom_fichier, lis_FR_etrangers) :
    """
    Données
        nom_fichier : chaîne de caractères
        lis_FR_etrangers : liste de type FR_etrangers
    Rôle
        La fonction enregistre la liste 
        dans le fichier csv de nom nom_fichier
        (1 ligne par pays)
    """
    fichier = open(nom_fichier, 'w')
    
    cw = csv.writer(fichier, dialect="unix", delimiter=';')
    for i in range(0, len(lis_FR_etrangers), 1 ) :
        f = lis_FR_etrangers[i]
        liste = [f.pays, f.annee1, f.annee2, f.evolution]
        cw.writerow( liste )

    fichier.close()

def plus_grand_indice_max_FR_etrangers (lis_FR_etrangers,debut,fin):
    """
    Donnée:
        lis_FR_etrangers: liste de valeur de types FR_etrangers
        début / fin : entier
    Résultat : entier
    Rôle: la fonction recherche et retourne le premier indice de la plus grande
    valeur de l'année1 (2016) parmi les éléments de lis_FR_etrangers d'indices
    compris entre début et fin.
    Préconditions : lis_FR_etrangers non vide
                    0<=debut<=fin<=len(lis_FR_etrangers)
    """
    ind_max = debut
    for i in range (debut+1,fin,1):
        if (lis_FR_etrangers[i].annee1 > lis_FR_etrangers[ind_max].annee1):
            ind_max = i
    return ind_max

def tri_croissant_liste_FR_etrangers (lis_FR_etrangers):
    """
    Donnée/résultat: lis_FR_etrangers: liste de valeur de type FR_etrangers
    Rôle: trie la lis_FR_etrangers de façon croissante à partir des valeurs de
    l'annee1 avec le principe de selection du maximun
    """
    for i in range (len(lis_FR_etrangers),1,-1):
        ind_max = plus_grand_indice_max_FR_etrangers (lis_FR_etrangers,0,i)
        tmp = lis_FR_etrangers[i-1]
        lis_FR_etrangers[i-1]= lis_FR_etrangers[ind_max]
        lis_FR_etrangers[ind_max] = tmp
    affiche_liste_FR_etrangers_annee1(lis_FR_etrangers)


