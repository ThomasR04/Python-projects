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

game_images = [rock,paper, scissors]
compchoice = random.randint(0, 2) 


userschoice = int(input("Type 0 for rock 1 for  paper or 2 for scissors"))
print("You chose")
print(game_images[userschoice])

print("The computer chose: ")
print(game_images[compchoice])


if compchoice == userschoice:
    print("the game is a tie")
elif compchoice == 0 and userschoice == 2:
     print("You lose")
elif compchoice == 1 and userschoice == 0:
     print( "You lose")
elif compchoice == 2 and userschoice == 1:
     print( "You lose")
elif compchoice == 2 and userschoice == 0:
     print("You win")
elif compchoice == 0 and userschoice == 1:
     print("You win")
elif compchoice == 1 and userschoice == 2:
    print("You win")



