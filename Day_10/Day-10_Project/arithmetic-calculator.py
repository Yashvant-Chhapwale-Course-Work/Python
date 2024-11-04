from calculator_v0 import arithmetic_calculator

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

8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8=8 
''')

continue_calc = True

while continue_calc:
    res = arithmetic_calculator()

    if res == None:
        print("Operation Unsuccessful!")
        print(" ")
    else:
        print(f"{res["var_1"]} {res["operator"]} {res["var_2"]} = {res["result"]}")
        print(" ")

        continue_op = input("Continue Operations? (Y/N): ")

        while True:
            if continue_op.lower() in ['y','yes']:
                break
            elif continue_op.lower() in ['n','no']:
                print("We Hope To See You Soon!")
                continue_calc = False
                break
            else:
                print("Not A Valid Input :// Please Try Again : :")
                continue_op = input("Continue Operations? (Y/N): ")

