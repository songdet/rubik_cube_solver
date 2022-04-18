from rubik_machine_state.detection_end_state import DetectionEndState
from .fake_transition_handlers import *
from cube import Color, Side
from solver import Isa
from transition import TransitionHandler
from rubik_machine_state import RubikMachineState, SolutionStartState

def test_rubik_machine_state():

    # Set up test objects
    communication = FakeCommunication()
    camera = FakeCamera()
    photo_detector = FakeColorDetector([Color.BLUE, Color.GREEN, Color.ORANGE, Color.ORANGE, Color.WHITE, Color.WHITE, Color.WHITE, Color.ORANGE, Color.RED])
    solver = FakeSolver([Isa.HH, Isa.HV, Isa.RBC])
    output = FakeOutput()
    transition_handler = TransitionHandler(communication, camera, photo_detector, solver, output)
    machine_state = RubikMachineState(transition_handler) 

    # Start transition
    assert machine_state.is_complete() == False
    machine_state.transition(b'O\n')
    assert communication.written_data[-1] == Isa.DT.get_isa_number().to_bytes(1, "little")

    # Front transition
    assert machine_state.is_complete() == False
    _test_transition(machine_state, camera, Side.FRONT, 1) 

    # Left transition
    assert machine_state.is_complete() == False
    _test_transition(machine_state, camera, Side.LEFT, 2) 

    # Back transition
    assert machine_state.is_complete() == False
    _test_transition(machine_state, camera, Side.BACK, 3) 

    # Right transition
    assert machine_state.is_complete() == False
    _test_transition(machine_state, camera, Side.RIGHT, 4) 

    # Top transition
    assert machine_state.is_complete() == False
    _test_transition(machine_state, camera, Side.TOP, 5) 

    # Bottom transition
    assert machine_state.is_complete() == False
    _test_transition(machine_state, camera, Side.BOTTOM, 6) 
    assert isinstance(machine_state._current_state, DetectionEndState)

    # End transistion
    assert machine_state.is_complete() == False
    machine_state.transition(b'O\n')
    assert communication.written_data[-1] == Isa.ST.get_isa_number().to_bytes(1, "little")

    # Test solution state transition
    assert machine_state.is_complete() == False
    machine_state.transition(b'O\n')
    assert communication.written_data[-1] == Isa.GR.get_isa_number().to_bytes(1, "little")

    assert machine_state.is_complete() == False
    machine_state.transition(b'O\n')
    assert communication.written_data[-1] == Isa.HH.get_isa_number().to_bytes(1, "little")

    assert machine_state.is_complete() == False
    machine_state.transition(b'O\n')
    assert communication.written_data[-1] == Isa.HV.get_isa_number().to_bytes(1, "little")

    assert machine_state.is_complete() == False
    machine_state.transition(b'O\n')
    assert communication.written_data[-1] == Isa.RBC.get_isa_number().to_bytes(1, "little")

    assert machine_state.is_complete() == False
    machine_state.transition(b'O\n')
    assert communication.written_data[-1] == Isa.ST.get_isa_number().to_bytes(1, "little")
    assert machine_state.is_complete() == True

def _test_transition(machine_state, camera, side, photo_count):
    machine_state.transition(b'O\n')
    assert len(camera.taken_photos) == photo_count
    assert machine_state._sides[side] == [Color.BLUE, Color.GREEN, Color.ORANGE, Color.ORANGE, Color.WHITE, Color.WHITE, Color.WHITE, Color.ORANGE, Color.RED]