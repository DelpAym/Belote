import random
import numpy as np
from carte import Couleur, Valeur, Carte
from partie import Partie
from joueur import Joueur

class Main:
    def __init__(self):
        self.joueur1 = Joueur(1, 'A')
        self.joueur2 = Joueur(2, 'B')
        self.joueur3 = Joueur(3, 'A')
        self.joueur4 = Joueur(4, 'B')


    def play(self):
        """
        Cette fonction permet de lancer et gérer l'avancement d'une partie.
    
        Args:
            cartes_par_joueur (int): Le nombre de carte à distribuer par joueur, 5 par défaut.
            nombre_joueurs (int): Le nombre de joueur.
        """
        jeu = Partie(self.joueur1, self.joueur2, self.joueur3, self.joueur4)
        try:
            score_max = int(input(f"En combien de point souaitez vous jouer la partie? ").strip())
        except ValueError:
            print("Veuillez saisir un nombre valide.")
            return self.play()
        premier_joueur = 0
        while jeu.scoreA < score_max and jeu.scoreB < score_max:
            jeu.melanger()
            jeu.distribuer1()
            jeu.joueurs[0].afficher_main()
            test = jeu.proposer_carte()
            if test == True:
                jeu.distribuer2()
                for i in range (1,9):
                    cs, j_m = jeu.pli()
                jeu.compte_point(j_m)
            premier_joueur += 1
            jeu.premier_joueur = premier_joueur
        if jeu.scoreA > jeu.scoreB:
            print("-" * 70)
            print(f"Félicitation, vous avez gagné avec {jeu.scoreA} contre {jeu.scoreB} pour l'autre équipe !!!")
            print("-" * 70)
        if jeu.scoreA < jeu.scoreB:
            print("-" * 70)
            print(f"Dommage, vous avez perdu avec {jeu.scoreA} contre {jeu.scoreB} pour l'autre équipe...")
            print("-" * 70)
        if jeu.scoreA == jeu.scoreB:
            print("-" * 70)
            print(f"C'est rare mais c'est un match nul...")
            print("-" * 70)
        



if __name__ == '__main__':
    jouer = Main()
    jouer.play()