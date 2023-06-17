#!/usr/bin/python3

from pygbif import occurrences as oc
from pathlib import Path
import json
from itertools import chain
from sys import argv

# get table
fossils_file = Path(argv[1])
fossils = list()
with open(fossils_file, 'r') as f:
    for line in f:
        if line.startswith('#'):
            continue
        node, name, date = line.strip().split(',')
        date = -1 * float(date)
        fossils.append((node, name, date))
# get data
def get_location(node, name, date):
    raw_genus, *raw_species = name.split(' ')
    result = list()
    result = {'value': [0, 0, 1]}
    locations = list()
    q_results = oc.search(q=name, limit=100)
    q2_results = oc.search(q=raw_genus, limit=100)
    for i in chain(q_results['results'], q2_results['results']):
        species = i.get('scientificName', '')
        order = i.get('order', '')
        family = i.get('family', '')
        genus =  i.get('genus', '')
        rank = i.get('taxonRank', '')
        lon = i.get('decimalLongitude', '')
        if lon == '':
            continue
        lat = i.get('decimalLatitude', '')
        yield [node, name, str(date),
               species, order, family, genus, rank, str(lon), str(lat)]

results = list()
f = open(fossils_file.with_suffix('.csv'), 'w', encoding='utf-8')
f.write('node,name,date,species,order,family,genus,rank,lon,lat\n')
for node, name, date in fossils:
    for r in get_location(node, name, date):
        print(r)
        try:
            f.write(','.join(r) + '\n')
        except UnicodeEncodeError:
            pass
f.close()
    # results.extend(get_location(node, name, date))
# with open('map_data_new.json', 'w') as f:
#     json.dump(results, f, indent=4)
