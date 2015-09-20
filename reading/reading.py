import json
from networkx import *
from networkx.readwrite import json_graph

Edges = open('net.edges').read().splitlines()
G = parse_edgelist(Edges, delimiter = ' ')
JsonG = json_graph.node_link_data(G)
json.dump(JsonG, open('output.json', 'w'))
