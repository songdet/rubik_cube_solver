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

def test_blue_detect():
    bounds = [(1100, 1450, 1340, 1695),
              (1420, 1450, 1655, 1695),
              (1730, 1450, 1970, 1695),
              (1100, 1765,1340, 1990),
              (1420, 1765, 1655, 1990),
              (1730, 1765, 1970, 1990),
              (1100, 2060, 1340, 2275),
              (1420, 2060, 1655, 2275),
              (1730, 2060, 1970, 2275)]
    result = detect("tests/color_detection/cube_blue.jpg", bounds)
    assert result == [Color.BLUE, Color.BLUE, Color.BLUE, 
                      Color.BLUE, Color.BLUE, Color.BLUE,
                      Color.BLUE, Color.BLUE, Color.BLUE]

def test_white_detect():
    bounds = [(985, 1375, 1230, 1630),
              (1310, 1375, 1555, 1630),
              (1635, 1375, 1880, 1630),
              (1000, 1705,1240, 1935),
              (1310, 1705, 1555, 1935),
              (1635, 1705, 1880, 1935),
              (1000, 2005, 1240, 2225),
              (1310, 2005, 1555, 2225),
              (1635, 2005, 1880, 2225)]
    result = detect("tests/color_detection/cube_white.jpg", bounds)
    assert result == [Color.WHITE, Color.WHITE, Color.WHITE, 
                      Color.WHITE, Color.WHITE, Color.WHITE,
                      Color.WHITE, Color.WHITE, Color.WHITE]

def test_yellow_detect():
    bounds = [(1005, 1315, 1245, 1565),
              (1325, 1315, 1565, 1565),
              (1640, 1315, 1885, 1565),
              (1025, 1635,1255, 1870),
              (1330, 1635, 1570, 1870),
              (1640, 1635, 1885, 1870),
              (1025, 1940, 1255, 2160),
              (1330, 1940, 1570, 2160),
              (1640, 1940, 1885, 2160)]
    result = detect("tests/color_detection/cube_yellow.jpg", bounds)
    assert result == [Color.YELLOW, Color.YELLOW, Color.YELLOW, 
                      Color.YELLOW, Color.YELLOW, Color.YELLOW,
                      Color.YELLOW, Color.YELLOW, Color.YELLOW]