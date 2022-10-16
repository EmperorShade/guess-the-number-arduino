#!/usr/bin/python
# -*- coding: utf-8 -*-
# move a servo from a Tk slider - scruss 2012-10-28
 

import time
import pyfirmata
import random


r1 = 1
r2 = 10

# board = pyfirmata.Arduino('')


while True:

    comp_no = random.randint(r1, r2)

    user_guess = float(input("Guess a numkber between 1 and 100: "))

    while user_guess != comp_no:
        if user_guess > comp_no:
            print("Number too high!! ")
            user_guess = float(input("Try again, guess lower: "))
        elif user_guess < comp_no:
            print("Number too low!!")
            user_guess = float(input("Try a bigger number: "))

    print("Thats great!! You won!")
    choice = input("Wanna play again?? (y/n): ").lower()

    if choice == "n":
        print("that was great playing with you? byeee")
        time.sleep(1.4)
        
        break