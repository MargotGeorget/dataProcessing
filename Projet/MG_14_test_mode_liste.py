from MG_1_def_FR_etrangers import*
from MG_3_liste_FR_etrangers import*
from MG_6_calcul_indicateurs_statistiques import*

#TEST 1:
lis= []
f= FR_etrangers("A",23,0,0)
lis.append(f)
print("Test1: Liste avec une seule valeur:")
tri_croissant_liste_FR_etrangers(lis)
print("Mode:",mode_liste_FR_etrangers(lis))

#TEST 2:
lis= []
f= FR_etrangers("A",23,0,0)
lis.append(f)
f= FR_etrangers("A",23,0,0)
lis.append(f)
f= FR_etrangers("A",55,0,0)
lis.append(f)
f= FR_etrangers("A",55,0,0)
lis.append(f)
f= FR_etrangers("A",67,0,0)
lis.append(f)
f= FR_etrangers("A",67,0,0)
lis.append(f)
print("\nTest2: Liste avec toutes les valeurs répétées 2 fois:")
tri_croissant_liste_FR_etrangers(lis)
print("Mode:",mode_liste_FR_etrangers(lis))

#TEST3:
lis= []
f= FR_etrangers("A",23,0,0)
lis.append(f)
f= FR_etrangers("A",23,0,0)
lis.append(f)
f= FR_etrangers("A",23,0,0)
lis.append(f)
f= FR_etrangers("A",23,0,0)
lis.append(f)
f= FR_etrangers("A",23,0,0)
lis.append(f)
f= FR_etrangers("A",23,0,0)
lis.append(f)
print("\nTest3: Liste avec toutes les valeurs identiques:")
tri_croissant_liste_FR_etrangers(lis)
print("Mode:",mode_liste_FR_etrangers(lis))

#TEST4:
lis= []
f= FR_etrangers("A",23,0,0)
lis.append(f)
f= FR_etrangers("A",24,0,0)
lis.append(f)
f= FR_etrangers("A",55,0,0)
lis.append(f)
f= FR_etrangers("A",55,0,0)
lis.append(f)
f= FR_etrangers("A",55,0,0)
lis.append(f)
f= FR_etrangers("A",67,0,0)
lis.append(f)
print("\nTest4: Liste avec 1 seul mode qui apparait 3 fois:")
tri_croissant_liste_FR_etrangers(lis)
print("Mode:",mode_liste_FR_etrangers(lis))

#TEST5:
lis= []
f= FR_etrangers("A",23,0,0)
lis.append(f)
f= FR_etrangers("A",23,0,0)
lis.append(f)
f= FR_etrangers("A",23,0,0)
lis.append(f)
f= FR_etrangers("A",55,0,0)
lis.append(f)
f= FR_etrangers("A",67,0,0)
lis.append(f)
f= FR_etrangers("A",67,0,0)
lis.append(f)
print("\nTest5: Liste avec un mode au début de la liste:")
tri_croissant_liste_FR_etrangers(lis)
print("Mode:",mode_liste_FR_etrangers(lis))

#TEST6:
lis= []
f= FR_etrangers("A",23,0,0)
lis.append(f)
f= FR_etrangers("A",23,0,0)
lis.append(f)
f= FR_etrangers("A",23,0,0)
lis.append(f)
f= FR_etrangers("A",55,0,0)
lis.append(f)
f= FR_etrangers("A",55,0,0)
lis.append(f)
f= FR_etrangers("A",55,0,0)
lis.append(f)
print("\nTest6: Liste avec 2 modes qui sont aussi les 2 modalités de la liste:")
tri_croissant_liste_FR_etrangers(lis)
print("Mode:",mode_liste_FR_etrangers(lis))

#TEST AVEC LES FICHIERS CSV:

#TEST7:
MG_csv1 = "MG_csv1.csv"
FR_etrangers = lecture_dans_fichier (MG_csv1)
print("\nTest7 à partir du fichier csv1:","\nTest sur la liste:")
tri_croissant_liste_FR_etrangers(FR_etrangers)
print ("Mode:", mode_liste_FR_etrangers(FR_etrangers))

#TEST8: 
MG_csv2 = "MG_csv2.csv"
FR_etrangers = lecture_dans_fichier (MG_csv2)
print("\nTest8 à partir du fichier csv2:","\nTest sur la liste:")
tri_croissant_liste_FR_etrangers(FR_etrangers)
print ("Mode:", mode_liste_FR_etrangers(FR_etrangers))

#TEST9:
MG_csv3 = "MG_csv3.csv"
FR_etrangers = lecture_dans_fichier (MG_csv3)
print("\nTest9 à partir du fichier csv3:","\nTest sur la liste:")
tri_croissant_liste_FR_etrangers(FR_etrangers)
print ("Mode:", mode_liste_FR_etrangers(FR_etrangers))

#TEST10:
MG_csv4 = "MG_csv4.csv"
FR_etrangers = lecture_dans_fichier (MG_csv4)
print("\nTest10 à partir du fichier csv4:","\nTest sur la liste:")
tri_croissant_liste_FR_etrangers(FR_etrangers)
print ("Mode:", mode_liste_FR_etrangers(FR_etrangers))


