from .state import State

class RubikMachineState(State):

    def __init__(self, transition_handlers):
        self._transition_handlers = transition_handlers
    
    def set_current_state(self, state):
        self._current_state = state
