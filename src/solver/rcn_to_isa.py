from solver.isa import Isa

SOLUTION_TO_ISA = {
    "R": [Isa.RLC],
    "U": [Isa.RTC],
    "L": [Isa.RRC],
    "D": [Isa.RBC],
    "R'": [Isa.RLCCW],
    "U'": [Isa.RTCCW],
    "L'": [Isa.RRCCW],
    "D'": [Isa.RBCCW],
    "R2": [Isa.RLC, Isa.RLC],
    "U2": [Isa.RTC, Isa.RTC],
    "L2": [Isa.RRC, Isa.RRC],
    "D2": [Isa.RBC, Isa.RBC]
}

def convert(solution: str):

    # Have one solution for the case where the cube is rotated and one not
    rotated_solution = solution.translate(str.maketrans("FLBR" , "RFLB"))

    # We now have two list of solutions for the case when cube is rotated and not rotated
    solution = solution.split()
    rotated_solution = rotated_solution.split()

    is_rotated = False
    isa_list = []
    for i in range(len(solution)):

        # Check first if we need to rotate the cube and correct for that
        cur_solution = rotated_solution[i] if is_rotated else solution[i]
        if 'F' in cur_solution or 'B' in cur_solution:
            isa_list.append(Isa.MHCCW) if is_rotated else isa_list.append(Isa.MH)
            is_rotated = not is_rotated
            cur_solution = rotated_solution[i] if is_rotated else solution[i]

        # Then use translation table to add item to isa list
        isa_list.extend(SOLUTION_TO_ISA[cur_solution])        

    return isa_list
