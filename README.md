YAHTZEE by Husain and Faisal

Plan:
* Player Class (Score sheets) - Keep track of the points and the categories that were used. - 
  * **Player.add_category** - This method keeps track of the categories that a player used so that he cannot use the same category more than one time. It needs hand.selectCategory to know and keep track of the categories that were used. 
* Hand Class - Select Dices you want (before you select to roll dice again or choose to just get the points based on what you have like full house or fives, etc). 
  * **Hand.selectDice** - This method allows the player to select what dices they want to keep so they can roll the other dices to roll in order to get a better score. Sends the information to hand.roll.
  * **Hand.selectCategory** - Arguably the most important method of them all. This method keeps helps the player select a category such as full house, ones or twos etc. Then it sends the information ot player.points and player.category so score adjustment can be made. Sub-functions could help here.
  * **Hand.roll** - This class has 5 dices. Numbered 1 through five. This method rolls 5 dices on the first roll, then receives information from hand.selectDice to know what dices to roll on the subsequent rolls.
  This class also has all the categories (rules) of the game and a bonus category.
  The points are calculated in this class in the categories themselves and then calculated by adding directly to the player's points attribute.
* Main code - Runs all the classes smoothly and uses the players' points to decide who wins. To elaborate, the main code creates player instances using a for loop and allows them to play the game using the methods from player and hand classes.
