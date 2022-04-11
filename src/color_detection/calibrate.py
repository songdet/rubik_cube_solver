from PIL import Image
from colorthief import ColorThief
from tempfile import NamedTemporaryFile
from statistics import median

def get_color_bound(img_file, img_bounds):
    dominant_colors = []
    img_file = Image.open(img_file)
    for bound in img_bounds:
        cur_img = img_file.crop(bound)
        with NamedTemporaryFile(mode="r+", suffix=".jpeg") as cropped_img:
            cur_img.save(cropped_img.name)
            color_thief = ColorThief(cropped_img.name)
            dominant_color = color_thief.get_palette(3,1)[0]
            dominant_colors.append(dominant_color)
    return (dominant_colors, _get_median_values(dominant_colors))

def _get_median_values(dominant_colors):
    r_val = [red for (red,_,_) in dominant_colors]
    g_val = [green for (_,green,_) in dominant_colors]
    b_val = [blue for (_,_,blue) in dominant_colors]
    median_values = (median(r_val), median(g_val), median(b_val))
    return median_values
