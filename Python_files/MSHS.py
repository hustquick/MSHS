from Stream import Stream
from CoolProp.CoolProp import PropsSI
from Const import *

Number_of_waterStatePoints = 31;
Number_of_Assamblies = 50;

st1 = []
for i in range(Number_of_waterStatePoints):
    st1.append(Stream())
    st1[i].fluid = FLUID[2]

st1[0].T = convtemp(371, 'C', 'K')
st1[0].P = 100e5
st1[0].dot_m = 38.8

st1[1].T = convtemp(241.6, 'C', 'K')
st1[1].P = 33.65e5
st1[1].dot_m = 2.9

st1[2].P = 18.58e5;
st1[2].dot_m = 35.74;
st1_2_h = 2710e3;
st1[2].x = PropsSI('Q', 'P', st1[2].P, 'H', st1_2_h, st1[2].fluid);
st1[2].T = PropsSI('T', 'P', st1[2].P, 'Q', st1[2].x, st1[2].fluid);

st1[3].T = convtemp(371, 'C', 'K');
st1[3].P = 17.10e5;
st1[3].dot_m = 33.16;

st1[4].T = convtemp(280.4, 'C', 'K');
st1[4].P = 7.98e5;
st1[4].dot_m = 2.10;

st1[5].T = convtemp(166.8, 'C', 'K');
st1[5].P = 2.73e5;
st1[5].dot_m = 1.76;

# st1[6].T = convtemp(98.556, 'C', 'K');    State point 7 is saturated
st1[6].P = 0.96e5;
st1[6].dot_m = 1.6205;
st1_6_h = 2624e3;
st1[6].x = PropsSI('Q', 'P', st1[6].P, 'H', st1_6_h, st1[6].fluid);
st1[6].T = PropsSI('T', 'P', st1[6].P, 'Q', st1[6].x, st1[6].fluid);

# st1[7].T = convtemp(68.111, 'C', 'K');    State point 8 is saturated
st1[7].P = 0.29e5;
st1[7].dot_m = 0.74;
st1_7_h = 2460e3;
st1[7].x = PropsSI('Q', 'P', st1[7].P, 'H',
                    st1_7_h, st1[7].fluid);
st1[7].T = PropsSI('T', 'P', st1[7].P, 'Q',
                    st1[7].x, st1[7].fluid);

# st1[8].T = convtemp(41.556, 'C', 'K');    State point 9 is saturated
st1[8].P = 0.08e5;
st1[8].dot_m = 26.65;
st1_8_h = 2348e3;
st1[8].x = PropsSI('Q', 'P', st1[8].P, 'H',
                    st1_8_h, st1[8].fluid);
st1[8].T = PropsSI('T', 'P', st1[8].P, 'Q',
                    st1[8].x, st1[8].fluid);

# st1[9].T = convtemp(41.439, 'C', 'K');   State point 10 is saturated
st1[9].P = 0.08e5;
st1[9].dot_m = 31.06;
st1_9_h = 174.1e3;
st1[9].x = PropsSI('Q', 'P', st1[9].P, 'H',
                    st1_9_h, st1[9].fluid);
st1[9].T = PropsSI('T', 'P', st1[9].P, 'Q',
                    st1[9].x, st1[9].fluid);

st1[10].T = convtemp(52.87, 'C', 'K');
st1[10].P = 0.14e5;
st1[10].dot_m = 4.41;

st1[11].T = convtemp(42.67, 'C', 'K');
st1[11].P = 14.76e5;
st1[11].dot_m = 31.06;

st1[12].T = convtemp(92.17, 'C', 'K');
st1[12].P = 0.29e5;
st1[12].dot_m = 1.04;
# st1_12_h = 2670.0e3;
# st1[12].x = PropsSI('Q', 'P', st1[12].P, 'H',
#                     st1_12_h, st1[12].fluid);
# st1[12].T = PropsSI('T', 'P', st1[12].P, 'Q',
#                     st1[12].x, st1[12].fluid);

st1[13].T = convtemp(64.72, 'C', 'K');
st1[13].P = 10.00e5;
st1[13].dot_m = 31.06;

# st1[14].T = convtemp(74.74, 'C', 'K');   State point 15 is saturated
st1[14].P = 0.38e5;
st1[14].dot_m = 3.37;
st1_14_h = 313.1e3;
st1[14].x = PropsSI('Q', 'P', st1[14].P, 'H',
                    st1_14_h, st1[14].fluid);
st1[14].T = PropsSI('T', 'P', st1[14].P, 'Q',
                    st1[14].x, st1[14].fluid);

st1[15].T = convtemp(95.11, 'C', 'K');
st1[15].P = 8.70e5;
st1[15].dot_m = 31.06;

# st1[16].T = convtemp(105.10, 'C', 'K');   State point 17 is saturated
st1[16].P = 1.21e5;
st1[16].dot_m = 1.76;
st1_16_h = 440.7e3;
st1[16].x = PropsSI('Q', 'P', st1[16].P, 'H', st1_16_h, st1[16].fluid);
st1[16].T = PropsSI('T', 'P', st1[16].P, 'Q', st1[16].x, st1[16].fluid);

st1[17].T = convtemp(126.70, 'C', 'K');
st1[17].P = 7.40e5;
st1[17].dot_m = 31.06;

# st1[18].T = convtemp(167.20, 'C', 'K');
st1[18].P = 7.40e5;
st1[18].dot_m = 38.80;
st1_18_h = 708.9e3;
st1[18].x = PropsSI('Q', 'P', st1[18].P, 'H', st1_18_h, st1[18].fluid);
st1[18].T = PropsSI('T', 'P', st1[18].P, 'Q', st1[18].x, st1[18].fluid);


