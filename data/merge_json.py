#!/usr/bin/python3
# merge meta json and tree json for auspice
import json
from sys import argv

meta_json = argv[1]
tree_json = argv[2]
merge_json = 'merge.json'
with open(argv[1], 'r') as _:
    meta = json.load(_)
with open(argv[2], 'r') as _:
    tree = json.load(_)
meta['tree'] = tree
with open(merge_json, 'w') as out:
    json.dump(meta, out)
