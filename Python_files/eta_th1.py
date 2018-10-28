#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 15:56:02 2018

@author: zhangcheng
"""
from math import cos, tan
from Trough import Trough
from Const import degtorad, convtemp
from Ambient import Ambient
from scipy.integrate import quad
from CoolProp.CoolProp import PropsSI
from MSHS import get_ratios
from scipy.optimize import fsolve


def M(receiver, alpha):
	f = receiver.f
	l = receiver.l
	return 1 - f * tan(alpha) / l

def K(alpha):
	K = cos(alpha) - 0.0003512 * alpha - 0.00003137 * alpha ** 2
	return K

def eta_th(receiver, Ambient, alpha, T):
	I = Ambient.I
	T_amb = Ambient.T
	tc_type = receiver.tc_type
	Delta_T = T - T_amb
	eta_th = K(alpha) * M(receiver, alpha)* (A[tc_type] + B[tc_type] * Delta_T) \
		+ C[tc_type] * Delta_T / I + D[tc_type] * Delta_T **2 \
		/ I
	return eta_th / 100

def cp(oil_type, T, P):
	return PropsSI('C', 'T', T, 'P', P, oil_type)

A = {}
A['cv'] = 73.3
A['ca'] = 73.4
A['cb'] = 74.7
A['bv'] = 73.6
A['ba'] = 73.8

B = {}
B['cv'] = -0.007276
B['ca'] = -0.004683
# B['cb'] = -0.042 - 0.00927 * amb.v_wind / M[rc, alpha]
B['cb'] = -0.042
B['bv'] = -0.004206
B['ba'] = -0.006460

C = {}
C['cv'] = -0.496
C['ca'] = -14.4
C['cb'] = 0
C['bv'] = 7.44
C['ba'] = -12.16

D = {}
D['cv'] = -0.0691
D['ca'] = -0.0637
D['cb'] = -0.000731
# D['cb'] = -0.000731 * amb.I
D['bv'] = -0.0958
D['ba'] = -0.0641

tc1 = Trough()
tc1.tc_type = 'cv'

amb1 = []

DNI_amb1 = [933.7, 968.2, 982.3, 909.5, 937.9, 880.6, 920.9, 903.2]
T_amb1 = [convtemp(21.2, 'C', 'K'),
	convtemp(22.4, 'C', 'K'),
	convtemp(24.3, 'C', 'K'),
	convtemp(26.2, 'C', 'K'),
	convtemp(28.8, 'C', 'K'),
	convtemp(27.5, 'C', 'K'),
	convtemp(29.5, 'C', 'K'),
	convtemp(31.1, 'C', 'K')]
v_wind1 = [2.6, 3.7, 2.5, 3.3, 1, 2.9, 2.6, 4.2]

alpha1 = degtorad(0)

T1 = [convtemp(102.2, 'C', 'K'),
	convtemp(151, 'C', 'K'),
	convtemp(197.5, 'C', 'K'),
	convtemp(250.7, 'C', 'K'),
	convtemp(297.8, 'C', 'K'),
	convtemp(299, 'C', 'K'),
	convtemp(379.5, 'C', 'K'),
	convtemp(355.9, 'C', 'K')]

eta1 = [''] * len(DNI_amb1)
for i in range(len(DNI_amb1)):
	amb1.append(Ambient())
	amb1[i].I = DNI_amb1[i]
	amb1[i].T = T_amb1[i]
	amb1[i].v_wind = v_wind1[i]
	eta1[i] = eta_th(tc1, amb1[i], alpha1, T1[i])
	print('%.4f' %eta1[i])
print('')

tc2 = Trough()
tc2.tc_type = 'ca'

amb2 = []

DNI_amb2 = [889.7, 874.1, 870.4, 813.1, 858.4, 878.7, 896.4, 906.7, 879.5, 898.6]
T_amb2 = [convtemp(28.6, 'C', 'K'),
	convtemp(28.7, 'C', 'K'),
	convtemp(29.1, 'C', 'K'),
	convtemp(25.8, 'C', 'K'),
	convtemp(27.6, 'C', 'K'),
	convtemp(28.6, 'C', 'K'),
	convtemp(30, 'C', 'K'),
	convtemp(31.7, 'C', 'K'),
	convtemp(27.4, 'C', 'K'),
	convtemp(29.7, 'C', 'K')]
v_wind2 = [2.8, 4, 0.6, 3.6, 3.1, 3.1, 0.9, 0, 1.8, 2.8]

alpha2 = degtorad(0)

T2 = [convtemp(251.1, 'C', 'K'),
	convtemp(344.9, 'C', 'K'),
	convtemp(345.5, 'C', 'K'),
	convtemp(101.2, 'C', 'K'),
	convtemp(154.3, 'C', 'K'),
	convtemp(202.4, 'C', 'K'),
	convtemp(250.7, 'C', 'K'),
	convtemp(299.5, 'C', 'K'),
	convtemp(348.9, 'C', 'K'),
	convtemp(376.6, 'C', 'K')]

eta2 = [''] * len(DNI_amb2)
for i in range(len(DNI_amb2)):
	amb2.append(Ambient())
	amb2[i].I = DNI_amb2[i]
	amb2[i].T = T_amb2[i]
	amb2[i].v_wind = v_wind2[i]
	eta2[i] = eta_th(tc2, amb2[i], alpha2, T2[i])
	print('%.4f' %eta2[i])
print('')


tc3 = Trough()
tc3.tc_type = 'bv'

amb3 = []

DNI_amb3 = [839.8, 882.7, 921.5, 902, 900.7, 871.8, 884.6, 744.6, 928.4]
T_amb3 = [convtemp(3.6, 'C', 'K'),
	convtemp(-3.1, 'C', 'K'),
	convtemp(-0.7, 'C', 'K'),
	convtemp(6.4, 'C', 'K'),
	convtemp(0.2, 'C', 'K'),
	convtemp(1.6, 'C', 'K'),
	convtemp(2.6, 'C', 'K'),
	convtemp(-5, 'C', 'K'),
	convtemp(-0.9, 'C', 'K'),
	]
v_wind3 = [1.1, 2.1, 0, 0, 1.3, 4, 3, 1.1, 2.4]

alpha3 = degtorad(0)

T3 = [convtemp(103.4, 'C', 'K'),
	convtemp(253.3, 'C', 'K'),
	convtemp(349.6, 'C', 'K'),
	convtemp(154, 'C', 'K'),
	convtemp(201.6, 'C', 'K'),
	convtemp(201.5, 'C', 'K'),
	convtemp(303.1, 'C', 'K'),
	convtemp(100.8, 'C', 'K'),
	convtemp(379.6, 'C', 'K'),
	]

eta3 = [''] * len(DNI_amb3)
for i in range(len(DNI_amb3)):
	amb3.append(Ambient())
	amb3[i].I = DNI_amb3[i]
	amb3[i].T = T_amb3[i]
	amb3[i].v_wind = v_wind3[i]
	eta3[i] = eta_th(tc3, amb3[i], alpha3, T3[i])
	print('%.4f' %eta3[i])
print('')

tc4 = Trough()
tc4.tc_type = 'ba'

amb4 = []

DNI_amb4 = [919.5, 755, 850.9, 899.7, 909.6, 908.1, 902.6]
T_amb4 = [convtemp(0.1, 'C', 'K'),
	convtemp(-1, 'C', 'K'),
	convtemp(-0.6, 'C', 'K'),
	convtemp(0.5, 'C', 'K'),
	convtemp(1.3, 'C', 'K'),
	convtemp(5.9, 'C', 'K'),
	convtemp(5.1, 'C', 'K'),
	]
v_wind4 = [1.4, 5.5, 4.7, 4.4, 1.2, 5.9, 1.7]

alpha4 = degtorad(0)

T4 = [convtemp(379.7, 'C', 'K'),
	convtemp(101.9, 'C', 'K'),
	convtemp(203.2, 'C', 'K'),
	convtemp(301.6, 'C', 'K'),
	convtemp(251.8, 'C', 'K'),
	convtemp(350.2, 'C', 'K'),
	convtemp(154.2, 'C', 'K'),
	]

eta4 = [''] * len(DNI_amb4)
for i in range(len(DNI_amb4)):
	amb4.append(Ambient())
	amb4[i].I = DNI_amb4[i]
	amb4[i].T = T_amb4[i]
	amb4[i].v_wind = v_wind4[i]
	eta4[i] = eta_th(tc4, amb4[i], alpha4, T4[i])
	print('%.4f' %eta4[i])
print('')

m_dot = 396.4

amb = Ambient()
amb.I = 774
amb.T = convtemp(25, 'C', 'K')
amb.v_wind = 1

tc = Trough()
tc.tc_type = 'bv'

alpha = 0

T_i = convtemp(297.78, 'C', 'K')
T_o = convtemp(390.58, 'C', 'K')

oil_type = 'INCOMP::TVP1'
P = 2e6

L = quad(lambda T:cp(oil_type, T, P)/eta_th(tc, amb, alpha, T) * (m_dot / 50 / amb.I / tc.w), T_i, T_o)[0]

N = L / 16 / tc.l
print(L, N)
print(cp(oil_type, T_i, P))
print(cp(oil_type, T_o, P))

h_o = PropsSI('H', 'T', T_o, 'P', P, oil_type)
h_i = PropsSI('H', 'T', T_i, 'P', P, oil_type)
Q = m_dot * (h_o - h_i)
r_p, r_e, r_s, r_r = get_ratios()
n_p = r_p * 50
n_e = r_e * 50
n_s = r_s * 50
n_r = r_r * 50

eta = Q / (N * 16 * 50 * tc.l * tc.w * amb.I)
print(eta)

m_dot_1 = (1 - r_r) * m_dot
m_dot_2 = m_dot - m_dot_1

Q_s = Q * r_s
T_s_i = T_o
h_s_i = h_o
h_s_o = h_s_i - Q_s / m_dot_1
T_s_o = PropsSI('T', 'H', h_s_o, 'P', P, oil_type)

Q_e = Q * r_e
T_e_i = T_s_o
h_e_i = h_s_o
h_e_o = h_e_i - Q_e / m_dot_1
T_e_o = PropsSI('T', 'H', h_e_o, 'P', P, oil_type)

Q_p = Q * r_p
T_p_i = T_e_o
h_p_i = h_e_o
h_p_o = h_p_i - Q_p / m_dot_1
T_p_o = PropsSI('T', 'H', h_p_o, 'P', P, oil_type)

Q_r = Q * r_r
T_r_i = T_o
h_r_i = h_o
h_r_o = h_r_i - Q_r / m_dot_2
T_r_o = PropsSI('T', 'H', h_r_o, 'P', P, oil_type)

def fun1(i):
	T_1, T2_p_i, m_dot_p = i[0], i[1], i[2]

	T2_p_o = convtemp(234.80 + 10, 'C', 'K')
	h2_p_o = PropsSI('H', 'T', T2_p_o, 'P', P, oil_type)
	return [
	T2_p_i - T_1 - 10,
   m_dot_p * (PropsSI('H', 'T', T2_p_i, 'P', P, oil_type) - h2_p_o) - 38.8 * (PropsSI('H', 'T', T_1, 'P', 10340000, 'water') - PropsSI('H', 'T', 234.8+273.15, 'P', 10340000, 'water')),
#	m_dot_p * (PropsSI('H', 'T', T2_p_i, 'P', P, oil_type) - h2_p_o) - 103.4 * 4200 * (T_1 - 234.8 - 273.15),
	8 * 16 * tc.l - quad(lambda T:cp(oil_type, T, P)/eta_th(tc, amb, alpha, T) * (m_dot_p / amb.I / tc.w), T2_p_o, T2_p_i)[0],
	]

r = fsolve(fun1, [310+273.15, 320+273.15, 85])
print(r)
N_p = 8
m_dot_p = r[2]
T2_p_i = r[1]
T2_p_o = convtemp(234.80 + 10, 'C', 'K')
h2_p_i = PropsSI('H', 'T', T2_p_i, 'P', P, oil_type)
h2_p_o = PropsSI('H', 'T', T2_p_o, 'P', P, oil_type)
Q_p_real = m_dot_p * (h2_p_i - h2_p_o)

eta_p = Q_p_real / (N_p * tc.l * tc.w * amb.I)

def fun2(j):
    T_2, T2_s_o, m_dot_s = j[0], j[1], j[2]

    T2_s_i = T_o
    h2_s_i = PropsSI('H', 'T', T2_s_i, 'P', P, oil_type)
    return [
    T2_s_o - T_2 - 20,
    m_dot_s * (h2_s_i - PropsSI('H', 'T', T2_s_o, 'P', P, oil_type)) - 38.8 * (PropsSI('H', 'T', 371+273.15, 'P', 10340000, 'water') - PropsSI('H', 'T', T_2, 'P', 10340000, 'water')),
    5 * 16 * tc.l - quad(lambda T:cp(oil_type, T, P)/eta_th(tc, amb, alpha, T) * (m_dot_s / amb.I / tc.w), T2_s_o, T2_s_i)[0],
    ]

r2 = fsolve(fun2, [600, 620, 70])
print(r2)
N_s = 5
m_dot_s = r2[2]
T2_s_o = r2[1]
T2_s_i = T_o
h2_s_i = PropsSI('H', 'T', T2_s_i, 'P', P, oil_type)
h2_s_o = PropsSI('H', 'T', T2_s_o, 'P', P, oil_type)
Q_s_real = m_dot_s * (h2_s_i - h2_s_o)

Delta_T1 = 40
T2_e_o = r[0] + Delta_T1
Delta_T2 = 40
T2_e_i = r2[0] + Delta_T2
h2_e_o = PropsSI('H', 'T', T2_e_o, 'P', P, oil_type)
h2_e_i = PropsSI('H', 'T', T2_e_i, 'P', P, oil_type)
Q_e_real = Q_e + Q_p + Q_s - Q_p_real - Q_s_real
m_dot_e = Q_e_real / (h2_e_i - h2_e_o)

L_e = quad(lambda T:cp(oil_type, T, P)/eta_th(tc, amb, alpha, T) * (m_dot_e / amb.I / tc.w), T2_e_o, T2_e_i)[0]

N_e = L_e / 16 / tc.l

T2_r_o = 228.67 +273.15
T2_r_i = T_o
h2_r_o = PropsSI('H', 'T', T2_r_o, 'P', P, oil_type)
h2_r_i = PropsSI('H', 'T', T2_r_i, 'P', P, oil_type)
m_dot_r = Q_r / (h2_r_i - h2_r_o)

L_r = quad(lambda T:cp(oil_type, T, P)/eta_th(tc, amb, alpha, T) * (m_dot_r / amb.I / tc.w), T2_r_o, T2_r_i)[0]

N_r = L_r / 16 / tc.l

print(m_dot_p, N_p)
print(m_dot_e, N_e)
print(m_dot_s, N_s)
print(m_dot_r, N_r)


