"""
GEORGET Margot
Fichier 11
Fichier de test des fonctions plus_grand_indice_max_FR_etrangers et tri_croissant_liste_FR_etrangers
contenus dans le dossier MG_3_liste_FR_etrangers
"""

from MG_1_def_FR_etrangers import*
from MG_3_liste_FR_etrangers import*

#TEST 1:
lis = []
f = FR_etrangers("A", 100 , 345, 1.2)
lis.append(f)
print("Test avec une liste d'un seul élément","\nListe de départ:")
affiche_liste_FR_etrangers_annee1(lis)
print("Indice de la plus petit valeur:",
      plus_grand_indice_max_FR_etrangers(lis,0,len(lis)))
print("Liste triée:")
tri_croissant_liste_FR_etrangers(lis)

#TEST 2:
lis = []
f = FR_etrangers("A", 100 , 345, 1.2)
lis.append(f)
f = FR_etrangers("A", 0 , 345, 1.2)
lis.append(f)
f = FR_etrangers("A", 50 , 345, 1.2)
lis.append(f)
print("\nTest avec une liste ayant le maximum au milieu:","\nListe de départ:")
affiche_liste_FR_etrangers_annee1(lis)
print("Indice de la plus petit valeur:",
      plus_grand_indice_max_FR_etrangers(lis,0,len(lis)))
print("Liste triée:")
tri_croissant_liste_FR_etrangers(lis)

#TEST 3:
lis = []
f = FR_etrangers("A", 1000 , 345, 1.2)
lis.append(f)
f = FR_etrangers("A", 300 , 345, 1.2)
lis.append(f)
f = FR_etrangers("A", 700 , 345, 1.2)
lis.append(f)
f = FR_etrangers("A", 400 , 345, 1.2)
lis.append(f)
f = FR_etrangers("A", 600 , 345, 1.2)
lis.append(f)
f = FR_etrangers("A", 0 , 345, 1.2)
lis.append(f)
print("\nTest avec une liste ayant le maximum à la fin:", "Liste de départ:")
affiche_liste_FR_etrangers_annee1(lis)
print("Indice de la plus petite valeur:",
      plus_grand_indice_max_FR_etrangers(lis,0,len(lis)))
print("Liste triée:")
tri_croissant_liste_FR_etrangers(lis)

#TEST 4:
lis = lecture_dans_fichier("MG_csv1.csv")
print("\nTest avec le fichier csv1:","Liste de départ:")
affiche_liste_FR_etrangers_annee1(lis)
print(plus_grand_indice_max_FR_etrangers(lis,0,len(lis)))
tri_croissant_liste_FR_etrangers(lis)

#TEST 5:
lis = lecture_dans_fichier("MG_csv2.csv")
print("\nTest avec le fichier csv2:","Liste de départ:")
affiche_liste_FR_etrangers_annee1(lis)
print("Indice de la plus petite valeur:",
      plus_grand_indice_max_FR_etrangers(lis,0,len(lis)))
print("Liste triée:")
tri_croissant_liste_FR_etrangers(lis)

#TEST 6:
lis = lecture_dans_fichier("MG_csv3.csv")
print("\nTest avec le fichier csv3:","Liste de départ:")
affiche_liste_FR_etrangers_annee1(lis)
print("Indice de la plus petite valeur:",
      plus_grand_indice_max_FR_etrangers(lis,0,len(lis)))
print("Liste triée:")
tri_croissant_liste_FR_etrangers(lis)

#TEST 7:
lis = lecture_dans_fichier("MG_csv4.csv")
print("\nTest avec le fichier csv4:","Liste de départ:")
affiche_liste_FR_etrangers_annee1(lis)
print("Indice de la plus petite valeur:",
      plus_grand_indice_max_FR_etrangers(lis,0,len(lis)))
print("Liste triée:")
tri_croissant_liste_FR_etrangers(lis)
