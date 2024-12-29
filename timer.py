import time #built in python library
from playsound import playsound 

minutes_s = int(input("How long do you want to study for? Enter the minutes: "))
minutes_b = int(input("How long is your break time? Enter the minutes: "))
seconds_s = minutes_s * 60
seconds_b = minutes_b * 60

while seconds_s > 0:
    # divmod assign the quotient to mins and reminder to secs (it divides 1st argument by the second) | 125 // 60 = 2 | 125 % 60 = 5 | 2 mins and 5 secs
    mins, secs = divmod(seconds_s, 60)
    
    # Display the time in minutes:seconds format
    print(f"{mins:02}:{secs:02}", end="\r")  # The end='\r' makes it overwrite the previous line

    # Decrease the time by one second
    time.sleep(1)
    seconds_s -= 1
    
    
playsound("resources/alarm.wav")

while seconds_b > 0:
    mins, secs = divmod(seconds_b, 60)

    print(f"{mins:02}:{secs:02}", end="\r")  

    time.sleep(1)
    seconds_b -= 1

playsound("resources/alarm.wav")