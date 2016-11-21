import socket
import sys
import time

IP = "192.168.1.105"
port = 10000
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, port))

# k = input("Enter the command: ")
k = sys.argv[1]
# k = 'v'
print(k)

factor = .55
loop = True

rightMotor = 0
leftMotor = 0
if k == 'f' or k == 'F':
    print ("Going Forward")
    rightMotor =255
    leftMotor = 255
elif k==('r') or k=='R':
    print ("Turining Right")
    rightMotor = -255
    leftMotor = 255
elif k==('b') or k=='B':
    print ("Going Backward")
    rightMotor = -255
    leftMotor = -255
elif k ==('l') or k=='L':
    print ("Turning Left")
    rightMotor = 255
    leftMotor = -255
elif k ==('s') or k=='S':
    print ("Stop ...")
    rightMotor = 0
    leftMotor = 0
else:
    print("Please issue one of 'f,b,r,l,s' commands")
    pass
MSG = str("*{:0=+4d},{:0=+4d}# | ").format(int(factor*leftMotor), int(factor*rightMotor))
print(MSG)
s.send(MSG.encode())

time.sleep(1)
rightMotor = 0
leftMotor = 0

MSG = str("*{:0=+4d},{:0=+4d}# | ").format(int(factor*leftMotor), int(factor*rightMotor))
s.send(MSG.encode())


s.close()

