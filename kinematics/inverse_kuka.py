from mpmath import *
from sympy import *

J2 = [0.35, 0, 0.75]
J3__0 = [0.35, 0, 2]
J5__0 = [1.85, 0, 1.946]
J5 = J5__0#[0.9439, 0, 3.3785]

L2_5_X = J5[0] - J2[0]
L2_5_Y = J5[1] - J2[1]
L2_5_Z = J5[2] - J2[2]
L2_5 = sqrt(L2_5_X**2 + L2_5_Y**2 + L2_5_Z**2)

L2_3__0 = 1.25

L3_5_X__0 = J5__0[0] - J3__0[0]
L3_5_Z__0 = J5__0[2] - J3__0[2]
L3_5__0 = sqrt(L3_5_X__0**2 + L3_5_Z__0**2)

print("L2_5", L2_5)
print("L3_5", L3_5__0)

#D = cos(theta)
D = (L2_5**2 - L2_3__0**2 - L3_5__0**2) / -(2 * L2_3__0 * L3_5__0)
print("D", D)

q3_internal = atan2(sqrt(1-D**2), D)
q3_1 = pi / 2 - (atan2(sqrt(1-D**2), D) - atan2(L3_5_Z__0, L3_5_X__0))
q3_2 = pi / 2 - (atan2(-sqrt(1-D**2), D) - atan2(L3_5_Z__0, L3_5_X__0))
#q3_1 = atan2(sqrt(1-D**2), D)
#q3_2 = atan2(-sqrt(1-D**2), D) 
print("q3_1", q3_1.evalf())
print("q3_2", q3_2.evalf())


q2 = atan2(L2_5_Z, L2_5_X) - atan2(L3_5__0 * sin(pi - q3_internal), L2_3__0 + L3_5__0 * cos(pi - q3_internal))
print("q2", q2.evalf())
print(atan2(L3_5__0 * sin(pi - q3_internal), L2_3__0 + L3_5__0 * cos(pi - q3_internal)))