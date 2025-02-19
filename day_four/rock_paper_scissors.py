import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [rock, paper, scissors]
print("Welcome to Rock, Paper, Scissors Game!")
player_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: ")
)
if player_choice >= 0 or player_choice <= 2:
    print(f"You choose: {game_images[player_choice]}")
else:
    print("Invalid choice")
computer_choice = random.randint(0, 2)
print(f"Computer chose: {game_images[computer_choice]}")
if player_choice == computer_choice:
    print("It's a draw")
elif player_choice == 0 and computer_choice == 2:
    print("You win!")
elif player_choice == 1 and computer_choice == 0:
    print("You win!")
elif player_choice == 2 and computer_choice == 1:
    print("You win!")
else:
    print("You lose!")
