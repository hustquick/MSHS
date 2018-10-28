import math

class Trough:
    A = 545         # Aperture area of the collector, m^2
    gamma = 0.93    # Intercept factor of the collector
    rho = 0.94      # Reflectance of the collector
    shading = 1     # Shading factor of the collector
    tau = 0.95     # Transmissivity of trough receiver
    alpha = 0.96   # Absorptivity of the absorber selective coating of trough collector
    w = 5       # Width of trough collector, m
    Fe = 0.97      # Soiling factor of the trough collector
    d_i = 0.066     # Inner diameter of the absorber, m
    d_o = 0.07     # Outer diameter of the absorber, m
    phi = 70 / 180 * math.pi     # Incidence angle
    v_min = 1.1       # Minimun fluid speed in pipe, corresponding to limiting the fouling, m/s
    v_max = 2.9       # Maximun fluid speed in pipe, corresponding to limiting the erosion, m/s
    f = 1.84
    l = 8 * 6
    tc_type = ''
