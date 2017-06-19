from mpmath import *
from sympy import *

J2 = [0.35, 0, 0.75]
J3__0 = [0.35, 0, 2]
J5__0 = [1.85, 0, 1.946]
#J5 = [2.239766, 0, 1.0804] #q1 = 0, q2 = 0.5, q3 = 0
#J5 = [-2.15925, 0, 1.87035] #q1 = 0, q2 = -1.1, q3 = -1.7
#J5 = [1.9556, 0, 0.7333] #q1 = 0, q2 = 0.5, q3 = 0.3
J5 = [0.9439, 0, 3.3785]   #q1 = 0, q2 = 0, q3 = -1.2

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
q3 = pi / 2 - (atan2(sqrt(1-D**2), D) - atan2(L3_5_Z__0, L3_5_X__0))
q3_2 = pi / 2 - (atan2(-sqrt(1-D**2), D) - atan2(L3_5_Z__0, L3_5_X__0))
#q3_1 = atan2(sqrt(1-D**2), D)
#q3_2 = atan2(-sqrt(1-D**2), D) 
print("q3", q3.evalf())
#print("q3_2", q3_2.evalf())


#q2 = atan2(L2_5_Z, L2_5_X) - atan2(L3_5__0 * sin(pi - q3_internal), L2_3__0 + L3_5__0 * cos(pi - q3_internal))
m1 = L3_5__0 * sin(q3_internal)
m2 = L2_3__0 - L3_5__0 * cos(q3_internal)
b2 = atan2(m1,m2)
b1 = atan2(J5[2]-J2[2], J5[0]-J2[0])
q2 = pi / 2 - b2 - b1

#print("m1", m1)
#print("m2",m2)
#print("b2",b2)
#print("b1",b1)
print("q2",q2.evalf())

#print("q2", q2.evalf())
#print(atan2(L3_5__0 * sin(pi - q3_internal), L2_3__0 + L3_5__0 * cos(pi - q3_internal)))