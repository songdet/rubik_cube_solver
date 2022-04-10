from rubik_machine_state import State
from cube import Cube, Side
from communication import Communication

class ParentState(State):
    def __init__(self, cube):
        self.current_state = None
        self.sides = {}
        self.solution = []
        self.cube = cube
    
    def set_current_state(self, state):
        self.current_state = state
    
    def set_side(self, side, side_values):
        self.sides[side] = side_values

    def set_current_state(self, state):
        self.current_state = state
    
    def get_cube(self):
        return self.cube

class FakeCommunication(Communication):

    def __init__(self):
        self.written_data = []
    def readline(self) -> bytes:
        pass

    def write(self, data: bytes):
        self.written_data.append(data)

class FakeCamera:

    def __init__(self):
        self.taken_photos = []

    def take_photo(self, img_file):
        self.taken_photos.append(img_file)

class FakeColorDetector:

    def __init__(self, detected_colors):
        self.photos_detected = []
        self.detected_colors = detected_colors
    
    def detect(self, img_file):
        self.photos_detected.append(img_file)
        return self.detected_colors

class FakeSolver:

    def __init__(self, solution_list):
        self.solution_list = solution_list

    def solve(self, _):
        return self.solution_list