from minesweeper import *

ia = MinesweeperAI(8,8)
ia.add_knowledge((1,2),0)
ia.add_knowledge((3,4),0)
ia.add_knowledge((5,6),0)
move_1 = ia.make_safe_move()
move_2 = ia.make_safe_move()

print(move_1)

print(move_2)