"""
GEORGET Margot
Fichier 19
Fichier de test de la fonction nombre_occurence contenu dans le fichier
MG_15_indice_presence.
"""

from MG_3_liste_FR_etrangers import*
from MG_15_indice_presence import*

#TEST 0:
lis_FR_etrangers = []
print("Test0:","\nListe triée:")
tri_croissant_liste_FR_etrangers (lis_FR_etrangers)
print("La valeur 67 est répétée :",
      nombre_occurence (67,lis_FR_etrangers),"fois")
print("La valeur 82 est répétée :",
      nombre_occurence (82,lis_FR_etrangers),"fois")
#TEST 1:
lis_FR_etrangers = []
f = FR_etrangers("A", 89 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 67 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 67 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 94 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 67 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 2 , 345, 1.2)
lis_FR_etrangers.append(f)

print("\nTest1 avec une liste où 67 est répété 3 fois:","\nListe triée:")
tri_croissant_liste_FR_etrangers (lis_FR_etrangers)
print("La valeur 67 est répétée :",
      nombre_occurence (67,lis_FR_etrangers),"fois")
print("La valeur 82 est répétée :",
      nombre_occurence (82,lis_FR_etrangers),"fois")

#TEST 2:
lis_FR_etrangers = []
f = FR_etrangers("A", 89 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 67 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 67 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 94 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 82 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 67 , 345, 1.2)
lis_FR_etrangers.append(f)

print("\nTest2 67 répété 3 fois et placé en début de liste triée:",
      "\nListe triée:")
tri_croissant_liste_FR_etrangers (lis_FR_etrangers)
print("La valeur 67 est répétée :",
      nombre_occurence (67,lis_FR_etrangers),"fois")
print("La valeur 82 est répétée :",
      nombre_occurence (82,lis_FR_etrangers),"fois")

#TEST 3:
lis_FR_etrangers = []
f = FR_etrangers("A", 89 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 67 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 67 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 94 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 82 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 67 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 89 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 67 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 67 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 13 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 82 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 17 , 345, 1.2)
lis_FR_etrangers.append(f)

print("\nTest3:","\nListe triée:")
tri_croissant_liste_FR_etrangers (lis_FR_etrangers)
print("La valeur 67 est répétée :",
      nombre_occurence (67,lis_FR_etrangers),"fois")
print("La valeur 82 est répétée :",
      nombre_occurence (82,lis_FR_etrangers),"fois")

#TEST 4:
lis_FR_etrangers = []
f = FR_etrangers("A", 82 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 67 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 67 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 82 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 82 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 67 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 82 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 82 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 67 , 345, 1.2)
lis_FR_etrangers.append(f)

print("\nTest4 82 répété 5 fois et placé en fin de liste triée:","\nListe triée:")
tri_croissant_liste_FR_etrangers (lis_FR_etrangers)
print("La valeur 67 est répétée :",
      nombre_occurence (67,lis_FR_etrangers),"fois")
print("La valeur 82 est répétée :",
      nombre_occurence (82,lis_FR_etrangers),"fois")

#TEST 5:
FR_etrangers = lecture_dans_fichier ("MG_csv1.csv")
print("\nTest5:","\nListe triée:")
tri_croissant_liste_FR_etrangers (FR_etrangers)
print("La valeur 7921 est presente à l'indice :",
      nombre_occurence (7921,FR_etrangers))
print("La valeur 82 est presente à l'indice :",
      nombre_occurence (82,FR_etrangers))

#TEST 6:
FR_etrangers = lecture_dans_fichier ("MG_csv2.csv")
print("\nTest6:","\nListe triée:")
tri_croissant_liste_FR_etrangers (FR_etrangers)
print("La valeur 45 est presente à l'indice :",
      nombre_occurence (45,FR_etrangers))
print("La valeur 207 est presente à l'indice :",
      nombre_occurence (207,FR_etrangers))

#TEST 7:
FR_etrangers = lecture_dans_fichier ("MG_csv3.csv")
print("\nTest7:","\nListe triée:")
tri_croissant_liste_FR_etrangers (FR_etrangers)
print("La valeur 45 est presente à l'indice :",
      nombre_occurence (45,FR_etrangers))
print("La valeur 82 est presente à l'indice :",
      nombre_occurence (82,FR_etrangers))

#TEST 8:
FR_etrangers = lecture_dans_fichier ("MG_csv4.csv")
print("\nTest8:","\nListe triée:")
tri_croissant_liste_FR_etrangers (FR_etrangers)
print("La valeur 1074 est presente à l'indice :",
      nombre_occurence (1074,FR_etrangers))
print("La valeur 0 est presente à l'indice :",
      nombre_occurence (0,FR_etrangers))
