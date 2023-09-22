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
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
import random
game_images = [rock,paper,scissor]
choice_name = ["Rock","Paper","Scissor"]

your_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissor: "))

if your_choice >= 3 or your_choice < 0:
    print("you typed an invalid number, you lost")

else:
    print("your choice is: ",choice_name[your_choice])   #print computer choice name
    print(game_images[your_choice])                      #print computer choice image

    computer_choice = random.randint(0,2)
    print("computer chose: ", choice_name[computer_choice])
    print(game_images[computer_choice])

    if your_choice==0 and computer_choice==2:
        print("you win the game")

    elif computer_choice== 0 and your_choice==2:
        print("you lost the game")

    elif computer_choice>your_choice:
        print("you lost the game")

    elif your_choice>computer_choice:
        print("you win the game")

    elif your_choice==computer_choice:
        print("It's a draw")


                  
# first checking if the input should not greater than 3 or less than 0 so that the game could be continued if will not check this first it could give error later no
#printing user choice and making computer select randomly and prinitng it's choice then checking for 0 and 2 for both users and computer 
