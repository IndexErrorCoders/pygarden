#!/usr/bin/python3
#-*- coding: utf-8 -*-

# pygarden version 0.1  (proof of concept) ==> ni optimisé ni pythonique , à peine montrable...
# buffalo technologies ;-)

# mettre le repertoire colorama a cote de votre fichier pygarden.py ;

# sur windows avec un grand moniteur, lancez pygarden.py a partir d' un fichier bat exemple:
# mode con: cols=250 lines=80
# python pygarden.py
# pause

from colorama import init, Fore, Back, Style
from os import system
import os
import copy
from copy import deepcopy

dico_AMIS = {
    "ail": {
        'carotte', 'concombre', 'oignon', 'fraise', 'tomate', 'epinard',
        'patate', 'navet'
    },
    "artichaut": {'asperge', 'laitue'},
    "aubergine": {
        'haricot', 'tomate', 'pois', 'piment', 'thym', 'persil', 'estragon'
    },
    "asperge": {'persil', 'poireau', 'tomate'},
    "aubergine": {
        'haricot', 'tomate', 'pois', 'piment', 'thym', 'persil', 'estragon'
    },
    "basilic": {'tomate', 'asperge', 'poivron', 'piment', 'aubergine'},
    "betterave": {'celeri', 'choux', 'laitue', 'haricot', 'oignon', 'radis'},
    "carotte": {
        'ail', 'aneth', 'endive', 'haricot', 'laitue', 'oignon', 'petit pois',
        'poireau', 'radis', 'salade', 'tomate', 'ciboulette'
    },
    "choux": {
        'betterave', 'haricot', 'laitue', 'petit pois', 'salade', 'tomate'
    },
    "courge": {'ciboulette', 'echalotte', 'haricot', 'oignon', 'petit pois'},
    "courgette": {
        'ciboulette', 'echalotte', 'haricot', 'oignon', 'petit pois'
    },
    "concombre": {'aneth', 'choux', 'haricot', 'laitue', 'oignon'},
    "epinard": {
        'haricot', 'petit pois', 'fraise', 'choux', 'radis', 'salade', 'tomate'
    },
    "feve": {'tomate', 'fraise', 'courge'},
    "fraise": {
        'ail', 'laitue', 'oignon', 'poireau', 'echalote', 'persil', 'sauge'
    },
    "haricot": {
        'carotte', 'choux', 'fraise', 'laitue', 'aubergine', 'celeri',
        'courgette', 'poireau', 'radis', 'patate'
    },
    "laitue": {
        'chou-fleur', 'aneth', 'carotte', 'radis', 'fraise', 'concombre',
        'courge', 'poireau'
    },
    "mache": {'ail', 'basilic', 'haricot', 'pois', 'radis'},
    "melon": {
        'mais', 'citrouille', 'courge', 'radis', 'epinard', 'tournesol',
        'potiron'
    },
    "navet": {'ail', 'celeri', 'ciboulette', 'epinard', 'petit pois'},
    "oignon": {'aneth', 'ail', 'carotte', 'concombre', 'salade', 'tomate'},
    "Petit pois": {'carotte', 'epinard', 'radis', 'choux', 'mache', 'patate'},
    "piment": {'basilic', 'carotte', 'oignon'},
    "poireau": {'carotte', 'fraise', 'epinard', 'tomate'},
    "poivron": {
        'aubergine', 'tomate', 'carotte', 'oignon', 'pois', 'trefle', 'fraise'
    },
    "patate": {'ail', 'haricot', 'pois'},
    "radis": {'carotte', 'fraise', 'haricot', 'salade', 'tomate', 'cresson'},
    "salade": {
        'aneth', 'betterave', 'concombre', 'choux', 'epinard', 'haricot',
        'petit pois', 'radis', 'tomate'
    },
    "thym": {'choux', 'brocolis'},
    "tomate": {
        'carotte', 'choux', 'epinard', 'oignon', 'persil', 'poireau', 'salade',
        'basilic'
    }
}

