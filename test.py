import hanoi
a = hanoi.Board(4)
a.display()
a.move(0,1)
a.move(0,2)
print(a.towers)
a.display()
