print(r'''
 ________ ___  ________  ________  ________  ___  ___  ________  ________     
|\  _____\\  \|\_____  \|\_____  \|\   __  \|\  \|\  \|\_____  \|\_____  \    
\ \  \__/\ \  \\|___/  /|\|___/  /\ \  \|\ /\ \  \\\  \\|___/  /|\|___/  /|   
 \ \   __\\ \  \   /  / /    /  / /\ \   __  \ \  \\\  \   /  / /    /  / /   
  \ \  \_| \ \  \ /  /_/__  /  /_/__\ \  \|\  \ \  \\\  \ /  /_/__  /  /_/__  
   \ \__\   \ \__\\________\\________\ \_______\ \_______\\________\\________\
    \|__|    \|__|\|_______|\|_______|\|_______|\|_______|\|_______|\|_______|
                                                                              
                                                                              
**************************************************************************************                                                                             
      ''')

#Taking Range Input
start = int(input("Input The Initial Value:")) 
end = int(input("Input The Terminal Value:"))

#Game_Logic
for number in range(start , end+1):
    if number % 3 == 0 and number % 5 == 0 :
        print("!! FizzBuzz !!")
    elif number % 3 == 0:
        print("Fizz!") 
    elif number % 5 == 0:
        print("Buzz!") 
    else :
        print(number)

#The 'range()' Method In Python Is Used To Define A Sequence Of Integers Within A Specified Interval.
#It Takes 3 Parameters:
#   start: The starting integer of the range (inclusive). Defaults to 0.
#   stop: The ending integer of the range (exclusive).
#   step(optional): The interval between each number in the range. Defaults to 1.

#Syntax: 
#   range(start, stop, step)