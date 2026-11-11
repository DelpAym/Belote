import random
import numpy as np
import time
from carte import Couleur, Valeur, Carte


class Joueur():
    def __init__(self, id, equipe):
        from partie import Partie
        self.id = id
        self.main = []
        self.equipe = equipe
    
    def __str__(self):
        return (f"Joueur {self.id} de l'équipe {self.equipe}")
    
    def trier_main(self):
        ordre_couleurs = list(Couleur)
        ordre_valeurs = list(Valeur)

        self.main.sort(
            key=lambda carte: (
                ordre_couleurs.index(carte.couleur),
                ordre_valeurs.index(carte.valeur)
            )
        )

    def afficher_main(self):
        self.trier_main()
        print("\nVotre main :")
        print("-" * 35)

        for i, carte in enumerate(self.main, start=1):
            print(f"{i}. {carte}")

        print("-" * 35)
    
    def afficher_main_jouable(self, atout, carte_m, joueur_m, cartes_posees = None, ):
        self.trier_main()
        cartes_main = []
        cartes_jouables = []
        if cartes_posees == None:
            for i, carte in enumerate(self.main, start=1):
                c = f"{i} : {carte}"
                cartes_main.append(c)
                cartes_jouables.append(carte)
            return cartes_main, cartes_jouables
        else:
            if cartes_posees[0].get_couleur() == atout:
                atout_en_main = 0
                atouts_jouables = []
                atouts_jouables2 = []
                atout_jouable = 0
                for i, carte in enumerate(self.main, start=1):
                    if carte.get_couleur() == atout :
                        atout_en_main += 1
                        if carte.get_value(atout) > carte_m.get_value(atout):
                            atout_jouable += 1
                            c = f"\033[1m{i} : {carte}\033[0m"
                            atouts_jouables.append(c)
                            atouts_jouables2.append(carte)
                        else:
                            c = f"\033[90m{i} : {carte}\033[0m"
                            atouts_jouables.append(c)
                        c = f"\033[1m{i} : {carte}\033[0m"
                        cartes_main.append(c)
                        cartes_jouables.append(carte)
                    else:
                        c = f"\033[90m{i} : {carte}\033[0m"
                        atouts_jouables.append(c)
                        cartes_main.append(c)
                if atout_en_main == 0:
                    cartes_main = []
                    for i, carte in enumerate(self.main, start=1):
                        c = f"\033[1m{i} : {carte}\033[0m"
                        cartes_main.append(c)
                        cartes_jouables.append(carte)
                    return cartes_main, cartes_jouables
                if atout_jouable > 0:
                    return atouts_jouables, atouts_jouables2
                else:
                    return cartes_main, cartes_jouables

            else:
                atout_en_main = 0
                atouts_jouables = []
                atouts_jouables2 = []
                couleur_en_main = 0
                for i, carte in enumerate(self.main, start=1):
                    if carte.get_couleur() == cartes_posees[0].get_couleur() :
                        couleur_en_main += 1
                        c = f"\033[1m{i} : {carte}\033[0m"
                        cartes_main.append(c)
                        cartes_jouables.append(carte)
                    else:
                        c = f"\033[90m{i} : {carte}\033[0m"
                        cartes_main.append(c)
                if couleur_en_main == 0:
                    cartes_main = []
                    cartes_main2 = []
                    if joueur_m + 1 == self.id + 2 or joueur_m + 1 == self.id - 2:
                        for i, carte in enumerate(self.main, start=1):
                            c = f"\033[1m{i} : {carte}\033[0m"
                            cartes_main.append(c)
                            cartes_main2.append(carte)
                        return cartes_main, cartes_main2
                    else:
                        for i, carte in enumerate(self.main, start=1):
                            if carte.get_couleur() == atout :
                                atout_en_main += 1
                                if carte_m.get_couleur() != atout:
                                    c = f"\033[1m{i} : {carte}\033[0m"
                                    atouts_jouables.append(c)
                                    atouts_jouables2.append(carte)

                                elif carte.get_value(atout) > carte_m.get_value(atout) and carte_m.get_couleur() == atout:
                                    c = f"\033[1m{i} : {carte}\033[0m"
                                    atouts_jouables.append(c)
                                    atouts_jouables2.append(carte)

                                else : 
                                    c = f"\033[90m{i} : {carte}\033[0m"
                                    atouts_jouables.append(c)
                                c = f"\033[1m{i} : {carte}\033[0m"
                                cartes_main.append(c)
                                cartes_main2.append(carte)
                            else : 
                                c = f"\033[90m{i} : {carte}\033[0m"
                                cartes_main.append(c)
                                atouts_jouables.append(c)

                        if atout_en_main == 0:
                            cartes_main = []
                            cartes_main2 = []
                            for i, carte in enumerate(self.main, start=1):
                                c = f"\033[1m{i} : {carte}\033[0m"
                                cartes_main.append(c)
                                cartes_main2.append(carte)
                            return cartes_main, cartes_main2
                if len(atouts_jouables) > 0:
                    return atouts_jouables, atouts_jouables2
                else:
                    return cartes_main, cartes_jouables





    def jouer(self, atout, carte_m, joueur_m, carte_posee = None, pli_equipeA = None, pli_equipeB = None, prise = None):
        cartes = []
        cartes_jouables = []
        if len(carte_posee) == 0 or carte_posee == None:
            cartes, cartes_jouables = self.afficher_main_jouable(atout, carte_m, joueur_m)
        else:
            cartes, cartes_jouables = self.afficher_main_jouable(atout, carte_m, joueur_m, carte_posee)
        if self.id == 1:
            print(f"Joueur {self.id}, quelle carte jouer parmi :")
            for carte in cartes:
                print(f"  {carte}")
            try:
                choix = int(input(f"Votre choix (entre 1 et {len(cartes)}): ").strip())
            except ValueError:
                print("Veuillez saisir un nombre valide.")
                return self.jouer(atout, carte_m, joueur_m, carte_posee, pli_equipeA, pli_equipeB, prise)
            if not 0 < choix < len(cartes) + 1 :
                print("Veuillez saisir un nombre valide.")
                return self.jouer(atout, carte_m, joueur_m, carte_posee, pli_equipeA, pli_equipeB, prise)
            if self.main[choix-1] not in cartes_jouables:
                print("Carte impossible à jouer.")
                return self.jouer(atout, carte_m, joueur_m, carte_posee, pli_equipeA, pli_equipeB, prise)
            else :
                carte_jouee = self.main[choix-1]
                self.main.pop(choix-1)
                return carte_jouee
        else:
            time.sleep(2)
            compte_atout_jouer = 0
            compte_atout_main = 0
            compte_atout_pli = 0
            cartes_jouees = pli_equipeA + pli_equipeB

            for carte in cartes_jouees:
                if carte.get_couleur()==atout:
                    compte_atout_jouer += 1
            for carte in  self.main:
                if carte.get_couleur()==atout:
                    compte_atout_main += 1
            if carte_posee != None:
                for carte in  carte_posee:
                    if carte.get_couleur()==atout:
                        compte_atout_main += 1
        
        if len(cartes_jouables) == 1:
            carte_jouee = cartes_jouables[0]
            self.main.remove(carte_jouee)
            return carte_jouee
        
        elif carte_posee == None and prise == self.equipe and (compte_atout_jouer + compte_atout_main) < 8 and compte_atout_main > 0:
            carte_jouee = cartes_jouables[0]
            for i in range(1, len(cartes_jouables)):
                if cartes_jouables[i].get_couleur() == atout and cartes_jouables[i].get_value() > carte_jouee:
                    carte_jouee = cartes_jouables[i]
            self.main.remove(carte_jouee)
            return carte_jouee
        
        elif carte_posee == None and prise == self.equipe and (compte_atout_jouer + compte_atout_main) == 8:
            if compte_atout_main == len(cartes_jouables):
                carte_jouee = cartes_jouables[0]
                self.main.remove(carte_jouee)
                return carte_jouee
            else:
                carte_jouee = cartes_jouables[0]
                for i in range(1, len(cartes_jouables)):
                    if cartes_jouables[i].get_couleur() != atout and cartes_jouables[i].get_value()== 11:
                        carte_jouee = cartes_jouables[i]
                self.main.remove(carte_jouee)
                return carte_jouee
                
        else:
            i = random.randint(0, len(cartes_jouables) - 1) 
            carte_jouee = cartes_jouables[i]
            self.main.remove(carte_jouee)
            return carte_jouee



