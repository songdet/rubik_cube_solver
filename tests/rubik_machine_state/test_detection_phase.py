from rubik_machine_state.detection_state import DetectionState
from solver import Isa
from transition import TransitionHandler
from .fake_transition_handlers import *
from cube import Color, Side


def test_detection_state():

    # Setup detection
    parent_state = ParentState(None)
    communication = FakeCommunication()
    camera = FakeCamera()
    photo_detector = FakeColorDetector([Color.BLUE, Color.GREEN, Color.ORANGE, Color.ORANGE, Color.WHITE, Color.WHITE, Color.WHITE, Color.ORANGE, Color.RED])
    solver = FakeSolver([Isa.HH, Isa.HV, Isa.RBC])
    transition_handler = TransitionHandler(communication, camera, photo_detector, solver)
    detection_state_1 = DetectionState(parent_state, Side.TOP, transition_handler, None, True)
    detection_state_2 = DetectionState(parent_state, Side.FRONT, transition_handler, detection_state_1, False)

    # Test that detection_state_2 is correct
    assert detection_state_2.is_complete() == False
    detection_state_2.transition(b'')
    assert len(camera.taken_photos) == 1
    assert parent_state.sides[Side.FRONT] == [Color.BLUE, Color.GREEN, Color.ORANGE, Color.ORANGE, Color.WHITE, Color.WHITE, Color.WHITE, Color.ORANGE, Color.RED]
    assert parent_state.current_state == detection_state_1
    assert detection_state_2.is_complete() == True

    # Test that detection_state_1 is correct
    assert detection_state_1.is_complete() == False
    detection_state_1.transition(b'')
    assert len(camera.taken_photos) == 2
    assert parent_state.sides[Side.TOP] == [Color.BLUE, Color.GREEN, Color.ORANGE, Color.ORANGE, Color.WHITE, Color.WHITE, Color.WHITE, Color.ORANGE, Color.RED]
    assert parent_state.current_state._solution_isa == [Isa.HH, Isa.HV, Isa.RBC, Isa.ST]
    assert detection_state_1.is_complete() == True