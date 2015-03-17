__author__ = 'dstuckey'

import networkx as nx

G = nx.Graph()

# G.add_nodes_from([1,2,3])
G.add_nodes_from(['a','b','c','d','e','f','g','h','i'])

# G.add_edge('a','b')
G.add_weighted_edges_from([('a','b',4),('a','c',8),('b','c',11),('b','d',8),
    ('c','d',8),('c','e',7),('c','f',1),('d','e',2),('d','g',7),('d','h',4),
    ('e','f',6),('f','h',2),('g','h',14),('g','i',9),('h','i',10)])

print "num nodes: ", G.number_of_nodes()
print "num edges: ", G.number_of_edges()

print "edges: ", G.edges()

print "degree: ", G.degree()

print "a edges: ", G['a']

nx.write_weighted_edgelist(G, "example_1a.edgelist")