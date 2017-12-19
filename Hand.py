import random 


class hand:
	def __init__(self):

#This class has 5 dices. Numbered 1 through five. This method rolls 5 dices on the first roll, then receives information from hand.selectDice 
#to know what dices to roll on the subsequent rolls.
	def roll():
		die = random.sample(range(1,7), 5)

	

			

#This method allows the player to select what dices they want to keep so they can roll the other dices to roll in order to get a better score. 
#Sends the information to hand.roll.
	def selectDice(self, list): 
		hand = input("select the dice position you would like to roll again. Do not select the dice you want to keep: ")
		hand = hand.split(",")
		for i in hand:
			intversion = int(i)
			die[intversion-1] = random.randrange(1,7)



#Arguably the most important method of them all. This method keeps helps the player select a category such as full house, ones or twos etc. 
#Then it sends the information ot player.points and player.category so score adjustment can be made. Sub-functions could help here.
	def selectCategory(self, choice, score):
		if choice == "sixes":
			upperSection(6)
		elif choice == "fives":
			upperSection(5)
		elif choice == "fours":
			upperSection(4)
		elif choice == "threes":
			upperSection(3)
		elif choice == "twos":
			upperSection(2)
		elif choice == "aces":
			upperSection(1)
		elif choice == "Three of a kind"
			ThreeOfKind()
		elif choice == "Four of a kind"
			FourOfKind()
		elif choice == "Full House"
			FullHouse()
		elif choice == "Small Straight"
			smallStraight()
		elif choice == "Large Straight"
			largeStraight()
		elif choice == "Yahtzee"
			yahtzee()
		elif choice == "chance"
			chance()

	def upperSection(self, value):
		num = hand.count (value)
		tempScore = num * value
		overallScore += num * value

	def ThreeOfKind(self, value):
		sorted(die)
		if (hand[0]==hand[1] and hand[2]==hand[1])
		or (hand[1]==hand[2] and hand[3]==hand[2])
		or (hand[2]==hand[3] and hand[4]==hand[3]):
			num = hand.count(value)
			tempScore = num * value
			overallScore = num * value
		else:
			num = hand.count(value)
			tempScore = num * value
			overallScore = num * value

	def FourOfKind(self, value):
		sorted(die)
		if (hand[0]==hand[1] and hand[2]==hand[1] and hand[3]==hand[2])
		or (hand[1]==hand[2] and hand[3]==hand[2] and hand[4]==hand[3]):
			num = hand.count(value)
			tempScore = num * value
			overallScore = num * value

	def FullHouse(self):
		sorted(die)
		if ((hand[0]==hand[1] and hand[2]==hand[1])
		and(hand[3]==hand[4])) 
		or ((hand[0]==hand[1])
		and (hand[2]==hand[3] and hand [4]==hand[3])):
			tempScore = 25 
		else:
			num = hand.count(value)
			tempScore = num * value
			overallScore = num * value

	def smallStraight(self):
		sorted(die)
		if ((hand[0]==1 and hand[1]==2 and hand[2]==3 hand[3]==4)
		or (hand[1]==2 and hand[2]==3 and hand[3]==4 and hand[4]==5)
		or (hand[0]==2 and hand[1]==3 and hand[2]==4 and hand[3]==5)
		or (hand[1]==3 and hand[2]==4 and hand[3]==5 and hand[4]==6)):
			tempScore = 30
		else:
			num = hand.count(value)
			tempScore = num * value
			overallScore = num * value

	def largeStraight(self):
		sorted(die)
		if ((hand[0]==1 and hand[1]==2 and hand[2]==3 and hand[3]==4 and hand[4]==5)
		or (hand[0]==2 and hand[1]==3 and hand[2]==4 and hand[3]==5 and hand[4]==6)):
			tempScore = 40
		else:
			num = hand.count(value)
			tempScore = num * value
			overallScore = num * value

	def yahtzee(self):
		if hand[0]==hand[1] and hand[2]==hand[1] and hand[3]==hand[2] and hand[4]==hand[3]:
			tempScore = 50
		else:
			num = hand.count(value)
			tempScore = num * value
			overallScore = num * value

	def chance(self):
		sum(hand)












