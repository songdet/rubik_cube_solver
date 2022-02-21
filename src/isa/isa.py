from enum import Enum

class Isa(Enum):
    ST = "ST", "Start", "Extend all 4 grippers so that they grip the rubik cube."
    HH = "HH", "Hold Horizontal", "The rubik cube is held by left and right gripper, while the top and bottom grippers are retracted."
    HV = "HV", "Hold Vertical", "The rubik cube is held by top and bottom gripper, while the left and right gripeprs are retracted." 
    MVCW = "MVCW", "Move Vertical Clockwise", "Starting in HH position, rotate left gripper counterclockwise and right gripper clockwise, then reset to HH position."
    MVCCW = "MVCCW", "Move Vertical Counterclockwise", "Starting in HH position, rotate left gripper clockwise and right gripper counterclockwise, then reset to HH position."
    MVL = "MVL", "Move Horizontal Left", "Starting in HV position, rotate top gripper clockwise and bottom gripper counterclockwise, then reset to HV position."
    MVR = "MVR", "Move Horizontal Right", "Starting in HV position, rotate top gripper counterclockwise and bottom gripper clockwise, then reset to HV position."
    RLC = "RLC", "Rotate Left Clockwise", "Starting in ST position, rotate left gripper clockwise, then reset to ST position."
    RLCCW = "RLCCW", "Rotate Left Counterclockwise", "Starting in ST position, rotate left gripper counterclockwise, then reset to ST position."
    RBC = "RBC", "Rotate Bottom Clockwise", "Starting in ST position, rotate bottom gripper clockwise, then reset to ST position."
    RBCCW = "RBCCW", "Rotate Bottom Counterclockwise", "Starting in ST position, rotate bottom gripper counterclockwise, then reset to ST position."
    RTC = "RTC", "Rotate Top Clockwise", "Starting in ST position, rotate top gripper clockwise, then reset to ST position."
    RTCCW = "RTCCW", "Rotate Top Counterclockwise", "Starting in ST position, rotate top gripper counterclockwise, then reset to ST position."

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj
    
    def __init__(self, _: str, short_description: str, long_description: str):
        self._short_description_ = short_description
        self._long_description_ = long_description

    def __str__(self) -> str:
        return self.value

    def get_short_description(self):
        return self._short_description_
    
    def get_long_description(self):
        return self._long_description_