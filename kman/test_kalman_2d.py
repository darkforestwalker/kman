from kalman_2d import KF2D

import unittest

class TestKF2D(unittest.TestCase):
    def test_can_construct_with_a_o_av_ov(self):
        a = 12.25
        o = 3.3
        av = 0
        ov = 0

        kf2d = KF2D(\
                initial_a=a,
                initial_av=av
                initial_o=o,
                initial_ov=ov,
                )
        self.assertAlmostEqual(kf2d.a[0], a)
        self.assertAlmostEqual(kf2d.o[0], o)
        self.assertAlmostEqual(kf2d.av[0], av)
        self.assertAlmostEqual(kf2d.ov[0], ov)

