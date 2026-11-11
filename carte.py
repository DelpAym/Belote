import numpy as np    
from dataclasses import dataclass
from enum import Enum


class Couleur(Enum):
    Pique = "Pique"
    Coeur = "Coeur"
    Trefle = "Trèfle"
    Carreau = "Carreau"


class Valeur(Enum):
    As = "As"
    Roi = "Roi"
    Dame = "Dame"
    Valet = "Valet"
    Dix = "10"
    Neuf = "9"
    Huit = "8"
    Sept = "7"


@dataclass(frozen=True)
class Carte:
    couleur: Couleur
    valeur: Valeur

    def __str__(self):

        symboles = {
            Couleur.Pique: "♠",
            Couleur.Coeur: "\033[31m♥\033[0m",
            Couleur.Carreau: "\033[31m♦\033[0m",
            Couleur.Trefle: "♣",
        }
        return f"{self.valeur.value} {symboles[self.couleur]}"

    def get_couleur(self):
        couleur_str = {
            Couleur.Pique: "Pique",
            Couleur.Coeur: "Coeur",
            Couleur.Carreau: "Carreau",
            Couleur.Trefle: "Trèfle",
        }
        return couleur_str[self.couleur]

    def get_value(self, atout = False):
        if self.get_couleur() == atout:
            if self.valeur == Valeur.As:
                return 11
            if self.valeur == Valeur.Roi:
                return 4
            if self.valeur == Valeur.Dame:
                return 3
            if self.valeur == Valeur.Valet:
                return 20
            if self.valeur == Valeur.Dix:
                return 10
            if self.valeur == Valeur.Neuf:
                return 14
            if self.valeur == Valeur.Huit:
                return -2
            if self.valeur == Valeur.Sept:
                return -3
        
        else:
            if self.valeur == Valeur.As:
                return 11
            if self.valeur == Valeur.Roi:
                return 4
            if self.valeur == Valeur.Dame:
                return 3
            if self.valeur == Valeur.Valet:
                return 2
            if self.valeur == Valeur.Dix:
                return 10
            if self.valeur == Valeur.Neuf:
                return -1
            if self.valeur == Valeur.Huit:
                return -2
            if self.valeur == Valeur.Sept:
                return -3


if __name__ == '__main__':
    c = None
    print(c)