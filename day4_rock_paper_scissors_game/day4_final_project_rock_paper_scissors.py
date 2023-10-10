import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

   rock
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

    PAPER
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

   SCISSORS
"""
game_images = [rock, paper, scissors]

player_choice = int(
    input("What do you choose? type 0 for rock, 1 for paper or 2 for scissors\n ")
)
computer_choice = random.randint(0, 2)

if player_choice >= 3 or player_choice < 0:
    print("You choose an invalide number. You lose")
else:
    print("\n\nYour choise:")
    print(f"{game_images[player_choice]}\n\n")
    print("computer choise:")
    print(f"{game_images[computer_choice]}\n\n")

    if player_choice == computer_choice:
        print("It's a tie")
    elif player_choice == 0 and computer_choice == 1:
        print("You lose :(")
    elif player_choice == 0 and computer_choice == 2:
        print("You wins!!")
    elif player_choice == 1 and computer_choice == 0:
        print("You win!!!")
    elif player_choice == 1 and computer_choice == 2:
        print("You lost :(")
    elif player_choice == 2 and computer_choice == 0:
        print("You lost :(")
    elif player_choice == 2 and computer_choice == 1:
        print("You wins!!!")
