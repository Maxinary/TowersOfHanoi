class Board():
	def __init__(self, rings):
		self.rings = rings
		self.moves = 0
		self.solved = False
		self.towers = [["I"],["I"],["I"]]
		for i in range(rings):
			self.towers[0].insert(1,i+1)

	def move(self, initial,final):
		if len(self.towers[initial]) > 1:
			if -1 < initial < 3 and -1 < final < 3:
				if len(self.towers[final]) > 1:
					if self.towers[final][1] > self.towers[initial][1]:
						ring = self.towers[initial][-1]
						del self.towers[initial][-1]
						self.towers[final].append(ring)
						self.moves+=1
					else:
						print("That won't fit")
				else:
					ring = self.towers[initial][-1]
					del self.towers[initial][-1]
					self.towers[final].append(ring)
					self.moves+=1
			else:
				print("That is not a valid peg :(")

	def display(self):
		print(self.towers)
		#iterate through rows
		max_height = 0
		for i in range(3):
			if len(self.towers[i]) > max_height:
				max_height = len(self.towers[i])
		max_width = (self.rings*2)-1
		center = self.rings#change to variable spacing
		for i in range(max_height-1,-1,-1):
			if i!=0:
				for j in range(3):
					if len(self.towers[j]) > i:
						#display one item
						#print(" "*(self.rings-self.towers[j][i])+"_"*((self.towers[j][i]*2)-1)),
						#shows 
						print((" "*(self.rings-self.towers[j][i]-1)+"_"*5)),
			else:
				print(" "*2+"I"+" "*6+"I"+" "*5+"I")
			print('')

	def simple_display(self):
		max_height = 0
		for i in range(3):
			if len(self.towers[i]) > max_height:
				max_height = len(self.towers[i])

		for i in range(max_height,-1,-1):
			for j in range(3):
				if len(self.towers[j]) > i:
					print(self.towers[j][i]),
				else:
					print(" "),
			print('')
	def solved_check(self):
		if len(self.towers[0])==1:
			if len(self.towers[1])==1:
				self.solved = True
