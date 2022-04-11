from communication import Communication
from transition import TransitionHandler
from rubik_machine_state import RubikMachineState
from solver import Isa
from cube import Color

# Communicate via user input to simulate serial communication
class UserInputCommunication(Communication):

    def readline(self):
        result = input("Enter 1 for ok, 2 for reset, and 3 for stop: ")
        if result == "1":
            return b'O\n'
        elif result == "2":
            return b'R\n'
        else:
            return b'S\n'
    
    def write(self, data):
        print("Command sent: %s" % repr(data))

# Fake camera that doesn't do anything
class FakeCamera:
    def take_photo(self, img_file):
        print("Taking photo and saving it to %s" % img_file)

# Fake color detector that doesn't do anything
class FakeColorDetector:
    def __init__(self, detected_colors):
        self._detected_colors = detected_colors

    def detect(self, _):
        print("The following colors are detected: %s" % repr(self._detected_colors))
        return self._detected_colors

# Fake solver that doesn't do anything
class FakeSolver:
    def __init__(self, solution):
        self._solution = solution

    def solve(self, _):
        print("The following solution is found %s" % repr(self._solution))
        return self._solution

# Set up transition handler that will be used by finite state machine to handle user input
communication = UserInputCommunication()
camera = FakeCamera()
first_photo_detector = FakeColorDetector([Color.BLUE, Color.GREEN, Color.ORANGE, Color.ORANGE, Color.WHITE, Color.WHITE, Color.WHITE])
second_photo_detector = FakeColorDetector([Color.ORANGE, Color.RED])
solver = FakeSolver([Isa.HH, Isa.HV, Isa.RBC])
transition_handler = TransitionHandler(communication, camera, first_photo_detector, second_photo_detector, solver)

# Set up finite state machine that will keep track of machine state
machine_state = RubikMachineState(transition_handler)

# Print welcome message
print("====================================================================================")
print("Control server started. Waiting for user input.")
print("====================================================================================\n")


# Loop forever, receiving input from the chip and using machine state to handle it
while True:
    user_input = communication.readline()
    machine_state.transition(user_input)
    if machine_state.is_complete():
        machine_state.transition(b'R\n')