st1[19].T = convtemp(171.40, 'C', 'K');
st1[19].P = 125e5;
st1[19].dot_m = 38.8;

# st1[20].T = convtemp(179.30, 'C', 'K');   State point 21 is saturated
st1[20].P = 9.86e5;
st1[20].dot_m = 5.48;
st1_20_h = 760.1e3;
st1[20].x = PropsSI('Q', 'P', st1[20].P, 'H', st1_20_h, st1[20].fluid);
st1[20].T = PropsSI('T', 'P', st1[20].P, 'Q', st1[20].x, st1[20].fluid);

# st1[21].T = convtemp(208.70, 'C', 'K');  State point 22 is saturated
st1[21].P = 18.58e5;
st1[21].dot_m = 2.58;
st1_21_h = 2710.0e3;
st1[21].x = PropsSI('Q', 'P', st1[21].P, 'H',
                    st1_21_h, st1[21].fluid);
st1[21].T = PropsSI('T', 'P', st1[21].P, 'Q',
                    st1[21].x, st1[21].fluid);

# st1[22].T = convtemp(208.70, 'C', 'K');   State point 23 is saturated
st1[22].P = 18.58e5;
st1[22].dot_m = 33.16;
st1_22_h = 2710.0e3;
st1[22].x = PropsSI('Q', 'P', st1[22].P, 'H',
                    st1_22_h, st1[22].fluid);
st1[22].T = PropsSI('T', 'P', st1[22].P, 'Q',
                    st1[22].x, st1[22].fluid);

st1[23].T = convtemp(203.60, 'C', 'K');
st1[23].P = 112e5;
st1[23].dot_m = 38.8;

# st1[24].T = convtemp(213.60, 'C', 'K');   State point 25 is saturated
st1[24].P = 20.50e5;
st1[24].dot_m = 2.90;
st1_24_h = 914.5e3;
st1[24].x = PropsSI('Q', 'P', st1[24].P, 'H',
                    st1_24_h, st1[24].fluid);
st1[24].T = PropsSI('T', 'P', st1[24].P, 'Q',
                    st1[24].x, st1[24].fluid);

st1[25].T = convtemp(234.80, 'C', 'K');
st1[25].P = 103.60e5;
st1[25].dot_m = 38.80;

st1_26_T = convtemp(313.40, 'C', 'K');
st1[26].P = 103.4e5;
st1[26].dot_m = 38.8;
st1[26].x = 0;
st1[26].T = PropsSI('T', 'P', st1[26].P, 'Q',
                    st1[26].x, st1[26].fluid);

# st1_27.T = convtemp(313.40, 'C', 'K');
st1[27].P = 103.4e5;
st1[27].dot_m = 38.8;
st1[27].x = 1;
st1[27].T = PropsSI('T', 'P', st1[27].P, 'Q',
                    st1[27].x, st1[27].fluid);

st1[28].T = convtemp(371, 'C', 'K');
st1[28].dot_m = 0.16;
st1_28_h = 3005e3;
st1[28].P = 100e5;

st1[29].T = convtemp(371, 'C', 'K');
st1[29].P = 17.10e5;
st1[29].dot_m = 0.3;

st1[30].T = convtemp(92.17, 'C', 'K');
st1[30].P = 0.29e5;
st1[30].dot_m = 1.04;

def get_ratios():
    Q_p = st1[26].dot_m * st1[26].h - st1[25].dot_m * st1[25].h;
    Q_e = st1[27].dot_m * st1[27].h - st1[26].dot_m * st1[26].h;
    Q_s = st1[0].dot_m * st1[0].h - st1[27].dot_m * st1[27].h;
    Q_r = st1[3].dot_m * st1[3].h - st1[22].dot_m * st1[22].h;

    Q = Q_p + Q_e + Q_s + Q_r;
    r_p = Q_p / Q;
    r_e = Q_e / Q;
    r_s = Q_s / Q;
    r_r = Q_r / Q;
    return r_p, r_e, r_s, r_r


Number_of_oilStatePoints = 9
st2 = []
for i in range(Number_of_oilStatePoints):
    st2.append(Stream())
    st2[i].fluid = FLUID[3]
    
st2[0].T = convtemp(391, 'C', 'K')
st2[0].P = 12.8e5
st2[0].dot_m = 364.58

st2[1].T = convtemp(391, 'C', 'K')
st2[1].P = 12.8e5
st2[1].dot_m = 316.63

st2[2].T = convtemp(391, 'C', 'K')
st2[2].P = 12.8e5
st2[2].dot_m = 47.95

st2[3].T = convtemp(378.6, 'C', 'K')
st2[3].P = 12.20e5
st2[3].dot_m = 316.63

st2[4].T = convtemp(301.4, 'C', 'K')
st2[4].P = 10.70e5
st2[4].dot_m = 316.63

st2[5].T = convtemp(297.8, 'C', 'K')
st2[5].P = 9.8e5
st2[5].dot_m = 316.63

st2[6].T = convtemp(260, 'C', 'K')
st2[6].P = 12.60e5
st2[6].dot_m = 47.95

st2[7].P = 10e5
st2[7].dot_m = 364.58
st2_7_h = (st2[6].dot_m * st2[6].h + st2[5].dot_m * st2[5].h) / st2[7].dot_m
st2[7].T = PropsSI('T', 'H', st2_7_h, 'P', st2[7].P, st2[7].fluid)

st2[8].T = convtemp(294.7, 'C', 'K')
st2[8].P = 33.5e5
st2[8].dot_m = 364.58

#st3 = st2
#p = range(980000, 3350000, 10000)
#for i in p:
#    H_t = PropsSI('H', 'P', i, 'T', st3[8].T, st3[8].fluid)
#    print(i, H_t)

Q_2 = st2[0].dot_m * (st2[0].h - st2[8].h)
