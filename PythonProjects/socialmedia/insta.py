from instagrapi import Client

# Replace 'YOUR_USERNAME' and 'YOUR_PASSWORD' with your Instagram account credentials
YOUR_USERNAME = "sahilacharya20"
YOUR_PASSWORD = "Acr9851133606@"

cl = Client()
cl.login(YOUR_USERNAME, YOUR_PASSWORD)

user_id = cl.user_id_from_username(YOUR_USERNAME)
medias = cl.user_medias(user_id, 20)
