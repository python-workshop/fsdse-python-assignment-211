from unittest import TestCase


class TestMove_zeroes(TestCase):
    def test_move_zeroes(self):
        try:
            from build import move_zeroes
        except ImportError:
            self.assertFalse("no function found")

        self.assertRaises(TypeError, move_zeroes, None)
        array = [0, 1, 0, 3, 12]
        move_zeroes(array)
        self.assertEqual(array, [1, 3, 12, 0, 0])
        array = [1, 0]
        move_zeroes(array)
        self.assertEqual(array, [1, 0])
        array = [0, 1]
        move_zeroes(array)
        self.assertEqual(array, [1, 0])
        array = [0]
        move_zeroes(array)
        self.assertEqual(array, [0])
        array = [1]
        move_zeroes(array)
        self.assertEqual(array, [1])
        array = [1, 1]
        move_zeroes(array)
        self.assertEqual(array, [1, 1])
