"""
Default data about relations between taxons and taxons themselves.

"""
# prefix of variables describing taxons
PREFIX_TAXONS = 'TAXONS_'


FRIENDS = {
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

ENEMIES = {
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

TAXONS_LEGUMES = sorted({
    'carotte', 'concombre', 'tomate', 'epinard', 'patate', 'navet', 'asperge',
    'laitue', 'haricot', 'poireau', 'radis', 'choux', 'courgette', 'epinard',
    'betterave', 'pois', 'potiron', 'aubergine', 'endive', 'artichaut', 'navet'
})

TAXONS_FRUITS = sorted({
    'fraise', 'melon', 'framboise', 'groseille', 'cassis', 'pomme', 'poire',
    'abricot', 'raisin', 'prune', 'peche', 'cerise', 'noisette', 'pasteque',
    'figue', 'citron', 'orange'
})

TAXONS_AROMATES = sorted({
    'ail', 'piment', 'thym', 'persil', 'estragon', 'basilic', 'aneth',
    'menthe', 'ciboulette', 'echalotte', 'oignon', 'celeri', 'moutarde',
    'cerfeuil', 'melisse', 'tanaisie'
})

TAXONS_CEREALES = sorted({
    'ble', 'mais', 'sarasin', 'orge', 'millet', 'seigle', 'epautre',
    'lentilles', 'quinoa'
})

TAXONS_FLEURS = sorted({
    'oeillet Inde', 'tabac', 'capucine', 'ortie', 'souci', 'petunia',
    'bourrache', 'myosotis', 'chicoree', 'chardon', 'coquelicot', 'echinacee',
    'aster', 'lavande', 'consoude', 'prele', 'hysope', 'micromerie', 'phlomis',
    'dracocephale', 'asclepiade', 'ammi', 'centauree', 'buplevre', 'ciste',
    'zinnia', 'sceau-de-salomon', 'eupatoire', 'miscanthus', 'verveine',
    'luzerne', 'colza', 'lin', 'trefle', 'tournesol', 'rose', 'pissenlit',
    'bleuet', 'pelargonium', 'armoise'
})
