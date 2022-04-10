
# Informal state interface
class State:

    def transition(self, data):
        # Transition from current state to the next using data
        raise NotImplementedError("transition must be implemented by subclass")

    def is_complete(self):
        # Whether we've transitioned to the final state
        raise NotImplementedError("is_complete must be implemented by subclass")