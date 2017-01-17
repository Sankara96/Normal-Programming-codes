import serial

ser = serial.Serial('COM8',baudrate=9600)
print 's'
for i in range(10000):
    ser.write('a')
print 't'
ser.sankar
ser.close()