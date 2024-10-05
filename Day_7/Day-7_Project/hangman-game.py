import random


print(r'''
 .----------------. .----------------. .-----------------..----------------. .----------------. .----------------. .-----------------.
| .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. |
| |  ____  ____  | | |      __      | | | ____  _____  | | |    ______    | | | ____    ____ | | |      __      | | | ____  _____  | |
| | |_   ||   _| | | |     /  \     | | ||_   \|_   _| | | |  .' ___  |   | | ||_   \  /   _|| | |     /  \     | | ||_   \|_   _| | |
| |   | |__| |   | | |    / /\ \    | | |  |   \ | |   | | | / .'   \_|   | | |  |   \/   |  | | |    / /\ \    | | |  |   \ | |   | |
| |   |  __  |   | | |   / ____ \   | | |  | |\ \| |   | | | | |    ____  | | |  | |\  /| |  | | |   / ____ \   | | |  | |\ \| |   | |
| |  _| |  | |_  | | | _/ /    \ \_ | | | _| |_\   |_  | | | \ `.___]  _| | | | _| |_\/_| |_ | | | _/ /    \ \_ | | | _| |_\   |_  | |
| | |____||____| | | ||____|  |____|| | ||_____|\____| | | |  `._____.'   | | ||_____||_____|| | ||____|  |____|| | ||_____|\____| | |
| |              | | |              | | |              | | |              | | |              | | |              | | |              | |
| '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' |
 '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' 
      
***************************************************************************************************************************************
      ''')



hangman = [r'''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     (`   | _ |   ')
| |          || ||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .
You Have 0 Lives Left :[
The Man Was Hanged And Could Not Be Saved :/         
           ''', r'''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     (`   |   |   ')
| |          ||
| |          || 
| |          || 
| |          || 
| |         / | 
""""""""""|_`-'      |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .
You Have 1 Life Left ❤︎ :[
''', r'''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     (`   |   |   ')
| |           ---
| |           
| |           
| |           
| |          
""""""""""|_         |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .
You Have 2 Lives Left ❤︎❤︎ :[
''', r'''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . .  |
| |       // |   | |
| |      //  | . |  
| |     (`   |   |   
| |           ---
| |          
| |         
| |          
| |         
""""""""""|_         |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .
You Have 3 Lives Left ❤︎❤︎❤︎ :[ 
''', r'''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        |  . .  |
| |        | |   | |
| |          | . |  
| |          |   |   
| |           ---
| |          
| |         
| |          
| |         
""""""""""|_         |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .
You Have 4 Lives Left ❤︎❤︎❤︎❤︎ :[  
''', r'''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |          .`--'.
| |       
| |        
| |           
| |          
| |           
| |          
| |         
| |          
| |         
""""""""""|_         |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .
You Have 5 Lives Left ❤︎❤︎❤︎❤︎❤︎ :[  
''', r'''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||
| |/         ||
| |          || 
| |         (  ) 
| |          ""
| |       
| |        
| |           
| |          
| |           
| |          
| |         
| |          
| |         
""""""""""|_         |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .
You Have 6 Lives Left ❤︎❤︎❤︎❤︎❤︎❤︎ ! 
''']

word_bank = ["ant", "baboon", "badger", "bat", "bear", "beaver", "camel", "cat", "clam", "cobra", "cougar", "coyote", "crow", "deer", "dog", "donkey", "duck", "eagle", "ferret", "fox", "frog", "goat",
             "goose", "hawk", "lion", "lizard", "llama", "mole", "monkey", "moose", "mouse", "mule", "newt", "otter", "owl", "panda", "parrot", "pigeon", "python", "rabbit", "ram", "rat", "raven",
             "rhino", "salmon", "seal", "shark", "sheep", "skunk", "sloth", "snake", "spider", "stork", "swan", "tiger", "toad", "trout", "turkey", "turtle", "weasel", "whale", "wolf", "wombat", "zebra" 
            ]

def hangman_game():
    continue_game = True

    #Function To Display Letters Guessed By User:
    def display_guess(already_guessed):
        display_guess = ""
        for letter in chosen_word:
                    if letter == guess.lower():
                        already_guessed.append(guess)
                        display_guess += guess
                    elif letter in already_guessed:
                        display_guess += letter
                    else:
                        display_guess += "_"
        return display_guess

    #Game_Logic
    #While 'continue_game == True' This Loop Will Execute:
    while continue_game == True:
        chosen_word = random.choice(word_bank)        

        lives = 6
        print(hangman[lives])

        placeholder = ""
        for position in range (len(chosen_word)):
            placeholder += "_"
        print(placeholder)

        win = False
        already_guessed = []

        #Actual_Logic
        #While 'lives > 0' This Loop Will Execute:
        while lives > 0:
            print(" ")
            guess = input("Guess A Letter: ")
            display_res = ""

            #If Users' Guess Is In The chosen_word Then Following Block Executes:
            if guess.lower() in chosen_word:
                print(hangman[lives])
                display = display_guess(already_guessed)
                print(display)
                print(" ")
                print("Choices: " + str(word_bank))
                print(" ")
                #If 'display' String is equal to 'chosen_word' Then User Wins & Exits From Loop: 
                if str(display) == str(chosen_word):
                    print("You Saved The Man From Being Hanged :)")
                    print("Lives Left: " + str(lives))
                    print(" ")
                    break
            #If Users' Guess Is Not In The chosen_word Then Following Block Executes:
            elif guess.lower() not in chosen_word:
                lives -= 1
                print(hangman[lives])
                display = display_guess(already_guessed)
                print(display)
                print(" ")
                print("Choices: " + str(word_bank))
                print(" ")

        #Continue_Game? Takes User Input To Determine If 'continue_game == True' or 'continue_game == False'       
        while True:
            continue_input = input("Try Again? (Y/N): ")
            if continue_input.capitalize() in ["Y","Yes"]:
                continue_game = True
                break
            elif continue_input.capitalize() in ["N","No"]:
                print ("Hope You Enjoyed The Game :) See You Soon!")
                continue_game = False
                break
            else :
                print ('Invalid Input! Enter "Yes"/"Y" or "No"/"N"')
                print(" ")
                continue_input = input("Try Again? (Y/N): ")

hangman_game()