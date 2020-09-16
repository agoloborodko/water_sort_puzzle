import unittest
import puzzle_solver as ps


class TestSolver(unittest.TestCase):

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
            self.assertIn(i, board_1_solved)


if __name__ == '__main__':
    unittest.main()
