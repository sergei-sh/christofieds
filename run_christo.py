

import numpy as np

from christofieds.find_tsp_route import find_tsp_route
from graph_algos import half_mx_dist, verify_dist_mx

half_matrix = np.array([
    [8, 2, 8, 6, 2],
    [14, 20, 12, 20],
    [10, 20, 20],
    [16, 2],
    [20],
    ]) 

complete_tsp = half_mx_dist(half_matrix)
verify_dist_mx(complete_tsp)
find_tsp_route(complete_tsp)
