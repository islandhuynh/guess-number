import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
difficulty = ""
lives = 0
while difficulty != "easy" and difficulty != "hard":
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': " ).lower()
  if difficulty != "easy" and difficulty != "hard":
    print("Please provide a valid input.")

if difficulty == "easy":
  lives = 10
if difficulty == "hard":
  lives = 5

number = random.randint(1,100)

while lives >= 0:
  if lives == 0:
    print("You've ran out of guesses, you lose.")
    break
  print(f"you have {lives} attemps remaining to guess the number.")
  guess = int(input("Make a guess: "))
  if guess > number:
    print("Too high")
    print("Guess again.")
    lives -= 1
  if guess < number:
    print("Too low")
    print("Guess again.")
    lives -= 1
  if guess == number:
    print(f"You guessed the right number! It was {number}.")
    break