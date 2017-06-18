from mpmath import *
from sympy import *

alpha0, alpha1, alpha2, alpha3, alpha4, alpha5, alpha6 = symbols('alpha0:7') # twist angles
a0, a1, a2, a3, a4, a5, a6 = symbols('a0:7') # link lengths
d1, d2, d3, d4, d5, d6, d7 = symbols('d1:8') # link offsets


# Joint angle symbols
q1, q2, q3, q4, q5, q6, q7 = symbols('q1:8')  # 'theta' joint angles


# Modified DH params
#q2 = q2 - pi / 2.
#q7 = 0


# Define Modified DH Transformation matrix
s = {alpha0: 0,     a0:   0,    d1: 0.75, 
     alpha1: -pi/2, a1: 0.35,   d2: 0,       q2: q2 - pi/2,  
     alpha2: 0,     a2: 1.25,   d3: 0,
     alpha3: -pi/2, a3: -0.054, d4: 1.5,
     alpha4: pi/2,  a4: 0,      d5: 0,
     alpha5: -pi/2, a5: 0,      d6: 0,
     alpha6: 0,     a6: 0,      d7: 0.303,   q7: 0}



# Create individual transformation matrices
T0_1 = Matrix([[             cos(q1),            -sin(q1),            0,              a0],
   [ sin(q1)*cos(alpha0), cos(q1)*cos(alpha0), -sin(alpha0), -sin(alpha0)*d1],
   [ sin(q1)*sin(alpha0), cos(q1)*sin(alpha0),  cos(alpha0),  cos(alpha0)*d1],
   [                   0,                   0,            0,               1]])

T0_1 = T0_1.subs(s)

T1_2 = Matrix([[             cos(q2),            -sin(q2),            0,              a1],
   [ sin(q2)*cos(alpha1), cos(q2)*cos(alpha1), -sin(alpha1), -sin(alpha1)*d2],
   [ sin(q2)*sin(alpha1), cos(q2)*sin(alpha1),  cos(alpha1),  cos(alpha1)*d2],
   [                   0,                   0,            0,               1]])

T1_2 = T1_2.subs(s)

T2_3 = Matrix([[             cos(q3),            -sin(q3),            0,              a2],
   [ sin(q3)*cos(alpha2), cos(q3)*cos(alpha2), -sin(alpha2), -sin(alpha2)*d3],
   [ sin(q3)*sin(alpha2), cos(q3)*sin(alpha2),  cos(alpha2),  cos(alpha2)*d3],
   [                   0,                   0,            0,               1]])

T2_3 = T2_3.subs(s)

T3_4 = Matrix([[             cos(q4),            -sin(q4),            0,              a3],
   [ sin(q4)*cos(alpha3), cos(q4)*cos(alpha3), -sin(alpha3), -sin(alpha3)*d4],
   [ sin(q4)*sin(alpha3), cos(q4)*sin(alpha3),  cos(alpha3),  cos(alpha3)*d4],
   [                   0,                   0,            0,               1]])

T3_4 = T3_4.subs(s)

T4_5 = Matrix([[             cos(q5),            -sin(q5),            0,              a4],
   [ sin(q5)*cos(alpha4), cos(q5)*cos(alpha4), -sin(alpha4), -sin(alpha4)*d5],
   [ sin(q5)*sin(alpha4), cos(q5)*sin(alpha4),  cos(alpha4),  cos(alpha4)*d5],
   [                   0,                   0,            0,               1]])

T4_5 = T4_5.subs(s)

T5_6 = Matrix([[             cos(q6),            -sin(q6),            0,              a5],
   [ sin(q6)*cos(alpha5), cos(q6)*cos(alpha5), -sin(alpha5), -sin(alpha5)*d6],
   [ sin(q6)*sin(alpha5), cos(q6)*sin(alpha5),  cos(alpha5),  cos(alpha5)*d6],
   [                   0,                   0,            0,               1]])

T5_6 = T5_6.subs(s)

