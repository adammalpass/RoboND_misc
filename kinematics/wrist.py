from mpmath import *
from sympy import *

roll = symbols("roll")
pitch = symbols("pitch")
yaw = symbols("yaw")

J5__0 = [1.85, 0, 1.946]

R_roll = Matrix([[ 1,              0,        0],
              [ 0,        cos(roll), -sin(roll)],
              [ 0,        sin(roll),  cos(roll)]])

R_pitch = Matrix([[ cos(pitch),        0,  sin(pitch)],
              [       0,        1,        0],
              [-sin(pitch),        0,  cos(pitch)]])

R_yaw = Matrix([[ cos(yaw), -sin(yaw),        0],
              [ sin(yaw),  cos(yaw),        0],
              [ 0,              0,        1]])

R0_6 = simplify(R_roll * R_pitch * R_yaw)

print("R0_6")
print(R0_6.evalf(subs={roll:0, yaw:0, pitch:0}))


P_EE = Matrix([[2.153],[0],[1.946]])
#P_EE = Matrix([[-0.18685],[2.1447],[1.9465]])

P_WC = simplify(P_EE - 0.303 * R0_6[0:3, 0:3] * Matrix([[0],[0],[1]]))
print("P_WC")
print(P_WC.evalf(subs={roll:0, yaw:0, pitch:0}))