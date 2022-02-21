from solver import solve
from cube import Cube

print("====================================================================================")
print("Orient the cube with (middle) green side facing you and (middle) top side facing up")
print("The color codes are [red = R], [yellow = Y], [white = W], [orange = O], [blue = B], [green = G]")
print("====================================================================================\n")

front = input("Enter colors for front (green) side: ")
left = input("Enter colors for left (orange) side: ")
right = input("Enter colors for right (red) side: ")
back = input("Enter colors for back (blue) side: ")
top = input("Enter colors for top (white) side: ")
bottom = input("Enter colors for bottom (yellow) side: ") 

cube_repr = Cube(front = front, left = left, right = right, back = back, top = top, bottom = bottom)
solution = solve(cube_repr)

print("\n====================================================================================")
print("The following cube machine instructions will solve the cube: ")
for cur_solution in solution:
    print("%s : %s" % (cur_solution, cur_solution.get_short_description()))
print("====================================================================================\n")
