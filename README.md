YAHTZEE

Plan:
* Player Class (Score sheets) - Keep track of the points and the categories that were used. - 
  * **player.points** - This method keeps track of each players' points. Needs method hand.selectCategory to know what category was selected by the player; then, player.points adds up the points and keeps track of them till the end of the game. 
  * **player.category** - This method keeps track of the categories that a player used so that he cannot use the same category more than one time. It needs hand.selectCategory to know and keep track of the categories that were used. 
* Hand Class - Select Dices you want (before you select to roll dice again or choose to just get the points based on what you have like full house or fives, etc). 
  * **hand.selectDice** - This method allows the player to select what dices they want to keep so they can roll the other dices to roll in order to get a better score. Sends the information to hand.roll.
  * **hand.selectCategory** - Arguably the most important method of them all. This method keeps helps the player select a category such as full house, ones or twos etc. Then it sends the information ot player.points and player.category so score adjustment can be made.
  * **hand.roll** - This class has 5 dices. Numbered 1 through five. This method rolls 5 dices on the first roll, then receives information from hand.selectDice to know what dices to roll on the subsequent rolls.
* Main code - Runs all the classes smoothly. 


