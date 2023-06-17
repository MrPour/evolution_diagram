#!/usr/bin/python3

from sys import argv
from Bio import Phylo

old = Phylo.read(argv[1], 'nexus')
for i in old.get_terminals():
    organism = i.name.split('_')[2:4]
    i.name = ' '.join(organism)
Phylo.write(old, argv[1]+'.new', 'nexus')


