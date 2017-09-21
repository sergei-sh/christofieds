
import numpy as np
import time

import networkx as nx 
from christofieds import find_tsp_route, find_tsp_brute
from graph_algos import half_mx_dist, verify_dist_mx, path_length, INF, graph_dist_mx

"""
half_matrix = np.array([
    [8, 2, 8, 6, 2],
    [14, 20, 12, 20],
    [10, 20, 20],
    [16, 2],
    [20],
    ]) 

complete_tsp = half_mx_dist(half_matrix)
verify_dist_mx(complete_tsp)
hamilton_crt = find_tsp_route(complete_tsp)
print("Found approximate shortest path: ", hamilton_crt)
"""

np.random.seed(0)

time_lst = []
factor = []
try:
    for vert in range(3, 30):
        tsp = half_mx_dist(np.random.randint(low=1, high=100, size=(vert, vert)))
        
        tm = time.time()
        route = find_tsp_route(tsp)
        print("Route found: ", route)
        delta_tm = time.time() - tm
        length = path_length(tsp, path=route)

        fact = 0
        if vert < 9:
            print(tsp)
            route_b, len_b = find_tsp_brute(tsp)
            fact = length/len_b
        factor.append(fact)

        print("Length Christofieds: {}, Length Brute: {},  approx {}".format(length, len_b, fact))
        print("Time: {}".format(delta_tm))
        time_lst.append(delta_tm)
except KeyboardInterrupt:
    pass
finally:    
    print(factor)        
    print(time_lst)


