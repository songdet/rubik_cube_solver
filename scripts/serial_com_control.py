from enum import Enum
import serial

class Button(Enum):
    GRIPPER = 0,
    ARM = 1

# Print welcome message
print("====================================================================================")
print("Control server started. Waiting for buttons to be pressed on microcontroller")
print("====================================================================================\n")

# Set up serial communication line
ser = serial.Serial('/dev/ttyUSB0', 9600)

while True:

    # Block read until data is received
    val = ser.readline()
    selected_button = Button.GRIPPER
    if val == b"A\n":
        print("Button A pressed. Gripper controls now selected.")
        selected_button = Button.GRIPPER
    elif val == b"B\n":
        print("Button B pressed. Arm controls now selected")
        selected_button = Button.ARM

    if selected_button == Button.GRIPPER:

        # Prompt for the speed with which to turn the servo motor
        speed = input("Select a speed for the motor between 1 (slowest) to 60 (highest): ")
        while not speed.isdigit() or int(speed) < 1 or int(speed) > 60:
            speed = input("Invalid input. Try selecting a value between 1-60: ")
        speed = int(speed)
        write_byte = speed.to_bytes(1, 'little')

        # Send back command to test receiver
        ser.write(write_byte)

        # Print output to let us know operation completed successfully
        print("Grippers should now be turning with speed %s" % speed)

    else:

        # Prompt for direction of rotation
        direction = input("Enter 1 to extend the arm and 2 to retract the arm: ")
        while not direction.isdigit() or ((not int(direction) == 1) and (not int(direction) == 2)):
            direction = input("Invalid input. Select 1 to extend and 2 to retract the arm: ")
        direction = int(direction)
        write_byte = direction.to_bytes(1, 'little')
        
        # Send back command to receiver
        ser.write(write_byte)

        # Print output to let us know operation completed successfully
        if direction == 1:
            print("Arm should now be extending.")
        else:
            print("Arm should now be retracting.")

    # print wait for next command
    print("\n====================================================================================")
    print("Waiting for the next button to be pushed")
    print("====================================================================================\n")