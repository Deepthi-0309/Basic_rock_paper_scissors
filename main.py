rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

game_images = [rock, paper, scissors]
user_choice = int(
    input(
        "\n What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors"
    ))
print("You choose:")
if user_choice == 0:
    print("Rock\n")
    print(rock)
elif user_choice == 1:
    print("Paper\n")
    print(paper)

else:
    print("Scissors\n")
    print(scissors)

computer_choice = random.randint(0, 2)
print("Computer chose:")
if computer_choice == 0:
    print("Rock\n")
    print(rock)
elif computer_choice == 1:
    print("Paper\n")
    print(paper)
else:
    print("Scissors\n")
    print(scissors)

if user_choice == 0 and computer_choice == 2:
    print("You Win")
elif user_choice == 1 and computer_choice == 0:
    print("You Win")
elif user_choice == 2 and computer_choice == 1:
    print("You Win")
elif user_choice == 0 and computer_choice == 0 or user_choice == 1 and computer_choice == 1 or user_choice == 2 and computer_choice == 2:
    print("It's a draw")
else:
    print("You lose")
