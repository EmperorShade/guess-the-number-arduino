import time
import pyfirmata
from fontstyle import apply

board = pyfirmata.Arduino('COM6')   #setup

servo = board.get_pin('p:6:s')
red = board.get_pin('d:9:p')      #red rgb
green = board.get_pin('d:10:p')    #green rgb 
blue = board.get_pin('d:11:p')     #blue rgb


#text
def get_input():
    get_input_string = apply("\nGuess a number between 1 and 100: ", 'bold/yellow')
    input_usr = input(get_input_string)
    return input_usr

def low_text():
    low_string = apply("Guess is too low. Guess higher: ", 'blue')
    low_input = input(low_string)
    return low_input

def high_text():
    high_string = apply("Guess is too high! Try a lower number: ", 'red')
    high_input = input(high_string)
    return high_input

def right_text():
    right_string = apply("Thats RIGHT!!", 'green/bold/blink')
    print(right_string)
    time.sleep(0.3)

def invalid_input():
    invalid_string = apply("Invalid input. Guess must be a number between 1 and 100: ", 'white/red_bg/bold/italic/')
    invalid_getinput = input(invalid_string)
    return invalid_getinput

def play_again():
    play_again_string = apply("Type 'n' if you wish to stop playing (press 'enter' to continue):  ", 'white/bold')
    play_again_input = str(input(play_again_string))
    return play_again_input

def alright():
    alright_string = apply("Alright!", 'bold/darkcyan')
    print(alright_string)

def thank_you():
    thank_string = apply("Thanks for playing!", 'cyan/bold')
    print(thank_string)

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

def initialize():                   #check if all components are working
    servo.write(83)
    ambient_light()
    led_stop()
    board.pass_time(1)

