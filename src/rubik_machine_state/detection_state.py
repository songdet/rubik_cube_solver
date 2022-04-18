from .state import State
from solver import Isa

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
        self._transition_handler.print("Waiting for camera photo.")
        detected_colors = self._transition_handler.camera_transition()
        self._rubik_machine_state.set_side(self._side, detected_colors)
        self._transition_handler.isa_transition(Isa.DT)

        # Report the detected colors 
        self._transition_handler.print("The following colors are detected: ")
        self._transition_handler.print("[%s %s %s]" % (detected_colors[0].get_color_code(), detected_colors[1].get_color_code(), detected_colors[2].get_color_code()))
        self._transition_handler.print("[%s %s %s]" % (detected_colors[3].get_color_code(), detected_colors[4].get_color_code(), detected_colors[5].get_color_code()))
        self._transition_handler.print("[%s %s %s]" % (detected_colors[6].get_color_code(), detected_colors[7].get_color_code(), detected_colors[8].get_color_code()))

        # Prompt user for change if necessary
        user_change = "Enter different colors if the detection is off. Otherwise press enter: "
        if user_change != '':
            self._rubik_machine_state.set_side(self._side, user_change)


        if (self._is_last_state):
            # If this is the last detection state, prompt user to remove cube while we transition to start position
            self._transition_handler.print("")
            self._transition_handler.print("====================================================================================")
            self._transition_handler.print("Please remove the cube and press start to compute solution.")
        else:
            # Otherwise, prompt for the next face to be shown towards the camera
            self._transition_handler.print("")
            self._transition_handler.print("====================================================================================")
            self._transition_handler.print("Please rotate the cube and put the {} side facing the camera".format(self._next_state._side.get_color()))

        # Set rubik machine state to next avaiable state and mark complete
        self._rubik_machine_state.set_current_state(self._next_state)
        self._is_complete = True
 
    def is_complete(self):
        return self._is_complete 
