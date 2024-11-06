from calculator_v1 import arithmetic_calculator

print('''
   _____________________
  |  _________________  |
  | |              0. | |
  | |_________________| |
  |  ___ ___ ___   ___  |   .d8888b.           888                   888          888                  
  | | 7 | 8 | 9 | | + | |  d88P  Y88b          888                   888          888                    
  | |___|___|___| |___| |  888    888          888                   888          888                    
  | | 4 | 5 | 6 | | - | |  888         8888b.  888  .d8888b 888  888 888  8888b.  888888 .d88b.  888d8888
  | |___|___|___| |___| |  888            "88b 888 d88P"    888  888 888     "88b 888   d88""88b 8888P"  
  | | 1 | 2 | 3 | | x | |  888    888 .d888888 888 888      888  888 888 .d888888 888   888  888 888
  | |___|___|___| |___| |  Y88b  d88P 888  888 888 Y88b.    Y88b 888 888 888  888 Y88b. Y88..88P 888   
  | | . | 0 | = | | / | |   "Y8888P"  "Y888888 888  "Y8888P  "Y88888 888 "Y888888  "Y888 "Y88P"  888
  | |___|___|___| |___| |
  |_____________________|         

8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8 
''')

continue_calc = True
previous_res = None

while continue_calc:
    res = arithmetic_calculator(previous_res)

    if res["result"] == None: #Error Condition
        print("Operation Unsuccessful!")
        print(" ")
    elif res["result"] == '@': #'Exit' Condition
        print("Operation Terminated! Shutting Down. . .")
        print(" ")
        break
    else: #Displaying Result According To Different Formats For Different Operation Types 
        # print(f"{res["equation"]} = {res["result"]}")                                                        #For "calculator_v0"
        if res["operator"] in ["!", "d=>f", "f=>d"]:                                                           #For "calculator_v1"
            print(f"{res["variables"][0]} {res["operator"]}  = {res["result"]}")  #For Operations With Single Parameters
        elif res["operator"] in ["sin","cos","tan","sec","cosec","cot"]:
            print(f"{res["operator"]} {res["variables"][0]}   = {res["result"]}") #For Trigonometric Operations
        elif res["operator"] == "fib":                                            # For Fibonnaci Sequence (Operations Returning List as Output)
            ("Obtained Fibonacci Sequence: \n")
            for num in res["result"]:
                print(f"{num} ", end = ' ')
        else:                                                                     #For Other 'General' Operations With Two Parameters
            print(f"{res["variables"][0]} {res["operator"]} {res["variables"][1]} = {res["result"]}")

        print(" ")

#Continue_Operations_Logic(Restart Prompt)-------------------------------------------------------------------------------------------------------------------------------------------#
        continue_op = input("Continue Operations? (Y/N): ")

        while True:
            if continue_op.lower() in ['y','yes']:
                previous_res = res["result"]
                break
            elif continue_op.lower() in ['n','no']:
                print("We Hope To See You Soon!")
                print(" ")
                continue_calc = False
                break
            else:
                print("Not A Valid Input :// Please Try Again : :")
                continue_op = input("Continue Operations? (Y/N): ")

