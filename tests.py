import unittest
import game_objects as obj


class TestVial(unittest.TestCase):

    def test_init(self):
        vial = obj.Vial(5)
        self.assertIsInstance(vial, obj.Vial)
        self.assertEqual(len(vial), 0)
        self.assertEqual(vial, [])
        self.assertEqual(vial.max_size, 5)

        vial = obj.Vial(4, [1, 2, 3])
        self.assertEqual(vial, [1, 2, 3])

        with self.assertRaises(AssertionError):
            obj.Vial(2, [1, 2, 3])
            obj.Vial(0, [1, 2, 3])
            obj.Vial(0)


if __name__ == '__main__':
    unittest.main()
