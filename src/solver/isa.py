from enum import Enum

class Isa(Enum):
    ST = "ST", 0, "Start", "Retract all 4 arms to start position."
    GR = "GR", 1, "Grip", "Extend all 4 arms so that they grip the rubik cube."
    HH = "HH", 2, "Hold Horizontal", "The rubik cube is held by left and right gripper, while the top and bottom grippers are retracted."
    HV = "HV", 3, "Hold Vertical", "The rubik cube is held by top and bottom gripper, while the left and right gripeprs are retracted." 
    MV = "MV", 4, "Move Vertical", "Starting in ST position, retract left gripper, rotate it cw, extend it, then retract top and bottom gripper, then rotate left gripper ccw and right gripper cw." 
    MH = "MH", 5, "Move Horizontal", "Starting in ST position, retract top gripper, rotate it cw, extend it, then retract left and right gripper, then rotate top gripper ccw and right gripper cw."
    MHCCW = "MHCCW", 6, "Move Horizontal Counterclockwise", "Starting in ST position, retract top gripper, rotate it cw, extend it, then retract left and right gripper, then rotate top gripper ccw and right gripper cw."
    RLC = "RLC", 7, "Rotate Left Clockwise", "Starting in ST position, rotate left gripper clockwise, then reset to ST position."
    RLCCW = "RLCCW", 8, "Rotate Left Counterclockwise", "Starting in ST position, rotate left gripper counterclockwise, then reset to ST position."
    RRC = "RRC", 9, "Rotate Right Clockwise", "Starting in ST position, rotate right gripper clockwise, then reset to ST position."
    RRCCW = "RRCCW", 10, "Rotate Right Counterclockwise", "Starting in ST position, rotate right gripper counterclockwise, then reset to ST position."
    RBC = "RBC", 11, "Rotate Bottom Clockwise", "Starting in ST position, rotate bottom gripper clockwise, then reset to ST position."
    RBCCW = "RBCCW", 12, "Rotate Bottom Counterclockwise", "Starting in ST position, rotate bottom gripper counterclockwise, then reset to ST position."
    RTC = "RTC", 13, "Rotate Top Clockwise", "Starting in ST position, rotate top gripper clockwise, then reset to ST position."
    RTCCW = "RTCCW", 14, "Rotate Top Counterclockwise", "Starting in ST position, rotate top gripper counterclockwise, then reset to ST position."

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj
    
    def __init__(self, _: str, isa_number, short_description: str, long_description: str):
        self._isa_number = isa_number
        self._short_description_ = short_description
        self._long_description_ = long_description

    def __str__(self) -> str:
        return self.value

    def get_isa_number(self):
        return self._isa_number

    def get_short_description(self):
        return self._short_description_
    
    def get_long_description(self):
        return self._long_description_