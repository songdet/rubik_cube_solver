from solver import Isa
from communication import Communication
from camera import Camera


class TransitionHandler:

    def __init__(self, communication: Communication, camera: Camera):
        self._communication = communication
        self._camera = camera

    def isa_transition(self, isa : Isa):
        self._communication.write(isa.get_isa_number().to_bytes(1, "little")) 

    def camera_transition(self, file_location):
        self._camera.take_photo(file_location)