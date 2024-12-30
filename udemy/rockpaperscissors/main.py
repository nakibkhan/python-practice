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

hand_list = [rock, paper, scissors]

userGuessNumber = int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

comp_gen = random.randint(0,2)

print(f"You chose : {userGuessNumber}" )

print(hand_list[userGuessNumber])

print(f"Computer chose {comp_gen}")

print(hand_list[comp_gen])

if userGuessNumber == comp_gen:
    print("Game drawn!")
elif (userGuessNumber == 0 and comp_gen == 2) or (userGuessNumber == 1 and comp_gen == 0) or (userGuessNumber == 2 and comp_gen == 1):
    print("You win!")
else:
    print("You lose!")