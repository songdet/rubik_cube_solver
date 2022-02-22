from solver import Isa
from solver import rcn_to_isa

def test_simple_conversion():
    result = rcn_to_isa.convert("D R U' L2 U2")
    assert result == [Isa.RBC, Isa.RRC, Isa.RTCCW, Isa.RLC, Isa.RLC, Isa.RTC, Isa.RTC] 

def test_conversion_with_rotation():
    result = rcn_to_isa.convert("R F2 F' R' U U2 B2")
    assert result == [Isa.RRC, Isa.MVHCW, Isa.RLC, Isa.RLC, Isa.RLCCW, Isa.MVHCCW, Isa.RRCCW, Isa.RTC, Isa.RTC, Isa.RTC, Isa.MVHCW, Isa.RRC, Isa.RRC]

def test_complex_cube():
    result = rcn_to_isa.convert("R2 F2 B U B' L2 B' U2 L' B2")
    assert result == [Isa.RRC, Isa.RRC, Isa.MVHCW, Isa.RLC, Isa.RLC, Isa.RRC, Isa.RTC, Isa.RRCCW, 
                      Isa.MVHCCW, Isa.RLC, Isa.RLC, Isa.MVHCW, Isa.RRCCW, Isa.RTC, Isa.RTC, Isa.MVHCCW, 
                      Isa.RLCCW, Isa.MVHCW, Isa.RRC, Isa.RRC]