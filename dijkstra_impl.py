__author__ = 'dstuckey'

# This program solves weighted network shortest path problems using Dijkstra's Algorithm

import networkx as nx
from time import time

approx_infinite_distance = 1000

def find_shortest_path(graph, source, destination):
    # initialize v as a dictionary
    v = {}
    for node in graph.nodes():
        v[node] = 0 if node==source else approx_infinite_distance

    # initialize permanence dictionary
    perm = {}
    for node in graph.nodes():
        perm[node] = (node==source)

    last_perm = source

    # initialize d as an empty dictionary
    d = {}
    # for node in graph.nodes():
    #     if (source, node) in graph.edges():
    #         d[node] = source

    print "v: ", v
    print "perm: ", perm
    print "d: ", d

    while (not perm[destination]):
        candidate_edges = graph[last_perm]

        # update v and d
        for edge_dest in candidate_edges.keys():
            new_dist = v[last_perm] + candidate_edges[edge_dest]['weight']
            print edge_dest, " new candidate dist: ", new_dist
            if new_dist < v[edge_dest]:
                print "new shortest path to ", edge_dest
                v[edge_dest] = new_dist
                d[edge_dest] = last_perm

        # choose next permanent node
        next_perm_candidates = [n for n in perm.keys() if not perm[n]]
        min_dist = approx_infinite_distance
        print "next perm cands: ", next_perm_candidates
        for cand in next_perm_candidates:
            if v[cand] < min_dist:
                next_perm = cand
                min_dist = v[cand]

        # update last_perm var and permanence dictionary
        perm[next_perm] = True
        last_perm = next_perm

    path_length = v[destination]
    return path_length



G = nx.read_weighted_edgelist("example_1a.edgelist")

# print "num nodes: ", G.number_of_nodes()
# print "num edges: ", G.number_of_edges()
#
# print "edges: ", G.edges()
#
# print "degree: ", G.degree()
#
print "a edges: ", G['a']
print G['a']['c']
print G['a']['c']['weight']

start = time()
shortest = find_shortest_path(G,'a','i')
finish = time()

print "shortest path length: ", shortest