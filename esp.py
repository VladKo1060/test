import time
import serial
import win32api
import keyboard

a = 90
keyboard.wait("w")

with serial.Serial('COM3', 9600) as ser:
    ser: serial.Serial
    ser.read()
    # x, y, btn = ser.readline().split()
    # print(x, y, btn)
    while True:
        mx, my = win32api.GetCursorPos()
        try:
            y, x, btn = map(int, bytes(ser.readline()).decode().split())
            print(x, y, btn)
            if not int(btn):
                win32api.SetCursorPos((int(mx + x // a), int(my - y // a)))
        except ValueError:
            print("ReadError")


