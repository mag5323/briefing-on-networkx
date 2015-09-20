import json
from networkx import *
from networkx.readwrite import json_graph

G = complete_graph(5)
JsonG = json_graph.node_link_data(G)
json.dump(JsonG, open('output.json', 'w'))
