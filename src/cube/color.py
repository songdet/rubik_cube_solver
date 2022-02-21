from enum import Enum

class Color(Enum):
    RED = "red", "R", "R"
    YELLOW = "yellow", "Y", "D"
    ORANGE = "orange", "O", "L"
    WHITE = "white", "W", "U"
    GREEN = "green", "G", "F"
    BLUE = "blue", "B", "B"

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj
    
    def __init__(self, _: str, color_code: str, cube_code: str):
        self._color_code_ = color_code
        self._cube_code_ = cube_code
    
    def __str__(self) -> str:
        return self.value
    
    def get_color_code(self):
        return self._color_code_

    def get_cube_code(self):
        return self._cube_code_

COLOR_CODES = [color.get_color_code() for color in Color] 
CUBE_CODES = [color.get_cube_code() for color in Color]
COLOR_TO_CUBE_CODE = {color : color.get_cube_code() for color in Color}
COLOR_CODE_TO_COLOR = {color.get_color_code() : color for color in Color}