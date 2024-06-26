import random

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

game_images = [rock, paper, scissors]

print('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.')

while True:
    player_num = int(input('> '))
    if player_num < 0 or player_num > 2:
        print("Please enter a value between 0 and 2 and try again.")
    else:
        player = game_images[player_num]
        break
         

computer = game_images[random.randint(0,2)]


print(f"Your opponent played: {computer}")
print(f"You played: {player}")
print("")
print("")
print("")


if computer == player:
    print("It was a tie!")
elif player == rock and computer == paper:
    print("You lose!")
elif player == paper and computer == scissors:
    print("You lose!")
elif player == scissors and computer == rock:
    print("You lose!")
elif computer == rock and player == paper:
    print("You win!")
elif computer == paper and player == scissors:
    print("You win!")
elif computer == scissors and player == rock:
    print("You win!")
else:
    print("There was an error with your game.")

