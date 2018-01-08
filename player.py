#This class is not exactly like it is on the README because I figured out that it is better to calculate points in hand.py. This also demonstrates flexibility that is required from a developer :)
import hand

#Each player has its own hand instance to get the score and the categories used. 
class Player:
		def __init__(self):
			#Each player has its own hand instance to get the score and the categories used. 
			self.hand = hand.Hand()
			self.categoriesUsed = []
		
#This method keeps track of the categories that a player used so that he cannot use the same category more than one time. 
#The way this function works is that it checks if the category is used. If it is used, it asks the user to select another. 
#If the category is not used, it executes the function in hand class and then appends the category in the list so it can't be used again.
		def add_category(self):
			category = input("select: sixes, fives, fours, threes, twos, aces, three of a kind, four of a kind, full house, small straight, large straight, yahtzee, chance or double chance? ")
			if len(self.categoriesUsed) == 13:
				print("error, you have used all categories.")
			elif category in self.categoriesUsed:
				print("Error, you have already used this category. Please select another.")
				self.add_category()
			#The next elifs make sure the user selects a valid category.
			elif category == "sixes" or category == "fives" or category == "fours" or category == "threes" or category == "twos" or category == "aces" or category == "three of a kind" or category == "four of a kind" or category == "full house" or category == "small straight" or category == "large straight" or category =="yahtzee" or category == "chance" or category == "double chance":
				self.hand.selectCategory(category)
				self.categoriesUsed.append(category)
			else:
				print ("Error, this category does not exist.")
				self.add_category()

