__author__ = 'dstuckey'


import networkx as nx
from time import time
import dijkstra_impl as di


G = nx.read_weighted_edgelist("example_1a.edgelist")

print "num nodes: ", G.number_of_nodes()
print "num edges: ", G.number_of_edges()

print "edges: ", G.edges()

print "degree: ", G.degree()

# print "a edges: ", G['a']
# print G['a']['c']
# print G['a']['c']['weight']

start = time()
shortest = di.find_shortest_path(G,'a','i')
finish = time()

print "\n\nshortest path length: ", shortest[0]
print "shortest path: ", shortest[1]
print "elapsed time: %0.0f ns" % ((finish - start) * 10**9)