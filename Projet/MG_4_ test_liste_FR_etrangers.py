"""
GEORGET Margot
Fichier 4
Fichier de test des fonctions affiche_liste_FR_etrangers et lecture_dans_fichier
contenus dans le fichier 3
"""

from MG_1_def_FR_etrangers import*
from MG_3_liste_FR_etrangers import*

print("\nTest de la fonction affiche_liste_FR_etrangers :")

lis = []
f=FR_etrangers("A", 23,34,2)
lis.append(f)
f=FR_etrangers("B", 43,21,2.45)
lis.append(f)
f=FR_etrangers("C", 12,24,3.34)
lis.append(f)
affiche_liste_FR_etrangers(lis)


print("\nTest de la fonction lecture_dans_fichier :")
print("\nFichier csv1:")
MG_csv1 = "MG_csv1.csv"
FR_etrangers = lecture_dans_fichier (MG_csv1)

affiche_liste_FR_etrangers (FR_etrangers)

print("\nFichier csv2:")
MG_csv2 = "MG_csv2.csv"
FR_etrangers = lecture_dans_fichier (MG_csv2)

affiche_liste_FR_etrangers (FR_etrangers)

print("\nFichier csv3:")
MG_csv3 = "MG_csv3.csv"
FR_etrangers = lecture_dans_fichier (MG_csv3)

affiche_liste_FR_etrangers (FR_etrangers)

print("\nFichier csv4:")
MG_csv4 = "MG_csv4.csv"
FR_etrangers = lecture_dans_fichier (MG_csv4)

affiche_liste_FR_etrangers (FR_etrangers)
