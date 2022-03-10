from PIL import Image
from colorthief import ColorThief
from cube import Color
from math import sqrt
from tempfile import NamedTemporaryFile

DEFAULT_COLOR_BOUNDS = {
    Color.BLUE: (10, 95, 180),
    Color.GREEN: (5, 140, 30),
    Color.ORANGE: (225, 80, 60),
    Color.RED: (160, 45, 55),
    Color.WHITE: (145, 160, 175),
    Color.YELLOW: (130, 175, 35)
}

def detect(img_file, img_bounds, color_bounds=DEFAULT_COLOR_BOUNDS):
    detected_colors = []
    img_file = Image.open(img_file)
    for bound in img_bounds:
        cur_img = img_file.crop(bound)
        with NamedTemporaryFile(mode="r+", suffix=".jpeg") as cropped_img:
            cur_img.save(cropped_img.name)
            color_thief = ColorThief(cropped_img.name)
            dominant_color = color_thief.get_color(quality=1)
            closest_color = _get_closest_color(dominant_color, color_bounds)
            detected_colors.append(closest_color)
    return detected_colors

def _get_closest_color(dominant_color, color_bounds):
    distances = {color:_euclidean_distance(dominant_color, threshold) for (color,threshold) in color_bounds.items()}
    closest_colors = sorted(distances.items(), key=lambda x: x[1])
    return closest_colors[0][0]

def _euclidean_distance(a,b):
    return sqrt(sum([(cur_elem[0]-cur_elem[1])**2 for cur_elem in zip(a,b)]))