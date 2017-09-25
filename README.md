
### About:
Christofieds algorithm implementation for Travelling Salesman problem.
Implemented from here https://en.wikipedia.org/wiki/Christofides_algorithm
Currently uses NetworkX for Blossom algorithm and some other routines and graph_algos for other algorithms.

### Measurements 

The complexity is O(V^3)

![measurements](https://github.com/sergei-sh/christofieds/blob/master/figs/time.png)

The approximation ration is 1.5 at most

![measurements](https://github.com/sergei-sh/christofieds/blob/master/figs/approx.png)

### Installation :
1) pip3
networkx
(matplotlib) if need drawing

2) Needs graph_algos git project (or symbolic link) cloned into source directory.