T6_7 = Matrix([[             cos(q7),            -sin(q7),            0,              a6],
   [ sin(q7)*cos(alpha6), cos(q7)*cos(alpha6), -sin(alpha6), -sin(alpha6)*d7],
   [ sin(q7)*sin(alpha6), cos(q7)*sin(alpha6),  cos(alpha6),  cos(alpha6)*d7],
   [                   0,                   0,            0,               1]])

T6_7 = T6_7.subs(s)



# Transform from base link to end effector
T0_7 = simplify(T0_1 * T1_2 * T2_3 * T3_4 * T4_5 * T5_6 * T6_7)


#Correction for orientation difference between defintion of gripper link URDF v DH

#first rotate around z-axis by pi
R_z = Matrix([[             cos(pi),            -sin(pi),            0,              0],
   [                        sin(pi),            cos(pi),             0,              0],
   [                        0,                  0,                   1,              0],
   [                        0,                  0,                   0,              1]])

#then rotate around y-axis by -pi/2
R_y = Matrix([[             cos(-pi/2),         0,                   sin(-pi/2),     0],
   [                        0,                  1,                   0,              0],
   [                        -sin(-pi/2),        0,                   cos(-pi/2),     0],
   [                        0,                  0,                   0,              1]])

#calculate total correction factor
R_corr = simplify(R_z * R_y)

#calculate corrected transform from base to end effector
T_total = simplify(T0_7 * R_corr)


# print("Print T0_1")
# print(T0_1.evalf(subs={q1: 0, q2: 0, q3: 0, q4: 0, q5: 0, q6:0, q7:0}))
# print("Print T1_2")
# print(T1_2.evalf(subs={q1: 0, q2: 0, q3: 0, q4: 0, q5: 0, q6:0, q7:0}))
# print("Print T2_3")
# print(T2_3.evalf(subs={q1: 0, q2: 0, q3: 0, q4: 0, q5: 0, q6:0, q7:0}))
# print("Print T3_4")
# print(T3_4.evalf(subs={q1: 0, q2: 0, q3: 0, q4: 0, q5: 0, q6:0, q7:0}))
# print("Print T4_5")
# print(T4_5.evalf(subs={q1: 0, q2: 0, q3: 0, q4: 0, q5: 0, q6:0, q7:0}))
# print("Print T5_6")
# print(T5_6.evalf(subs={q1: 0, q2: 0, q3: 0, q4: 0, q5: 0, q6:0, q7:0}))
# print("Print T6_7")
# print(T6_7.evalf(subs={q1: 0, q2: 0, q3: 0, q4: 0, q5: 0, q6:0, q7:0}))

print("Print T_total")
print(T_total.evalf(subs={q1: 0, q2: 0, q3: 0, q4: 0, q5: 0, q6:0, q7:0}))

T0_2 = simplify(T0_1 * T1_2)
T0_5 = simplify(T0_1 * T1_2 * T2_3 * T3_4 * T4_5)

print("Print 0_2")
print(T0_2.evalf(subs={q1: 0, q2: 0, q3: 0, q4: 0, q5: 0, q6:0, q7:0}))

print("Print 0_5")
print(T0_5.evalf(subs={q1: 0, q2: 0, q3: 0, q4: 0, q5: 0, q6:0, q7:0}))

#print("Print T_total")
#print(T_total.e3valf(subs={q1: 1.44, q2: 0.4, q3: -2.88, q4: 4.3, q5: 1.70, q6:2.25, q7:0}))


#P_EE = Matrix([[2.153],[0],[1.946]])
P_EE = Matrix([[-0.18685],[2.1447],[1.9465]])

P_WC = simplify(P_EE - 0.303 * T0_7[0:3, 0:3] * Matrix([[0],[0],[1]]))

#print("Print P_WC")
#print (P_WC)
#P_WC_num = P_WC.evalf(subs={q1: 0, q2: 0, q3: 0, q4: 0, q5: 0, q6:0, q7:0})
#P_WC_num = P_WC.evalf(subs={q4: 0, q5: 0, q6:0, q7:0})
#print(P_WC_num)

XC = 1.85
YC = 0
ZC = 1.946

q1 = atan2(YC, XC)
#print ("Q1: ", q1)