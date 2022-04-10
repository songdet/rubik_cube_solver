from .state import State
from cube import Side
from cube import Cube

def construct_default_state():
    pass

class RubikMachineState(State):

    def __init__(self, transition_handlers):
        self._transition_handlers = transition_handlers
        self._current_state = construct_default_state()
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
    
    def set_solution(self, solution):
        self._solution = solution

    def get_cube(self):
        return Cube(
            front=self._sides[Side.FRONT],
            back=self._sides[Side.BOTTOM],
            left=self._sides[Side.LEFT],
            right=self._sides[Side.RIGHT],
            top=self._sides[Side.TOP],
            bottom=self._sides[Side.BOTTOM]
        )

