from .state import State
from .solution_state import SolutionState
from .solution_start_state import SolutionStartState

class DetectionState(State):

    def __init__(self, rubik_machine_state, side, transition_handler, next_state, is_last_state):
        self._rubik_machine_state = rubik_machine_state
        self._side = side
        self._transition_handler = transition_handler
        self._next_state = next_state
        self._is_last_state = is_last_state
        self._is_complete = False

    def transition(self, _):
        
        # Just return if we've already done transiton
        if self._is_complete:
            return
        
        # Take a photo of result and set detection to parent
        detected_colors = self._transition_handler.camera_transition()
        self._rubik_machine_state.set_side(self._side, detected_colors)

        # If this is the last detection state, we already have everything to solve cube, so solve it
        if (self._is_last_state):
            cube = self._rubik_machine_state.get_cube()
            solution = self._transition_handler.solve_transition(cube)
            solution_state = SolutionState(solution, self._transition_handler)
            self._next_state = SolutionStartState(self._rubik_machine_state, self._transition_handler, solution_state)

        # Set rubik machine state to next avaiable state and mark complete
        self._rubik_machine_state.set_current_state(self._next_state)
        self._is_complete = True
 
    def is_complete(self):
        return self._is_complete 