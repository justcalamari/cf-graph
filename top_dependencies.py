import networkx as nx

g = nx.read_yaml('graph.yml')
order = sorted(list(g.nodes), key=lambda x: len(nx.descendants(g, x)), reverse=True)

with open('top_100.txt', 'w') as f:
    f.write('\n'.join(order[:100]))
