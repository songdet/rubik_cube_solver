from .state import State
from solver import Isa

class SolutionStartState(State):

    def __init__(self, rubik_machine_state, transition_handler, next_state):
        self._rubik_machine_state = rubik_machine_state
        self._transition_handler = transition_handler
        self._next_state = next_state
        self._is_complete = False


    def transition(self, _):

        # Just return if we've already transitioned
        if self._is_complete:
            return

        # Tell the machine to put itself in grip configuration and continue
        self._transition_handler.isa_transition(Isa.GR)
        self._rubik_machine_state.set_current_state(self._next_state)

        # Make sure we don't transition again
        self._is_complete = True
    
    def is_complete(self):
        return self._is_complete