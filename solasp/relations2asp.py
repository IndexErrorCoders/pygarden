"""
Get all relations and groups of taxons in ASP-readable format.

"""

import taxons

ASP_DATA_FILE = 'data.lp'
ASP_ATOM_FRIEND = 'friend'
ASP_ATOM_ENEMY = 'enemy'


def stringify(predicate, args):
    return predicate + '(' + ','.join('"'+str(_)+'"' for _ in args) + ')'


with open(ASP_DATA_FILE, 'w') as fd:
    # write friends, then enemies
    for taxon, friends in taxons.FRIENDS.items():
        for friend in friends:
            fd.write(stringify(ASP_ATOM_FRIEND, (taxon, friend)) + '.\n')
    for taxon, enemies in taxons.ENEMIES.items():
        for enemy in enemies:
            fd.write(stringify(ASP_ATOM_ENEMY, (taxon, enemy)) + '.\n')

    # write taxons and associated group
    groups = (attr for attr in dir(taxons)
              if attr.startswith(taxons.PREFIX_TAXONS))
    for group in groups:
        group_name = group[len(taxons.PREFIX_TAXONS):].lower()
        for taxon in getattr(taxons, group):
            fd.write(stringify(group_name, [taxon]) + '.\n')
