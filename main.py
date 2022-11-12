import random
from functions import *         #import required functions from 'functions.py'

low_angle = 140
high_angle = 35
right_angle = 84


initialize()

#game and arduino output:
choice = True

while choice:
    gen = random.randint(1, 101)
    usr = get_input()
    
    while usr != gen:
        if usr.isdigit() :     
            usr = int(usr) 
            if usr > gen:
                servo.write(high_angle)
                high_light()
                usr = high_text()
            
            elif usr < gen:
                servo.write(low_angle)
                low_light()
                usr = low_text()
        else :    
            usr = invalid_input()

    
    servo.write(right_angle)
    right_light()
    right_text()
    
    choice = play_again()
    if choice == "n":
        thank_you()
        choice = False
    else:
        alright()
        choice = True