dico_ENNEMIS = {
    "ail": {'choux', 'haricot'},
    "asperge": {'ail', 'choux', 'echalote', 'oignon', 'poireeee'},
    "aubergine": {'oignon', 'patate'},
    "betterave": {'epinard'},
    "carotte": {'betterave', 'menthe'},
    "choux": {'autres varietes de chouxxxxx', 'ail'},
    "courgette et courge": {'concombre'},
    "concombre": {'radis'},
    "epinard": {'betterave rouge'},
    "feve": {'ail', 'ciboulette'},
    "fraise": {'choux'},
    "haricot": {'ail', 'oignon', 'pois', 'poireau'},
    "mache": {'choux', 'epinard', 'salade'},
    "melon": {'concombre'},
    "navet": {'radis'},
    "oignon": {'haricot', 'petit pois', 'poireau', 'choux', 'feve'},
    "petit pois": {'ail', 'echalotte', 'oignon', 'tomate'},
    "Piment": {'fenouil'},
    "poireau": {'haricot', 'pois'},
    "patate": {'aubergine', 'courgette', 'radis', 'tomate'},
    "radis": {'cerfeuil', 'concombre'},
    "salade": {'persil', 'tournesol'},
    "tomate": {'betterave', 'choux rouge', 'fenouil', 'pois'}
}

set_Legumes = {
    'carotte', 'concombre', 'tomate', 'epinard', 'patate', 'navet', 'asperge',
    'laitue', 'haricot', 'poireau', 'radis', 'choux', 'courgette', 'epinard',
    'betterave', 'pois', 'potiron', 'aubergine', 'endive', 'artichaut', 'navet'
}

set_Fruits = {
    'fraise', 'melon', 'framboise', 'groseille', 'cassis', 'pomme', 'poire',
    'abricot', 'raisin', 'prune', 'peche', 'cerise', 'noisette', 'pasteque',
    'figue', 'citron', 'orange'
}

set_Aromates = {
    'ail', 'piment', 'thym', 'persil', 'estragon', 'basilic', 'aneth',
    'menthe', 'ciboulette', 'echalotte', 'oignon', 'celeri', 'moutarde',
    'cerfeuil', 'melisse', 'tanaisie'
}

set_Cereales = {
    'ble', 'mais', 'sarasin', 'orge', 'millet', 'seigle', 'epautre',
    'lentilles', 'quinoa'
}

set_Fleurs = {
    'oeillet Inde', 'tabac', 'capucine', 'ortie', 'souci', 'petunia',
    'bourrache', 'myosotis', 'chicoree', 'chardon', 'coquelicot', 'echinacee',
    'aster', 'lavande', 'consoude', 'prele', 'hysope', 'micromerie', 'phlomis',
    'dracocephale', 'asclepiade', 'ammi', 'centauree', 'buplevre', 'ciste',
    'zinnia', 'sceau-de-salomon', 'eupatoire', 'miscanthus', 'verveine',
    'luzerne', 'colza', 'lin', 'trefle', 'tournesol', 'rose', 'pissenlit',
    'bleuet', 'pelargonium', 'armoise'
}

catalogue_legume = sorted(set_Legumes)
catalogue_fruit = sorted(set_Fruits)
catalogue_aromate = sorted(set_Aromates)
catalogue_cereale = sorted(set_Cereales)
catalogue_fleur = sorted(set_Fleurs)

init()
os.system('cls')

print("\n\n")
print(Back.BLACK + Fore.GREEN + Style.NORMAL + "	set_Legumes :  ", set_Legumes)
print(Back.RESET + Fore.RESET + Style.NORMAL + "\n   ")

print(Back.RESET + Fore.RED + Style.BRIGHT + "\n	set_Fruits :  ", set_Fruits)
print(Back.RESET + Fore.RESET + Style.NORMAL + "\n   ")

print(Fore.BLUE + Back.CYAN + "\n	set_Aromates :", set_Aromates)
print(Back.RESET + Fore.RESET + Style.NORMAL + "\n   ")

print(Back.BLACK + Fore.YELLOW + "\n	set_Cereales :  ", set_Cereales)
print(Back.RESET + Fore.RESET + Style.NORMAL + "\n   ")

