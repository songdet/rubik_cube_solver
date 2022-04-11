from color_detection import detect
from cube import Color

COLOR_BOUNDS = {
    Color.BLUE: (20, 105, 190),
    Color.GREEN: (70, 175, 100),
    Color.ORANGE: (220, 105, 90),
    Color.RED: (120, 30, 30),
    Color.WHITE: (175, 180, 200),
    Color.YELLOW: (170, 200, 120)
}

def test_green_detect():
    bounds = [(1105, 1170, 1310, 1385),
              (1375, 1170, 1585, 1385),
              (1645, 1170, 1855, 1385),
              (1105, 1450, 1310, 1655),
              (1375, 1450, 1585, 1655),
              (1645, 1450, 1855, 1655),
              (1105, 1715, 1310, 1920),
              (1375, 1715, 1585, 1920),
              (1645, 1715, 1855, 1920)]
    result = detect("tests/color_detection/cube_green.jpg", bounds, COLOR_BOUNDS)
    assert result == [Color.GREEN, Color.GREEN, Color.GREEN, 
                      Color.GREEN, Color.GREEN, Color.GREEN,
                      Color.GREEN, Color.GREEN, Color.GREEN]

def test_orange_detect():
    bounds = [(1090, 1070, 1295, 1290),
              (1350, 1070, 1565, 1290),
              (1630, 1070, 1840, 1290),
              (1090, 1350, 1295, 1570),
              (1350, 1350, 1565, 1570),
              (1630, 1350, 1840, 1570),
              (1090, 1630, 1295, 1835),
              (1350, 1630, 1565, 1835),
              (1630, 1630, 1840, 1835)]
    result = detect("tests/color_detection/cube_orange.jpg", bounds, COLOR_BOUNDS)
    assert result == [Color.ORANGE, Color.ORANGE, Color.ORANGE, 
                      Color.ORANGE, Color.ORANGE, Color.ORANGE,
                      Color.ORANGE, Color.ORANGE, Color.ORANGE]

def test_blue_detect():
    bounds = [(1090, 1025, 1300, 1240),
              (1365, 1025, 1575, 1240),
              (1640, 1025, 1850, 1240),
              (1095, 1310, 1305, 1520),
              (1370, 1310, 1575, 1520),
              (1640, 1310, 1845, 1520),
              (1105, 1585, 1310, 1785),
              (1375, 1585, 1575, 1785),
              (1640, 1585, 1840, 1785)]
    result = detect("tests/color_detection/cube_blue.jpg", bounds, COLOR_BOUNDS)
    assert result == [Color.BLUE, Color.BLUE, Color.BLUE, 
                      Color.BLUE, Color.BLUE, Color.BLUE,
                      Color.BLUE, Color.BLUE, Color.BLUE]

def test_white_detect():
    bounds = [(1080, 890, 1295, 1110),
              (1355, 890, 1570, 1110),
              (1630, 890, 1845, 1110),
              (1080, 1175,1295, 1390),
              (1355, 1175, 1570, 1390),
              (1630, 1175, 1845, 1390),
              (1080, 1450, 1295, 1660),
              (1355, 1450, 1570, 1660),
              (1630, 1450, 1845, 1660)]
    result = detect("tests/color_detection/cube_white.jpg", bounds, COLOR_BOUNDS)
    assert result == [Color.WHITE, Color.WHITE, Color.WHITE, 
                      Color.WHITE, Color.WHITE, Color.WHITE,
                      Color.WHITE, Color.WHITE, Color.WHITE]