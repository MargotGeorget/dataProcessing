"""
GEORGET Margot
Fichier 13
Ce fichier contient des tests de la fonction modalites_liste_FR_etrangers_liste_FR_etrangers
"""

from MG_3_liste_FR_etrangers import*
from MG_6_calcul_indicateurs_statistiques import*

#TEST SUR DES LISTES RENTREES MANUELLEMENT :

#TEST 1 : 
lis_FR_etrangers = []
f = FR_etrangers("A", 100 , 345, 1.2)
lis_FR_etrangers.append(f)
print("\nTest1:","\nTest sur la liste (1 seul valeur):")
tri_croissant_liste_FR_etrangers(lis_FR_etrangers)
print ("Modalité de la liste:", modalites_liste_FR_etrangers(lis_FR_etrangers))

#TEST 2 : 
lis_FR_etrangers = []
f = FR_etrangers("A", 100 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 0 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 50 , 345, 1.2)
lis_FR_etrangers.append(f)
print("\nTest2:","\nTest sur la liste (sans doublons):")
tri_croissant_liste_FR_etrangers(lis_FR_etrangers)
print ("Modalité de la liste:", modalites_liste_FR_etrangers(lis_FR_etrangers))

#TEST 3 : 
lis_FR_etrangers = []
f = FR_etrangers("A", 700 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 0 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 700 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 400 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 400 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 0 , 345, 1.2)
lis_FR_etrangers.append(f)
print("\nTest3:","\nTest sur la liste (plusieurs doublons):")
tri_croissant_liste_FR_etrangers(lis_FR_etrangers)
print ("Modalité de la liste:", modalites_liste_FR_etrangers(lis_FR_etrangers))

#TEST 4 : 
lis_FR_etrangers = []
f = FR_etrangers("A", 13 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 13 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 13 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 13 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 13 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 13 , 345, 1.2)
lis_FR_etrangers.append(f)
print("\nTest4:","\nTest sur la liste (toutes les valeurs identiques):")
tri_croissant_liste_FR_etrangers(lis_FR_etrangers)
print ("Modalité de la liste:", modalites_liste_FR_etrangers(lis_FR_etrangers))

#TEST SUR DES LISTES TIREES D'UN FICHIER CSV:

#TEST 5:
MG_csv1 = "MG_csv1.csv"
FR_etrangers = lecture_dans_fichier (MG_csv1)
print("\nTest5 à partir du fichier csv1:","\nTest sur la liste:")
tri_croissant_liste_FR_etrangers(FR_etrangers)
print ("Modalité de la liste:", modalites_liste_FR_etrangers(FR_etrangers))

#TEST 6: 
MG_csv2 = "MG_csv2.csv"
FR_etrangers = lecture_dans_fichier (MG_csv2)
print("\nTest6 à partir du fichier csv2:","\nTest sur la liste:")
tri_croissant_liste_FR_etrangers(FR_etrangers)
print ("Modalité de la liste:", modalites_liste_FR_etrangers(FR_etrangers))

#TEST 7:
MG_csv3 = "MG_csv3.csv"
FR_etrangers = lecture_dans_fichier (MG_csv3)
print("\nTest7 à partir du fichier csv3:","\nTest sur la liste:")
tri_croissant_liste_FR_etrangers(FR_etrangers)
print ("Modalité de la liste:", modalites_liste_FR_etrangers(FR_etrangers))

#TEST 8:
MG_csv4 = "MG_csv4.csv"
FR_etrangers = lecture_dans_fichier (MG_csv4)
print("\nTest8 à partir du fichier csv4:","\nTest sur la liste:")
tri_croissant_liste_FR_etrangers(FR_etrangers)
print ("Modalité de la liste:", modalites_liste_FR_etrangers(FR_etrangers))