print(Back.BLACK + Fore.MAGENTA + "\n	set_Fleurs :  ", set_Fleurs)
print(Back.RESET + Fore.RESET + Style.NORMAL + "\n   ")
print(Back.RESET + Fore.RESET + Style.NORMAL + "\n   \n")


class Big_carre():
    def __init__(self,
                 Case_5=set(),
                 Case_8=set(),
                 Case_9=set(),
                 Case_6=set(),
                 Case_3=set(),
                 Case_2=set(),
                 Case_1=set(),
                 Case_4=set(),
                 Case_7=set(),
                 Case_0=set(),
                 TargetCase=None,
                 presents=set(),
                 GREENset=set(),
                 REDset=set(),
                 DISCORDset=set(),
                 zeroHAINE=set()):

        self.Case_5 = Case_5

        self.Case_8 = Case_8

        self.Case_9 = Case_9

        self.Case_6 = Case_6

        self.Case_3 = Case_3

        self.Case_2 = Case_2

        self.Case_1 = Case_1

        self.Case_4 = Case_4

        self.Case_7 = Case_7

        self.Case_0 = Case_0

        self.TargetCase = TargetCase

        self.presents = presents

        self.GREENset = GREENset

        self.REDset = REDset

        self.DISCORDset = DISCORDset

        self.zeroHAINE = zeroHAINE

    def scan_presents(self):

        self.presents = self.Case_5 | self.Case_8 | self.Case_9 | self.Case_6 | self.Case_3 | self.Case_2 | self.Case_1 | self.Case_4 | self.Case_7

    def cherche_conflit(self):

        for present in self.presents:

            if present in self.REDset:

                try:
                    for suspect in dico_ENNEMIS[present]:
                        if suspect in self.presents:
                            print("Attention  à ", present,
                                  " qui semble etre en conflit avec :", suspect)

                except KeyError:

                    print(
                        "KeyError entre  ", present,
                        " et le dico_ENNEMIS : MERCI de mettre à jour ou signaler ce bug (penser a relever le traceback si possible) ")
            else:
                pass

    def show_amis_respectifs(self):

        print("len(self.presents)   : ", len(self.presents))

        for mangeable in (self.presents):

            try:

                print(Back.BLACK + Fore.GREEN + Style.NORMAL + "\n ",
                      mangeable, "est ami avec  :", dico_AMIS[mangeable])

                (self.GREENset).update(tuple(dico_AMIS[mangeable]))

            except KeyError:

                print("\n ", mangeable, "n a pas d ami directement connu...")

            print(Back.BLACK + Fore.WHITE + Style.NORMAL + "\n ")

    def show_ennemis_respectifs(self):

        for mangeable in (self.presents):

            try:

                print(Back.BLACK + Fore.RED + Style.NORMAL + "\n ", mangeable,
                      "est ennemi avec  :", dico_ENNEMIS[mangeable])

                (self.REDset).update(tuple(dico_ENNEMIS[mangeable]))

            except KeyError:

                print("\n ", mangeable, "n a pas d ennemi directement connu...")

            print(Back.BLACK + Fore.WHITE + Style.NORMAL + "\n ")

    def show_DISCORDANTS(self):

        self.DISCORDset.update(set(self.GREENset) & set(self.REDset))

        if len(mon_bigcarre.DISCORDset) > 0:

            print(Back.BLACK + Fore.CYAN + Style.BRIGHT +
                  " \n Voici les especes ambigues discordantes :  ",
                  self.DISCORDset)
            print(
                Back.BLACK + Fore.CYAN + Style.NORMAL +
                " \n   (c.a.d. amie avec certaines plantes de votre big carre, mais cependant aussi ennemie avec d autres plantes deja en terre) ")

            print(Back.BLACK + Fore.WHITE + Style.NORMAL + "\n ")

    def show_zeroHAINE(self):

        self.zeroHAINE.update((self.GREENset) - set(self.REDset))

        if len(mon_bigcarre.zeroHAINE) > 0:

            print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT +
                  " \n Voici les especes zeroHAINE :  ", self.zeroHAINE)
            print(
                Back.BLACK + Fore.MAGENTA + Style.NORMAL +
                " \n c.a.d. qui ne pose aucun probleme avec les especes deja en terre")

            print(Back.BLACK + Fore.WHITE + Style.NORMAL + "\n ")

    def show_REDset(self):

        if len(mon_bigcarre.REDset) > 0:

            print(Back.RED + Fore.BLACK + Style.NORMAL +
                  " \n Voici les rivales a eviter dans ce big carre : REDset =  "
                  + Back.RED + Fore.BLACK + Style.BRIGHT, self.REDset)

        print(Back.BLACK + Fore.WHITE + Style.NORMAL + "\n ")

    def check_friendhole(self):

        print("\n\n ************	check_friendhole	*************")

        for v in dico_AMIS.values():

            print("\n ")
            for element in v:

                if element not in dico_AMIS.keys():

                    print(
                        "\n plante renseignee de facon unidirectionnelle : il manque dans dico_AMIS la clef  ",
                        element)

        input("\n PRESS ENTER   ")

    def check_AgentDouble(self):

        print("\n\n ************	check_AgentDouble	*************")

        for plante_test in dico_AMIS.keys():

            for pretendue_amie in dico_AMIS[plante_test]:

                try:

                    if pretendue_amie in dico_ENNEMIS[plante_test]:

                        print(
                            Back.BLACK + Fore.RED + Style.BRIGHT +
                            " \n AgentDouble decouvert : verifier pretendue_amie  :  ",
                            pretendue_amie, " chez la pauvre plante_test ",
                            plante_test)
                        print(Back.BLACK + Fore.WHITE + Style.NORMAL + "\n ")

                except KeyError:

                    print(" \n KeyError decouvert avec pretendue_amie  :  ",
                          pretendue_amie, " et plante_test ", plante_test)

        input("\n PRESS ENTER  ")


