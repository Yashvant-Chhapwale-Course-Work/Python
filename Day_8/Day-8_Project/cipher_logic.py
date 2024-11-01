from character_list import alphabets,numbers,symbols


def caesar_cipher(text_input,shift,action_input):
    transformed_text = ""

    #Transforming 'shift' value to negative for 'decode' action so as to shift the characters back to original position for 'Decryption'.
    if action_input.lower() == "decode":
      shift *= -1


    for letter in text_input:
      #Cipher Logic For Alphabets:
      if letter in alphabets:
        shift_in_position = alphabets.index(letter) + shift
        shift_in_position %= len(alphabets)     #>>>>>>>> This Expression ensures that the 'shift_in_position' value wraps around if it exceeds the length of the lists, which prevents an 'Index Out Of Range' error.      
        transformed_text += alphabets[shift_in_position] #For Example: The 'alphabets_small[]' list contains 26 letters (like the English alphabet),and the 'shift_in_position' is 28,then it would update 'shift_in_position' to '2' (since 28 % 26 = 2), effectively circling back to the start of the 'alphabets_small[]' list. 

      #Cipher Logic For Numbers:
      elif letter in numbers:
        shift_in_position = numbers.index(letter) + shift
        shift_in_position %= len(numbers)                     
        transformed_text += numbers[shift_in_position]

      #Cipher Logic For Symbols:  
      elif letter in symbols:
        shift_in_position = symbols.index(letter) + shift
        shift_in_position %= len(symbols)                     
        transformed_text += symbols[shift_in_position]

      else:
        transformed_text += letter


    print(f"{action_input.capitalize()}d Result: {transformed_text}")      
    print(" ")