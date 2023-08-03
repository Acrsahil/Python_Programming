from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def end(seconds):
    time_elapsed = 0
    print(CLEAR)

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        
        minutes_left = time_left // 60
        seconds_left = time_left % 60 

        print(f"{CLEAR_AND_RETURN}Rest will be: {minutes_left:02d}:{seconds_left:02d}")
    playsound("start.mp3")
    playsound("start.mp3")
 

def start(seconds):
    time_elapsed = 0
    print(CLEAR)

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        
        minutes_left = time_left // 60
        seconds_left = time_left % 60 

        print(f"{CLEAR_AND_RETURN}Start will be in: {minutes_left:02d}:{seconds_left:02d}")
    playsound("end.mp3")
    playsound("end.mp3")


def conveter():
    minutes = 30
    seconds = 0
    total_seconds = minutes * 60 + seconds
    return total_seconds

def gapsec():
    minutes = 5
    seconds = 0
    total_seconds = minutes * 60 + seconds
    return total_seconds
    

hour = int(input("Enter the total hour: "))
count = 0
for i in range(0,(hour*2)):
    end(conveter())
    if count<(hour*2)-1 :
       start(gapsec())
       count+=1
       
    







