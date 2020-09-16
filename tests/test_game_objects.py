import unittest
import game_objects as obj
import exceptions as ex


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

    def test_init_from_vial(self):
        vial_1 = obj.Vial(4, [1, 2, 3])
        vial_2 = obj.Vial(5, vial_1)
        self.assertEqual(vial_1, vial_2)
        self.assertEqual(5, vial_2.max_size)

    def test_is_appendable(self):
        vial_1 = obj.Vial(2)
        self.assertTrue(vial_1.can_accept(1))

        vial_2 = obj.Vial(1, [0])
        self.assertFalse(vial_2.can_accept(0))
        self.assertFalse(vial_2.can_accept(1))

        vial_3 = obj.Vial(2, [0])
        self.assertFalse(vial_3.can_accept(1))
        self.assertTrue(vial_3.can_accept(0))

    def test_append(self):
        vial_1 = obj.Vial(2)
        vial_1.append(1)
        self.assertEqual(vial_1, [1])

        vial_1.append(2)
        self.assertEqual(vial_1, [1, 2])

        vial_3 = obj.Vial(2, [1, 1])
        with self.assertRaises(ex.VialIsFullException):
            vial_3.append(1)

    def test_pop(self):
        vial_1 = obj.Vial(3, [1, 2, 3])
        x = vial_1.pop()
        self.assertEqual(x, 3)
        self.assertEqual(vial_1, [1, 2])

        vial_2 = obj.Vial(3)
        with self.assertRaises(IndexError):
            vial_2.pop()

    def test_is_full(self):
        vial_1 = obj.Vial(3, [1, 2, 3])
        vial_2 = obj.Vial(4, [1, 2, 3])
        self.assertTrue(vial_1.is_full())
        self.assertFalse(vial_2.is_full())

    def test_is_empty(self):
        vial_1 = obj.Vial(3, [])
        vial_2 = obj.Vial(4)
        vial_3 = obj.Vial(2, [1])

        self.assertTrue(vial_1.is_empty())
        self.assertTrue(vial_2.is_empty())
        self.assertFalse(vial_3.is_empty())


class TestGameObjectsFunctions(unittest.TestCase):

    def test_check_vial_arguments_meet_requirements(self):
        with self.assertRaises(AssertionError):
            obj.check_vial_arguments_meet_requirements(0, [])
        with self.assertRaises(AssertionError):
            obj.check_vial_arguments_meet_requirements(-1, [])
        with self.assertRaises(AssertionError):
            obj.check_vial_arguments_meet_requirements(2, [1, 2, 3])

        obj.check_vial_arguments_meet_requirements(3, [1, 2, 3])
        obj.check_vial_arguments_meet_requirements(5, None)

    def test_check_board_arguments_meet_requirements(self):
        vial_1 = obj.Vial(3, [1, 2, 3])
        vial_2 = obj.Vial(3)
        vial_3 = obj.Vial(5, [1, 2])

        obj.check_board_arguments_meet_requirements([vial_1, vial_2])

        with self.assertRaises(AssertionError):
            obj.check_board_arguments_meet_requirements([vial_1, vial_2, vial_3])
        with self.assertRaises(AssertionError):
            obj.check_board_arguments_meet_requirements([vial_1])
        with self.assertRaises(AssertionError):
            obj.check_board_arguments_meet_requirements([vial_1, 5])
        with self.assertRaises(AssertionError):
            obj.check_board_arguments_meet_requirements([])
        with self.assertRaises(AssertionError):
            obj.check_board_arguments_meet_requirements([1, 2, 2])


class TestVialBoard(unittest.TestCase):

    def setUp(self):
        self.vial_1 = obj.Vial(3, [1, 2, 3])
        self.vial_2 = obj.Vial(3)
        self.vial_3 = obj.Vial(5, [1, 2])
        self.vial_4 = obj.Vial(3, [1, 1])
        self.vial_5 = obj.Vial(3, [10])
        self.vial_board = obj.VialBoard([self.vial_1, self.vial_2, self.vial_4, self.vial_5])

    def test_init(self):
        self.assertIsInstance(self.vial_board, obj.VialBoard)

        with self.assertRaises(AssertionError):
            obj.VialBoard([1, 2, 3])
        with self.assertRaises(AssertionError):
            obj.VialBoard([self.vial_2, 2, 3])
        with self.assertRaises(AssertionError):
            obj.VialBoard([self.vial_3])

    def test_init_from_lists(self):
        vial_board = obj.VialBoard(
            [
                [0, 1, 1],
                [],
                [1, 0, 0]
            ]
        )
        self.assertIsInstance(vial_board, obj.VialBoard)
        self.assertEqual(vial_board[0], [0, 1, 1])

    def test_move(self):
        self.vial_board.move(0, 1)
        self.assertEqual(self.vial_board[0], [1, 2])
        self.assertEqual(self.vial_board[1], [3])

    def test_move_all(self):
        self.vial_board.move(2, 1)
        self.assertEqual(self.vial_board[2], [])
        self.assertEqual(self.vial_board[1], [1, 1])

    def test_print(self):
        print(self.vial_board)


if __name__ == '__main__':
    unittest.main()
