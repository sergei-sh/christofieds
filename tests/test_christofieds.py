""" 
Updated: 2017
Author: Sergei Shliakhtin
Contact: xxx.serj@gmail.com
Notes: 

"""

import numpy as np
import unittest


from christofieds.find_tsp_route import odd_vertices
from graph_algos import INF

class TestChristo(unittest.TestCase):

    def test_odd_vertices(self):
        dist_mx = np.array([
            [INF, 1, 1, INF],
            [1, INF, 1, 1],
            [1, 1, INF, INF],
            [INF, 1, INF, INF],
            ])

        vert = odd_vertices(dist_mx)
        check = np.array([1, 3])

        self.assertEqual(np.ma.allequal(vert, check), True)

    def setUp(self):
        pass

    def tearDown(self):
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestChristo)
unittest.TextTestRunner(verbosity=2).run(suite)



