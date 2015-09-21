import json
from networkx import *
from networkx.readwrite import json_graph

# Generating a random graph
# gnp_random_graph(Nodes, Probability for edge creation)
G = gnp_random_graph(10, 0.4)

# Get degrees
Degrees = G.degree()

# Get max degree node
MaxDeg = max(Degrees, key=Degrees.get)

# Get neighbors of MaxDeg
Neighbors = G.neighbors(MaxDeg)

# Generating json format dic
JsonG = json_graph.node_link_data(G)

# Coloring max deg and it's neighbors
JsonG['nodes'][MaxDeg]['group'] = 1

for node in Neighbors:
    JsonG['nodes'][node]['group'] = 1

json.dump(JsonG, open('output.json', 'w'))
