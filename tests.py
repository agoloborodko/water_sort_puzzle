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
        with self.assertRaises(AssertionError):
            obj.Vial(0, [1, 2, 3])
        with self.assertRaises(AssertionError):
            obj.Vial(0)
        with self.assertRaises(AssertionError):
            obj.Vial(4.5, [5])
        with self.assertRaises(TypeError):
            obj.Vial(4, 5)


class TestGameObjectsFunctions(unittest.TestCase):

    def test_check_vial_arguments_meet_requirements(self):
        with self.assertRaises(AssertionError):
            obj.check_vial_arguments_meet_requirements(0, [])
            obj.check_vial_arguments_meet_requirements(-1, [])
            obj.check_vial_arguments_meet_requirements(2, [1, 2, 3])

        obj.check_vial_arguments_meet_requirements(3, [1, 2, 3])
        obj.check_vial_arguments_meet_requirements(5, None)


if __name__ == '__main__':
    unittest.main()
