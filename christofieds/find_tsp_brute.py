""" 
Updated: 2017
Author: Sergei Shliakhtin
Contact: xxx.serj@gmail.com
Parser: Python3
Complexity: O(V!)
Notes: 

Brute-force implemnation. Finds the shortest path used to assess other algorithms.
"""

import itertools as it
from graph_algos import INF, path_length

def find_tsp_brute(dist_mx):
    """Implements naive TSP algortihm 

    dist_mx - numpy distance matrix, following triangle inequality. 0 is the start.
    return (route, length) - tuple of vertices to follow, length
    """

    vertices = range(dist_mx.shape[0])
    # routes without the starting and trailing 0 vertex 
    routes_inc = permutations_no_inverse(it.islice(vertices, 1, None))
    length_min = INF
    route_found = None
    for route_inc in routes_inc:
        route = [0] + list(route_inc) + [0]

        """DEBUG"""
        # print([v for v in route])

        length = path_length(dist_mx, path=iter(route))
        # print(length)
        if length < length_min:
            length_min = length
            route_found = route

    return route_found, length_min            

def permutations_no_inverse(iterable):    
    """Return the half of permutations, treating mirrored sequences as the same,
    e.g. (0, 1, 2) and (2, 1, 0) are the same.
    Assume 1) itertools.permutations returns tuples 2) they are in lexicographical order
    """

    all_perm = it.permutations(iterable)
    cur_start = None 
    starts_processed = set()
    for perm in all_perm:
        new_start = perm[0] 
        if new_start != cur_start:
            if cur_start != None:
                starts_processed.add(cur_start)
            cur_start = new_start
        if perm[-1] in starts_processed:
            continue
        else:
            yield perm

 
