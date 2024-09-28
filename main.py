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

import random

game = [rock, paper, scissors]

play_again = 'y'

while play_again == 'y':
    a = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

    if a >= 3 or a < 0:
        print("You typed an invalid number, you lose!")
    else:
        print(game[a])

        b = random.randint(0, 2)
        print("Computer chose:")
        print(game[b])

        if a == b:
            print("It's a draw")
        elif (a == 0 and b == 2) or (a == 1 and b == 0) or (a == 2 and b == 1):
            print("You win")
        else:
            print("You lose")

    play_again = input("Do you want to play again? Type 'y' for yes or 'n' for no: ").lower()

print("Thanks for playing!")
