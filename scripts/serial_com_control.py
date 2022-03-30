import serial

# Set up serial communication line
ser = serial.Serial('/dev/ttyUSB0', 9600)


while True:

    # Block read until data is received
    val = ser.readline()
    print("The value %s is received!" % val)

    # Send back command to test receiver
    ser.write(b'OK\n')