
import numpy as np
import time

import networkx as nx 
from christofieds import find_tsp_route, find_tsp_brute, log, log_debug
from graph_algos import half_mx_dist, verify_dist_mx, path_length, INF, generate_geometric_dist_mx

np.random.seed(0)

time_lst = []
factor = []
try:
    for vert in range(3, 11):
        tsp = generate_geometric_dist_mx(vert)
        
        tm = time.time()
        route = find_tsp_route(tsp)
        delta_tm = time.time() - tm

        length = path_length(tsp, path=route)
        log("Route found: ", route, length)
        fact = 0
        if vert < 9:
             log(tsp)
        route_b, len_b = find_tsp_brute(tsp)
        log("Route brute: ", route_b)
        fact = length/len_b
        factor.append(fact)

        log("Length Christofieds: {}, Length Brute: {},  approx {}".format(length, len_b, fact))
        log("Time: {}".format(delta_tm))
        time_lst.append(delta_tm)
except KeyboardInterrupt:
    pass
finally:    
    log(factor)        
    log(time_lst)


