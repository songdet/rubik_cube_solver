from .solution_state import SolutionState
from .solution_start_state import SolutionStartState
from .state import State
from solver import Isa

class DetectionEndState(State):

    def __init__(self, rubik_machine_state, transition_handler):
        self._rubik_machine_state = rubik_machine_state
        self._transition_handler = transition_handler
        self._is_complete = False


    def transition(self, _):

        # Just return if we've already transitioned
        if self._is_complete:
            return

        # Tell machine to reset to start position
        self._transition_handler.isa_transition(Isa.ST)

        # Generate solution
        cube = self._rubik_machine_state.get_cube()
        solution = self._transition_handler.solve_transition(cube)
        solution_state = SolutionState(solution, self._transition_handler)
        next_state = SolutionStartState(self._rubik_machine_state, self._transition_handler, solution_state)
        self._rubik_machine_state.set_current_state(next_state)

        # Report the solution found
        self._transition_handler.print("The following solution was found: {}".format(str(solution)))
        self._transition_handler.print("Please now insert the cube with green side facing the camera and white side facing the top.")

        # Make sure we don't transition again
        self._is_complete = True
    
    def is_complete(self):
        return self._is_complete