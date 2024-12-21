import random

print("********Game: Sessior Paper Rock *******")
print("****************************************")
print()
turn = int(input("How many round you want to play? "))
compcnt = 0
usercnt = 0
draw = 0

maps = {1: "Sessior", 2: "Paper", 3: "Rock"}
while turn:
    comp = random.randint(1, 3)
    user = int(input("enter 1 :sessior, 2:paper, 3:rock :"))
    print()
    if comp == user:
        print(f"Match Draw! \nyou: {maps[user]} \ncomputer: {maps[comp]}")
        draw += 1
        print(f"Draw score is {draw}")
    elif (
        (comp == 1 and user == 2)
        or (comp == 3 and user == 1)
        or (comp == 2 and user == 3)
    ):
        print(f"!lose, \nYou: {maps[user]} \nComputer: {maps[comp]}")
        compcnt += 1
    else:
        print(f"!Won, \nYou: {maps[user]} \nComputer: {maps[comp]}")
        usercnt += 1
    turn -= 1
    print(f"Your score: {usercnt} \nComputer: {compcnt}")
    print()

if compcnt == usercnt:
    print("The match was draw !")
elif compcnt > usercnt:
    print(f"The match was won by conputer with the score {compcnt}")
else:
    print(f"The match was won by user with the score {usercnt}")
