from transition import TransitionHandler
from rubik_machine_state import SolutionState
from .fake_transition_handlers import *
from cube import Color
from solver import Isa


def test_solution_state():

    # Set up detection fake objects
    communication = FakeCommunication()
    camera = FakeCamera()
    first_photo_detector = FakeColorDetector([Color.BLUE, Color.GREEN, Color.ORANGE, Color.ORANGE, Color.WHITE, Color.WHITE, Color.WHITE])
    second_photo_detector = FakeColorDetector([Color.ORANGE, Color.RED])
    solver = FakeSolver([Isa.HH, Isa.HV, Isa.RBC])
    transition_handler = TransitionHandler(communication, camera, first_photo_detector, second_photo_detector, solver)
    solution_isa = [Isa.MHCCW, Isa.RRC, Isa.RBC, Isa.RLC]
    solution_state = SolutionState(solution_isa, transition_handler)    

    # Check that transitions are correct
    assert solution_state.is_complete() == False 

    solution_state.transition(b'')
    assert communication.written_data[0] == Isa.MHCCW.get_isa_number().to_bytes(1, "little")

    solution_state.transition(b'')
    assert communication.written_data[1] == Isa.RRC.get_isa_number().to_bytes(1, "little")

    solution_state.transition(b'')
    assert communication.written_data[2] == Isa.RBC.get_isa_number().to_bytes(1, "little")

    solution_state.transition(b'')
    assert communication.written_data[3] == Isa.RLC.get_isa_number().to_bytes(1, "little")

    assert solution_state.is_complete() == True