from color_detection import detect
from cube import Color

def test_green_detect():
    bounds = [(1030, 1575, 1280, 1815),
              (1360, 1575, 1590,1815),
              (1660, 1575, 1900, 1815),
              (1030, 1880, 1280, 2115),
              (1360, 1880, 1590, 2115),
              (1660, 1880, 1900, 2115),
              (1060, 2180, 1290, 2400),
              (1360, 2180, 1590, 2400),
              (1660, 2180, 1900, 2400)]
    result = detect("tests/color_detection/cube_green.jpg", bounds)
    assert result == [Color.GREEN, Color.GREEN, Color.GREEN, 
                      Color.GREEN, Color.GREEN, Color.GREEN,
                      Color.GREEN, Color.GREEN, Color.GREEN]

def test_red_detect():
    bounds = [(980, 1520, 1220, 1755),
              (1290, 1520, 1530, 1755),
              (1605, 1520, 1840, 1755),
              (980, 1830, 1220, 2050),
              (1300, 1830, 1535, 2050),
              (1605, 1830, 1840, 2050),
              (980, 2120, 1220, 2340),
              (1300, 2120, 1535, 2340),
              (1605, 2120, 1840, 2340)]
    result = detect("tests/color_detection/cube_red.jpg", bounds)
    assert result == [Color.RED, Color.RED, Color.RED, 
                      Color.RED, Color.RED, Color.RED,
                      Color.RED, Color.RED, Color.RED]

def test_orange_detect():
    bounds = [(1055, 1430, 1290, 1665),
              (1360, 1430, 1590, 1665),
              (1660, 1430, 1890, 1665),
              (1065, 1735,1290, 1950),
              (1360, 1735, 1590, 1950),
              (1660, 1735, 1890, 1950),
              (1065, 2020, 1290, 2230),
              (1360, 2020, 1590, 2230),
              (1660, 2020, 1890, 2230)]
    result = detect("tests/color_detection/cube_orange.jpg", bounds)
    assert result == [Color.ORANGE, Color.ORANGE, Color.ORANGE, 
                      Color.ORANGE, Color.ORANGE, Color.ORANGE,
                      Color.ORANGE, Color.ORANGE, Color.ORANGE]