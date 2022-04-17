from numpy import isin
from rubik_machine_state import DetectionState, DetectionStartState
from rubik_machine_state import SolutionState, SolutionStartState
from solver.isa import Isa
from .state import State
from cube import Side
from cube import Cube

class RubikMachineState(State):

    def __init__(self, transition_handler):
        self._transition_handler = transition_handler
        self._current_state = self._construct_default_state(transition_handler)
        self._sides = {}
        self._solution = []
    
    def transition(self, data):
        if data == b'O\n':
            # Do transition if previous state was ok
            self._current_state.transition(data)
        elif data == b'R\n':
            # Reset state to default
            self._current_state = self._construct_default_state(self._transition_handler)
            self._sides = {}
            self._solution = []
            self._transition_handler.isa_transition(Isa.ST)
        elif data == b'S\n':
            if (isinstance(self._current_state, DetectionState)):
                # If we are in detection state, put DetectStartState as current state before stopping
                start_state = DetectionStartState(self, self._transition_handler, self._current_state)
                self._current_state = start_state
            if (isinstance(self._current_state, SolutionState)):
                # If we are in solution state, put SolutionStartState as current state before continuing
                start_state = SolutionStartState(self, self._transition_handler, self._current_state)
                self._current_state = start_state
            # Tell machine to go back to start state
            self._transition_handler.isa_transition(Isa.ST)
    
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
        detect_bottom = DetectionState(self, Side.BOTTOM, transition_handler, None, True)
        detect_top = DetectionState(self, Side.TOP, transition_handler, detect_bottom, False)
        detect_right = DetectionState(self, Side.RIGHT, transition_handler, detect_top, False)
        detect_back = DetectionState(self, Side.BACK, transition_handler, detect_right, False)
        detect_left = DetectionState(self, Side.LEFT, transition_handler, detect_back, False)
        detect_front = DetectionState(self, Side.FRONT, transition_handler, detect_left, False)
        detect_start = DetectionStartState(self, transition_handler, detect_front)
        return detect_start