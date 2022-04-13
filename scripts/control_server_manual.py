from communication import SerialCommunication
from solver import Isa

STRING_TO_ISA = {cur_isa.get_short_description() : cur_isa for cur_isa in Isa}

# Set up elements to be used in script
communication = SerialCommunication('/dev/ttyUSB0', 9600)

# Print welcome message
print("====================================================================================")
print("Control server started. Waiting for user input.")
print("====================================================================================\n")

# Loop forever, manually specifying each state transition
while True:

    # Receive next input and print to check received item
    firmware_input = communication.readline()
    print("Input was %s", firmware_input)

    # Select the next ISA to send to microcontroller
    next_isa = input("Select the next ISA instruction to send: ")
    while not next_isa in STRING_TO_ISA:
        next_isa = input("Invalid isa. Try a different value")
    next_isa = STRING_TO_ISA[next_isa]

    # Send the ISA to microcontroler
    communication.write(next_isa.get_isa_number().to_bytes(1, "little"))
