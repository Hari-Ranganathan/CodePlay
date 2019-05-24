import random

def findResult(userChoice,computerChoice):
	if(userChoice == "Rock" and computerChoice == "Paper") or (userChoice == "Paper" and computerChoice == "Rock"):
		result = "Paper"
	elif(userChoice == "Rock" and computerChoice == "Sicssors") or (userChoice == "Sicssors" and computerChoice == "Rock"):
		result = "Rock"
	else:
		result = "Sicssors"
	return result

def declareWinner(userChoice,computerChoice,result):
	if(userChoice == result):
		print("You Won")
	elif(computerChoice == result):
		print("You Lost")
	else:
		print("Tied")

def playGame():
	userChoice = input("Rock,Paper,Sissors? ")
	print("Now.! It's Computer Turn..")
	computer_list = ["Rock","Paper","Sicssors"]
	computerChoice = random.choice(computer_list)
	result = findResult(userChoice,computerChoice)
	declareWinner(userChoice,computerChoice,result)

def printOpenBanner():
	print("Game Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")
	print("Lets Play \n"
		+"your turn...")

printOpenBanner()
while True:
	playGame()
	ans =input("Wanna Play Again? Y or N ")
	if(ans == 'n' or ans == 'N'):
		break
print("Thanks for playing the Game! See You Soon..")		