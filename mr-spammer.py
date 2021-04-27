#Author- Kushagra-Jain99

#importing required packages
import pyautogui  
import time

time.sleep(5)  #delaying the program so that it dosent spam on any undesired platform 

f = open("beespam.txt", 'r')  #change beespam.txt with any other text file contaning a long spammable message
#loop 
for word in f:
    pyautogui.typewrite(word) #types the word
    pyautogui.press("enter")  #enters the word
