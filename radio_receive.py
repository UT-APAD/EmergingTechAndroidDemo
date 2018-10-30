from microbit import *
import radio

radio.on()
radio.config(channel=19)        # Choose your own channel number
radio.config(power=7)           # Turn the signal up to full strength

#my_message = "Be nice to yu turkeys dis christmas, Cos' turkeys just wanna hav fun, Turkeys are cool, turkeys are wicked, An every turkey has a Mum."

# Event loop.
while True:
        incoming = radio.receive()
        if incoming is not None:
            display.show(incoming)
            print(incoming)
        sleep(500)