mon_bigcarre = Big_carre()


def show_bigcarre():

    print("\n")
    print("Case_7   :  ", mon_bigcarre.Case_7, "		Case_8   :  ",
          mon_bigcarre.Case_8, "		Case_9   :  ", mon_bigcarre.Case_9)
    print("\n")
    print("Case_4   :  ", mon_bigcarre.Case_4, "		Case_5   :  ",
          mon_bigcarre.Case_5, "		Case_6   :  ", mon_bigcarre.Case_6)
    print("\n")
    print("Case_1   :  ", mon_bigcarre.Case_1, "		Case_2   :  ",
          mon_bigcarre.Case_2, "		Case_3   :  ", mon_bigcarre.Case_3)
    print("\n")

    mon_bigcarre.scan_presents()

    print("\n presents   :  ", mon_bigcarre.presents)

    mon_bigcarre.show_amis_respectifs()

    print("\n")
    mon_bigcarre.show_ennemis_respectifs()
    print("\n")

    mon_bigcarre.show_REDset()

    mon_bigcarre.show_DISCORDANTS()


def RESUME_bigcarre():

    print("\n")
    print("\n")
    print("Case_7   :  ", mon_bigcarre.Case_7, "		Case_8   :  ",
          mon_bigcarre.Case_8, "		Case_9   :  ", mon_bigcarre.Case_9)
    print("\n")
    print("Case_4   :  ", mon_bigcarre.Case_4, "		Case_5   :  ",
          mon_bigcarre.Case_5, "		Case_6   :  ", mon_bigcarre.Case_6)
    print("\n")
    print("Case_1   :  ", mon_bigcarre.Case_1, "		Case_2   :  ",
          mon_bigcarre.Case_2, "		Case_3   :  ", mon_bigcarre.Case_3)
    print("\n")
    print("\n")

    mon_bigcarre.scan_presents()

    print("\n presents   :  ", mon_bigcarre.presents)


def show_brouette():

    print("\n")
    print(
        Back.BLACK + Fore.WHITE + Style.NORMAL +
        "A planter / repiquer , en attente sur votre brouette 			: Case_0   =  ",
        mon_bigcarre.Case_0)


show_bigcarre()

show_brouette()


