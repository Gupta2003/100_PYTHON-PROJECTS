import random
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0,3)
if(user == 0):
    print('''  
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)''')
elif(user == 1):
    print(''' 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

else:
    print(''' 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')

if(computer == 0):
    print('''  
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)''')
elif(computer == 1):
    print(''' 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
else:
    print(''' 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')

if(user == computer):
    print("It's a draw")
elif((user == 0 and computer == 2) or (user == 2 and computer == 1) or(user == 1 and computer == 0) ):
    print("You win")
else:
    print("You lose")