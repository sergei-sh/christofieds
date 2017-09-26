""" 
Updated: 2017
Author: Sergei Shliakhtin
Contact: xxx.serj@gmail.com
Parser: Python3
Complexity: O(V^3)
Notes: 

Currently uses NetworkX for Blossom algorithm and graph_algos for other algorithms
"""

import networkx as nx
import numpy as np

from graph_algos import prims_mst, INF, induced_subgraph, odd_vertices, eulerian_circuit, verify_dist_mx

def find_tsp_route(dist_mx):
    """Implements Chrisofieds algorithm to find a minimum-weight circuit (1.5 approximate) in a complete weighted
    graph, following triangle inequality

    dist_mx - distance matrix, following triangle inequality. 0-th vertex is assumed to be the start
    return - tuple of vertices to follow
    """

    if dist_mx.shape[0] < 3:
        raise ValueError("Need at least 3 vertices")

    verify_dist_mx(dist_mx)

#Refer for set names G, T, O, M, to https://en.wikipedia.org/wiki/Christofides_algorithm


#Initial complete graph    
    G = dist_mx
#Extract Minimum Spanning Tree    
    T = prims_mst(dist_mx=G) # O(V^2)
#Vertices with odd degree of MST
    print("MST", T)
    O = odd_vertices(dist_mx=T) #O(V^2)
    print("O ", O)
#Induced subgraph of G by O 
    (I, i_to_g_converter) = induced_subgraph(dist_mx=G, vertices=O) # ?O(V^2)
    print("I ", I)

    if not I.size == np.count_nonzero(I):
        raise ValueError("""Zero weights are not allowed (would mean 2 vertices are the same"""
    """in a metric space""")
    if np.any(I < 0):
        raise ValueError("Negative weights are not allowed in metric space")

#Invert all weights so that max_weight_matching gives us minimum-weight matching
#Weights must be positive (checked above)
    I_inv = np.float_power(I, -1) # O(V^2)

    graph_I = nx.from_numpy_matrix(A=I_inv)
    print("Ix ", graph_I)
#Find a minimum-weight perfect matching
    dict_min = nx.max_weight_matching(G=graph_I, maxcardinality=True) # O(V^3)
    print("Perf matching: ", dict_min)
#Returns dictionary where each edge is doubled. I don't know why. The input Graph is clearly not
#a DiGraph...
    M = nx.Graph()
    M.add_edges_from([(i_to_g_converter(k), i_to_g_converter(v)) 
        for k, v 
        in dict_min.items()]) # O(E)

    print("M ", M.edges())        

# Compose MST and p.matching    
    M_mg = nx.MultiGraph(M)
    T_mg = dist_mx_to_networkx(T, netx_obj=nx.MultiGraph())
    
    T_mg.add_edges_from(M_mg.edges()) # ?O(2V)
    H = T_mg 
    print("H ", H.edges())

    eulerian_crt_gen = nx.eulerian_circuit(H) # O((V + E))
    eulerian_crt = np.array([v for v in eulerian_crt_gen]).flatten()
    print("Eul: ", eulerian_crt)
    u, idxs = np.unique(eulerian_crt, return_index=True) # O(V^2)
    hamilton_crt = np.concatenate((eulerian_crt[np.sort(idxs)], np.array([0])), axis=0)

    return hamilton_crt

def dist_mx_to_networkx(dist_mx, netx_obj=nx.Graph):
    """Convert distance matrix to networkx graph"""
    #creates graph but includes INF edges
    graph = nx.from_numpy_matrix(dist_mx, create_using=netx_obj) 
    
    #INF edges coordinates as 2 rows
    inf_coord = np.where(dist_mx == INF)
    #remove INF edges   
    graph.remove_edges_from(zip(inf_coord[0], inf_coord[1]))
    return graph

    