def afficher_catalogue_legume():

    i = 0

    for legume in catalogue_legume:

        if legume in mon_bigcarre.zeroHAINE:

            print(Back.BLACK + Fore.GREEN + Style.NORMAL + " \n ", legume,
                  " : ", i)
            i += 1

        elif legume in mon_bigcarre.DISCORDset:
            print(Back.BLACK + Fore.CYAN + Style.NORMAL + " \n ", legume,
                  " : ", i)
            i += 1

        elif legume in mon_bigcarre.REDset:
            print(Back.BLACK + Fore.RED + Style.NORMAL + " \n ", legume, " : ",
                  i)
            i += 1

        else:
            print(Back.BLACK + Fore.WHITE + Style.NORMAL + " \n ", legume,
                  " : ", i)
            i += 1

    print(Back.BLACK + Fore.WHITE + Style.NORMAL + "\n")


def afficher_catalogue_fruit():

    i = 0

    for fruit in catalogue_fruit:

        if fruit in mon_bigcarre.zeroHAINE:

            print(Back.BLACK + Fore.GREEN + Style.NORMAL + " \n ", fruit,
                  " : ", i)
            i += 1

        elif fruit in mon_bigcarre.DISCORDset:
            print(Back.BLACK + Fore.CYAN + Style.NORMAL + " \n ", fruit, " : ",
                  i)
            i += 1

        elif fruit in mon_bigcarre.REDset:
            print(Back.BLACK + Fore.RED + Style.NORMAL + " \n ", fruit, " : ",
                  i)
            i += 1

        else:
            print(Back.BLACK + Fore.WHITE + Style.NORMAL + " \n ", fruit,
                  " : ", i)
            i += 1

    print(Back.BLACK + Fore.WHITE + Style.NORMAL + "\n")


def afficher_catalogue_aromate():

    i = 0

    for aromate in catalogue_aromate:

        if aromate in mon_bigcarre.zeroHAINE:

            print(Back.BLACK + Fore.GREEN + Style.NORMAL + " \n ", aromate,
                  " : ", i)
            i += 1

        elif aromate in mon_bigcarre.DISCORDset:
            print(Back.BLACK + Fore.CYAN + Style.NORMAL + " \n ", aromate,
                  " : ", i)
            i += 1

        elif aromate in mon_bigcarre.REDset:
            print(Back.BLACK + Fore.RED + Style.NORMAL + " \n ", aromate,
                  " : ", i)
            i += 1

        else:
            print(Back.BLACK + Fore.WHITE + Style.NORMAL + " \n ", aromate,
                  " : ", i)
            i += 1

    print(Back.BLACK + Fore.WHITE + Style.NORMAL + "\n")


def afficher_catalogue_cereale():

    i = 0

    for cereale in catalogue_cereale:

        if cereale in mon_bigcarre.zeroHAINE:

            print(Back.BLACK + Fore.GREEN + Style.NORMAL + " \n ", cereale,
                  " : ", i)
            i += 1

        elif cereale in mon_bigcarre.DISCORDset:
            print(Back.BLACK + Fore.CYAN + Style.NORMAL + " \n ", cereale,
                  " : ", i)
            i += 1

        elif cereale in mon_bigcarre.REDset:
            print(Back.BLACK + Fore.RED + Style.NORMAL + " \n ", cereale,
                  " : ", i)
            i += 1

        else:
            print(Back.BLACK + Fore.WHITE + Style.NORMAL + " \n ", cereale,
                  " : ", i)
            i += 1

    print(Back.BLACK + Fore.WHITE + Style.NORMAL + "\n")


def afficher_catalogue_fleur():

    i = 0

    for fleur in catalogue_fleur:

        if fleur in mon_bigcarre.zeroHAINE:

            print(Back.BLACK + Fore.GREEN + Style.NORMAL + " \n ", fleur,
                  " : ", i)
            i += 1

        elif fleur in mon_bigcarre.DISCORDset:
            print(Back.BLACK + Fore.CYAN + Style.NORMAL + " \n ", fleur, " : ",
                  i)
            i += 1

        elif fleur in mon_bigcarre.REDset:
            print(Back.BLACK + Fore.RED + Style.NORMAL + " \n ", fleur, " : ",
                  i)
            i += 1

        else:
            print(Back.BLACK + Fore.WHITE + Style.NORMAL + " \n ", fleur,
                  " : ", i)
            i += 1

    print(Back.BLACK + Fore.WHITE + Style.NORMAL + "\n")


