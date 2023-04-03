from tictactoe.tictactoe_optimisation_failed import *



state2 = [[X, O, X],
                [O, X, O],
                [X, O, O]]

state1 = [[X, O, X],
             [O, X, O],
             [X, O, EMPTY]]
    
state3 = [[EMPTY, X, O],
             [O, X, EMPTY],
             [X, EMPTY, O]]

state4 = [[EMPTY, X, O],
             [O, X, X],
             [X, EMPTY, O]]


def test_player():
    print("Testing player()...")
    assert player(initial_state()) == X
    #one option with x
    assert player(state1) == X
    #test game over
    assert player(state2) == X
    print("Passed! :)")

def test_actions():
    print("Testing actions()...")
    assert actions(initial_state()) == {(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)}
    assert actions(state2) == None
    print("Passed! :)")

def test_result():
    print("Testing result()...")
    assert result(initial_state(), (0,0)) == [[X, None, None], [None, None, None], [None, None, None]]
    assert result(initial_state(), (1,1)) == [[None, None, None], [None, X, None], [None, None, None]]
    assert result(initial_state(), (2,2)) == [[None, None, None], [None, None, None], [None, None, X]]
    assert result(state1, (2,2)) == [[X, O, X], [O, X, O], [X, O, X]]
    print("Passed! :)")

def test_winner():
    print("Testing winner()...")
    assert winner(state1) == X
    assert winner(state2) == X
    print("Passed! :)")

def test_terminal():
    print("Testing terminal()...")
    assert terminal(state1) == True
    assert terminal(state2) == True
    print("Passed! :)")

def test_utility():
    print("Testing utility()...")
    assert utility(state1) == 1
    assert utility(state2) == 1
    print("Passed! :)")

def test_minimax():
    print("Testing minimax()...")
    print (minimax(state4))
    print("Passed! :)")

def main():
    """test_player()
    test_actions()
    test_result()
    test_winner()
    test_terminal()
    test_utility()"""
    print(player(state3), "is the player and chooses", minimax(state4))
    #test_minimax()
    print("All tests passed!")

if __name__ == "__main__":
    main()