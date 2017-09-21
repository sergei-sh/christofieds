
import numpy as np
import unittest


from christofieds.find_tsp_brute import find_tsp_brute
from graph_algos import INF, verify_dist_mx

class TestBrute(unittest.TestCase):

    def test_brute1(self):
        dist_mx = np.array(
                   [[INF, 2, 1, 5],
                   [2, INF, 4, 7],
                   [1, 4, INF, 6],
                   [5, 7, 6, INF]])

        verify_dist_mx(dist_mx)
        vert, length = find_tsp_brute(dist_mx)

        self.assertEqual(list(vert), [0, 1, 3, 2, 0])
        self.assertEqual(length, 16)

    def setUp(self):
        pass

    def tearDown(self):
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestBrute)
unittest.TextTestRunner(verbosity=2).run(suite)



