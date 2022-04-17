from color_detection.defaults import DEFAULT_CALIBRATION_BOUND
from color_detection.calibrate import get_color_bound
from pathlib import Path
from camera import Camera
from cube import Color
import os, sys


TMP_IMAGE_FILE = "/tmp/img_file.jpg"

def get_and_print_img_bound(camera, color):
    camera.take_photo(TMP_IMAGE_FILE)
    (boxed_color, color_bound) = get_color_bound(TMP_IMAGE_FILE, DEFAULT_CALIBRATION_BOUND)
    print("Boxed values: %s" % str(boxed_color))
    print("%s bound: %s" % (str(color).capitalize(), str(color_bound)))
    return color_bound

if __name__ == "__main__":
    try:

        # Create a temporary file that will be used to store images throughout the program
        Path(TMP_IMAGE_FILE).touch()
        is_error = False

        # Instantiate objects needed for calibrate
        camera = Camera("192.168.4.1", "80")

        # Print welcome message
        print("\n====================================================================================")
        print("This script helps you calibrate the color bounds so that the color detection is accurate.")
        print("====================================================================================\n")
        print()

        input("Orient GREEN side towards the camera and press enter")
        green_bound = get_and_print_img_bound(camera, Color.GREEN)

        input("Orient ORANGE side towards the camera and press enter")
        orange_bound = get_and_print_img_bound(camera, Color.ORANGE)

        input("Orient RED side towards the camera and press enter")
        red_bound = get_and_print_img_bound(camera, Color.RED)

        input("Orient BLUE side towards the camera and press enter")
        blue_bound = get_and_print_img_bound(camera, Color.BLUE)

        input("Orient WHITE side towards the camera and press enter")
        white_bound = get_and_print_img_bound(camera, Color.WHITE)

        input("Orient YELLOW side towards the camera and press enter")
        yellow_bound = get_and_print_img_bound(camera, Color.YELLOW)

        print("The following bounds should be used: ")
        print("GREEN: %s" % str(green_bound))
        print("ORANGE: %s" % str(orange_bound))
        print("RED: %s" % str(red_bound))
        print("BLUE: %s" % str(blue_bound))
        print("WHITE: %s" % str(white_bound))
        print("YELLOW: %s" % str(yellow_bound))

    except Exception as e:
        print("Error while executing: %s", str(e), file=sys.stderr)
        is_error = True
    finally:
        # Make sure the temporary file is removed before exiting
        os.remove(TMP_IMAGE_FILE)