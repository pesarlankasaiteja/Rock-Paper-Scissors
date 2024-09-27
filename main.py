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

a= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game[a])

b= random.randint(0, 2)
print("Computer chose:")
print(game[b])

if a>=3 and a<0:
    print("You typed an invalid number, you lose!")
elif a==b:
    print("It's a draw")
elif a==0 and b==1:
    print("You loose")
elif a==1 and b==0:
  print("You loose")
elif a==1 and b==2:
  print("You loose")
elif a==2 and b==1:
  print("You loose")
else:
    print("You win")