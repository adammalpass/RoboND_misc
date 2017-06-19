from mpmath import *
from sympy import *

J2 = [0.35, 0, 0.75]
J3 = [0.35, 0, 2]
#J5 = [1.85, 0, 1.946]
J5 = [0.943866, 0, 3.3784]

L2_5_X = J5[0] - J2[0]
L2_5_Y = J5[1] - J2[1]
L2_5_Z = J5[2] - J2[2]
L2_5 = sqrt(L2_5_X**2 + L2_5_Y**2 + L2_5_Z**2)

L2_3 = 1.25

L3_5_X = 1.85 - 0.35
L3_5_Z = 1.9465 - 2
L3_5 = sqrt(L3_5_X**2 + L3_5_Z**2)

print("L2_5", L2_5)
print("L3_5", L3_5)

#D = cos(theta)
D = (L2_5**2 - L2_3**2 - L3_5**2) / -(2 * L2_3 * L3_5)
print("D", D)

q3_1 = pi / 2 - (atan2(sqrt(1-D**2), D) - atan2(L3_5_Z, L3_5_X))
q3_2 = pi / 2 - (atan2(-sqrt(1-D**2), D) - atan2(L3_5_Z, L3_5_X))
#q3_1 = atan2(sqrt(1-D**2), D)
#q3_2 = atan2(-sqrt(1-D**2), D) 
print("q3_1", q3_1.evalf())
print("q3_2", q3_2.evalf())