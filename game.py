import random

mysteryNumber = random.randint(1, 100)
score = 0

while True:
	guess = int(input("Pick a number between 1 and 100: "))
	score = score + 1

	if guess == mysteryNumber:
		print("Good Guess")
		break
	if guess > mysteryNumber:
		print("Too high, try again.")

	if guess < mysteryNumber:
		print("Too low, try again.")

print("Your number of guesses is: " + str(score))
