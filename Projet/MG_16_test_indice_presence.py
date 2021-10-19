"""
GEORGET Margot
Fichier 16
Fichier de test de la fonction indice_presence contenu dans le fichier
MG_15_indice_presence.
"""

from MG_15_indice_presence import*

#TEST 1:
lis_FR_etrangers = []
print("Test1 sur liste vide:","\nListe triée:")
tri_croissant_liste_FR_etrangers (lis_FR_etrangers)
print("La valeur 45 est presente à l'indice :",
      indice_presence (45,lis_FR_etrangers))
print("La valeur 82 est presente à l'indice :",
      indice_presence (82,lis_FR_etrangers))

#TEST 2:
lis_FR_etrangers = []
f = FR_etrangers("A", 13 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 256 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 67 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 54 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 78 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 82 , 345, 1.2)
lis_FR_etrangers.append(f)

print("\nTest2:","\nListe triée:")
tri_croissant_liste_FR_etrangers (lis_FR_etrangers)
print("La valeur 45 est presente à l'indice :",
      indice_presence (45,lis_FR_etrangers))
print("La valeur 82 est presente à l'indice :",
      indice_presence (82,lis_FR_etrangers))

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
f = FR_etrangers("A", 67 , 345, 1.2)
lis_FR_etrangers.append(f)
f = FR_etrangers("A", 2 , 345, 1.2)
lis_FR_etrangers.append(f)

print("\nTest3:","\nListe triée:")
tri_croissant_liste_FR_etrangers (lis_FR_etrangers)
print("La valeur 67 est presente à l'indice :",
      indice_presence (67,lis_FR_etrangers))
print("La valeur 82 est presente à l'indice :",
      indice_presence (82,lis_FR_etrangers))

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
      indice_presence (67,lis_FR_etrangers))
print("La valeur 82 est presente à l'indice :",
      indice_presence (82,lis_FR_etrangers))

#TEST 5:
FR_etrangers = lecture_dans_fichier ("MG_csv1.csv")
print("\nTest5:","\nListe triée:")
tri_croissant_liste_FR_etrangers (FR_etrangers)
print("La valeur 45 est presente à l'indice :",
      indice_presence (45,FR_etrangers))
print("La valeur 82 est presente à l'indice :",
      indice_presence (82,FR_etrangers))

#TEST 6:
FR_etrangers = lecture_dans_fichier ("MG_csv2.csv")
print("\nTest6:","\nListe triée:")
tri_croissant_liste_FR_etrangers (FR_etrangers)
print("La valeur 45 est presente à l'indice :",
      indice_presence (45,FR_etrangers))
print("La valeur 207 est presente à l'indice :",
      indice_presence (207,FR_etrangers))

#TEST 7:
FR_etrangers = lecture_dans_fichier ("MG_csv3.csv")
print("\nTest7:","\nListe triée:")
tri_croissant_liste_FR_etrangers (FR_etrangers)
print("La valeur 45 est presente à l'indice :",
      indice_presence (45,FR_etrangers))
print("La valeur 82 est presente à l'indice :",
      indice_presence (82,FR_etrangers))

#TEST 8:
FR_etrangers = lecture_dans_fichier ("MG_csv4.csv")
print("\nTest8:","\nListe triée:")
tri_croissant_liste_FR_etrangers (FR_etrangers)
print("La valeur 1074 est presente à l'indice :",
      indice_presence (1074,FR_etrangers))
print("La valeur 2208 est presente à l'indice :",
      indice_presence (2208,FR_etrangers))
