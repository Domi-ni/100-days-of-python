from art import logo
import random
import sys

def check_guess(user_guess, answer):
  if user_guess < answer:
    print("Too low.\nTry again.\n")

  elif user_guess > answer:
    print("Too high.\nTry again.")

  else:
    print(f"You got it! the answer was {answer}")
    sys.exit()
    
def set_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == "easy":
    return 10
  elif difficulty == "hard":
    return 5
  else:
    print("Invalid difficulty. Try again.")
    set_difficulty()
    
def game():
  print(logo)
  print('welcome to "Guess the number"')
  print("Im thinking of a number between 1 and 100, Can you guess it?")
  random_number = random.randint(1,100)
  attempts = set_difficulty()
  while attempts > 0:
    print(f"\nyou have {attempts} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    attempts = attempts - 1
    check_guess(guess, random_number)
      
  print("You've run out of guesses, you lose.")

game()
  


# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

