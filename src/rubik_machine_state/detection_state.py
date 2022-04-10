from solver import Isa
from .state import State

DETECTION_PHASES = [Isa.ST, Isa.HH, "photo1", Isa.HV, "photo2"]

class DetectionState(State):

    def __init__(self, rubik_machine_state, transition_handler, next_state, transition_isa, first_photo_location, second_photo_location):
        self._rubik_machine_state = rubik_machine_state
        self._transiton_handler = transition_handler
        self._next_state = next_state
        self._first_photo_location = first_photo_location
        self._second_photo_location = second_photo_location
        self._detection_phases = DETECTION_PHASES.copy()
        self._detection_phases.append(transition_isa)
        self._current_phase_index = 0
    
    def transition(self, _):
        
        # Get current phase and call transition handler to do the necessary transiton
        current_phase = self._detection_phases[self._current_phase_index]
        if isinstance(current_phase, Isa):
            self._transiton_handler.isa_transition(current_phase)
        elif isinstance(current_phase, str):
            if current_phase == "photo1":
                self._transiton_handler.camera_transition(self._first_photo_location)
            elif current_phase == "photo2":
                self._transiton_handler.camera_transition(self._second_photo_location)

        # Set new state in parent if we are end of detection phase
        self._current_phase_index += 1
        if self._current_phase_index == len(self._detection_phases):
            self._rubik_machine_state.set_current_state(self._next_state)
    
    def is_complete(self):
        return self._current_phase_index >= len(self._detection_phases)
