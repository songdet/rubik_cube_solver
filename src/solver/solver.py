from cube import Cube
from solver import rcn_to_isa
import kociemba

def solve(cube: Cube):
    return Solver().solve(cube)
    
class Solver:
    def solve(self, cube: Cube):
        rcn_solution = kociemba.solve(cube.get_cube_code())
        return rcn_to_isa.convert(rcn_solution)
