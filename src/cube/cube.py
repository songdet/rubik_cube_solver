from enum import Enum
from color import COLOR_CODES, COLOR_TO_CUBE

class Cube:
    def __init__(self, front, back, left, right, top, bottom):
        self.front = self.__convert_code(self.__validate(front))
        self.back = self.__convert_code(self.__validate(back))
        self.left = self.__convert_code(self.__validate(left))
        self.right = self.__convert_code(self.__validate(right))
        self.top = self.__convert_code(self.__validate(top))
        self.bottom = self.__convert_code(self.__validate(bottom))

    def __str__(self):
        return self.top + self.right + self.front + self.bottom + self.left + self.back

    def __convert_code(self, cstring):
        converted = [COLOR_TO_CUBE[cur_char] for cur_char in cstring]
        return str.join(converted)

    def __validate(self, cstring):
        if len(cstring) != 9:
            raise ValueError("The string %s does not have 9 characters" % cstring)

        if not all([cur_char in COLOR_CODES for cur_char in cstring]):
            raise ValueError("The string %s contain invalid code" % cstring)
        return cstring