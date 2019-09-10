# In this file, classes for handling calculated Vector Network
# Analyzer Spectra is defined

from numpy import pi


class calculatedSingleVNASpectrum:
    """Definition of a class used to handle instances
    refering to a single antenna modelled as a inductor (L1)
    and a resistor (R1) connected in parallel with a capacitor (C1).
    For the future, a variable for a resistor, R0, in series with
    the above circuit is also defined"""

    def __init__(self, frequency, R0, R1, F0, Q):
        # Initialization of (private) variables from values provided
        # in the GUI singleAntennaAnalysis
        # frequency: array, provided in MHz
        # R0, R1: see above
        # F0: resonance for the antenna
        # Q: quality factor for the antenna
        # Both filename and expdata are stored as private variables
        self.__frequency = frequency
        self.__R0 = R0
        self.__R1 = R1
        self.__F0 = F0
        self.__Q = Q
        # Calculation of corresponding L1 and C1 values
        # from provided R1, F0 and Q
        # Note that frequency is converted to Hz
        self.updateL1C1Values()
        # Caluclation of equivalent (and normalized)
        # real and imaginary impedances
        self.calculateImpedanceSingleAntenna()

    def calculateImpedanceSingleAntenna(self):
        fr = self.__frequency / self.__F0
        self.__ReZ = self.__R0 + self.__R1 * self.__Q**2 * (
            1 - (1/fr) * (fr - 1 / fr)) / (1 + (self.__Q * (fr - 1 / fr))**2)
        self.__ImZ = - self.__R1 *\
            (self.__Q**3 * (fr - 1 / fr) + self.__Q / fr) /\
            (1 + (self.__Q * (fr - 1 / fr))**2)

    def updateL1C1Values(self):
        self.__L1 = self.__Q * self.__R1 / (2 * pi * self.__F0 * 1e6)
        self.__C1 = 1 / (self.__Q * self.__R1 * 2 * pi * self.__F0 * 1e6)

    def setR0(self, R0):
        self.__R0 = R0

    def setR1(self, R1):
        self.__R1 = R1

    def setF0(self, F0):
        self.__F0 = F0

    def setQ(self, Q):
        self.__Q = Q

    def getFreq(self):
        return self.__frequency

    def getR0(self):
        return self.__R0

    def getR1(self):
        return self.__R1

    def getF0(self):
        return self.__F0

    def getQ(self):
        return self.__Q

    def getL1(self):
        return self.__L1

    def getC1(self):
        return self.__C1

    def getReZ(self):
        return self.__ReZ

    def getImZ(self):
        return self.__ImZ
