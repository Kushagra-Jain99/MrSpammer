#Author- Kushagra-Jain99

#importing required packages
import keyboard
import pyautogui  
import time

time.sleep(5)  #delaying the program so that it dosent spam on any undesired platform 

f = open("beespam.txt", 'r')  #change beespam.txt with any other text file contaning a long spammable message
#loop 
for word in f:
    if not keyboard.is_pressed('q'):  #the program will terminate if you press 'q' for 1sec
        pyautogui.typewrite(word)
        pyautogui.press("enter")
