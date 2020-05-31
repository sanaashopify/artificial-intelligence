"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X
    countX = board[0].count(X) + board[1].count(X) + board[2].count(X)
    countO = board[0].count(O) + board[1].count(O) + board[2].count(O)

    if terminal(board):
        return 0
    if countX > countO:
        return O
    if countX == countO:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return 0

    possible_actions = set()
    for i, row in enumerate(board):
        for j, position in enumerate(row):
            if position == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    player = player(board)
    board_copy = copy.deepcopy(board)

    if board_copy[action[0]][action[1]] == X or board_copy[action[0]][action[1]] == O:
        raise ValueError('Move invalid.')
    else:
        if player == X:
            board_copy[action[0]][action[1]] == X
        else:
            board_copy[action[0]][action[1]] == O

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    potential_wins = []

    # 3 in a row
    for row in board:
        potential_wins.append(set(row))

    # 3 in a column
    for i in range(3):
        potential_wins.append(set([board[k][i] for k in range(3)]))

    # 3 in a diagonal
    potential_wins.append(set([board[i][i] for i in range(3)]))
    potential_wins.append(set([board[i][2 - i] for i in range(3)]))

    # Checking if any three are the same
    for win in potential_wins:
        if win == {X}:
            return X
        elif win == {O}:
            return O
    return -1


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for row in board:
        if EMPTY in row:
            return False
        else:
            return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner == X:
        return 1
    elif winner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
