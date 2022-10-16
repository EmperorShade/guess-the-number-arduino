#jai shriram

#github.com/shriramsburger
#reddit: u/randomlazycat

#### less gooooo ######

#importing modules
import time
import pyfirmata
import random

#presetting some variables
range1 = 1          #lower limit of value to be guessed
range2 = 10         #higher limit of value to be guessed
high_angle = 160    #angle at which servo points at "high"
low_angle = 45      #angle at which servo points at "low"
right_angle = 77    #angle at which servo points at "right"

#initializing arduino
board = pyfirmata.Arduino('')

#defining components
servo = board.get_pin('d:pin:p')     #servo

red = board.get_pin('d:pin:p')      #red rgb
green = board.get_pin('d:pin:p')    #green rgb 
blue = board.get_pin('d:pin:p')     #blue rgb

#creating some functions
def high_servo():                   #servo movement -  guess is large
    servo.write(high_angle)
    board.pass_time(1)

def low_servo():                    #servo movement - guess is low
    servo.write(low_angle)

def right_servo():                  #servo movement - guess is right
    servo.write(right_angle)

def high_light():                   #led - high (red light)
    red.write(1)
    time.sleep(3)
    red.write(0)

def low_light():                    #led - low (yellow light)
    red.write(255)
    green.write(234)
    blue.write(0)
    time.sleep(4)
    red.write(0)
    green.write(0)
    blue.write(0)

def right_light():                  #led - right (green light)
    green.write(128)
    time.sleep(5)
    green.write(0)

def ambient_light():                #constant color changing 
    while choice != "yes" and choice != "no":
        red.write(random.random())
        green.write(random.random())
        blue.write(random.random())
        board.pass_time(0.3)

def led_stop():
    red.write(0)
    green.write(0)
    blue.write(0)

while True:
    led_stop()
    comp_no = random.randint(range1, range2)

    user_guess = float(input("Guess a numkber between 1 and 100: "))

    while user_guess != comp_no:

        #high
        if user_guess > comp_no:
            high_servo()
            high_light()
            print("Number too high!! ")
            user_guess = float(input("Try again, guess lower: "))

        #low    
        elif user_guess < comp_no:
            low_servo()
            low_light()
            print("Number too low!!")
            user_guess = float(input("Try a bigger number: "))

    right_servo()
    print("Thats great!! You won!")
    right_light()
    choice = input("Wanna play again?? (y/n): ").lower()
    ambient_light()

    if choice == "n":
        led_stop()
        print("that was great playing with you? byeee")
        time.sleep(1.4)
        
        break