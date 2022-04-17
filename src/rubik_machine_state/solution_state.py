from solver.isa import Isa
from .state import State

class SolutionState(State):

    def __init__(self, solution_isa, transition_handler):
        self._solution_isa = solution_isa.copy()
        self._solution_isa.append(Isa.ST)
        self._transition_handler = transition_handler
        self._current_phase_index = 0
    
    def transition(self, _):

        # Don't transition if we are already done
        if self.is_complete():
            return

        # Select the next transition to do
        current_state = self._solution_isa[self._current_phase_index]
        self._transition_handler.isa_transition(current_state)
        self._current_phase_index += 1

        #Report the transition that was done
        self._transition_handler.print("Performing operation {}".format(current_state.get_short_description()))
    
    def is_complete(self):
        return self._current_phase_index >= len(self._solution_isa)
