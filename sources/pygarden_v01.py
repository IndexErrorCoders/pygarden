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
"""
A savoir

Les légumes de la famille des liliacées et ceux de la famille des légumineuses ne s'aiment pas
La carotte ne s'aime pas elle-même, de même que le choux n'aime pas les autres membres de sa famille (les crucifères)
Peu de légumes aiment le cresson, hormis les fraisiers, les tomates et les radis.

Fleurissez à tout va les bordures du potager et les espaces libres du jardin, avec diverses plantes mellifères et aromatiques

Plantez ou semez aux pieds des arbres et des arbustes.

Parmi les aromatiques compagnes, la famille des ombellifères (très appréciées des auxiliaires butineurs) est bien représentée.
On citera en exemple l'aneth, bon répulsif contre les pucerons, mais également stimulateur de croissance pour les concombres
ou encore la coriandre qui éloigne la mouche de la carotte.

Moins connue que l'association légumes-fleurs, il y a l'association légumes-légumes. La famille la plus réputée en tant que répulsif est celle 
des alliacées (ail, oignon, ciboulette), dont l'odeur a tendance à éloigner de nombreux parasites. Leur est également attribué le pouvoir de protéger les fraises
 de la pourriture grise et les tomates et les pommes de terre du mildiou. L'ail et l'oignon agiraient aussi contre la cloque du pêcher et la ciboulette protégerait les pommiers 
 de la tavelure et des chancres. Voici donc des promesses intéressantes à vérifier !

Mais les associations les plus étonnantes restent celles où il y a échanges réciproques : c'est le cas entre la carotte et le poireau (la carotte met en fuite la mouche du poireau
 tandis que le poireau éloigne la mouche de la carotte) ou bien encore entre le céleri et le choux ; en effet, si la chenille de la piéride du choux n'apprécie guère 
l'odeur du céleri, le choux quant à lui protègerait le céleri de la maladie des taches brunes. En plus de cela, il semble que leur association leur permette de mieux profiter 
des nutriments disponibles dans le sol et par conséquent de mieux se développer.

La liste des bonnes fleurs est longue : sauge, armoise, basilic, lavande, mélisse, rue...faites votre choix !



Associer des plantes répulsives
Les plantes aromatiques : 
Les aromatiques ont toutes un pouvoir répulsif sur les nuisibles. Entre autre intérêt, leurs racines diffusent des substances repoussantes pour les nématodes (nuisibles notamment aux tomates). Le thym est aussi réputé pour éloigner les limaces. Les seules exceptions, le fenouil et l’absinthe sont à utiliser à l’extérieur de la zone potagère. Car elles ont toutefois une action repoussante sur la piéride du chou.

Les aromatiques ont toutes un effet bénéfique sur les autres plantes. Les aromatiques sont, soit récoltées et séchées (poudre) pour protéger des rats et des limaces ou empêcher les insectes de manger les graines (semis), soit plantées à proximité pour leur influence bénéfique sur fruits et légumes : elles améliorent la vigueur et contribuent à éloigner les insectes ravageurs (dessus et dessous la surface du sol)
Profitez de l’odeur fortes des aromatiques à feuillage, ainsi que des Alliacées (ail, échalote, oignon, poireau) pour créer des confusions olfactives qui perturbent les ravageurs : disséminez ces plantes entre les cultures (surtout carotte, chou, tomate).

Exemples de plantes aromatiques: thym, basilic, sauge, menthe, santoline, mélisse, marjolaine (ou origan), lavande, aneth, santoline, romarin, rue...

Associer des plantes trompe-l’œil
Certaines plantes ‘’cachent’’ les plantes potagères aux insectes et autres nuisibles. Les cosmos sont associés aux choux qu’ils protègent de la piéride.

Les plantes à associer contre les nuisibles
Bactéries et les champignons nuisibles se multiplient plus facilement dans les monocultures. Avec les cultures associées, ils se heurtent rapidement à une limite, c'est à dire à une autre plante qu'ils n'arrivent pas à envahir. Les associations diminuent la menace des ravageurs pour les plantes potagères et les fleurs, et améliorent le sol grâce à la fertilisation en surface.
Les capucines attirent irrésistiblement les pucerons. Les capucines éloingent les puceront du potager et des rosiers.
Vous pouvez par exemple associer les capucines aux haricots.

Des plantes associées comme insecticides naturels.
Associer des plantes pour en repousser d'autres :
haricots, maïs et courges vont ensemble mais ne vont pas avec pois, oignons, haricots.
myosotis / framboisiers : oui contre vers de framboisier
capucines / rangs de tomates, choux, carottes, pommes de terre, haricots : oui contre mouches blanches (aleurodes)
œillets d'inde avec les tomates , les choux, les haricots, les carottes, les pommes de terre et les poireaux contre les mouches blanches
ciboulette / rosiers : oui contre l'oïdium et les taches noires
romarin, thym / le chou : oui contre pucerons, piéride
tomate / chou : oui contre la piéride
carottes / tomate : oui
carottes, choux / laitues : non
Quelques associations de plantes complémentaires :
Asperge Tomate / Persil
Aubergine Haricot
Betterave Haricot/ Oignon / Chou / Laitue
Carotte Laitue / Ciboulette / Radis / Poireau / Oignon / Pois
Chou Romarin / Menthe / Sauge / Thym / Capucine / Pomme de terre
Concombre Maïs / Tournesol / Pomme de terre / Radis / Haricot / Origan / Pois
Courge & Potiron Capucine / Maïs / Pomme de Terre
Epinard Fraisier / Radis
Fraisier Oignon / Bourrache / Epinard / Laitue
Haricot Carotte / Aubergine / Œillet d’Inde et Souci / Betterave / Maïs / Pomme de terre / Concombre
Laitue Fraisier / Carotte / Radis
Maïs Haricot / Pois / Concombre / Courge & Potiron
Melon Origan
Oignon Carotte / Fraisier
Pêcher Tanaisie
Pomme de Terre Chou / Courge & Potiron / Pois / Haricot / Œillet d’Inde et Souci / Concombre
Poireau Carotte
Poirier Sauge
Pois Radis / Carotte / Concombre / Maïs / Pomme de Terre
Pommier Ciboulette / Capucine
Radis Epinard / Menthe / Concombre / Capucine / Carotte / Laitue / Pois
Tomate Persil / Basilic / Asperge / Œillet d’Inde et Souci

Autres exemples d'associations de plantes compagnes
• La mouche de l’oignon est repoussée par les carottes. Leur odeur repousse les mouches.
• Les carottes sont également utiles à planter entre les rangs de céleri pour lutter contre la teigne du poireau .
• La mouche de la carotte est repoussée par les oignons. Le poireau éloigne, lui aussi, la mouche de la carotte.
• Pour éloigner les mouches des carottes, semez des graines de carotte en les mélangeant à du terreau et du marc de café.
• Le basilic et le persil sont des défenseurs de la tomate, les géraniums protègent les rosiers
• Contre les chenilles plantez du fenouil, de la menthe ou de sauge près des choux le protège des papillons qui les mangent.
• Le myosotis cohabitent parfaitement avec les cultures de framboisiers car son odeur empêche le ver du framboisier de proliférer.
• L'hysope évite aux choux la pontes des mouches blanches.
• Le piéride du chou est un papillon qui fait des dégâts sur vos plantes à sa seconde génération : associez des cultures de céleri et de tomates.
• Les salades sont protégées des limaces quand elles sont plantées à proximité du fenouil. Effet, l’odeur du fenouil dégage une odeur qui fait fuir les limaces.
• Les pucerons noirs des rosiers sont repoussés par la menthe verte ou poivrée. La menthe « Buddleia » attire les abeilles et favorise la pollinisation des plantes.
• Contre les puces de terre ou altises , le plus efficace est l’ "herbe à chat", la chataire.
• Contre les pucerons, les coccinelles sont de bons prédateurs. Les pucerons sont également repoussés par des plants de sauges officinales ou de capucines.
• Haricots, maïs et courges vont ensemble mais ne vont pas avec pois, oignons, haricots.
• Myosotis / framboisiers : oui contre les vers de framboisier
• Oeillets d'inde avec les tomates , les choux, les haricots, les carottes, les pommes de terre et les poireaux contre les mouches blanches
• Ciboulette / rosiers : oui contre l'oïdium et les taches noires
• Romarin, thym / le chou : oui contre pucerons, piéride
• Tomate / chou : oui contre la piéride
• Carottes / tomate : oui
• Carottes, choux / laitues : non

Quelques exemples d'associations de plantes
Quelques exemples de compagnonnage :

L’aneth protège les carottes et concombres. N’hésitez pas à les planter ensemble.
Le basilic est un fort répulsif des mouches et moustiques. Il s’associe parfaitement avec les tomates, asperges, poivrons, piments, aubergines.
La bourrache attire les abeilles, fait fuir les limaces, réduit les doryphores, éloigne les vers des tomates. Elle est appréciée des pommes de terre, courgettes, choux, fraisiers, tomates.
La capucine attire les pucerons (il vous suffira ensuite d’arracher les capucines et de les brûler), éloigne les punaises des courgettes et citrouilles. Elle s’accommode avec les radis, courgettes, choux, tomates.
Le cerfeuil réduit l’invasion des limaces.
La lavande éloigne les pucerons.
Les œillets d’Inde protègeront la plupart de vos plantes (pommes de terre, tomates, asperges, haricots, choux) des insectes nuisibles. A planter en bordure de votre jardin.
Le thym éloigne les mouches blanches, protège les choux et brocolis.
Les associations favorables :
Artichaut : fève
Asperge : haricot, persil, tomate
Aubergine : haricots vert
Carotte : poireau, oignon, laitue, pois, radis, tomate, haricot nain, ciboulette, coriandre, scorsonère, romarin
Capucine : rangs de tomates, choux, carottes, pommes de terre, haricots. Utile contre les mouches blanches (aleurodes)
Céleri branche : poireau, tomate, chou fleur
Céleri rave : radis, betterave, pois, haricot
Ciboulette : carotte, concombre
Courge : maïs, laitue
Cresson : radis
Echalotte : betterave, fraisier, laitue, tomate
Epinard : betterave, fraisier, laitue, haricot à rame
Fraisier : bourrache, épinard, laitue, haricot nain, tomate, thym
Fève : artichaut, maïs
Haricot : pomme de terre, carotte, concombre, chou-fleur, fraisier, aubergine, maïs, chou, betterave, céleri, épinard, sarriette
Laitue : chou-fleur, aneth, carotte, radis, fraisier, concombre, courge, poireau
Mâche : poireau, oignon blanc
Maïs : pomme de terre, concombre, courge, pois, fève
Navet : pois, romarin, menthe
Panais : oignon
Persil : asperge, tomate
Poireau : oignon, tomate, carotte, laitue, céleri, mâche
Pois : navet, concombre, carotte, radis, maïs, pomme de terre, chou-rave
Pomme de terre : haricot, maïs, chou, pois, fève, raifort
Radis : pois, laitue, carotte, cresson, épinard
Tomate : ail, oignon, carotte, asperge, céleri, poireau, basilic, persil
Tournesol : concombre

Par exemple : Légumes + - ail carotte, fraisier, tomate, chou, pois, haricot betterave rouge céleri, laitue, oignon, chou poireau, carotte, haricot, épinard carotte ail, haricot, laitue, oignon aneth céleri chou, concombre, cornichon, pomme de terre, tomate laitue, poireau chou céleri, concombre, cornichon, pomme de terre, tomate ail, fraisier, échalote concombre haricot, maïs, radis, pois, tournesol pomme de terre, herbes aromatiques courgette laitue, haricot chou, fenouil épinard +/- tout fenouil fenouil mâche, sauge, concombre pas avec la plupart des autres plantes haricot +/- tout ail, betterave, échalote laitue +/- tout céleri, persil navet laitue, pois fenouil oignon betterave, carotte, fraisier, laitue, poireau, tomate haricot, pois persil asperge, radis, tomate céleri, laitue, pois radis carotte, persil, haricot, pois, tomate chou, cerfeuil tomate ail, asperge, carotte, céleri, chou, haricot concombre, pois, pomme de terre, fenouil


Les plantes qui ne s’aiment pas

4 petites règles à mémoriser :
1 - Une règle facile à retenir est d’éviter de cultiver côte à côte, des membres de la même famille.
2 - D’une manière générale, évitez de cultiver ensemble 2 légumes fortement aromatiques et dont les nuances olfactives s’opposent.
3 - Les Liliacées et les Légumineuses doivent être séparées car elles ne font pas bon ménage. 4 - Les légumes feuilles et tiges se montrent particulièrement tolérants, mais il existe quelques cas particuliers qui retiennent l’attention :

Les associations de plantes à éviter :
Ail : pois, haricot, fève, lentille
Aneth : à éloigner des carottes.
Absinthe : carvi, sauge, anis, fenouil
Artichaut : l'artichaut n'aime pas la fève
Asperge : le voisinage de l’oignon modifie la saveur de ses turions.
Basilic : rue officinale
Betterave : haricot à rame
Carotte : aneth
Cerfeuil : radis
Chou : ne semble guère apprécier la présence des fraisiers, des oignons et des tomates
Chou-rave : haricot, tomate
Concombre : pomme de terre, tomate
Courge : pomme de terre
Echalote : pois, haricot, fève, lentille
Épinard : la proximité d’une culture de pomme de terre semble lui être préjudiciable.
Fenouil : tomate, chou-rave, absinthe, carvi, haricot, pois, échalote. la présence d’absinthe et de coriandre paraît gêner la formation de ses graines.
Framboisier : ronce. Ne pas planter avec les pommes de terre.
Haricot : oignon, ail, échalote, tomate, fenouil
Laitue : tournesol, persil
Melon : concombre, courge
Oignon : pois, haricot, fève, lentille, haricots
Poireau : éviter la présence proche des brocolis, fève, haricot.
Poirée : poireau
Pois : ail, échalote, oignon, poireau
Pomme de terre : tomate, courge, carotte, oignon, framboisier, arroche, tournesol, melon
Radis : cerfeuil
Tomate : haricot, concombre, chou-rave, pomme de terre, betterave
Sauge : à ne pas planter près des oignons.
Oignons et haricots.
Betteraves rouges et épinards.
Concombres et courgettes.
Tomates et pois
Tomate & Pomme de terre
Laitues et persil.
Chou et Fraisier
Chou et Tomate
Echalote et Oignon
Ail & Pois – Haricot
Tournesol & Pomme de terre

Les plantes qu'il faut isoler
A isoler car nuisibles aux autres plantes : le cresson, le fenouil, le noyer.
Haricots, maïs et courges vont ensemble mais ne vont pas avec pois, oignons, haricots.


http://www.encyclo-ecolo.com/Association_de_plantes
http://www.rustica.fr/articles-jardin/associer-legumes-plantes-et-fleurs-contre-maladies-et-parasites,286.html
http://www.binette-et-jardin.com/dossier-68-association-plantes-jardin-technique-compagnonnage.html

Les associations favorables au jardin

Ail : betterave, fraisier, laitue, carotte, tomate
Artichaut : fève
Asperge : haricot, persil, tomate
Aubergine : haricots vert
Carotte : poireau, oignon, laitue, pois, radis, tomate, haricot nain, ciboulette, coriandre, scorsonère, romarin
Céleri branche : poireau, tomate, chou fleur
Céleri rave : radis, betterave, pois, haricot
Ciboulette : carotte, concombre
Courge : maïs, laitue
Cresson : radis
Echalotte : betterave, fraisier, laitue, tomate
Epinard : betterave, fraisier, laitue, haricot à rame
Fraisier : bourrache, épinard, laitue, haricot nain, tomate, thym
Fève : artichaut, maïs
Haricot : pomme de terre, carotte, concombre, chou-fleur, fraisier, aubergine, maïs, chou, betterave, céleri, épinard, sarriette
Laitue : chou-fleur, aneth, carotte, radis, fraisier, concombre, courge, poireau
Mâche : poireau, oignon blanc
Maïs : pomme de terre, concombre, courge, pois, fève
Navet : pois, romarin, menthe
Panais : oignon
Persil : asperge, tomate
Poireau : oignon, tomate, carotte, laitue, céleri, mâche
Pois : navet, concombre, carotte, radis, maïs, pomme de terre, chou-rave
Pomme de terre : haricot, maïs, chou, pois, fève, raifort
Radis : pois, laitue, carotte, cresson, épinard
Tomate : ail, oignon, carotte, asperge, céleri, poireau, basilic, persil
Tournesol : concombre
Les associations défavorables du potager

Absinthe : carvi, sauge, anis, fenouil
Ail : pois, haricot, fève, lentille
Basilic : rue officinale
Betterave : haricot à rame
Carotte : betterave
Cerfeuil : radis
Chou : fraisier, tomate, oignon
Chou-rave : haricot, tomate
Concombre : pomme de terre, tomate
Courge : pomme de terre
Echalote : pois, haricot, fève, lentille
Fenouil : tomate, chou-rave, absinthe, coriandre, carvi, haricot, pois, échalote
Haricot : oignon, ail, échalote, tomate, fenouil
Laitue : tournesol, persil
Melon : concombre, courge
Oignon : pois, haricot, fève, lentille
Poirée : poireau
Pois : ail, échalote, oignon, poireau
Pomme de terre : tomate, courge, carotte, oignon, framboisier, arroche, tournesol
Radis : cerfeuil
Tomate : haricot, concombre, chou-rave, pomme de terre, betterave


http://www.consommerdurable.com/2010/11/tentative-de-cultures-associees-bio/
http://potager.comprendrechoisir.com/fiche/voir/262558/associer-fleurs-et-legumes-au-potager 
http://inra-dam-front-resources-cdn.brainsonic.com/ressources/afile/246508-6e585-resource-article-inra-toulouse-cultures-associees.html
http://www.rustica.fr/articles-jardin/20-fleurs-pour-jardin-ecologique,2261.html
http://www.graines-et-plantes.com/index.php?jardin=jardinage-bio&conseils=les-associations-de-plantes
"""
