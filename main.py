import pyfirmata
import random
import time

board = pyfirmata.Arduino('COM6')

servo = board.get_pin('p:5:s')
red = board.get_pin('d:9:p')      #red rgb
green = board.get_pin('d:10:p')    #green rgb 
blue = board.get_pin('d:11:p')     #blue rgb

def led_stop():
    red.write(0)
    green.write(0)
    blue.write(0)

def high_light():                   #led - high (red light)
    red.write(1)
    green.write(0.25)
    time.sleep(2.4)
    red.write(0)
    green.write(0)

def right_light():                  #led - right (green light)
    green.write(1)
    time.sleep(5) 
    green.write(0)

def low_light():
    blue.write(1)
    time.sleep(2.4)
    blue.write(0)

def ambient_light():                #constant color changing 
    red.write(1)
    green.write(1)
    blue.write(1)
    board.pass_time(3)


servo.write(15)
time.sleep(1)
servo.write(135)
time.sleep(1)
servo.write(83)
ambient_light()
led_stop()
board.pass_time(1)
while True:
    gen = random.randint(1, 101)
    print(gen)
    # low_light()
    usr = input("guess: ")
    while usr != gen:
        if usr.isdigit() :     
            usr = int(usr) 
            if usr > gen:
                servo.write(35)
                print("high")
                high_light()
                # board.pass_time(2)
                # servo.write(0)
                usr = (input("guess: "))
            elif usr < gen:
                servo.write(140)
                print("less")
                # board.pass_time(2)
                low_light()
                usr = (input("guess: "))
        else :
            print('wrong input')        
            usr = input('guess: ')
    servo.write(85)
    # board.pass_time(0.4)
    right_light()
    choice = input("play again? y/n").lower

    if choice == "n":
        break
    elif choice == "y":
        print('alright')
        