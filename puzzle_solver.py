from game_objects import VialBoard


def solve(vial_board):
    if vial_board.solved():
        return vial_board
    else:
        for i in range(len(vial_board)):
            for j in range(len(vial_board)):
                if vial_board.can_move(i, j):
                    vial_board.move(i, j)
                    return solve(vial_board)
