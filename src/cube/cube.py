from curses.ascii import SI
from enum import Enum, auto
from color import Color, COLOR_CODES, COLOR_TO_CUBE_CODE

class Side(Enum):
    FRONT = auto()
    BACK = auto()
    LEFT = auto()
    RIGHT = auto()
    TOP = auto()
    BOTTOM = auto()

class Cube:
    def __init__(self, front, back, left, right, top, bottom):
        self.front = self.__validate(front)
        self.back = self.__validate(back)
        self.left = self.__validate(left)
        self.right = self.__validate(right)
        self.top = self.__validate(top)
        self.bottom = self.__validate(bottom)

    def __getitem__(self, side: Side):
        if isinstance(side, Side):
            raise TypeError("side must be Side enum")

        if side == Side.FRONT:
            return self.front
        if side == Side.BACK:
            return self.back
        if side == Side.LEFT:
            return self.left
        if side == Side.RIGHT:
            return self.right
        if side == Side.TOP:
            return self.top
        if side == Side.BOTTOM:
            return self.bottom


    def get_cube_code(self):
        return self.__to_cube_code(self.top) \
             + self.__to_cube_code(self.right) \
             + self.__to_cube_code(self.front) \
             + self.__to_cube_code(self.bottom) \
             + self.__to_cube_code(self.left) \
             + self.__to_cube_code(self.back)

    def __to_cube_code(self, colors):
        converted = [COLOR_TO_CUBE_CODE[cur_color] for cur_color in colors]
        return str.join(converted)

    def __validate(self, input):
        if len(input) != 9:
            raise TypeError("The vector %s needs to have 9 items" % input)

        if not all([isinstance(Color, cur_color) for cur_color in input]):
            raise TypeError("The vector %s must contain only Color" % input)

        return input