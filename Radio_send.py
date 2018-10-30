from microbit import *
import radio

radio.on()
radio.config(channel=19)        # Choose your own channel number
radio.config(power=7)           # Turn the signal up to full strength

my_message = "Be nice to yu turkeys dis christmas, Cos' turkeys just wanna hav fun, Turkeys are cool, turkeys are wicked, An every turkey has a Mum."
steps=0
# Event loop.
while True:
    if accelerometer.was_gesture("shake"):
        steps=steps+1
        radio.send(str(steps))
        display.show(str(steps))