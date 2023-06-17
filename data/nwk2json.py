#!/usr/bin/python3
from sys import argv
import json
from Bio import Phylo
from pathlib import Path
from random import randint

print('Usage: nwk2json.py <input_file> <echarts|auspice>')
tree_file = Path(argv[1])
tree_type = argv[2]
try:
    tree = Phylo.read(tree_file, 'nexus')
except Exception:
    tree = Phylo.read(tree_file, 'newick')

root = tree.root
n = 0
organisms = set()


def get_echarts_json(node):
    json_ = {'name': node.name if node.name is not None else '',
            # year
            'value': -1*float(node.branch_length),
            'type': 'node' if node.clades else 'leaf'}
    if node.clades:
        json_['children'] = []
        for ch in node.clades:
            json_['children'].append(get_echarts_json(ch))
    return json_


def get_auspice_json(node):
    # name: Order_family_genus_species_others
    if node.name is None:
        order, family, genus, species, *_ = list('_'*5)
    else:
        try:
            order, family, genus, species, *_ = node.name.split('_')
        except Exception:
            order, family, genus, species, *_ = list('_'*5)
    organism = '_'.join([genus, species]) if genus else '_'
    order = order.strip("'")
    family = family.strip("'")
    organism = organism.strip("'")
    global n, organisms
    if organism in organisms:
        organism = f'{organism}_{n}'
        n += 1
    else:
        organisms.add(organism)
    length = float(node.branch_length) if node.branch_length is not None else 0
    json_ = {'name': organism,
             'node_attrs': {
                 #'div': 0.01,
                            'div': -1*length,
                            'num_date': {'value': -1*length},
                            'order': {'value': order},
                            'family': {'value': family}},
             'branch_attrs': {'mutations': {}}}
    if node.clades:
        json_['children'] = []
        for ch in node.clades:
            json_['children'].append(get_auspice_json(ch))
    return json_


if tree_type == 'echarts':
    json_ = get_echarts_json(root)
elif tree_type == 'auspice':
    print('auspice json file should join with meta json!')
    json_ = get_auspice_json(root)
else:
    raise ValueError('tree_type must be echarts or auspice')
json_file = tree_file.with_suffix('.json')
with open(json_file, 'w') as f:
    json.dump(json_, f)
print(tree_file)
print(json_file)
