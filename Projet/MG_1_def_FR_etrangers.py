""""
GEORGET Margot
Fichier 1
Ce fichier contient : 
    - une déclaration de nouveau type de données (FR_etrangers)
    - une fonction permettant d'afficher une instance d'enregistrement de
    type FR_etrangers
"""

class FR_etrangers (object):
    def __init__( self,
                 valeur_pays,
                 valeur_annee1,
                 valeur_annee2,
                 valeur_evolution
                 ):
        self.pays = valeur_pays
        self.annee1 = valeur_annee1
        self.annee2 = valeur_annee2
        self.evolution = valeur_evolution 
            
def affiche_FR_etrangers (f):
    """
    Données : f : FR_etrangers : Nombre de français inscrits dans un pays étranger
    donné en 2016 et 2017
    Rôle : Permet d'afficher les caratéristiques de FR_etrangers
    """
    print("\nPays:",f.pays, "\nNombre de Français inscrit en 2016:",
          f.annee1, "\nNombre de Français inscrit en 2017:",
          f.annee2, "\nEvolution Français inscrit entre 2016 et 2017:",
          f.evolution) 
