"""
GEORGET Margot
Fichier 18
Fichier de test de la fonction plus_grand_indice_presence contenu dans le fichier
MG_15_indice_presence.
"""

from MG_3_liste_FR_etrangers import*
from MG_15_indice_presence import*

#TEST 0:
lis_FR_etrangers = []
print("Test0:","\nListe triée:")
tri_croissant_liste_FR_etrangers (lis_FR_etrangers)
print("La valeur 67 est presente à l'indice :",
      plus_grand_indice_presence (67,lis_FR_etrangers))
print("La valeur 82 est presente à l'indice :",
      plus_grand_indice_presence (82,lis_FR_etrangers))

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
print("La valeur 67 est presente à l'indice :",
      plus_grand_indice_presence (67,lis_FR_etrangers))
print("La valeur 82 est presente à l'indice :",
      plus_grand_indice_presence (82,lis_FR_etrangers))

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
print("La valeur 67 est presente à l'indice :",
      plus_grand_indice_presence (67,lis_FR_etrangers))
print("La valeur 82 est presente à l'indice :",
      plus_grand_indice_presence (82,lis_FR_etrangers))

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
print("La valeur 67 est presente à l'indice :",
      plus_grand_indice_presence (67,lis_FR_etrangers))
print("La valeur 82 est presente à l'indice :",
      plus_grand_indice_presence (82,lis_FR_etrangers))

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

print("\nTest4:","\nListe triée:")
tri_croissant_liste_FR_etrangers (lis_FR_etrangers)
print("La valeur 67 est presente à l'indice :",
      plus_grand_indice_presence (67,lis_FR_etrangers))
print("La valeur 82 est presente à l'indice :",
      plus_grand_indice_presence (82,lis_FR_etrangers))

#TEST 5:
lis_FR_etrangers = []
f = FR_etrangers("A", 89 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 12 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 15 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 94 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 82 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 67 , 345, 1.2)
lis_FR_etrangers.append(f)

print("\nTest5:","\nListe triée:")
tri_croissant_liste_FR_etrangers (lis_FR_etrangers)
print("La valeur 67 est presente à l'indice :",
      plus_grand_indice_presence (67,lis_FR_etrangers))
print("La valeur 82 est presente à l'indice :",
      plus_grand_indice_presence (82,lis_FR_etrangers))

#TEST 6:
lis_FR_etrangers = []
f = FR_etrangers("A", 89 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 103 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 80 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 94 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 82 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 67 , 345, 1.2)
lis_FR_etrangers.append(f)

print("\nTest6:","\nListe triée:")
tri_croissant_liste_FR_etrangers (lis_FR_etrangers)
print("La valeur 67 est presente à l'indice :",
      plus_grand_indice_presence (67,lis_FR_etrangers))
print("La valeur 82 est presente à l'indice :",
      plus_grand_indice_presence (82,lis_FR_etrangers))

#TEST AVEC LES FICHIERS CSV:

#TEST 7:
lis_FR_etrangers= lecture_dans_fichier("MG_csv1.csv")
print("\nTest7:","\nListe triée:")
tri_croissant_liste_FR_etrangers (lis_FR_etrangers)
print("La valeur 67 est presente à l'indice :",
      plus_grand_indice_presence (67,lis_FR_etrangers))
print("La valeur 7921 est presente à l'indice :",
      plus_grand_indice_presence (7921,lis_FR_etrangers))

#TEST 8:
lis_FR_etrangers= lecture_dans_fichier("MG_csv2.csv")
print("\nTest8:","\nListe triée:")
tri_croissant_liste_FR_etrangers (lis_FR_etrangers)
print("La valeur 67 est presente à l'indice :",
      plus_grand_indice_presence (67,lis_FR_etrangers))
print("La valeur 82 est presente à l'indice :",
      plus_grand_indice_presence (82,lis_FR_etrangers))

#TEST 9:
lis_FR_etrangers= lecture_dans_fichier("MG_csv3.csv")
print("\nTest9:","\nListe triée:")
tri_croissant_liste_FR_etrangers (lis_FR_etrangers)
print("La valeur 6143 est presente à l'indice :",
      plus_grand_indice_presence (6143,lis_FR_etrangers))
print("La valeur 118331 est presente à l'indice :",
      plus_grand_indice_presence (118331,lis_FR_etrangers))

#TEST 10:
lis_FR_etrangers= lecture_dans_fichier("MG_csv4.csv")
print("\nTest10:","\nListe triée:")
tri_croissant_liste_FR_etrangers (lis_FR_etrangers)
print("La valeur 207 est presente à l'indice :",
      plus_grand_indice_presence (207,lis_FR_etrangers))
print("La valeur 8922 est presente à l'indice :",
      plus_grand_indice_presence (8922,lis_FR_etrangers))
