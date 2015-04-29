import hanoi
game = hanoi.Board(4)
while game.solved == False:
	print("Move")
	start = input("Move from peg: ")
	end = input("...To peg: ")
	game.move(start-1, end-1)
	game.simple_display()
	game.solved_check()
print("Moves: "+str(game.moves))
