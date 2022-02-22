from PIL import Image
from colorthief import ColorThief
from cube import Color
from math import sqrt
from tempfile import NamedTemporaryFile

COLOR_BOUNDS = {
    Color.BLUE: (20, 45, 70),
    Color.GREEN: (10, 75, 30),
    Color.ORANGE: (150, 50, 15),
    Color.RED: (100, 30, 10),
    Color.WHITE: (150, 140, 120),
    Color.YELLOW: (130, 130, 40)
}

def detect(img_file, bounds):
    detected_colors = []
    img_file = Image.open(img_file)
    for bound in bounds:
        cur_img = img_file.crop(bound)
        with NamedTemporaryFile(mode="r+", suffix=".jpeg") as cropped_img:
            cur_img.save(cropped_img.name)
            color_thief = ColorThief(cropped_img.name)
            dominant_color = color_thief.get_color(quality=1)
            closest_color = _get_closest_color(dominant_color)
            detected_colors.append(closest_color)
    return detected_colors

def _get_closest_color(dominant_color):
    distances = {color:_euclidean_distance(dominant_color, threshold) for (color,threshold) in COLOR_BOUNDS.items()}
    closest_colors = sorted(distances.items(), key=lambda x: x[1])
    return closest_colors[0][0]

def _euclidean_distance(a,b):
    return sqrt(sum([(cur_elem[0]-cur_elem[1])**2 for cur_elem in zip(a,b)]))