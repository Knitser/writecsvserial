import serial
import time

ser = serial.Serial('COM5', 115200)

with open('can.csv', 'r') as file:
    for line in file:
        ser.write(line.encode())
        # print(f'Sent: {line.strip()}')
        read = ser.readline().decode('utf-8').strip()
        print(read)

        time.sleep(0.1)
