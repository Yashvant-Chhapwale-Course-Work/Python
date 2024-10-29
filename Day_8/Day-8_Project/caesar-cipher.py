from cipher_logic import caesar_cipher

print(r'''
 ______     ______     ______     ______     ______     ______   
/\  ___\   /\  __ \   /\  ___\   /\  ___\   /\  __ \   /\  == \  
\ \ \____  \ \  __ \  \ \  __\   \ \___  \  \ \  __ \  \ \  __<  
 \ \_____\  \ \_\ \_\  \ \_____\  \/\_____\  \ \_\ \_\  \ \_\ \_\
  \/_____/   \/_/\/_/   \/_____/   \/_____/   \/_/\/_/   \/_/ /_/
                                                                 
     ______     __     ______   __  __     ______     ______         
    /\  ___\   /\ \   /\  == \ /\ \_\ \   /\  ___\   /\  == \        
    \ \ \____  \ \ \  \ \  _-/ \ \  __ \  \ \  __\   \ \  __<        
     \ \_____\  \ \_\  \ \_\    \ \_\ \_\  \ \_____\  \ \_\ \_\      
      \/_____/   \/_/   \/_/     \/_/\/_/   \/_____/   \/_/ /_/    

####################################################################
      ''')


restart = True

while restart:
  action = input('Enter "Encode" or "Decode": ') 
  if action.lower() in ['encode','decode']:
    message = input(f'Please enter the text you would like to {action.lower()}: ')
    key = int(input('Please input the Key or Shift value: '))

    caesar_cipher(message,key,action)

    while True:
      restart_choice = input("Would you like to continue with data encryption/decryption? (Y/N): ")
      if restart_choice.lower() in ['yes','y']:
        restart = True
        break
      elif restart_choice.lower() in ['no','n']:
        print("We look forward to your return!")
        restart = False
        break
      else:
        print("Invalid Action :// Try Again ::")
  else:
    print("Invalid Action :// Try Again ::")

