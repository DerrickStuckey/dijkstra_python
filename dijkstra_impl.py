__author__ = 'dstuckey'

# This program solves weighted network shortest path problems using Dijkstra's Algorithm

import networkx as nx
from time import time

approx_infinite_distance = 1000

def find_shortest_path(graph, source, destination):
    # initialize v as a dictionary
    init_v = lambda n: 0 if n==source else approx_infinite_distance
    # v = [init_v(n) for n in graph.nodes()]
    v_keys = [n for n in graph.nodes()]
    v = {}
    for key in graph.nodes():
        v[key] = init_v(key)

    # initialize permanence dictionary
    perm = {}
    for key in graph.nodes():
        perm[key] = (key==source)

    # initialize d as a dictionary


    print "v: ", v
    print "perm: ", perm



G = nx.read_weighted_edgelist("example_1a.edgelist")

print "num nodes: ", G.number_of_nodes()
print "num edges: ", G.number_of_edges()

print "edges: ", G.edges()

print "degree: ", G.degree()

print "a edges: ", G['a']

find_shortest_path(G,'a','i')