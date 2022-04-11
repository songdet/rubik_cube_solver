from PIL import Image
from colorthief import ColorThief
from math import sqrt
from tempfile import NamedTemporaryFile
from color_detection.defaults import DEFAULT_COLOR_BOUNDS

def detect(img_file, img_bounds, color_bounds=DEFAULT_COLOR_BOUNDS):
    color_detector = ColorDetector(img_bounds, color_bounds)
    return color_detector.detect(img_file)


class ColorDetector:

    def __init__(self, img_bounds, color_bounds=DEFAULT_COLOR_BOUNDS):
        self._img_bounds = img_bounds
        self._color_bounds = color_bounds
    
    def detect(self, img_file):
        detected_colors = []
        img_file = Image.open(img_file)
        for bound in self._img_bounds:
            cur_img = img_file.crop(bound)
            with NamedTemporaryFile(mode="r+", suffix=".jpeg") as cropped_img:
                cur_img.save(cropped_img.name)
                color_thief = ColorThief(cropped_img.name)
                dominant_color = color_thief.get_palette(3, 1)[0]
                closest_color = self._get_closest_color(dominant_color, self._color_bounds)
                detected_colors.append(closest_color)
        return detected_colors

    def _get_closest_color(self, dominant_color, color_bounds):
        distances = {color: self._euclidean_distance(dominant_color, threshold) for (color,threshold) in color_bounds.items()}
        closest_colors = sorted(distances.items(), key=lambda x: x[1])
        return closest_colors[0][0]

    def _euclidean_distance(self, a,b):
        return sqrt(sum([(cur_elem[0]-cur_elem[1])**2 for cur_elem in zip(a,b)]))