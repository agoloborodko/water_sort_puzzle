from game_objects import VialBoard
import copy
import queue
from exceptions import CannotSolveThisException


def clone_vial_board(board):
    board_data = copy.deepcopy(board.data)
    board_path = copy.deepcopy(board.path)
    new_board = VialBoard(board_data)
    new_board.path = board_path

    return new_board


def solve(vial_board):
    if vial_board.solved():
        return vial_board
    else:
        for i in range(len(vial_board)):
            for j in range(len(vial_board)):
                if vial_board.can_move(i, j):
                    new_vial_board = copy.deepcopy(vial_board)
                    new_vial_board.move(i, j)
                    solve(new_vial_board)


