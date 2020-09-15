import unittest
import game_objects as obj


class TestVial(unittest.TestCase):

    def test_init(self):
        vial = obj.Vial(5)
        self.assertIsInstance(vial, obj.Vial)
        self.assertEqual(len(vial), 0)
        self.assertEqual(vial, [])
        self.assertEqual(vial.max_size, 5)


if __name__ == '__main__':
    unittest.main()
