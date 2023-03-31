import itertools
import serial
import time

ser = serial.Serial('COM5', 115200)

with open('can.csv', 'r') as file:
    lines = itertools.cycle(file)
    for line in lines:
        ser.write(line.encode())
        print(ser.readline().decode('utf-8').strip())
        time.sleep(0.1)
