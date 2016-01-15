# pygarden

# Introduction du concept 

Il s' agit de cultures associées dans le jardinage : certaines plantes se boostent mutuellement par leur action sur le pH, leurs secrétions et leur rôle sur la flore bactériologique et mycologique etc. D'autres se font la guerre.

Initialisé par buffalo974, ce projet est expliqué plus en détails sur ce post :

- http://indexerror.net/2421/un-python-dans-le-jardin

Pour en savoir plus sur la culture associée, ça se passe par là :

- http://mag.plantes-et-jardins.com/conseils-de-jardinage/fiches-conseils/bien-associer-les-legumes-au-potager

- http://www.truffaut.com/webtv/jardin/video-bonnes-associations-plantes-jardin/id_video/146.htm

# Dependences 

To install all dependences, make :

	pip install -r requirements.txt

# Test / Interface

    python3 pygarden_v01.py

<a href="http://www.zimagez.com/zimage/capturedcran2015-08-0813-40-03.php">
  <img src="http://www.zimagez.com/miniature/capturedcran2015-08-0813-40-03.php" />
</a>

# Solasp
Cette partie du projet est complémentaire au reste. Cela n'implémente pas d'interface, ni avec l'utilisateur, ni avec Python, mais propose un solveur complet pour le problème suivant : *sachant une taille de jardin, quelle sont les disposition maximisant les relations symbiotiques et minimisant les relations concurrentes entre plantes*.

Cette partie fait principalement appel à [l'Answer Set Programming](https://en.wikipedia.org/wiki/Answer_set_programming), permettant de modéliser simplement le problème (*integrity.lp*), en utilisant les données d'entrées (*data.lp*) générées à partir du programme python dédié (*relations2asp.py*).

L'intérêt de l'approche est multiple :
- optimisation du résultat facile à compléter/améliorer
- écriture simple du solver
- interfacage possible avec Python via [pyasp](https://pypi.python.org/pypi/pyasp)

## Performances
Le soleur, vu la quantité de données d'entrée et la combinatoire inhérente au problème, ne peux fournir la solution optimale au problème en un temps faible.

Sur une machine personnelle, pour un jardin de 10 par 10, avec l'ensemble des données d'entrées considérées,
calculer la meilleure solution nécessite plus de 4Go de RAM et de 10 minutes de calcul.

Il est certainement possible d'améliorer le temps de calcul en jouant avec (1) les options du solveur (2) le choix des heuristiques de base. (cf *solasp/Makefile*)
Par défaut, 4 thread sont utilisés.

La première partie du calcul, le *grounding*, n'est pas compressible à moins de trouver de meilleures modélisation pour *integrity.lp*.

## Usage
Tout d'abord, il est nécessaire de récupérer le grounder/solver *clingo* sur le site du [projet Potassco](http://sourceforge.net/projects/potassco/files/clingo/), et de placer l'executable dans le PATH ou au même niveau que le *Makefile* de solasp.
Les recettes décrites dans le *Makefile* sont suffisante pour un premier usage.

    make g  # générer data.lp à partir des données python
    make p  # lancer le solver


## Perspectives
De nombreuses améliorations peuvent être modélisées, comme par exemple l'impossibilité de placer côte à côte deux plantes enemies. Cette dernière pourrait potentiellement réduire le temps de calcul.
L'intégration de solasp au sein d'un script python plus global (incluant toutes les specs du projet initial) pourrait permettre d'assurer les features suivantes :
- optimisation d'un jardin sachant des conditions initiales de taille et de placement de plantes
- vérification des contraintes lors d'un nouveau placement
- conseil de placement

# Espaces de discussion autour du projet 

- IndexError : http://indexerror.net/2421/un-python-dans-le-jardin

- Reddit Sam&Max : https://www.reddit.com/r/sametmax/comments/3g8fva/indexerrorcoders_pygarden/

# Support 

- Users looking for support should file an issue on the GitHub issue tracking page (https://github.com/IndexErrorCoders/pygarden/issues), 

- or file a pull request (https://github.com/IndexErrorCoders/pygarden/pulls?q=is%3Aopen+is%3Apr) if you have a fix available

- Those who wish to contribute directly to the project can contact me at [no mail for the moment]  to talk about getting repository access granted.

# En savoir plus sur l'organisation IndexErrorCoders 

http://sametmax.com/indexerrorcoders-le-compte-github-de-la-communaute-dindexerror/