def choisir_legume():

    print(Back.BLACK + Fore.GREEN + Style.NORMAL +
          "\n\nQuel legume voulez vous planter ?  ")

    choix_legume = input("\n")

    choix_legume = int(choix_legume)

    print(Back.BLACK + Fore.GREEN + Style.BRIGHT + "\n Vous avez choisi :  ",
          choix_legume, "  : ", catalogue_legume[choix_legume])

    print(Back.BLACK + Fore.WHITE + Style.NORMAL + "\n")

    mon_bigcarre.Case_0 |= {catalogue_legume[choix_legume]}

    print("\n")


def choisir_fruit():

    print(Back.BLACK + Fore.RED + Style.NORMAL +
          "\n\nQuel fruit voulez vous planter ?  ")

    choix_fruit = input("\n")

    choix_fruit = int(choix_fruit)

    print(Back.BLACK + Fore.RED + Style.BRIGHT + "\n Vous avez choisi :  ",
          choix_fruit, "  : ", catalogue_fruit[choix_fruit])

    print(Back.BLACK + Fore.WHITE + Style.NORMAL + "\n")

    mon_bigcarre.Case_0 |= {catalogue_fruit[choix_fruit]}

    print("\n")


def choisir_aromate():

    print(Back.BLUE + Fore.CYAN + Style.NORMAL +
          "\n\nQuel aromate voulez vous planter ?  ")

    choix_aromate = input("\n")

    choix_aromate = int(choix_aromate)

    print(Back.CYAN + Fore.BLUE + Style.BRIGHT + "\n Vous avez choisi :  ",
          choix_aromate, "  : ", catalogue_aromate[choix_aromate])

    print(Back.BLACK + Fore.WHITE + Style.NORMAL + "\n")

    mon_bigcarre.Case_0 |= {catalogue_aromate[choix_aromate]}

    print("\n")


def choisir_cereale():

    print(Back.YELLOW + Fore.BLACK + Style.NORMAL +
          "\n\nQuelle cereale voulez vous planter ?  ")

    choix_cereale = input("\n")

    choix_cereale = int(choix_cereale)

    print(Back.BLACK + Fore.YELLOW + Style.BRIGHT + "\n Vous avez choisi :  ",
          choix_cereale, "  : ", catalogue_cereale[choix_cereale])

    print(Back.BLACK + Fore.WHITE + Style.NORMAL + "\n")

    mon_bigcarre.Case_0 |= {catalogue_cereale[choix_cereale]}

    print("\n")


def choisir_fleur():

    print(Back.MAGENTA + Fore.BLACK + Style.NORMAL +
          "\n\nQuelle fleur voulez vous planter ?  ")

    choix_fleur = input("\n")

    choix_fleur = int(choix_fleur)

    print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT + "\n Vous avez choisi :  ",
          choix_fleur, "  : ", catalogue_fleur[choix_fleur])

    print(Back.BLACK + Fore.WHITE + Style.NORMAL + "\n")

    mon_bigcarre.Case_0 |= {catalogue_fleur[choix_fleur]}

    print("\n")


