"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from itertools import chain
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    board_unnested = list(chain.from_iterable(board))
    win_position = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )
    for position in win_position:
        if (
            board_unnested[position[0]]
            == board_unnested[position[1]]
            == board_unnested[position[2]]
            != "-"
        ):
            return f"{board_unnested[position[0]]} wins!"
    if "-" not in board_unnested:
        return "draw!"
    return "unfinished"
