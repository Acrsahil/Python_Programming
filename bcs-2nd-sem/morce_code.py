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
MORSE_CODE = dict((x, y) for x, y in MORSE_CODE)

def print_intro():# first function call
 print("\nWelcome to Texasmorse \nThis program encodes and decodes Morse code.\n")

def encode(message):
    try:
        present = 0  # Initialize present for each character iteration
        encoded_message = ""
        for c in message:
            for key, value in MORSE_CODE.items():
                if c == value: 
                    encoded_message = key + " " # adding blank to add space in between
                    print(encoded_message,end = "")
    except UnicodeEncodeError:
        print("Invalid Code!")
   

def decode(message):
    try:
        encoded_message = ""
        morse_chars = message.split()  # Split the input Morse code into individual characters
        for char in morse_chars:
            for key, value in MORSE_CODE.items(): #itrating key and value from dictionary
                if char == key:
                    encoded_message=value # encoding each character to morse code
                    print(encoded_message,end = "") # printing morse code
    except :
        print("Invalid Code!")




def print_outro():
  print("\nThanks for using the program, goodbye!")

def get_input(): # second function call
    notvalid = 1 
    while(notvalid):
        encodeORDecode = input("\nWould you like to encode (e) or decode (d):",)

        if(encodeORDecode.lower() == 'e' ): # handeling both cases
        #  to cheak wheather user input the valid character or not
          message = input("\nWhat message would you like to encode: ")
          message = message.upper() #change the case before passing
          encode(message) # function call to encode
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
          decode(message) # function code to decode
          check = input("\nWould you like to encode/decode another message? (y/n): ")

          if(check.lower() == 'y'):
            notvalid = 0 # breaks loops
            get_input() # Recurssion call to input
          elif(check.lower() == 'n'):
            notvalid = 0
            print_outro() # function call to print outro
            break
        else:
          print("Invalid Mode")

if __name__ == '__main__':

 print_intro() #prints intro
 get_input() # takes input from user

 