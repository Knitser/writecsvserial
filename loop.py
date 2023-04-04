import itertools
import serial
import time

ser = serial.Serial('COM3', 115200)

with open('can2.csv', 'r') as file:
    lines = itertools.cycle(file)
    for line in lines:
        ser.write(line.encode())
        print(ser.readline().decode('utf-8').strip())
        time.sleep(0.050)
