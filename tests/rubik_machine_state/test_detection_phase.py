from rubik_machine_state.detection_state import DetectionState
from rubik_machine_state.non_isa import NonIsa
from rubik_machine_state.solution_state import SolutionState
from solver import Isa
from transition import TransitionHandler
from .fake_transition_handlers import *
from cube import Color, Side


def test_detection_state():

    # Setup detection
    parent_state = ParentState(None)
    communication = FakeCommunication()
    camera = FakeCamera()
    first_photo_detector = FakeColorDetector([Color.BLUE, Color.GREEN, Color.ORANGE, Color.ORANGE, Color.WHITE, Color.WHITE, Color.WHITE])
    second_photo_detector = FakeColorDetector([Color.ORANGE, Color.RED])
    solver = FakeSolver([Isa.HH, Isa.HV, Isa.RBC])
    transition_handler = TransitionHandler(communication, camera, first_photo_detector, second_photo_detector, solver)
    detection_state_1 = DetectionState(parent_state, Side.TOP, transition_handler, None, NonIsa.SOLVE)
    detection_state_2 = DetectionState(parent_state, Side.FRONT, transition_handler, detection_state_1, Isa.MV)

    # Test that detection_state_2 is correct
    assert detection_state_2.is_complete() == False

    detection_state_2.transition(b'')
    assert communication.written_data[0] == Isa.GR.get_isa_number().to_bytes(1, "little")

    detection_state_2.transition(b'')
    assert communication.written_data[1] == Isa.HH.get_isa_number().to_bytes(1, "little")

    detection_state_2.transition(b'')
    assert len(camera.taken_photos) == 1

    detection_state_2.transition(b'')
    assert communication.written_data[2] == Isa.HV.get_isa_number().to_bytes(1, "little")

    detection_state_2.transition(b'')
    assert len(camera.taken_photos) == 2
    assert parent_state.sides[Side.FRONT] == [Color.BLUE, Color.GREEN, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.RED, Color.WHITE, Color.WHITE, Color.WHITE]

    detection_state_2.transition(b'')
    assert communication.written_data[3] == Isa.MV.get_isa_number().to_bytes(1, "little")
    assert parent_state.current_state == detection_state_1
    assert detection_state_2.is_complete() == True

    # Test that detection_state_1 is correct
    assert detection_state_1.is_complete() == False

    detection_state_1.transition(b'')
    assert communication.written_data[4] == Isa.GR.get_isa_number().to_bytes(1, "little")

    detection_state_1.transition(b'')
    assert communication.written_data[5] == Isa.HH.get_isa_number().to_bytes(1, "little")

    detection_state_1.transition(b'')
    assert len(camera.taken_photos) == 3

    detection_state_1.transition(b'')
    assert communication.written_data[6] == Isa.HV.get_isa_number().to_bytes(1, "little")

    detection_state_1.transition(b'')
    assert len(camera.taken_photos) == 4
    assert parent_state.sides[Side.TOP] == [Color.BLUE, Color.GREEN, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.RED, Color.WHITE, Color.WHITE, Color.WHITE]

    detection_state_1.transition(b'')
    assert detection_state_1._next_state._solution_isa == [Isa.HH, Isa.HV, Isa.RBC, Isa.ST]
    assert detection_state_1.is_complete() == True