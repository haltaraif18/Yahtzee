#In this yahtzee, game still ends in 13 rounds. However, there is an extra category to make the game more interesting. 
import player

#Try and except force the user to type an integer.
while True:
	try:
		numOfPlayers = int (input("How many players are going to play? "))
		break
	except:
            print("That's not a valid option. Please type an integer")

gamers = []
#This for loop creates an array and then adds instances in the array for every player.
for x in range(numOfPlayers):
	gamers.append(str(x))
	gamers[x] = player.Player()

#This outer loop makes sure only 13 rounds are played. The inner loop gives changes turns for players smoothly.
for y in range (0,2):
	for x in range (numOfPlayers):
		gamers[x].hand.roll()
		for z in range (0,2):
			hands = input("Select the dice positions (1-5) you would like to roll again. Use commas (,) to separate them. Type none if you don't want to roll: ")
			if hands == "none":
				break
			else:
				gamers[x].hand.selectDice(hands)
		gamers[x].add_category()
		print ("Player " + str(x) + " score is " + str(gamers[x].hand.points))

#This block of code puts the total points of the players in a list to help figure out who's the winner.
pointsList = []
for x in range (numOfPlayers):
	pointsList.append(gamers[x].hand.points)
m = max(pointsList)
print("player " + str([i for i, k in enumerate(pointsList) if k == m]) + " wins!")