def choisir_type():

    print(Back.WHITE + Fore.BLACK + Style.NORMAL +
          "\n\nQue voulez vous planter ?		 " + Back.BLACK + Fore.GREEN +
          Style.NORMAL + " 0 => Legume   " + Back.BLACK + Fore.RED +
          Style.NORMAL + "  1 => Fruit  " + Back.BLUE + Fore.CYAN +
          Style.NORMAL + "  2=> Aromates   " + Back.BLACK + Fore.YELLOW +
          Style.NORMAL + "   3 => Cereale  " + Back.BLACK + Fore.MAGENTA +
          Style.NORMAL + "  4=> Fleur " + Back.BLACK + Fore.BLACK +
          Style.NORMAL + "  \n\n\n" + Back.BLACK + Fore.WHITE + Style.BRIGHT)

    choix_type = input(" ")

    choix_type = int(choix_type)

    print("\n")

    print("\n Vous avez choisi :  ", choix_type)

    print(Back.BLACK + Fore.WHITE + Style.NORMAL + " ")

    print(" \n ")

    if len(mon_bigcarre.presents) > 0:
        print(mon_bigcarre.REDset)

    if choix_type == 0:
        afficher_catalogue_legume()
        choisir_legume()

    if choix_type == 1:
        afficher_catalogue_fruit()
        choisir_fruit()

    if choix_type == 2:
        afficher_catalogue_aromate()
        choisir_aromate()

    if choix_type == 3:
        afficher_catalogue_cereale()
        choisir_cereale()

    if choix_type == 4:
        afficher_catalogue_fleur()
        choisir_fleur()

    if choix_type not in {0, 1, 2, 3, 4}:
        print("\n Erreur de saisie, veuillez recommencer svp ...")
        choisir_type()


"""


# http://stackoverflow.com/questions/3392354/python-append-values-to-a-set
# http://stackoverflow.com/questions/2376464/typeerror-unsupported-operand-types-for-str-and-int

"""


def rappeller_complementaire():

    try:

        print(Back.BLACK + Fore.GREEN + Style.NORMAL + "\n Voici les amis de  ",
              ', '.join(mon_bigcarre.Case_0), "  :  ",
              dico_AMIS[', '.join(mon_bigcarre.Case_0)])
    except KeyError:
        print("\n Pas d amis connus pour ", str(mon_bigcarre.Case_0),
              "  ;-'(  ")

    try:
        print(Back.BLACK + Fore.RED + Style.NORMAL +
              "\n Voici les ennemis de  ", ', '.join(mon_bigcarre.Case_0),
              "  :  ", dico_ENNEMIS[', '.join(mon_bigcarre.Case_0)])
    except KeyError:
        print("\n Pas d ennemis connus pour ", str(mon_bigcarre.Case_0),
              "  :-)  ")

    print(Back.BLACK + Fore.WHITE + Style.NORMAL + "\n")


def menu():

    if len(mon_bigcarre.presents) > 0:

        if len(mon_bigcarre.Case_0) == 1:

            for key in mon_bigcarre.Case_0:
                try:
                    (mon_bigcarre.REDset).update(dico_ENNEMIS[key])

                    (mon_bigcarre.GREENset).update(dico_AMIS[key])
                except KeyError:
                    print(
                        "KeyError avec  ", key,
                        " verifier son absence dans dico_ENNEMIS ou dico_AMIS")

        print(" Evitez de planter ceci  :  ", mon_bigcarre.REDset)

        mon_bigcarre.show_zeroHAINE()

    try:
        choisir_type()
    except ValueError:
        print(
            "\n Erreur de saisie, entrez le nombre correspondant a votre demande  :  ")
        choisir_type()


def reset_Case_0():

    mon_bigcarre.Case_0 = set()


