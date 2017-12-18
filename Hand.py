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
		list = input('select the dice position you would like to roll again. Do not select the dice you want to keep: ')
		list = list.split(",")
		for i in list:
			intversion = int(i)
			die[intversion-1] = random.randrange(1,7)



#Arguably the most important method of them all. This method keeps helps the player select a category such as full house, ones or twos etc. 
#Then it sends the information ot player.points and player.category so score adjustment can be made. Sub-functions could help here.
	def selectCategory(self, choice):
		if choice == "threes":
			threes()

	def threes(self):
		# determine if the user has 3s
			#if they do, what is their score
		# if not, take 0 for the score
		# mark 3s as taken  





