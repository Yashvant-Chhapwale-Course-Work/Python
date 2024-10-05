import random
from hangman_words import word_bank
from hangman_art import logo
from hangman_art import stages
from hangman_art import win_art

print(logo)

hangman = stages

def hangman_game():
    continue_game = True

    #Function To Display Letters Guessed By User: 
    def display_guess(already_guessed):
        display_guess = ""
        for letter in chosen_word:
                    if letter == guess.lower():        #If chosen_word's Letter is same as Users' Guessed Letter Then 'display_guess += Users' Guessed Letter'. 
                        already_guessed.append(guess)
                        display_guess += guess
                    elif letter in already_guessed:    #If chosen_word's Letter is already present in 'already_guessed' List Then 'display_guess += chosen_word's Letter '. 
                        display_guess += letter
                    else:                              #Else 'display_guess += "_" '.
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
        already_guessed = [] #Holds The Values Already Guessed By User And Helps In Printing Them To The 'display'/'display_guess' Variable.

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
                    print(win_art)
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
                if lives > 0:
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