def choisirGeometry():

    print("\n Quel geometrie pour votre big carré ? ")

    print("\n taper 0 pour X ")
    print("\n taper 1 pour O ")
    print("\n taper 2 pour U ")
    print("\n taper 3 pour = ")
    print("\n taper 4 pour + ")

    print("\n\n taper 5 pour losange ")
    print("\n taper 6 pour triangle ")
    print("\n taper 7 pour : ")
    print("\n taper 8 pour imperial ")

    print("\n\n taper 9 pour Angles ")
    print("\n taper 10 pour Barre ")
    print("\n taper 11 pour / ")
    print("\n taper 12 pour \ ")

    choixGeometry = input("\n\n Votre choix   ")

    choixGeometry = int(choixGeometry)

    if choixGeometry == 0:

        mon_bigcarre.Case_7 = mon_bigcarre.Case_9 = mon_bigcarre.Case_5 = mon_bigcarre.Case_1 = mon_bigcarre.Case_3 = copy.deepcopy(
            mon_bigcarre.Case_0)

    if choixGeometry == 1:

        mon_bigcarre.Case_7 = mon_bigcarre.Case_8 = mon_bigcarre.Case_9 = mon_bigcarre.Case_4 = mon_bigcarre.Case_6 = mon_bigcarre.Case_1 = mon_bigcarre.Case_2 = mon_bigcarre.Case_3 = copy.deepcopy(
            mon_bigcarre.Case_0)

    elif choixGeometry == 2:

        mon_bigcarre.Case_7 = mon_bigcarre.Case_9 = mon_bigcarre.Case_4 = mon_bigcarre.Case_6 = mon_bigcarre.Case_1 = mon_bigcarre.Case_2 = mon_bigcarre.Case_3 = copy.deepcopy(
            mon_bigcarre.Case_0)

    elif choixGeometry == 3:

        mon_bigcarre.Case_7 = mon_bigcarre.Case_8 = mon_bigcarre.Case_9 = mon_bigcarre.Case_1 = mon_bigcarre.Case_2 = mon_bigcarre.Case_3 = copy.deepcopy(
            mon_bigcarre.Case_0)

    elif choixGeometry == 4:

        mon_bigcarre.Case_8 = mon_bigcarre.Case_4 = mon_bigcarre.Case_5 = mon_bigcarre.Case_6 = mon_bigcarre.Case_2 = copy.deepcopy(
            mon_bigcarre.Case_0)

    elif choixGeometry == 5:

        mon_bigcarre.Case_8 = mon_bigcarre.Case_4 = mon_bigcarre.Case_6 = mon_bigcarre.Case_2 = copy.deepcopy(
            mon_bigcarre.Case_0)

    elif choixGeometry == 6:

        mon_bigcarre.Case_8 = mon_bigcarre.Case_1 = mon_bigcarre.Case_3 = copy.deepcopy(
            mon_bigcarre.Case_0)

    elif choixGeometry == 7:

        mon_bigcarre.Case_8 = mon_bigcarre.Case_2 = copy.deepcopy(
            mon_bigcarre.Case_0)

    elif choixGeometry == 8:

        mon_bigcarre.Case_5 = copy.deepcopy(mon_bigcarre.Case_0)

    elif choixGeometry == 9:

        mon_bigcarre.Case_7 = mon_bigcarre.Case_9 = mon_bigcarre.Case_1 = mon_bigcarre.Case_3 = copy.deepcopy(
            mon_bigcarre.Case_0)

    if choixGeometry == 10:

        mon_bigcarre.Case_4 = mon_bigcarre.Case_5 = mon_bigcarre.Case_6 = copy.deepcopy(
            mon_bigcarre.Case_0)

    if choixGeometry == 11:

        mon_bigcarre.Case_1 = mon_bigcarre.Case_5 = mon_bigcarre.Case_9 = copy.deepcopy(
            mon_bigcarre.Case_0)

    if choixGeometry == 12:

        mon_bigcarre.Case_7 = mon_bigcarre.Case_5 = mon_bigcarre.Case_3 = copy.deepcopy(
            mon_bigcarre.Case_0)

    reset_Case_0()

# MAIN--------------------------------------

#-----------TEST start ---------

# mon_bigcarre.check_friendhole()

# mon_bigcarre.check_AgentDouble()

#-----------TEST end ---------


# SUPER MENU --------------------------------------
def Planter_Premier_DUO():

    menu()
    rappeller_complementaire()
    menu()
    choisirGeometry()
    os.system('cls')
    show_bigcarre()

# SUPER MENU -------------------------------------- END

# ///////////  MAIN  /////////////////

Planter_Premier_DUO()

Planter_Premier_DUO()

Planter_Premier_DUO()

os.system('cls')
show_bigcarre()

os.system('cls')
show_bigcarre()
mon_bigcarre.cherche_conflit()

ferme = input("\n\n\nappuie pour fermer")
os.system('cls')
print("\n Voici votre Big Carre")
print("\n\n\n\n ")
RESUME_bigcarre()
print("\n\n\n\n ")
mon_bigcarre.cherche_conflit()

ferme = input("\n\n\nappuie pour fermer")
