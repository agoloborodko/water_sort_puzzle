from game_objects import VialBoard
import copy
import queue
from exceptions import CannotSolveThisException


class GenVialBoard(VialBoard):
    gen = 0


def clone_vial_board(board):
    board_data = copy.deepcopy(board.data)
    board_path = copy.deepcopy(board.path)

    new_board = GenVialBoard(board_data)
    new_board.path = board_path

    if not isinstance(board, GenVialBoard):
        new_board.gen = 1
    else:
        new_board.gen = board.gen + 1

    return new_board


def solve_queue_wide(q):
    current_gen = 0
    while not q.empty():
        board = q.get()
        for i in range(len(board)):
            for j in range(len(board)):
                if board.can_move(i, j):
                    new_board = clone_vial_board(board)
                    new_board.move(i, j)
                    if new_board.solved():
                        return new_board
                    q.put(new_board)

                    if new_board.gen > current_gen:
                        current_gen = new_board.gen
                        print(f'current generation: {current_gen}, queue size: {q.qsize()}')

    raise CannotSolveThisException()


def solve(vial_board):
    q = queue.Queue()
    q.put(vial_board)

    if is_solvable(vial_board):
        return solve_queue_wide(q)
    else:
        raise CannotSolveThisException()


def is_solvable(vial_board):
    el_set = vial_board.get_set_of_items()
    if len(el_set) > len(vial_board):
        return False

    if check_each_el_fits_vial(vial_board):
        return True
    else:
        return False


def check_each_el_fits_vial(vial_board):
    counts = count_board_elements(vial_board)
    size = vial_board[0].max_size

    for v in counts.values():
        if v > size:
            return False
    return True


def count_board_elements(vial_board):
    d = {}
    for vial in vial_board:
        for el in vial:
            if el in d:
                d[el] += 1
            else:
                d[el] = 1
    return d
