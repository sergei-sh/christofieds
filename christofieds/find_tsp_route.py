""" 
Updated: 2017
Author: Sergei Shliakhtin
Contact: xxx.serj@gmail.com
Compiler: Python3
Notes: 

Currently uses NetworkX for Blossom algorithm and graph_algos for other algorithms
"""

import networkx as nx
import numpy as np

from graph_algos import prims_mst, INF, induced_subgraph

def find_tsp_route(dist_mx):
    """Implements Chrisofieds algorithm to find a minimum-weight circuit (1.5 approximate) in a complete weighted
    graph, following triangle inequality

    dist_mx - distance matrix, following triangle inequality
    return - tuple of vertices to follow
    """

#Refer for set names G, T, O, M, to https://en.wikipedia.org/wiki/Christofides_algorithm

    import matplotlib.pyplot as plt

#Initial complete graph    
    G = dist_mx
#Extract Minimum Spanning Tree    
    T = prims_mst(dist_mx=G)
#Vertices with odd degree of MST
    O = odd_vertices(dist_mx=T)
    print("O ", O)
#Induced subgraph of G by O 
    (I, i_to_g_converter) = induced_subgraph(dist_mx=G, vertices=O)
    print("I ", I)

    assert I.size == np.count_nonzero(I), """Zero weights are not allowed (would mean 2 vertices are the same"""
    """in a metric space"""
    assert not np.any(I < 0), "Negative weights are not allowed in metric space"

#Invert all weights so that max_weight_matching gives us minimum-weight matching
#Weights must be positive (checked above)
    I_inv = np.float_power(I, -1)

    graph_I = nx.from_numpy_matrix(A=I_inv)
    print("Ix ", graph_I)
#Find a minimum-weight perfect matching
    dict_min = nx.max_weight_matching(G=graph_I, maxcardinality=True)
#Returns dictionary where each edge is doubled. I don't know why. The input Graph is clearly not
#a DiGraph...
    M = nx.Graph()
    M.add_edges_from([(i_to_g_converter(k), i_to_g_converter(v)) 
        for k, v 
        in dict_min.items()])

    M_mg = nx.MultiGraph(M)
    T_mg = dist_mx_to_networkx(T, netx_obj=nx.MultiGraph())
    H = nx.compose(M_mg, T_mg)

    nx.draw_circular(H, with_labels=True)
    #nx.draw_circular(nx.from_numpy_matrix(G), with_labels=True)
    plt.show()

def dist_mx_to_networkx(dist_mx, netx_obj=nx.Graph):
#creates graph but includes INF edges
   graph = nx.from_numpy_matrix(dist_mx, create_using=netx_obj) 
#INF edges coordinates as 2 rows
   inf_coord = np.where(dist_mx == INF)
   graph.remove_edges_from(zip(inf_coord[0], inf_coord[1]))
   return graph

def odd_vertices(dist_mx):
    """Take odd degree vertices from a graph   

    dist_mx - distance matrix
    return - tuple of vertices
    """
    return np.where(
        [(np.sum(dist_mx[row] != INF) % 2 == 1) 
        for row in range(0, dist_mx.shape[0])]
        )[0] 

    


