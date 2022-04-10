from communication import Communication
from transition import TransitionHandler
from rubik_machine_state import SolutionState
from solver import Isa

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

def test_solution_state():
    communication = FakeCommunication()
    camera = FakeCamera()
    transition_handler = TransitionHandler(communication, camera)
    solution_isa = [Isa.MVHCCW, Isa.MVVCW, Isa.RBC, Isa.RLC]
    solution_state = SolutionState(solution_isa, transition_handler)    
    assert solution_state.is_complete() == False 

    solution_state.transition(b'')
    assert communication.written_data[0] == Isa.MVHCCW.get_isa_number().to_bytes(1, "little")

    solution_state.transition(b'')
    assert communication.written_data[1] == Isa.MVVCW.get_isa_number().to_bytes(1, "little")

    solution_state.transition(b'')
    assert communication.written_data[2] == Isa.RBC.get_isa_number().to_bytes(1, "little")

    solution_state.transition(b'')
    assert communication.written_data[3] == Isa.RLC.get_isa_number().to_bytes(1, "little")

    assert solution_state.is_complete() == True