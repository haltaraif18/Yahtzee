import random

class Hand:
	def __init__(self):
		self.points = 0
		self.die = []

#This class has 5 dices. Numbered 1 through five. This method rolls 5 dices.
	def roll(self):
		self.die = random.sample(range(1,7), 5)
		print (self.die)

#This method allows the player to select what dices they want to roll again to get a better score.
	def selectDice(self, hands):
		hand = hands.split(",")
		for i in hand:
				intversion = int(i)
				self.die[intversion-1] = random.randrange(1,7)
		print (self.die)

#This method helps the player select a category such as full house, ones or twos etc. player class sends info to this function.
	def selectCategory(self, choice):
		if choice == "sixes":
			self.upperSection(6)
		elif choice == "fives":
			self.upperSection(5)
		elif choice == "fours":
			self.upperSection(4)
		elif choice == "threes":
			self.upperSection(3)
		elif choice == "twos":
			self.upperSection(2)
		elif choice == "aces":
			self.upperSection(1)
		elif choice == "three of a kind":
			self.ThreeOfKind()
		elif choice == "four of a kind":
			self.FourOfKind()
		elif choice == "full house":
			self.FullHouse()
		elif choice == "small straight":
			self.smallStraight()
		elif choice == "large straight":
			self.largeStraight()
		elif choice == "yahtzee":
			self.yahtzee()
		elif choice == "chance":
			self.chance()
		elif choice == "21":
			self.21()


#The following lines of code are the categories. They are just the rules of the game.
#They also add points to our points variable depending on the used category.
	def upperSection(self, value):
		num = self.die.count (value)
		self.points += (num * value)

	def ThreeOfKind(self):
		self.die.sort()
		if any ( [self.die[0]==self.die[1] and self.die[2]==self.die[1], 
			self.die[1]==self.die[2] and self.die[3]==self.die[2], 
			self.die[2]==self.die[3] and self.die[4]==self.die[3] ]):
			self.points += sum(self.die)
		else:
			self.points += 0

	def FourOfKind(self):
		self.die.sort()
		if any([self.die[0]==self.die[1] and self.die[2]==self.die[1] and self.die[3]==self.die[2],
		self.die[1]==self.die[2] and self.die[3]==self.die[2] and self.die[4]==self.die[3]]):
			self.points += sum(self.die)
		else: 
			self.points += 0

	def FullHouse(self):
		self.die.sort()
		if any ([self.die[0]==self.die[1] and self.die[2]==self.die[1] and self.die[3]==self.die[4],
		self.die[0]==self.die[1] and self.die[2]==self.die[3] and self.die [4]==self.die[3]]):
			self.points += 25 
		else:
			self.points += 0

	def smallStraight(self):
		self.die.sort()
		if any ([self.die[0]== 1 and self.die[1]==2 and self.die[2]==3 and self.die[3]==4,
		self.die[1]==2 and self.die[2]==3 and self.die[3]==4 and self.die[4]==5,
		self.die[0]==2 and self.die[1]==3 and self.die[2]==4 and self.die[3]==5,
		self.die[1]==3 and self.die[2]==4 and self.die[3]==5 and self.die[4]==6]):
			self.points += 30
		else:
			self.points += 0

	def largeStraight(self):
		self.die.sort()
		if any([self.die[0]==1 and self.die[1]==2 and self.die[2]==3 and self.die[3]==4 and self.die[4]==5,
		self.die[0]==2 and self.die[1]==3 and self.die[2]==4 and self.die[3]==5 and self.die[4]==6]):
			self.points += 40
		else:
			self.points += 0

	def yahtzee(self):
		if self.die[0]==self.die[1] and self.die[2]==self.die[1] and self.die[3]==self.die[2] and self.die[4]==self.die[3]:
			self.points += 50
		else:
			self.points += 0

	def chance(self):
		self.points += sum(self.die)

#This is the custom-created category. 
	def 21(self):
		if sum(self.die) == 21:
			self.points += 42
		else:
			self.points += 0




