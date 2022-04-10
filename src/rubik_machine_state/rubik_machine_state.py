from rubik_machine_state.detection_state import DetectionState
from rubik_machine_state.non_isa import NonIsa
from solver.isa import Isa
from .state import State
from cube import Side
from cube import Cube

class RubikMachineState(State):

    def __init__(self, transition_handler):
        self._current_state = self._construct_default_state(transition_handler)
        self._sides = {}
        self._solution = []
    
    def transition(self, data):
        self._current_state.transition(data)
    
    def is_complete(self):
        return self._current_state.is_complete()

    def set_side(self, side, side_values):
        self._sides[side] = side_values

    def set_current_state(self, state):
        self._current_state = state
    
    def get_cube(self):
        return Cube(
            front=self._sides[Side.FRONT],
            back=self._sides[Side.BOTTOM],
            left=self._sides[Side.LEFT],
            right=self._sides[Side.RIGHT],
            top=self._sides[Side.TOP],
            bottom=self._sides[Side.BOTTOM]
        )

    def _construct_default_state(self, transition_handler):
        detect_right = DetectionState(self, Side.RIGHT, transition_handler, None, NonIsa.SOLVE)
        detect_left = DetectionState(self, Side.LEFT, transition_handler, detect_right, [Isa.RT, Isa.RT])
        detect_bottom = DetectionState(self, Side.BOTTOM, transition_handler, detect_left, Isa.RT)
        detect_back = DetectionState(self, Side.BACK, transition_handler, detect_bottom, Isa.RV)
        detect_top = DetectionState(self, Side.TOP, transition_handler, detect_back, Isa.RV)
        detect_front = DetectionState(self, Side.FRONT, transition_handler, detect_top, Isa.RV)
        return detect_front