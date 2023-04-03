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


def my_count(board, p):
    c = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == p:
                c += 1
    return c

def player(board):
    """
    Returns player who has the next turn on a board.
    
    In the initial game state, X gets the first move. 
    Subsequently, the player alternates with each additional move.
    Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).
    """
    nbr_X = my_count(board, X)
    nbr_O = my_count(board, O)
    if nbr_X == nbr_O:
        return X
    elif nbr_X > nbr_O:
        return O
    else:
        return X
            


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    
    Each action should be represented as a tuple (i, j) 
    where i corresponds to the row of the move (0, 1, or 2) and j corresponds 
    to which cell in the row corresponds to the move (also 0, 1, or 2).
    Possible moves are any cells on the board that do not already have an X or an O in them.
    Any return value is acceptable if a terminal board is provided as input.
    """
    tab_of_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                tab_of_actions.add((i,j))
    if len(tab_of_actions) == 0:
        return None
    else:
        return tab_of_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.

    If action is not a valid action for the board, your program should raise an exception.
    The returned board state should be the board that would result from taking the original input board, 
    and letting the player whose turn it is make their move at the cell indicated by the input action.
    Importantly, the original board should be left unmodified:
    since Minimax will ultimately require considering many different board states during its computation. 
    This means that simply updating a cell in board itself is not a correct implementation of the result function. 
    You’ll likely want to make a deep copy of the board first before making any changes.
    """
    if action not in actions(board):
        raise Exception("Not a valid action")
    else:
        #deep copy of the board
        new_board = [row[:] for row in board]
        new_board[action[0]][action[1]] = player(board)
        return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.

    If the X player has won the game, your function should return X. 
    If the O player has won the game, your function should return O.
    One can win the game with three of their moves in a row horizontally, vertically, or diagonally.
    You may assume that there will be at most one winner
    (that is, no board will ever have both players with three-in-a-row, since that would be an invalid board state).
    If there is no winner of the game (either because the game is in progress, or because it ended in a tie), 
    the function should return None
    """
    #check if there is a winner
    #check if there is a winner in the rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
    #check if there is a winner in the columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != EMPTY:
            return board[0][j]
    #check if there is a winner in the diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] != EMPTY:
        return board[2][0]
    #otherwise return None
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.

    If the game is over, either because someone has won the game or 
    because all cells have been filled without anyone winning, the function should return True.
    Otherwise, the function should return False if the game is still in progress.
    """
    if winner(board) != None:
        return True
    elif actions(board) == None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.

    If X has won the game, the utility is 1. 
    If O has won the game, the utility is -1. If the game has ended in a tie, the utility is 0.
    You may assume utility will only be called on a board if terminal(board) is True.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.

    The move returned should be the optimal action (i, j) 
    that is one of the allowable actions on the board. 
    If multiple moves are equally optimal, any of those moves is acceptable.
    If the board is a terminal board, the minimax function should return None.
    """
    #Take a look of minimax algorithm for more details
    if terminal(board):
        return None
    else:
        if player(board) == X:
            option = (0,0)
            max_ = -math.inf
            for action in actions(board):
                if min_value(result(board,action)) > max_:
                    max_ = min_value(result(board,action))
                    option = action
            return option
        elif player(board) == O:
            option = (0,0)
            min_ = math.inf
            for action in actions(board):
                if max_value(result(board,action)) < min_:
                    min_ = max_value(result(board,action))
                    option = action
            return option


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v