from subprocess import run
a = run(r'python .\nwk2json.py .\2881_dating_Species.tre auspice', shell=True)
b = run(r'python .\merge_json.py .\auspice_tree_meta.json .\2881_dating_Species.json', shell=True)
