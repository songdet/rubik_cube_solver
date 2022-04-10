from solver import Isa
from .non_isa import NonIsa
from .state import State

DETECTION_PHASES = [Isa.ST, Isa.HH, NonIsa.PHOTO_1, Isa.HV, NonIsa.PHOTO_2]

class DetectionState(State):

    def __init__(self, rubik_machine_state, side, transition_handler, next_state, transition_value):
        self._rubik_machine_state = rubik_machine_state
        self._side = side
        self._transition_handler = transition_handler
        self._next_state = next_state
        self._detection_phases = DETECTION_PHASES.copy()
        self._detection_phases.append(transition_value)
        self._current_phase_index = 0

    def transition(self, _):
        
        # Get current phase and call transition handler to do the necessary transiton
        current_phase = self._detection_phases[self._current_phase_index]
        if isinstance(current_phase, Isa):
            self._transition_handler.isa_transition(current_phase)
        elif isinstance(current_phase, NonIsa):
            if current_phase == NonIsa.PHOTO_1:
                self._first_photo_result = self._transition_handler.camera_transition_first_photo()
            elif current_phase == NonIsa.PHOTO_2:
                self._second_photo_result = self._transition_handler.camera_transition_second_photo()
                self._rubik_machine_state.set_side(self._side, self._combine_photo_results())
            elif current_phase == NonIsa.SOLVE:
                cube = self._rubik_machine_state.get_cube()
                solution = self._transition_handler.solve_transition(cube)
                self._rubik_machine_state.set_solution(solution)

        # Set new state in parent if we are end of detection phase
        self._current_phase_index += 1
        if self._current_phase_index == len(self._detection_phases):
            self._rubik_machine_state.set_current_state(self._next_state)
    
    def is_complete(self):
        return self._current_phase_index >= len(self._detection_phases)
    
    def _combine_photo_results(self):
        all_results = self._first_photo_result.copy()
        all_results.insert(3, self._second_photo_result[0])
        all_results.insert(5, self._second_photo_result[1])
        return all_results