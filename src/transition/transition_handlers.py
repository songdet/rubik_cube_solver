from solver import Isa
from communication import Communication
from camera import Camera
from color_detection import ColorDetector
from solver import Solver

_DEFAULT_PHOTO_LOCATION = "/tmp/saved_photo.jpg"

class TransitionHandler:

    def __init__(self, communication: Communication, camera: Camera, photo_detector: ColorDetector, solver: Solver):
        self._communication = communication
        self._camera = camera
        self._photo_detector = photo_detector
        self._solver = solver

    def isa_transition(self, isa : Isa):
        self._communication.write(isa.get_isa_number().to_bytes(1, "little")) 

    def camera_transition(self):
        self._camera.take_photo(_DEFAULT_PHOTO_LOCATION)
        return self._photo_detector.detect(_DEFAULT_PHOTO_LOCATION)
    
    def solve_transition(self, cube):
        return self._solver.solve(cube)