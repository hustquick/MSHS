import math
SIGMA = 5.67e-8
G = 9.807
R = 8.314

FLUID = {1: 'Air', 2: 'Water', 3: 'INCOMP::TVP1', 4: 'Toluene', 5: 'R123'}


def logMean(a, b):
    if a * b > 0:
        return (a - b) / math.log(a / b)
    else:
        print("The two numbers are wrong!")
        return []


def convtemp(valuesToConvert, inputTempUnit, outputTempUnit):
    Unit = ['K', 'F', 'C', 'R']
    UnitSlope = {'K': 1, 'F': 5 / 9, 'C': 1, 'R': 5 / 9}
    UnitBias = {'K': 0, 'F': - 273.15 * 9 / 5 + 32, 'C': - 273.15, 'R': 0}

    if (inputTempUnit in Unit) and (outputTempUnit in Unit):
        return (valuesToConvert - UnitBias[inputTempUnit]) * UnitSlope[inputTempUnit] / \
            UnitSlope[outputTempUnit] + UnitBias[outputTempUnit]
    else:
        print("The units must be 'K', 'C', 'F' or 'R'. Please check!")

def degtorad(value):
    return value * math.pi / 180