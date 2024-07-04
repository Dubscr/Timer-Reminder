# link to lab https://amrita.olabs.edu.in/?sub=79&brch=16&sim=126&cnt=4

import playsound
import os
import time
import keyboard
import webbrowser

# Grabs directory path of this file
dir_path = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")

# This defines when the current timer interval is ended.
# This gets set to true when the timer is done with its 
# current countdown and then reset to false.
completed = False

# Can be link or just string
linkOrThing = input("What is the link or thing you want reminded of? (Input string or link)\n")

# Check if link. Will handle it later
isLink = bool(linkOrThing.__contains__("https://") or linkOrThing.__contains__("http://") or linkOrThing.__contains__("www"))

# Amount of times that it has looped
timesLooped = 0

# Amount of times that it will loop (Set by user).
loopAmount = 1

# Make sure that user cannot put wrong input in. If they do put wrong input, tell user and exit.
try:
    minutesToWait = input("In how many minutes do you want to be reminded? \n")
    minutesToWait = int(minutesToWait) * 60
    initialTimeToWait = minutesToWait
except:
    print("Invalid input: Must answer with an integer (1, 2, 3, ...).")
    exit()
try:
    loop = bool(int(input("Do you want it to loop? no: 0 yes: 1\n")))
except:
    print("Invalid input: Must answer with an integer such as: -> '0' (no) or '1' (yes)")
    exit()

if(loop):
    try:
        loopAmount = int(input("How many times do you want it to loop before ending timer and reminding you for the last time (opens link if link)? \n"))
    except:
        print("Invalid input: Must answer with an integer (1, 2, 3, ...).")
        exit()

# Set start time
startTime = time.time()

# Calls final function, then stops script.
def OnExit():
    if(isLink):
        webbrowser.open(linkOrThing)
    else:
        for x in range(10):
            print(linkOrThing)
    exit()

# Get time in seconds since timer start
def GetCurrentTime(roundToWhole = False):
    if(roundToWhole):
        return round(time.time() - startTime)
    elif(not roundToWhole):
        return time.time() - startTime

# Get time in seconds left before timer ends
def GetTimeLeft(roundToWhole = False):
    return minutesToWait - GetCurrentTime(roundToWhole)

# When timer has reached it's end. It plays sound and checks if it should exit (Only if finite looping is set).
def OnTimerFinish():
    playsound.playsound(dir_path + "/HelloWorld.mp3")
    if(loopAmount != 0 and timesLooped >= loopAmount):
        OnExit()

# Main Loop. Runs until stop when not looping.
while(completed == False or loop):    
    if(GetCurrentTime() >= minutesToWait):
        completed = True

    if(completed == True):
        if(not loop):
            timesLooped += 1
            OnTimerFinish()
            OnExit()
        else:
            timesLooped += 1
            OnTimerFinish()
            minutesToWait += initialTimeToWait
            completed = False

# Checking for key 'press'. This needs further optimization, as it is constantly checking.
while(completed == False or loop):
    ### Why I did release instead of pressed:
    # if key '\' is released. This is to optimize key pressing
    # as constantly checking would cause performance issues.
    # There is a better way of doing this, but this works for now.
    if (keyboard.release('\\')):  
        exit()