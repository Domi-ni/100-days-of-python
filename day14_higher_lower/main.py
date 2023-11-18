import random
from art import logo, vs
from game_data import data
from replit import clear

def choose_personality(letter):
  personality = random.choice(data)
  data.remove(personality)

  print(f"compare {letter}: {personality['name']}, a {personality['description']}, from {personality['country']}.")
  return personality
  
def compare_followers(personality1, personality2):
  if personality1['follower_count'] > personality2['follower_count']:
    return "a"
  elif personality1['follower_count'] < personality2['follower_count']:
    return"b"

def new_fase(personality_a, personality_b, score, answer, player_guess):
  if player_guess == answer:
    score += 1
    clear()
    print(logo)

    print(f"You're right! Current score: {score}")

    personality_a = personality_b
    print(f"compare A: {personality_a['name']}, a {personality_a['description']}, from {personality_a['country']}.")

    print(vs)

    personality_b = choose_personality("B")

    player_guess = input("Who has more followers? Type 'A' or 'B':").lower()
    answer = compare_followers(personality_a, personality_b)
    return score
    new_fase(personality_a, personality_b, score, answer, player_guess)


score = 0
clear()
print(logo)
personality_a = choose_personality("A")
  
print(vs)
  
personality_b = choose_personality("B")

answer = compare_followers(personality_a, personality_b).lower()

player_guess = input("Who has more followers? Type 'A' or 'B':").lower()  

score = new_fase(personality_a, personality_b, score, answer, player_guess)

clear()
print(logo)
print(f"Sorry, that's wrong. Final score: {score}")

    




