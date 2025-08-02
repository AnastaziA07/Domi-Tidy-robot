import serial
import time

def notify_robot():
    ser = serial.Serial('COM3', 9600)  # ดูพอร์ตก่อนว่า micro:bit ต่อกับอะไร
    time.sleep(2)
    ser.write(b'ALERT\n')  # micro:bit ต้องมีโค้ดให้รับคำว่า ALERT แล้วเปิดไฟ/เล่นเสียง
    ser.close()
