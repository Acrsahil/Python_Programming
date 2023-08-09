def encode(message):
    ans = ""
    for char in message.upper():  # Convert the whole message to uppercase for encoding
        if char in MORSE_CODE:
            ans += MORSE_CODE[char] + " "  # Add Morse code for the character and a space
        else:
            ans += " "  # If character not found, add a space
    print(ans)

MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    # ... (rest of the dictionary entries)
}

message_to_encode = input("Enter a message to encode: ")
encode(message_to_encode)
