import pytest
from rubik_machine_state.detection_state import DetectionState
from solver import Isa
from rubik_machine_state import State
from communication import Communication
from transition import TransitionHandler

class ParentState(State):
    def __init__(self):
        self.current_state = None
    
    def set_current_state(self, state):
        self.current_state = state

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

def test_detection_state():

    # Setup detection
    parent_state = ParentState()
    communication = FakeCommunication()
    camera = FakeCamera()
    transition_handler = TransitionHandler(communication, camera)
    detection_state_1 = DetectionState(parent_state, transition_handler, None, Isa.RV, "photo_location1.jpg", "photo_location2.jpg")
    detection_state_2 = DetectionState(parent_state, transition_handler, detection_state_1, Isa.RV, "photo_location1.jpg", "photo_location2.jpg")
    assert detection_state_2.is_complete() == False

    # Test transitions
    detection_state_2.transition(b'')
    assert communication.written_data[0] == Isa.ST.get_isa_number().to_bytes(1, "little")

    detection_state_2.transition(b'')
    assert communication.written_data[1] == Isa.HH.get_isa_number().to_bytes(1, "little")

    detection_state_2.transition(b'')
    assert camera.taken_photos[0] == "photo_location1.jpg"

    detection_state_2.transition(b'')
    assert communication.written_data[2] == Isa.HV.get_isa_number().to_bytes(1, "little")

    detection_state_2.transition(b'')
    assert camera.taken_photos[1] == "photo_location2.jpg"

    detection_state_2.transition(b'')
    assert communication.written_data[3] == Isa.RV.get_isa_number().to_bytes(1, "little")

    # Check that after the final transition, the next state has been set
    assert parent_state.current_state == detection_state_1
    assert detection_state_2.is_complete() == True