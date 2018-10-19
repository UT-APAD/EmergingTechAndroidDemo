#import sys
#sys.path.append('/usr/lib/python3/dist-packages')
import serial,time
#from /usr/lib/python3/dist-packages/serial import serial
#import time
port = "/dev/ttyACM1"

baud=115200
while True:
    s = serial.Serial(port)
    s.baudrate = baud
    data = s.readline()
    data = int(data[0:4])
    print(data)
    time.sleep(1)
