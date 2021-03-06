import unittest


class TestWarmupExercises(unittest.TestCase):

    def test_warmup1(self):
        from warmup1 import zeroremover
        self.assertEqual(
            zeroremover([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]),
            [5, 3, 2, 6, 2, 7, 2, 5]
        )
        self.assertEqual(
            zeroremover([4, 0, 0, 1, 3]),
            [4, 1, 3]
        )
        self.assertEqual(
            zeroremover([1, 2, 3]), [1, 2, 3]
        )
        self.assertEqual(
            zeroremover([0, 0, 0]), []
        )
        self.assertEqual(
            zeroremover([]), []
        )

    def test_warmup2(self):
        from warmup2 import sort_descending
        self.assertEqual(
            sort_descending([5, 1, 3, 4, 2]),
            [5, 4, 3, 2, 1]
        )
        self.assertEqual(
            sort_descending([0, 0, 0, 4, 0]),
            [4, 0, 0, 0, 0]
        )
        self.assertEqual(
            sort_descending([1]), [1]
        )
        self.assertEqual(
            sort_descending([]), []
        )

    def test_warmup3(self):
        from warmup3 import length_check
        self.assertFalse(length_check(7, [6, 5, 5, 3, 2, 2, 2]))
        self.assertFalse(length_check(5, [5, 5, 5, 5, 5]))
        self.assertTrue(length_check(5, [5, 5, 5, 5]))
        self.assertTrue(length_check(3, [1, 1]))
        self.assertTrue(length_check(1, []))
        self.assertFalse(length_check(0, []))

    def test_warmup4(self):
        from warmup4 import front_elimination
        self.assertEqual(
            front_elimination(4, [5, 4, 3, 2, 1]),
            [4, 3, 2, 1, 1]
        )
        self.assertEqual(
            front_elimination(11, [14, 13, 13, 13, 12, 10, 8, 8, 7, 7, 6, 6, 4, 4, 2]),
            [13, 12, 12, 12, 11, 9, 7, 7, 6, 6, 5, 6, 4, 4, 2]
        )
        self.assertEqual(
            front_elimination(1, [10, 10, 10]),
            [9, 10, 10]
        )
        self.assertEqual(
            front_elimination(3, [10, 10, 10]),
            [9, 9, 9]
        )
        self.assertEqual(front_elimination(1, [1]), [0])

    def test_challenge(self):
        from challenge import havel_hakimi
        self.assertFalse(havel_hakimi([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]))
        self.assertFalse(havel_hakimi([4, 2, 0, 1, 5, 0]))
        self.assertTrue(havel_hakimi([3, 1, 2, 3, 1, 0]))
        self.assertTrue(havel_hakimi([16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]))
        self.assertTrue(havel_hakimi([14, 10, 17, 13, 4, 8, 6, 7, 13, 13, 17, 18, 8, 17, 2, 14, 6, 4, 7, 12]))
        self.assertFalse(havel_hakimi([15, 18, 6, 13, 12, 4, 4, 14, 1, 6, 18, 2, 6, 16, 0, 9, 10, 7, 12, 3]))
        self.assertFalse(havel_hakimi([6, 0, 10, 10, 10, 5, 8, 3, 0, 14, 16, 2, 13, 1, 2, 13, 6, 15, 5, 1]))
        self.assertFalse(havel_hakimi([2, 2, 0]))
        self.assertFalse(havel_hakimi([3, 2, 1]))
        self.assertTrue(havel_hakimi([1, 1]))
        self.assertFalse(havel_hakimi([1]))
        self.assertTrue(havel_hakimi([]))


if __name__ == '__main__':
    unittest.main()
