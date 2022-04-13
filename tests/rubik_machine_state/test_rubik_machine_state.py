from .fake_transition_handlers import *
from cube import Color, Side
from solver import Isa
from transition import TransitionHandler
from rubik_machine_state import RubikMachineState, SolutionState

def test_rubik_machine_state():

    # Set up test objects
    communication = FakeCommunication()
    camera = FakeCamera()
    first_photo_detector = FakeColorDetector([Color.BLUE, Color.GREEN, Color.ORANGE, Color.ORANGE, Color.WHITE, Color.WHITE, Color.WHITE])
    second_photo_detector = FakeColorDetector([Color.ORANGE, Color.RED])
    solver = FakeSolver([Isa.HH, Isa.HV, Isa.RBC])
    transition_handler = TransitionHandler(communication, camera, first_photo_detector, second_photo_detector, solver)
    machine_state = RubikMachineState(transition_handler) 

    # Front transition
    assert machine_state.is_complete() == False
    _test_transition(machine_state, communication, camera, Side.FRONT, 1) 
    machine_state.transition(b'O\n')
    assert communication.written_data[-1] == Isa.MH.get_isa_number().to_bytes(1, "little")

    # Left transition
    _test_transition(machine_state, communication, camera, Side.LEFT, 3) 
    machine_state.transition(b'S\n') # Test that stopping and starting works correctly
    assert communication.written_data[-1] == Isa.ST.get_isa_number().to_bytes(1, "little")
    machine_state.transition(b'O\n')
    assert communication.written_data[-1] == Isa.MH.get_isa_number().to_bytes(1, "little")

    # Back transition
    _test_transition(machine_state, communication, camera, Side.BACK, 5) 
    machine_state.transition(b'O\n')
    assert communication.written_data[-1] == Isa.MH.get_isa_number().to_bytes(1, "little")

    # Right transition
    _test_transition(machine_state, communication, camera, Side.RIGHT, 7) 
    machine_state.transition(b'O\n')
    assert communication.written_data[-1] == Isa.MH.get_isa_number().to_bytes(1, "little")
    machine_state.transition(b'O\n')
    assert communication.written_data[-1] == Isa.MV.get_isa_number().to_bytes(1, "little")

    # Top transition
    _test_transition(machine_state, communication, camera, Side.TOP, 9) 
    machine_state.transition(b'O\n')
    assert communication.written_data[-1] == Isa.MV.get_isa_number().to_bytes(1, "little")
    machine_state.transition(b'O\n')
    assert communication.written_data[-1] == Isa.MV.get_isa_number().to_bytes(1, "little")

    # Bottom transition
    _test_transition(machine_state, communication, camera, Side.BOTTOM, 11) 
    machine_state.transition(b'O\n')
    assert isinstance(machine_state._current_state, SolutionState)

    # Test solution state transition
    machine_state.transition(b'O\n')
    assert communication.written_data[-1] == Isa.HH.get_isa_number().to_bytes(1, "little")

    machine_state.transition(b'O\n')
    assert communication.written_data[-1] == Isa.HV.get_isa_number().to_bytes(1, "little")

    machine_state.transition(b'O\n')
    assert communication.written_data[-1] == Isa.RBC.get_isa_number().to_bytes(1, "little")

    machine_state.transition(b'O\n')
    assert communication.written_data[-1] == Isa.ST.get_isa_number().to_bytes(1, "little")
    assert machine_state.is_complete() == True

def _test_transition(machine_state, communication, camera, side, photo_count):

    machine_state.transition(b'O\n')
    assert communication.written_data[-1] == Isa.GR.get_isa_number().to_bytes(1, "little")

    machine_state.transition(b'O\n')
    assert communication.written_data[-1] == Isa.HH.get_isa_number().to_bytes(1, "little")

    machine_state.transition(b'O\n')
    assert len(camera.taken_photos) == photo_count

    machine_state.transition(b'O\n')
    assert communication.written_data[-1] == Isa.GR.get_isa_number().to_bytes(1, "little")

    machine_state.transition(b'O\n')
    assert communication.written_data[-1] == Isa.HV.get_isa_number().to_bytes(1, "little")

    machine_state.transition(b'O\n')
    assert len(camera.taken_photos) == (photo_count + 1)
    assert machine_state._sides[side] == [Color.BLUE, Color.GREEN, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.RED, Color.WHITE, Color.WHITE, Color.WHITE]
    
    machine_state.transition(b'O\n')
    assert communication.written_data[-1] == Isa.GR.get_isa_number().to_bytes(1, "little")