from color_detection.detect import DEFAULT_COLOR_BOUNDS
from camera import take_photo
from cube import Color, Cube
from solver import solve
from color_detection import get_color_bound, detect
from pathlib import Path
import sys, os

IMAGE_BOUND = [
    (675, 465, 730, 520),
    (755, 470, 810, 520),
    (835, 475, 890, 525),
    (675, 550, 725, 595),
    (755, 550, 805, 600),
    (835, 555, 890, 605),
    (675, 630, 725, 680),
    (750, 630, 805, 685),
    (835, 640, 895, 685)
]

TMP_IMAGE_FILE = "/tmp/img_file.jpg"

def calibrate(camera_ip):
    input("Orient GREEN side towards the camera and press enter")
    green_bound = get_and_print_img_bound(camera_ip, Color.GREEN)

    input("Orient ORANGE side towards the camera and press enter")
    orange_bound = get_and_print_img_bound(camera_ip, Color.ORANGE)

    input("Orient RED side towards the camera and press enter")
    red_bound = get_and_print_img_bound(camera_ip, Color.RED)

    input("Orient BLUE side towards the camera and press enter")
    blue_bound = get_and_print_img_bound(camera_ip, Color.BLUE)

    input("Orient WHITE side towards the camera and press enter")
    white_bound = get_and_print_img_bound(camera_ip, Color.WHITE)

    input("Orient YELLOW side towards the camera and press enter")
    yellow_bound = get_and_print_img_bound(camera_ip, Color.YELLOW)

    return {
        Color.GREEN: green_bound,
        Color.ORANGE: orange_bound,
        Color.RED: red_bound,
        Color.BLUE: blue_bound,
        Color.WHITE: white_bound,
        Color.YELLOW: yellow_bound
    }

def get_and_print_img_bound(camera_ip, color):
    take_photo(camera_ip, TMP_IMAGE_FILE)
    (boxed_color, color_bound) = get_color_bound(TMP_IMAGE_FILE, IMAGE_BOUND)
    print("Boxed values: %s" % str(boxed_color))
    print("%s bound: %s" % (str(color).capitalize(), str(color_bound)))
    return color_bound
    
def detect_cube_colors(camera_ip, color_bounds):

    input("Place the GREEN (front) side towards the camera and WHITE side (top) towards the top and press enter")
    front_side = detect_and_print_color(camera_ip, color_bounds)

    input("Rotate the cube counterclockwise so the ORANGE (left) side faces the camera and press enter")
    left_side = detect_and_print_color(camera_ip, color_bounds)

    input("Rotate the cube counterclockwise so the BLUE (back) side faces the camera and press enter")
    back_side = detect_and_print_color(camera_ip, color_bounds)

    input("Rotate the cube counterclockwise so the RED (right) side faces the camera and press enter")
    right_side = detect_and_print_color(camera_ip, color_bounds)

    input("Rotate the cube counterclockwise one more time so we are back to green and rotate WHITE side (top) down and press enter")
    top_side = detect_and_print_color(camera_ip, color_bounds)

    input("Rotate the cube counterclockwise in vertical plane twice so the YELLOW side (bottom) faces camera and press enter")
    bottom_side = detect_and_print_color(camera_ip, color_bounds)

    return Cube(
        front = front_side,
        left = left_side,
        back = back_side,
        right = right_side,
        top = top_side,
        bottom = bottom_side
    )

def detect_and_print_color(camera_ip, color_bounds):
    take_photo(camera_ip, TMP_IMAGE_FILE)
    detected_colors = detect(TMP_IMAGE_FILE, IMAGE_BOUND, color_bounds) 
    print("[%s %s %s]" % (detected_colors[0].get_color_code(), detected_colors[1].get_color_code(), detected_colors[2].get_color_code()))
    print("[%s %s %s]" % (detected_colors[3].get_color_code(), detected_colors[4].get_color_code(), detected_colors[5].get_color_code()))
    print("[%s %s %s]" % (detected_colors[6].get_color_code(), detected_colors[7].get_color_code(), detected_colors[8].get_color_code()))
    return detected_colors

if __name__ == "__main__":
    try:
        # Create a temporary file that will be used to store images throughout the program
        Path(TMP_IMAGE_FILE).touch()

        # Print welcome message
        print("\n====================================================================================")
        print("This script takes you through the whole process of calibrating rubik cube color bounds, ")
        print("detecting rubik cube color, solving the rubik cube, and getting cube instruction set to")
        print("solve the rubik cube. Follow the instructions to solve the cube.")
        print("====================================================================================\n")
        print()

        # Get camera ip address
        #camera_ip = input("Please enter the ip address of the camera: ")
        camera_ip = "192.168.1.189"

        # Calibrate the cube colors
        print("====================================================================================")
        print("                                CALIBRATION PHASE                                   ")
        should_calibrate = input("Do you want to calibrate the cube colors? If not, defaults will be used ([y]/n): ")
        color_bounds = DEFAULT_COLOR_BOUNDS if should_calibrate == "n" else calibrate(camera_ip)
        print("The following bounds will be used: ")
        print("GREEN: %s" % str(color_bounds[Color.GREEN]))
        print("ORANGE: %s" % str(color_bounds[Color.ORANGE]))
        print("RED: %s" % str(color_bounds[Color.RED]))
        print("BLUE: %s" % str(color_bounds[Color.BLUE]))
        print("WHITE: %s" % str(color_bounds[Color.WHITE]))
        print("YELLOW: %s" % str(color_bounds[Color.YELLOW]))
        print("====================================================================================\n")

        # Detect cube colors
        print("====================================================================================")
        print("                                 DETECTION PHASE                                    ")
        print("Rotate the cube to random orientation. We will now attempt to solve the cube. Note that")
        print("a side is referred to by the color of the box in the middle of the cube.\n")
        cube_colors = detect_cube_colors(camera_ip, color_bounds)
        print("====================================================================================\n")

        # Cube solving phase
        print("====================================================================================")
        print("                                  SOLVING PHASE                                     ")
        print("The following cube machine instructions will solve the cube: ")
        solution = solve(cube_colors)
        for cur_solution in solution:
            print("%s : %s" % (cur_solution, cur_solution.get_short_description()))
        print("====================================================================================\n")

    except Exception as e:
        print("Error while executing: %s", str(e), file=sys.stderr)
        exit(1)

    # Make sure the temporary file is removed before exiting
    os.remove(TMP_IMAGE_FILE)