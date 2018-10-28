from Const import convtemp
class Ambient:
    def __init__(self):
        self.I = 800;    # Solar direct noral irradiance, W/m^2
        self.T = convtemp(25, 'C', 'K')  # Ambien temperature, K
        self.v_wind = 1.5    # Ambient wind speed
