def decrypt(encypted, n):
    temp = ""
    for i in range(0, n):
        temp += chr(ord(encypted[i]) - i - 1)
    return temp


def encrypt(passwd):
    temp = ""
    for i in range(0, len(passwd)):
        temp += chr(ord(passwd[i]) + i + 1)
    return temp + "5f4dcc3b5aa765d61d8327deb882cf99"


passwd = input("Enter the password: ")

encryptes = encrypt(passwd)

print("Encrypted password: ", encryptes)
print("Decrypted password: ", decrypt(encryptes, len(passwd)))
