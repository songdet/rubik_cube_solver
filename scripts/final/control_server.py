from color_detection.defaults import DEFAULT_COLOR_BOUNDS, DEFAULT_IMAGE_BOUND
from communication import SerialCommunication
from camera import Camera
from color_detection import ColorDetector
from solver import Solver
from output import StandardOutput
from transition import TransitionHandler
from rubik_machine_state import RubikMachineState

# Set up transition handler that will be used by finite state machine to handle user input
communication = SerialCommunication('/dev/ttyUSB0', 9600)
camera = Camera("192.168.4.1", "80")
photo_detector = ColorDetector(DEFAULT_IMAGE_BOUND, DEFAULT_COLOR_BOUNDS)
solver = Solver()
output = StandardOutput()
transition_handler = TransitionHandler(communication, camera, photo_detector, solver, output)

# Set up finite state machine that will keep track of machine state
machine_state = RubikMachineState(transition_handler)

# Print welcome message
print("====================================================================================")
print("Control server started. Waiting for user input.")
print("====================================================================================\n")


# Loop forever, receiving input from the chip and using machine state to handle it
while True:
    input = communication.readline()
    machine_state.transition(input)
    if machine_state.is_complete():
        machine_state.transition(b'R\n')
