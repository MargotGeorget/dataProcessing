"""
GEORGET Margot
Fichier BONUS
Ce fichier contient un programme de test pour la fonction sauvegarde_dans_fichier
contenu dans le fichier 3 (MG_3_liste_FR_etrangers) 
"""

from MG_3_liste_FR_etrangers import *

liste = []
liste.append( FR_etrangers("A", 10 , 50 , 3) )
liste.append( FR_etrangers("B", 20 , 20 , 3) )
liste.append( FR_etrangers("C", 30 , 20 , 3) )
liste.append( FR_etrangers("D", 40 , 60 , 3) )
liste.append( FR_etrangers("E", 50 , 30 , 3) )
liste.append( FR_etrangers("F", 60 , 70 , 3) )

nom_fichier = "MG_csvBONUS.csv"
sauvegarde_dans_fichier( nom_fichier, liste)

FR_etrangers = lecture_dans_fichier(nom_fichier)
affiche_liste_FR_etrangers (FR_etrangers)
