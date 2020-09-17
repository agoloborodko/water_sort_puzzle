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


if __name__ == '__main__':
    unittest.main()
