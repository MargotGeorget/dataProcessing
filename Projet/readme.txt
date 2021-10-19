Mon jeu de données présente l'état des inscriptions au registre des Français établis hors de France en 2016 et 2017 pour les 100 pemiers pays pris dans l'ordre alphabétique. Je donne donc à mon objet le nom de FR_etrangers.

Fichier 1 : MG_1_def_FR_etrangers
Ce fichier contient les fonctions suivantes : 
- Déclaration de nouveau type de données (1. Remise1) 
- Fonctions qui affiche une instance d'enregistrement de FR_etrangers (2. Remise1) 

Fichier 2: MG_2_test_def_FR_etrangers 
Ce fichier contient des tests des fonctions présentes dans le fichier 1. (3. Remise1)

Fichier 3: MG_3_liste_FR_etrangers 
Ce fichier contient plusieurs fonctions permettant de gérer des listes de type FR_etrangers:
- une fonction qui permet d'afficher une liste de ce type (4. Remise1)
- une fonction qui permet de créer une liste à partir d'un fichier csv (6. remise1)
- une fonction qui permet de sauvegarder une liste écrite manuellement dans un fichier csv (BONUS remise2)
- une fonction qui permet de créer et d'afficher une liste comportant toutes les valeurs de l'année 1 (2016) pour les pays d'une liste de type FR_etrangers afin de m'en servir pour afficher les valeurs sur lesquels je travaille dans mon fichier test_calcul_indicateurs_statistiques. Ce qui me permet de verifier les calculs plus facilement. (ajout personnel)
- une fonction qui permet de retourner le plus grand indice de la plus grande valeur (annee1) de la liste (utilisée pour la fonction suivante) 
- une fonction qui permet de trier par ordre croissant des valeurs (annee1) une liste (Remise3) 

Fichier 4: MG_4_test_liste_FR_etrangers
Ce fichier contient des tests des 2 premières fonctions du fichier 3 :
- affiche_liste_FR_etrangers (modifié entre la remise1 et la remise2 afin de tester cette fonction sur tous les fichiers csv)
- lecture_dans_fichier
(5.7. Remise1)

Fichier 5: MG_5_test_sauvegarde_dans_fichier
Ce fichier contient des tests de la fonction BONUS sauvegarde_dans_fichier (BONUS remise2) (modifié entre la remise2 et la remise3 afin de tester si le fichier sauvegardé pouvait être lu par la fonction lecture_dans_fichier) 

Fichier 6: MG_6_calcul_indicateurs_statistiques
Ce fichier contient des fonctions permettant de calculer, pour une liste de
valeurs de type FR_etrangers les indicateurs statistiques suivants :
Remise 2: 
- le minimum 
- le maximum
- la moyenne
- l'écart type
Remise 3: 
- la médiane
- les modalités
- le(s) mode(s) 
- (et une fonction maxi qui retourne le maximum pour les listes d'entier, utilisé pour calculer le mode)

Les fichier suivant sont uniquement des fichiers de test pour les indicateurs statistiques : 
(modifié entre la remise2 et la remise3 pour mettre les tests de chaques fonctions dans un fichier différent)
Fichier 7: MG_7_test_minimum_liste
Fichier 8: MG_8_test_maximum_liste
Fichier 9: MG_9_test_moyenne_liste
Fichier 10: MG_10_test_ecart_type_liste
Fichier 12: MG_12_test_mediane_liste
Fichier 13: MG_13_test_modalites_liste 
Fichier 14: MG_14_test_mode_liste

Fichier 11: MG_test_tri_liste_FR_etrangers
Ce fichier contient des test de la fonction de tri (remise3) 

Fichier 15: MG_15_indice_presence 
Ce fichier contient :
- une fonction qui permet de retourner l'indice de presence d'une valeur (prise en paramètre) dans une liste de valeurs de type FR_etrangers  
- une fonction qui permet de retourner le plus petit indice de presence d'une valeur (prise en paramètre) dans une liste de valeurs de type FR_etrangers  
- une fonction qui permet de retourner le plus grand indice de presence d'une valeur (prise en paramètre) dans une liste de valeurs  de type FR_etrangers
- une fonction qui permet de retourner le nombre d'occurence d'une valeur (prise en paramètre) dans une liste de valeurs de type FR_etrangers
(chaque fonction traite uniquement des valeurs de l'année1 de FR_etrangers) 

Fichier de test des fonctions du fichier 15: 
Fichier 16 : MG_16_test_indice_presence
Fichier 17: MG_17_test_plus_petit_indice_presence
Fichier 18: MG_18_test_plus_grand_indice_presence
Fichier 19: MG_19_test_nombre_occurence 