import pytest
from cube import Cube
from cube import Side
from cube import Color

def test_incomplete_cube():
    with pytest.raises(TypeError, match = r'needs to have 9 items'):
        Cube(front = [Color.RED] * 8,
             back =  [Color.BLUE] * 9,
             left = [Color.GREEN] * 9,
             right = [Color.WHITE] *9,
             top = [Color.YELLOW] * 9,
             bottom = [Color.ORANGE] * 9)
    with pytest.raises(TypeError, match = r'needs to have 9 items'):
        Cube(front = [Color.RED] * 8,
             back =  [Color.BLUE] * 9,
             left = [Color.GREEN] * 9,
             right = [Color.WHITE] *9,
             top = [Color.YELLOW] * 9,
             bottom = [Color.ORANGE] * 9)

def test_invalid_type():
    with pytest.raises(TypeError, match = r'must contain either all Color or all strings'):
        Cube(front = ["test"] + ([Color.BLUE]*8),
             back =  [Color.BLUE] * 9,
             left = [Color.GREEN] * 9,
             right = [Color.WHITE] *9,
             top = [Color.YELLOW] * 9,
             bottom = [Color.ORANGE] * 9)

def test_invalid_color_code():
    with pytest.raises(TypeError, match = r'invalid color code'):
        Cube(front = "ABCDEFGHI",
             back =  [Color.BLUE] * 9,
             left = [Color.GREEN] * 9,
             right = [Color.WHITE] *9,
             top = [Color.YELLOW] * 9,
             bottom = [Color.ORANGE] * 9)

def test_get_side():
    cube = Cube(front = [Color.RED] * 9,
                back =  [Color.BLUE] * 9,
                left = [Color.GREEN] * 9,
                right = [Color.WHITE] *9,
                top = [Color.YELLOW] * 9,
                bottom = [Color.ORANGE] * 9)
    assert cube[Side.FRONT] == [Color.RED] * 9
    assert cube[Side.BACK] == [Color.BLUE] * 9
    assert cube[Side.LEFT] == [Color.GREEN] * 9
    assert cube[Side.RIGHT] == [Color.WHITE] * 9
    assert cube[Side.TOP] == [Color.YELLOW] * 9
    assert cube[Side.BOTTOM] == [Color.ORANGE] * 9

def test_different_colors():
    cube = Cube(front = "RRRWWWGGG",
                back =  [Color.BLUE] * 9,
                left = [Color.GREEN] * 9,
                right = [Color.WHITE] *9,
                top = [Color.YELLOW] * 9,
                bottom = [Color.ORANGE] * 9)
    assert cube[Side.FRONT] == ([Color.RED]*3 + [Color.WHITE]*3 + [Color.GREEN]*3)
    assert cube[Side.BACK] == [Color.BLUE] * 9
    assert cube[Side.LEFT] == [Color.GREEN] * 9
    assert cube[Side.RIGHT] == [Color.WHITE] * 9
    assert cube[Side.TOP] == [Color.YELLOW] * 9
    assert cube[Side.BOTTOM] == [Color.ORANGE] * 9

def test_get_cube_code():
    cube = Cube(front = "RYOWGBRYO",
                back =  "OYRBGWOYR",
                left = [Color.GREEN] * 9,
                right = [Color.WHITE] *9,
                top = [Color.YELLOW] * 9,
                bottom = [Color.ORANGE] * 9)
    assert cube.get_cube_code() == "DDDDDDDDDUUUUUUUUURDLUFBRDLLLLLLLLLLFFFFFFFFFLDRBFULDR"