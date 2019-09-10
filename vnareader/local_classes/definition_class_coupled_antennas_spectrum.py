# In this file, classes for handling calculated Vector Network
# Analyzer Spectra is defined

from numpy import pi, real, imag


class calculatedCoupledAntennasSpectrum:
    """Definition of a class used to handle instances
    refering to a single antenna (R1, L1, C1) magnetically
    coupled (k) to another antenna (R2, L2, C2) connected
    in parallelel with an additional resistor (Rsensor)
    and a capacitor (Csensor). For future implementations,
    a variable for a resistor, R0, in series with the first
    antenna is also defined"""

    def __init__(
            self, frequency, R0, R1, L1, C1, R2, L2, C2, Rsensor, Csensor, k):
        # Initialization of (private) variables from values provided
        # in the GUI singleAntennaAnalysis
        # frequency: array, provided in MHz
        # R0, R1: see above
        # F0: resonance for the antenna
        # Q: quality factor for the antenna
        # Both filename and expdata are stored as private variables
        self.__Freq = frequency
        self.__R0 = R0
        self.__R1 = R1
        self.__L1 = L1
        self.__C1 = C1
        self.__R2 = R2
        self.__L2 = L2
        self.__C2 = C2
        self.__Rsensor = Rsensor
        self.__Csensor = Csensor
        self.__k = k
        # Caluclation of equivalent (and normalized)
        # real and imaginary impedances
        self.calculateImpedanceCoupledAntennas()
        self.calculateS11()

    def calculateImpedanceCoupledAntennas(self):
        # frequency array in Hz
        f = self.__Freq * 1e6
        # Capacitative impedance of reader antenna
        ZC1 = -1j / (2 * pi * f * self.__C1)
        # inductive impedance of reader antenna
        ZL1 = 1j * 2 * pi * f * self.__L1
        # resistive impedance of reader antenna
        ZR1 = self.__R1
        # resistive impedance of transponder antenna
        ZRtag = self.__R2
        # Inductive impedance of transponder antenna
        ZLtag = 1j * 2 * pi * f * self.__L2
        # Overall capacitative impedance of
        # transponder antenna and sensor component
        # (for this analysis it is considered that
        # the capacitor of the transponder antenna
        # forms part of the sensor component)
        ZCtag = -1j / (2 * pi * f * (self.__C2 + self.__Csensor))
        # Resistive impedance of sensor component
        ZRsensor = self.__Rsensor
        # Overall impedance of the sensor component
        Zsensor = (ZCtag * ZRsensor) / (ZCtag + ZRsensor)
        # Overall impedance of transponder antenna and sensor component
        Ztag = ZRtag + ZLtag + Zsensor
        # Overall reflected impedance
        # (ZL1 + that from magnetic coupling)
        Zreflected = ZL1 + (
            self.__k**2 * self.__L1 * self.__L2 * (2 * pi * f)**2) / Ztag
        # Equivalent impedace, stores as a private variable of the class
        self.__Zeq = ZC1 * (Zreflected + ZR1) / (ZC1 + Zreflected + ZR1)

    def calculateS11(self):
        self.__S11 = (50 - self.__Zeq) / (50 + self.__Zeq)
    # ***************************************************
    # ***************************************************
    # ***************************************************
    #
    # ***************************************************
    # Definition of methods for accessing class variables
    # ***************************************************

    def setR0(self, R0):
        self.__R0 = R0

    def setR1(self, R1):
        self.__R1 = R1

    def setL1(self, L1):
        self.__L1 = L1

    def setC1(self, C1):
        self.__C1 = C1

    def setR2(self, R2):
        self.__R2 = R2

    def setL2(self, L2):
        self.__L2 = L2

    def setC2(self, C2):
        self.__C2 = C2

    def setRsensor(self, Rsensor):
        self.__Csensor = Rsensor

    def setCsensor(self, Csensor):
        self.__Csensor = Csensor

    def setk(self, k):
        self.__k = k

    def getFreq(self):
        return self.__Freq

    def getR0(self):
        return self.__R0

    def getR1(self):
        return self.__R1

    def getL1(self):
        return self.__L1

    def getC1(self):
        return self.__C1

    def getR2(self):
        return self.__R2

    def getL2(self):
        return self.__L2

    def getC2(self):
        return self.__C2

    def getRsensor(self):
        return self.__Rsensor

    def getCsensor(self):
        return self.__Csensor

    def getk(self):
        return self.__k

    def getReZ(self):
        return real(self.__Zeq)

    def getImZ(self):
        return imag(self.__Zeq)

    def getReS11(self):
        return real(self.__S11)

    def getImS11(self):
        return imag(self.__S11)

    def getModS11(self):
        return abs(self.__S11)
    # ***************************************************
    # ***************************************************
    # ***************************************************
