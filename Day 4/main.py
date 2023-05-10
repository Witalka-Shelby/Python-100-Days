import random

def painting(pick):
    if pick == 0:
        pick = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''
        return pick
    
    if pick == 1:
        pick = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
        return pick
    
    if pick == 2:
        pick = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
        return pick


user_pick = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ?\n"))
computer_pick = random.randrange(0, 2)

print(painting(user_pick))
print("Computer chose: \n")
print(painting(computer_pick))

if user_pick == computer_pick:
    print("It\'s a draw")
elif user_pick == 0 and computer_pick == 2 or user_pick == 1 and computer_pick == 0 or user_pick == 2 and computer_pick == 1:
    print("You win")
else:
    print("You lose")
