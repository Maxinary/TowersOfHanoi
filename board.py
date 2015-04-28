class Board():
	def __init__(self, rings):
		self.solved = False
		self.towers = [[]*3]
		for i in range(rings):
			towers[0].append(Ring(rings-1))

	def move(initial,final):
		if -1 < initial < 3 and -1 < final < 3
			if self.towers[final][-1].size > self.towers[initial][-1].size:
				ring = self.towers[initial][-1]
				del self.towers[initial][-1]
				self.towers[final].append(ring)
			else:
				print("That won't fit")
		else:
			print("That is not a valid peg :(")

	def display():
		#iterate through rows
		max_height = 0
		for i in range(3):
			if len(self.towers[i]) > max_height:
				max_height = len(self.towers[i])
		max_width = (2*max_height)-1
		for i in range(max_height):
			for j in range(3):
				if len(self.towers[j]) > max_height-i:
					#display one item

	def simple_display():
		max_height = 0
		for i in range(3):
			if len(self.towers[i]) > max_height:
				max_height = len(self.towers[i])

		for i in range(max_height):
			for j in range(3):
				if len(self.towers[j]) > max_height:
					print(self.towers[j][i]),
			print()
