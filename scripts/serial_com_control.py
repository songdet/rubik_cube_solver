from enum import Enum
import serial

class Button(Enum):
    A = 0,
    B = 1

# Print welcome message
print("====================================================================================")
print("Control server started. Waiting for buttons to be pressed on microcontroller")
print("====================================================================================\n")

# Set up serial communication line
ser = serial.Serial('/dev/ttyUSB0', 9600)

while True:

    # Block read until data is received
    val = ser.readline()
    selected_button = Button.A
    if val == b"A\n":
        print("Button A pressed. Top and bottom grippers are now selected.")
        selected_button = Button.A
    elif val == b"B\n":
        print("Button B pressed. Left and right grippers are now selected.")
        selected_button = Button.B

    # Prompt for the speed with which to turn the servo motor
    speed = input("Select a speed for the motor between 1 (slowest) to 100 (highest). A value of 0 means unlimited speed: ")
    while not speed.isdigit() and (int(speed) < 0 or int(speed) > 100):
        speed = input("Invalid input. Try selecting a value between 0-100: ")
    write_byte = int(speed).to_bytes(1, 'little')

    # Send back command to test receiver
    ser.write(write_byte)

    # Print out confirmation that command was sent
    if selected_button == Button.A:
        print("Top and bottom grippers should now be turning with speed %s" % speed)
    else:
        print("Left and right grippers should now be turning with speed %s" % speed)

    # print wait for next command
    print("\n====================================================================================")
    print("Waiting for the next button to be pushed")
    print("====================================================================================\n")