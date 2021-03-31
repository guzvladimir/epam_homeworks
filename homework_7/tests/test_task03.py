from task03.task03 import tic_tac_toe_checker

example_x_wins = [["-", "-", "x"], ["o", "o", "x"], ["-", "x", "x"]]
example_o_wins = [["-", "-", "o"], ["o", "o", "o"], ["-", "x", "x"]]
example_draw = [["o", "x", "o"], ["x", "o", "x"], ["x", "o", "x"]]
example_unfinished = [["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]]


def test_tic_tac_toe_checker():
    assert tic_tac_toe_checker(example_x_wins) == "x wins!"
    assert tic_tac_toe_checker(example_o_wins) == "o wins!"
    assert tic_tac_toe_checker(example_draw) == "draw!"
    assert tic_tac_toe_checker(example_unfinished) == "unfinished"
