from microbit import *

steps = 0
display.show(str(steps))

while True:
    if accelerometer.was_gesture("shake") or button_a.is_pressed():
        steps += 1
        print(steps)
        display.scroll(str(steps))
