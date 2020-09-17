import unittest
import game_objects as obj
import exceptions as ex


class TestPath(unittest.TestCase):

    def test_init(self):
        p = obj.Path([(0, 1), (1, 2)])
        self.assertIsInstance(p, obj.Path)
        with self.assertRaises(AssertionError):
            p = obj.Path([(0, 1), (1, 2, 3)])

    def test_str(self):
        p = obj.Path([(0, 1), (1, 2)])
        self.assertEqual('1->2, 2->3', p.__str__())

        p = obj.Path([(0, 1), (0, 1), (1, 2), (0, 1)])
        self.assertEqual('1->2, 2->3, 1->2', p.__str__())

        p = obj.Path([(0, 1), (0, 1), (0, 1)])
        self.assertEqual('1->2', p.__str__())

    def test_validate_path(self):
        p1 = [(0, 1), (1, 2)]
        obj.validate_path(p1)

        p2 = [(0, 1), (1, 2, 3)]
        p3 = [1, 2]
        p4 = 'Hello'

        with self.assertRaises(AssertionError):
            obj.validate_path(p2)
        with self.assertRaises(AssertionError):
            obj.validate_path(p3)
        with self.assertRaises(AssertionError):
            obj.validate_path(p4)


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

    def test_check_type_list_of_lists(self):
        l_1 = [[], [1, 2]]
        l_2 = [1, []]
        l_3 = 5
        v1 = obj.Vial(5)
        l_4 = [v1]
        self.assertTrue(obj.check_type_list_of_lists(l_1))
        self.assertFalse(obj.check_type_list_of_lists(l_2))
        self.assertFalse(obj.check_type_list_of_lists(l_3))
        self.assertFalse(obj.check_type_list_of_lists(l_4))

    def test_check_type_list_of_vials(self):
        l_1 = [[], [1, 2]]
        l_2 = 5
        v1 = obj.Vial(5)
        l_3 = [v1]
        self.assertFalse(obj.check_type_list_of_vials(l_1))
        self.assertFalse(obj.check_type_list_of_vials(l_2))
        self.assertTrue(obj.check_type_list_of_vials(l_3))

    def test_raise_exception_if_not_list_of_lists(self):
        l_1 = [[], [1, 2]]
        l_2 = [1, []]
        l_3 = 5
        v1 = obj.Vial(5)
        l_4 = [v1]

        obj.raise_exception_if_not_list_of_lists(l_1)
        with self.assertRaises(TypeError):
            obj.raise_exception_if_not_list_of_lists(l_2)
        with self.assertRaises(TypeError):
            obj.raise_exception_if_not_list_of_lists(l_3)
        with self.assertRaises(TypeError):
            obj.raise_exception_if_not_list_of_lists(l_4)

    def test_get_max_internal_list_size(self):
        l_1 = [[], [1, 2]]
        l_2 = [[], []]

        self.assertEqual(2, obj.get_max_internal_list_size(l_1))
        self.assertEqual(0, obj.get_max_internal_list_size(l_2))

    def test_make_vials_from_lists(self):
        l_1 = [[], [1, 2]]
        l_2 = [[], []]

        v_1 = obj.make_vials_from_lists(l_1)
        v_2 = obj.make_vials_from_lists(l_2)

        for i in v_1:
            self.assertIsInstance(i, obj.Vial)
            self.assertEqual(2, i.max_size)

        for i in v_2:
            self.assertIsInstance(i, obj.Vial)
            self.assertEqual(2, i.max_size)


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
        self.assertEqual([0, 1, 1], vial_board[0])

        vial_board.move(0, 1)
        self.assertEqual([0], vial_board[0])
        self.assertEqual([1, 1], vial_board[1])
        self.assertEqual([1, 1], vial_board[1])
        self.assertEqual([(0, 1), (0, 1)], vial_board.path)

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

    def test_restart_game(self):
        board_1 = obj.VialBoard([
            [1, 2, 3],
            []
        ])
        board_2 = obj.VialBoard([
            [1, 2, 3],
            []
        ])

        board_1.move(0, 1)
        self.assertNotEqual(board_1, board_2)
        board_1.restart_game()
        self.assertEqual(board_1, board_2)
        self.assertEqual([], board_1.path)

    def test_solved(self):
        board_1 = obj.VialBoard([
            [1, 1],
            [2, 2],
            []
        ])
        board_2 = obj.VialBoard([
            [1, 2],
            [2, 1],
            []
        ])
        board_3 = obj.VialBoard([
            [1],
            [1],
            []
        ])
        self.assertTrue(board_1.solved())
        self.assertFalse(board_2.solved())
        self.assertFalse(board_3.solved())

    def test_get_set_of_items(self):
        board_1 = obj.VialBoard([
            [1, 1, 3],
            [2, 2, 1],
            []
        ])
        s = board_1.get_set_of_items()
        self.assertEqual(s, {1, 2, 3})

    def test_get_path(self):
        board = obj.VialBoard([
            [1, 1, 2],
            [2, 2, 1],
            []
        ])
        board.move(2, 0)
        self.assertEqual([], board.path)
        board.move(0, 2)
        self.assertEqual([(0, 2)], board.path)
        board.move(1, 0)
        self.assertEqual([(0, 2), (1, 0)], board.path)
        board.move(1, 0)
        self.assertEqual([(0, 2), (1, 0)], board.path)

        board_2 = obj.VialBoard([
            [1, 1],
            [2, 2],
            []
        ])
        board_2.move(0, 2)
        self.assertEqual([(0, 2), (0, 2)], board_2.path)

    def test_get_path_for_multimove(self):
        board = obj.VialBoard([
            [1, 1],
            []
        ])

        board.move(0, 1)
        self.assertEqual([(0, 1), (0, 1)], board.path)

    def test_step_back(self):
        board = obj.VialBoard([
            [1, 1],
            []
        ])
        board.move(0, 1)
        board.step_back()
        self.assertEqual([[1, 1], []], board)
        self.assertEqual([], board.path)


if __name__ == '__main__':
    unittest.main()
