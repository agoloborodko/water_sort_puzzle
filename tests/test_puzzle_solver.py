import unittest
import puzzle_solver as ps


class TestSolver(unittest.TestCase):

    def test_clone_vial_board(self):
        board = ps.VialBoard(
            [
                [0, 1, 0],
                [1, 1, 0],
                []
            ]
        )
        board.move(0, 2)

        new_board = ps.clone_vial_board(board)
        self.assertEqual(board, new_board)
        self.assertEqual(board.path, new_board.path)

        new_board.move(1, 2)
        self.assertNotEqual(board, new_board)
        self.assertNotEqual(board.path, new_board.path)

    def test_clone_vial_board_generation(self):
        board = ps.VialBoard(
            [
                [0, 1, 0],
                [1, 1, 0],
                []
            ]
        )
        board.move(0, 2)

        new_board = ps.clone_vial_board(board)
        self.assertEqual(1, new_board.gen)
        new_board = ps.clone_vial_board(new_board)
        self.assertEqual(2, new_board.gen)

    def test_solve(self):
        board_1 = ps.VialBoard(
            [
                [0, 1, 0],
                [1, 1, 0],
                []
            ]
        )
        board_1_target = ps.VialBoard(
            [
                [0, 0, 0],
                [1, 1, 1],
                []
            ]
        )
        board_1_solved = ps.solve(board_1)
        for i in board_1_solved:
            self.assertIn(i, board_1_target)

    def test_solve_2(self):
        board = ps.VialBoard(
            [
                [1, 2, 2, 1],
                [2, 3, 5, 1],
                [3, 3, 5, 4],
                [1, 4, 4, 5],
                [5, 2, 3, 4],
                [],
                []
            ]
        )
        board_solved = ps.solve(board)
        self.assertTrue(board_solved.solved())

        print(board)
        print(board_solved)
        print(board_solved.path)

    def test_solve_3(self):
        board = ps.VialBoard(
            [
                [7, 5, 1, 11],
                [8, 11, 3, 3],
                [4, 9, 7, 1],
                [8, 11, 10, 9],
                [6, 4, 12, 4],
                [10, 11, 8, 1],
                [12, 8, 5, 6],
                [6, 12, 3, 10],
                [9, 10, 1, 6],
                [2, 7, 2, 2],
                [7, 3, 12, 9],
                [2, 4, 5, 5],
                [],
                []
            ]
        )
        board_solved = ps.solve(board)

        self.assertTrue(board_solved.solved())
        print(board)
        print(board_solved)
        print(board_solved.path)

    def test_solve_4(self):
        board = ps.VialBoard(
            [
                [1, 10, 11, 1],
                [2, 7, 8, 4],
                [3, 10, 8, 11],
                [4, 1, 3, 6],
                [5, 6, 9, 10],
                [6, 10, 12, 9],
                [7, 12, 12, 6],
                [8, 5, 2, 4],
                [9, 5, 12, 8],
                [7, 1, 11, 2],
                [7, 11, 2, 5],
                [4, 3, 3, 9],
                [],
                []
            ]
        )
        board_solved = ps.solve(board)

        self.assertTrue(board_solved.solved())
        print(board)
        print(board_solved)
        print(board_solved.path)

    def test_is_path_repeats(self):
        path = [(0, 1), (1, 0), (0, 1), (1, 0)]
        self.assertTrue(ps.is_path_repeats(path))

        path = [(1, 2), (2, 3), (1, 3), (1, 2), (2, 3), (1, 3)]
        self.assertTrue(ps.is_path_repeats(path))

        path = [(1, 2), (1, 2), (2, 3), (1, 2), (2, 3), (1, 2), (2, 3)]
        self.assertTrue(ps.is_path_repeats(path, 2))

        path = [(1, 2), (2, 3), (1, 3), (1, 2), (2, 3), (1, 3)]
        self.assertFalse(ps.is_path_repeats(path, 2))

    def test_unsolvable(self):
        board = ps.VialBoard(
            [
                [7, 5, 1, 11],
                [8, 11, 3, 3],
                [4, 9, 7, 1],
                [8, 11, 10, 9],
                [2, 4, 5, 5],
                [],
                []
            ]
        )

        self.assertFalse(ps.is_solvable(board))
        with self.assertRaises(ps.CannotSolveThisException):
            ps.solve(board)

    def test_solvable(self):
        board = ps.VialBoard(
            [
                [1, 2, 2, 1],
                [2, 3, 5, 1],
                [3, 3, 5, 4],
                [1, 4, 4, 5],
                [5, 2, 3, 4],
                [],
                []
            ]
        )

        self.assertTrue(ps.is_solvable(board))

    def test_count_board_elements(self):
        board = ps.VialBoard(
            [
                [1, 2, 2, 1],
                [2, 3, 5, 1],
                [3, 3, 5, 4],
                [1, 4, 4, 5],
                [5, 2, 3, 4],
                [],
                []
            ]
        )

        d = ps.count_board_elements(board)
        self.assertEqual(
            {1: 4, 2: 4, 3: 4, 4: 4, 5: 4},
            d
        )

    def test_check_each_el_fits_vial(self):
        board_1 = ps.VialBoard(
            [
                [1, 2, 2, 1],
                [2, 3, 1, 1],
                [3, 3, 2, 3],
                []
            ]
        )
        board_2 = ps.VialBoard(
            [
                [1, 2, 2, 1],
                [2, 2, 1, 1],
                [3, 2, 2, 3],
                []
            ]
        )

        self.assertTrue(ps.check_each_el_fits_vial(board_1))
        self.assertFalse(ps.check_each_el_fits_vial(board_2))

    def test_move_is_reasonable(self):
        board = ps.VialBoard(
            [
                [1, 2],
                [3, 3],
                [1],
                []
            ]
        )

        self.assertTrue(ps.move_is_reasonable(board, (0, 3)))
        self.assertFalse(ps.move_is_reasonable(board, (1, 3)))
        self.assertFalse(ps.move_is_reasonable(board, (2, 3)))

    def test_move_is_reasonable_repeats(self):
        board = ps.VialBoard(
            [
                [2, 1],
                [1],
                [1, 2, 3]
            ]
        )

        self.assertTrue(ps.move_is_reasonable(board, (1, 0)))
        board.move(1, 0)
        self.assertFalse(ps.move_is_reasonable(board, (0, 1)))

    def test_calc_water_depth(self):
        vial = [1, 2, 3]
        self.assertEqual(1, ps.calc_water_depth(vial))

        vial = [1, 2, 2]
        self.assertEqual(2, ps.calc_water_depth(vial))

        vial = [1, 1]
        self.assertEqual(2, ps.calc_water_depth(vial))

        vial = []
        self.assertEqual(0, ps.calc_water_depth(vial))

        vial = [1]
        self.assertEqual(1, ps.calc_water_depth(vial))

    def test_move_cleans_upper_el(self):
        board = ps.VialBoard(
            [
                ps.Vial(3, [1, 2, 2]),
                ps.Vial(3, [2]),
                ps.Vial(3, [1, 2])
            ]
        )

        self.assertTrue(ps.move_cleans_upper_el(board[0], board[1]))
        self.assertFalse(ps.move_cleans_upper_el(board[0], board[2]))


if __name__ == '__main__':
    unittest.main()
