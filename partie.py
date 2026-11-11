import random
import numpy as np
import time
from carte import Couleur, Valeur, Carte
from joueur import Joueur

class Partie:
    def __init__(self, joueur1, joueur2, joueur3, joueur4, atout = None, premier_joueur = 0, pli_equipeA = [], pli_equipeB = [], scoreA = 0, scoreB = 0, prise = None, belote = None):
        self.cartes = [
            Carte(couleur, valeur)
            for couleur in Couleur
            for valeur in Valeur
        ]
        self.joueurs = [joueur1, joueur2, joueur3, joueur4]
        self.atout = atout
        self.premier_joueur = premier_joueur
        self.pli_equipeA = pli_equipeA
        self.pli_equipeB = pli_equipeB
        self.scoreA = scoreA
        self.scoreB = scoreB
        self.prise = prise
        self.belote = belote


    def melanger(self):
        random.shuffle(self.cartes)


    def distribuer1(self, cartes_par_joueur=5, nombre_joueurs=4):
        
        cartes_restantes = self.cartes.copy()
        for joueur in self.joueurs:
            for i in range (cartes_par_joueur):
                carte_tiree = cartes_restantes.pop()
                joueur.main.append(carte_tiree)
        self.cartes = cartes_restantes
    

    def proposer_carte(self):
        cartes_restantes = self.cartes.copy()
        carte_tiree = cartes_restantes.pop()
        print(f"Carte proposée : {carte_tiree}")
        for i in range(len(self.joueurs)):
            k = (self.premier_joueur + i)%4
            if k == 0:
                choix = input("Garder cette carte ? (o/n) : ").lower().strip()
                if choix == 'o' or choix == 'oui':
                    self.joueurs[0].main.append(carte_tiree)
                    self.atout = carte_tiree.get_couleur()
                    self.cartes = cartes_restantes
                    return True
            else:
                time.sleep(2)
                couleur = carte_tiree.get_couleur()
                prendre = carte_tiree.get_value(couleur)
                if prendre < 0:
                    prendre = 1
                if prendre == 20:
                    prendre = 25
                nb_atout = 0
                for carte in self.joueurs[k].main:
                    if carte.get_couleur() == couleur:
                        val = carte.get_value(couleur)
                        nb_atout+=1
                        if val < 0:
                            val = 1
                        if val == 20:
                            val = 25
                        prendre += val
                cond1 = prendre > 25 and nb_atout >= 3
                cond2 = prendre > 14 and nb_atout >= 4
                if cond1 or cond2:
                    self.joueurs[k].main.append(carte_tiree)
                    self.atout = carte_tiree.get_couleur()
                    self.cartes = cartes_restantes
                    self.prise = self.joueurs[k].equipe
                    print(f'Joueur {k + 1} prend à {couleur}')
                    return True
                else:
                    print(f'Joueur {k + 1} passe')

        for i in range(len(self.joueurs)):
            k = (self.premier_joueur + i)%4
            if k == 0:
                #gérer les cas ou l'IA prend
                couleur_possible = ["Pique", "Coeur", "Trèfle", "Carreau", "n"]
                couleur_possible.remove(carte_tiree.get_couleur())
                continuer = True
                while continuer:
                    choix2 = input(f"Prendre à une autre couleur parmi {couleur_possible}? ").lower().strip()
                    if choix2 != 'n':
                        if choix2 == "p" or choix2 == "pique" or choix2 == "Pique":
                            self.joueurs[0].main.append(carte_tiree)
                            self.atout = "Pique"
                            continuer = False
                            self.cartes = cartes_restantes
                            self.prise = self.joueurs[0].equipe
                            return True
                        elif choix2 == "co" or choix2 == "coeur" or choix2 == "Coeur" or choix2 == "cœur" or choix2 == "Cœur":
                            self.joueurs[0].main.append(carte_tiree)
                            self.atout = "Coeur"
                            continuer = False
                            self.cartes = cartes_restantes
                            self.prise = self.joueurs[0].equipe
                            return True
                        elif choix2 == "t" or choix2 == "trefle" or choix2 == "Trefle" or choix2 == "trèfle" or choix2 == "Trèfle":
                            self.joueurs[0].main.append(carte_tiree)
                            self.atout = "Trefle"
                            continuer = False
                            self.cartes = cartes_restantes
                            self.prise = self.joueurs[0].equipe
                            return True
                        elif choix2 == "ca" or choix2 == "carreau" or choix2 == "Carreau":
                            self.joueurs[0].main.append(carte_tiree)
                            self.atout = "Carreau"
                            continuer = False
                            self.cartes = cartes_restantes
                            self.prise = self.joueurs[0].equipe
                            return True
                        else:
                            print("Erreur de syntaxe")

                    else:
                        continuer = False
            else:
                time.sleep(2)
                couleur_possible = ["Pique", "Coeur", "Trèfle", "Carreau"]
                couleur_possible.remove(carte_tiree.get_couleur())
                for couleur in couleur_possible:
                    prendre = 0
                    nb_atout = 0
                    for carte in self.joueurs[k].main:
                        if carte.get_couleur() == couleur:
                            val = carte.get_value(couleur)
                            nb_atout+=1
                            if val < 0:
                                val = 1
                            if val == 20:
                                val = 25
                            prendre += val
                    cond1 = prendre > 25 and nb_atout >= 3
                    cond2 = prendre > 14 and nb_atout >= 4
                    if cond1 or cond2:
                        self.joueurs[k].main.append(carte_tiree)
                        self.atout = couleur
                        self.cartes = cartes_restantes
                        self.prise = self.joueurs[k].equipe
                        print(f'Joueur {k + 1} prend à {couleur}')
                        return True
                print(f'Joueur {k + 1} passe une seconde fois')
                
        self.cartes = [
            Carte(couleur, valeur)
            for couleur in Couleur
            for valeur in Valeur
        ]
        for joueur in self.joueurs:
            joueur.main = []
        return False



    def distribuer2(self, nombre_joueurs=4):
        cartes_restantes = self.cartes.copy()
        for joueur in self.joueurs:
            dame_b = False
            roi_b = False
            carte_a_donner = 3
            if len(joueur.main) == 6:
                carte_a_donner = 2
                self.prise = joueur.equipe
            for i in range (carte_a_donner):
                carte_tiree = cartes_restantes.pop()
                if carte_tiree.get_value(self.atout) == 3 and carte_tiree.get_couleur() == self.atout:
                    dame_b = True
                if carte_tiree.get_value(self.atout) == 4 and carte_tiree.get_couleur() == self.atout:
                    roi_b = True
                joueur.main.append(carte_tiree)
            if dame_b and roi_b:
                belote = joueur.id - 1
        self.cartes = cartes_restantes

    
    def carte_maitre(self, cartes):
        if self.atout == None:
            return None, None
        if len(cartes) == 0:
            return None, None
        carte1 = cartes[0]
        j_maitre = self.premier_joueur
        joueur = 0
        carte = carte1
        for e in cartes:
            if e.get_couleur() == carte.get_couleur() and e.get_value(self.atout) > carte.get_value(self.atout):
                carte = e
                j_maitre = (self.premier_joueur + joueur)%4
            elif e.get_couleur() != carte1.get_couleur() and e.get_couleur() == self.atout:
                if carte.get_couleur() == self.atout and e.get_value(self.atout) > carte.get_value(self.atout):
                    carte = e
                    j_maitre = (self.premier_joueur + joueur)%4
                elif carte.get_couleur() != self.atout:
                    carte = e
                    j_maitre = (self.premier_joueur + joueur)%4
            joueur += 1

        return carte, j_maitre


    def pli(self):
        premier_j = self.premier_joueur
        carte_jouee = []
        atout_pli = self.atout
        for i in range (4):
            carte_m, joueur_m = self.carte_maitre(carte_jouee)
            joueur_selectionne = (premier_j +i)%4
            carte_choisie = self.joueurs[joueur_selectionne].jouer(atout_pli, carte_m, joueur_m, carte_jouee, self.pli_equipeA, self.pli_equipeB, self.prise)
            carte_jouee.append(carte_choisie)
            print(f"Pli en cours :")
            print("-" * 50)
            for j in range(len(carte_jouee)):
                if carte_jouee[j].get_value(self.atout) == 3 and carte_jouee[j].get_couleur() == self.atout and self.belote == (premier_j + j)%4 :
                    print(f"Joueur {(premier_j + j)%4 + 1} a posé {carte_jouee[j]}, Belote")
                elif carte_jouee[j].get_value(self.atout) == 4 and carte_jouee[j].get_couleur() == self.atout and self.belote == (premier_j + j)%4 :
                    print(f"Joueur {(premier_j + j)%4 + 1} a posé {carte_jouee[j]}, Belote")
                else:
                    print(f"Joueur {(premier_j + j)%4 + 1} a posé {carte_jouee[j]}")
            print("-" * 50)
        carte_m, joueur_m = self.carte_maitre(carte_jouee)
        self.premier_joueur = joueur_m
        if joueur_m == 0 or joueur_m == 2:
            for carte in carte_jouee:
                self.pli_equipeA.append(carte)
        if joueur_m == 1 or joueur_m == 3:
            for carte in carte_jouee:
                self.pli_equipeB.append(carte)
        return carte_jouee, joueur_m


    def compte_point(self, joueur_m):
        score_jeu_A = 0
        score_jeu_B = 0

        for carte in self.pli_equipeA:
            val = carte.get_value(self.atout)
            if val<0:
                val = 0
            score_jeu_A += val

        for carte in self.pli_equipeB:
            val = carte.get_value(self.atout)
            if val<0:
                val = 0
            score_jeu_B += val
        
        if joueur_m == 0 or joueur_m == 2:
            score_jeu_A += 10
        if joueur_m == 1 or joueur_m == 3:
            score_jeu_B += 10
        
        if self.belote == 0 or self.belote == 2:
            score_jeu_A += 20
        if self.belote == 1 or self.belote == 3:
            score_jeu_B += 20


        print(f"L'équipe A a gagné {score_jeu_A}")
        print(f"L'équipe B a gagné {score_jeu_B}")

        if  self.prise == 'A':
            if len(self.pli_equipeB) == 0:
                score_jeu_A = 252
                score_jeu_B = 0
                if self.belote == 0 or self.belote == 2:
                    score_jeu_A += 20
                if self.belote == 1 or self.belote == 3:
                    score_jeu_B += 20
            if score_jeu_B >= score_jeu_A:
                score_jeu_A = 0
                score_jeu_B = 162
                if self.belote == 0 or self.belote == 2:
                    score_jeu_A += 20
                if self.belote == 1 or self.belote == 3:
                    score_jeu_B += 20

        if  self.prise == 'B':
            if len(self.pli_equipeA) == 0:
                score_jeu_A = 0
                score_jeu_B = 252
                if self.belote == 0 or self.belote == 2:
                    score_jeu_A += 20
                if self.belote == 1 or self.belote == 3:
                    score_jeu_B += 20
            if score_jeu_B >= score_jeu_A:
                score_jeu_A = 162
                score_jeu_B = 0
                if self.belote == 0 or self.belote == 2:
                    score_jeu_A += 20
                if self.belote == 1 or self.belote == 3:
                    score_jeu_B += 20
        
        self.belote = None

        print(f"L'équipe A marque {score_jeu_A}")
        print(f"L'équipe B marque {score_jeu_B}")
        time.sleep(2)
        self.scoreA += score_jeu_A
        self.scoreB += score_jeu_B
        self.pli_equipeA = []
        self.pli_equipeB = []
        self.prise = None        
        self.cartes = [
            Carte(couleur, valeur)
            for couleur in Couleur
            for valeur in Valeur
        ]


