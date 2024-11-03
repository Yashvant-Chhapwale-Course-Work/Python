print(r'''*******************************************************************************  
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************''')                                      #The (''') or (""") i.e Triple Quotes can be used to accept Multi-Line String Values.
                                                                                                                         #The 'r' keyword before the Triple Quotes indicates a Raw String, which tells Python to Ignore Escape Sequences within the String.
print(" ")
print("Welcome To Treasure Island! Your Mission Is To Find The Legendary Treasure Of The Ancients.")
print(" ")

print("On Your Conquest You Arrive At A Cross-Road!")
cross_road = str(input('Which Path Will You Choose? "Left" or "Right" \n'))
if cross_road.capitalize() == 'Left' or cross_road.capitalize() == 'L':                                                     #The 'capitalize()' Function in Python is used to capitalize the first letter of a string. It turns the rest of all letters to lowercase.
    print(" ")
    print("You Chose The Left Path And Continued Onward With Your Quest!\n")
    print("You've Arrived At The Mushy Lake! There Is A Hidden Island At The Middle Of The Lake.")
    cross_lake = str(input('How Do You Wish To Proceed? "Wait For The Ferry" or "Swim To The Island". Choose Between "Wait" or "Swim" \n'))
    if cross_lake.capitalize() == 'Wait' or cross_lake.capitalize() == 'Wait for the ferry' or cross_lake.capitalize() == 'W':
        print(" ")
        print("You Reached The Island Safely! \n")
        print("There Is A House On The Island With 3 Doors: 'Red', 'Yellow' & 'Blue'.")
        choose_door = str(input('Which Door Do You Choose? "Red", "Yellow" or "Blue" \n'))
        if choose_door.capitalize() == 'Red' or choose_door.capitalize() == 'R'  :
            print(" ")
            print("You Win! Your Quest Was Triumphant, And You Unearthed The Legendary Treasure Of The Ancients :) \n")
        elif choose_door.capitalize() == 'Yellow' or choose_door.capitalize() == 'Y'  :
            print(" ")
            print('Game Over! You\'ve Chosen The Yellow Door And Fell Straight To Hell Into A Pit Of Fire :( \n')          #You can Escape A Quote by using a Backslash '\' before it. 
        elif choose_door.capitalize() == 'Blue' or choose_door.capitalize() == 'B'   :
            print(" ")
            print('Game over! You\'ve Chosen The Blue Door And Tumbled Into The Lair Of The Venomous Scorpion King :( \n')
        else:
            print(" ")
            print("I Am The Creator, Wielding The Power To Obliterate You!")
            print("Game Over! You have angered the Creator And Shall Now Face Wrath Of The Hand Of The Creator :[ ")
    elif cross_lake.capitalize() == 'Swim' or cross_lake.capitalize() == 'Swim to the island' or cross_lake.capitalize() == 'S': 
        print(" ")
        print("Game Over! You Were Vanquished By The Lake's Fearsome Guardian During Your Quest. :( \n")
    elif cross_lake.capitalize() == 'Fly' or cross_lake.capitalize() == 'Fly to the island' or cross_lake.capitalize() == 'Helicopter helicopter' or cross_lake.capitalize() == 'Helicopter' or cross_lake.capitalize() == 'Plane':
        print(" ")
        print("Game Over! The Airborne Wyrm Of The Lake Detected Your Presence :(")
    else:
        print(" ")
        print("I Am The Creator, Wielding The Power To Obliterate You!")
        print("Game Over! You have angered the Creator And Shall Now Face Wrath Of The Hand Of The Creator :[ ")
elif cross_road.capitalize() == 'Right' or cross_road.capitalize() == 'R':
    print(" ")
    print("Game Over! You’ve Found Yourself Stuck In A Ditch On Your Quest :( \n")
else:
    print(" ")
    print("I Am The Creator, Wielding The Power To Obliterate You!")
    print("Game Over! You have angered the Creator And Shall Now Face Wrath Of The Hand Of The Creator :[ ")