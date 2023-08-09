MORSE_CODE = (
 ("-...", "B"), (".-", "A"), ("-.-.", "C"), ("-..", "D"), (".", "E"), ("..-.", "F"), ("--.", "G"),
 ("....", "H"), ("..", "I"), (".---", "J"), ("-.-", "K"), (".-..", "L"), ("--", "M"), ("-.", "N"),
 ("---", "O"), (".--.", "P"), ("--.-", "Q"), (".-.", "R"), ("...", "S"), ("-", "T"), ("..-", "U"),
 ("...-", "V"), (".--", "W"), ("-..-", "X"), ("-.--", "Y"), ("--..", "Z"), (".-.-.-", "."),
 ("-----", "0"), (".----", "1"), ("..---", "2"), ("...--", "3"), ("....-", "4"), (".....", "5"),
 ("-....", "6"), ("--...", "7"), ("---..", "8"), ("----.", "9"), ("-.--.", "("), ("-.--.-", ")"),
 (".-...", "&"), ("---...", ":"), ("-.-.-.", ";"), ("-...-", "="), (".-.-.", "+"), ("-....-", "-"),
 ("..--.-", "_"), (".-..-.", '"'), ("...-..-", "$"), (".--.-.", "@"), ("..--..", "?"), ("-.-.--", "!")
)
MORSE_CODE = dict(MORSE_CODE) # changing the data types

def print_intro():# first function call
 print("\nWelcome to Texasmorse \nThis program encodes and decodes Morse code.\n")

def encode(message):
    ans = ""
    for char in message:  # Convert the whole message to uppercase for encoding
        if char in MORSE_CODE:
            ans += MORSE_CODE[char] + " "  # Add Morse code for the character and a space
        else:
            ans += " "  # If character not found, add a space
    print(ans)

   

def decode(message): # third function call
    try:
        for key,value in MORSE_CODE.items():
            if(message == key): # if the message is values then printing key
                ans1 = value
        print(ans1)
    except UnboundLocalError:
       print("Invalid Code!")


def print_outro():
  print("\nThanks for using the program, goodbye!")

def get_input(): # second function call
    notvalid = 1 
    while(notvalid):
        encodeORDecode = input("\nWould you like to encode (e) or decode (d):",)

        #  to cheak wheather user input the valid character or not
        if(encodeORDecode.lower() == 'e' ): # handeling both cases
          message = input("\nWhat message would you like to encode: ")
          message = message.upper()
          encode(message)
          check = input("\nWould you like to encode/decode another message? (y/n): ")
          if(check.lower() == 'y'):
            notvalid = 0 # breaks  loops
            get_input()
          elif(check.lower() == 'n'):
            notvalid = 0
            print_outro()
            break;
          

        elif encodeORDecode.lower() == 'd':
          message = input("\nWhat message would you like to decode: ")
          decode(message)
          check = input("\nWould you like to encode/decode another message? (y/n): ")

          if(check.lower() == 'y'):
            notvalid = 0 # breaks loops
            get_input()
          elif(check.lower() == 'n'):
            notvalid = 0
            print_outro() 
            break
        else:
          print("Invalid Mode")

if __name__ == '__main__':

 print_intro() #prints intro
 get_input() # takes input from user

 