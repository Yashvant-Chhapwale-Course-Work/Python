import random

print(r'''
**************************************************
$$\   $$\ $$$$$$$$\ $$\       $$\       $$$$$$\    
$$ |  $$ |$$  _____|$$ |      $$ |     $$  __$$\   
$$ |  $$ |$$ |      $$ |      $$ |     $$ /  $$ |  
$$$$$$$$ |$$$$$\    $$ |      $$ |     $$ |  $$ |  
$$  __$$ |$$  __|   $$ |      $$ |     $$ |  $$ |  
$$ |  $$ |$$ |      $$ |      $$ |     $$ |  $$ |  
$$ |  $$ |$$$$$$$$\ $$$$$$$$\ $$$$$$$$\ $$$$$$  |  
\__|  \__|\________|\________|\________|\______/  
**************************************************
      ''')

rock = (''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

''')

paper = (''' 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)


''')

scissor = (''' 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
           
''')

# Win_Logic
win_streak = 0 
loss_streak = 0
continue_game = True

while continue_game: #If 'continue_game = True' >> Proceeds Inside Loop ,Else If 'continue_game = False' >> Exits From Loop.
    
    # Player's Move:
    valid_move = False  
    while not valid_move: #Now 'valid_move = False', Therefore 'not valid_move == True', so 'while True' >> Proceeds Inside Loop, After Which If 'valid_move = True', 'not valid_move == False', so 'while False' >> Exits From Loop.
        print(" ")
        print('Make Your Move! "Rock", "Paper" Or "Scissors"!')
        player_input = input("Enter 'R' If You Choose \"Rock\", 'P' If You Choose \"Paper\" And 'S' If You Choose \"Scissors\": ")
        print(" ")

        if player_input.capitalize() in ['R', 'Rock', 'Rocks']:
            print("Player's Move:")
            print(rock)
            player_choice = rock
            valid_move = True 
        elif player_input.capitalize() in ['P', 'Paper', 'Papers']:
            print("Player's Move:")
            print(paper)
            player_choice = paper
            valid_move = True
        elif player_input.capitalize() in ['S', 'Scissor', 'Scissors']:
            print("Player's Move:")
            print(scissor)
            player_choice = scissor
            valid_move = True
        else:
            print("Not A Valid Move :/  Please Try Again::")

    # Computer's Move
    computer_input = [rock, paper, scissor]     
    computer_choice = random.choice(computer_input)
    print("Computer's Move:")
    print(computer_choice)

    # Logic
    if player_choice == computer_choice:
        print("The Clash Ended In A Fabled Stalemate!")
    elif (player_choice == rock and computer_choice == paper) or (player_choice == paper and computer_choice == scissor) or (player_choice == scissor and computer_choice == rock):
        print("Computer Wins")
        print("You Achieved A Streak Of " + str(win_streak) + " Consecutive Wins!")
        win_streak = 0
        loss_streak += 1
    else:
        print("Player Wins!")
        print("You Shattered Your Legendary " + str(loss_streak) + "-Loss Curse")
        win_streak += 1
        loss_streak = 0

    #The Value Of 'continue_game' remains 'True' Till This Point In The Program, Due To Which The Loop Is Re-Executed For Invalid Inputs.
    # Continue_Game? Reinitializing 'continue_game':
    print(" ")
    continue_input = input('Play Another Round? "Yes" or "No" \n')
    while True :   # The Loop Is Set To Run Indefinitely Until A 'break' Statement Is Encountered. This Also Simultes A Do-While Loop In Python.
        if continue_input.capitalize() in ["Yes", "Y"]:
            continue_game = True
            break
        elif continue_input.capitalize() in ["No", "N"]:
            continue_game = False
            break
        else:
            print("Invalid input :/ Please enter 'Yes' or 'No'.")
            print(" ")
            continue_input = input('Play Another Round? "Yes" or "No" \n')


#The 'in' Keyword Is Used To Check For Membership Or Inclusion Within Sequences.

