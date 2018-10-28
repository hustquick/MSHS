"""This class describes a fluid stream that has inherent
    properties and dependent properties"""
from CoolProp.CoolProp import PropsSI


class Stream:
    """This class describes a fluid stream that has inherent
    properties and dependent properties
    """
    fluid = ''      # Fluid type
    dot_m = 0       # Mass flow rate, kg/s
    T = 0           # Temperature, K
    P = 0 		    # Pressure, Pa
    x = []
    """ Quality, [0, 1] for two phase stream; NaN for single
        phase stream
    """

    def get_T_c(self):
        return self.T - 273.15
    T_c = property(get_T_c)

    def get_h(self):
        if self.x == []:
            return PropsSI('H', 'T', self.T, 'P', self.P, self.fluid)
        return PropsSI('H', 'P', self.P, 'Q', self.x, self.fluid)
    h = property(get_h)

    def get_s(self):
        if self.x == []:
            return PropsSI('S', 'T', self.T, 'P', self.P, self.fluid)
        return PropsSI('S', 'T', self.T, 'Q', self.x, self.fluid)
    s = property(get_s)

    def get_cp(self):
        if self.x == []:
            return PropsSI('C', 'T', self.T, 'P', self.P, self.fluid)
        return []
    cp = property(get_cp)

    def flow_to(self, st):
        st.fluid = self.fluid
        st.dot_m = self.dot_m

    def mix(self, st1):
        st2 = Stream()
        if self.fluid == st1.fluid and self.P == st1.P:
            st2.fluid = self.fluid
            st2.P = self.P
            st2.dot_m = self.dot_m + st1.dot_m
            h = (self.dot_m * self.h + st1.dot_m * st1.h) / \
                (self.dot_m + st1.dot_m)
            st2.T = PropsSI('T', 'H', h, 'P', st2.P)
            return st2
        print('Fluid types and pressures of the fluids must be the same!')
        return []

    def convergeTo(self, st1):
        pass
