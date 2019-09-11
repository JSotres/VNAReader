'''
Class definition for spectra for single
R0+[(R1+L1)||C1] antennas
'''

from numpy import pi


class calculatedSingleVNASpectrum:
    '''
    Class used to handle instances refering to a single 
    antenna modelled as a inductor (L1) and a resistor (R1)
    connected in parallel with a capacitor (C1).
    For the future, a variable for a resistor, R0, in
    series with the above circuit is also defined.
    
    Attributes:
        __frequency: frequency array
        __R0: resistance of connection between antenna and VNA
        __R1: antennas's resistance
        __Q: antenna's quelity factor
        __L1: antenna's impedance
        __C1: antenna's parasitic capacitance
        __ReZ: antenna's equivalent real impedance (NOT normalized)
        __ImZ: antenna's equivalent imaginary impedance (NOT normalized)
    
    Methods:
        __init__(frequency, R0, R1, F0, Q): Initialization of
            class and attributes
        updateL1C1Values(): updates L1 and C1 values from provided R1, F0 and Q
        calculateImpedanceSingleAntenna(): calculates equivalent real and
            imaginary impedances (NOT normalized) for the antenna
        **** Methods for setting attribute values ****
        setR0(R0)
        setR1(R1)
        setF0(F0)
        setQ(Q)
        **** Methods for retrieving attribute values ***
        getFreq()
        getR0()
        getR1()
        getF0()
        getQ()
        getL1()
        getC1()
        getReZ()
        getImZ()
    '''

    def __init__(self, frequency, R0, R1, F0, Q):
        '''Initialization of (private) variables from values provided
        in the GUI singleAntennaAnalysis
        '''
        # frequency: array, provided in MHz
        # R0, R1: see above
        # F0: resonance for the antenna
        # Q: quality factor for the antenna
        self.__Freq = frequency
        self.__R0 = R0
        self.__R1 = R1
        self.__F0 = F0
        self.__Q = Q
        # Calculation of corresponding L1 and C1 values
        # from provided R1, F0 and Q
        # Note that frequency is converted to Hz
        self.updateL1C1Values()
        # Caluclation of equivalent (NOT normalized)
        # real and imaginary impedances
        self.calculateImpedanceSingleAntenna()

    def calculateImpedanceSingleAntenna(self):
        ''' Calculation of the antenna's (NOT normalized real and imaginary
        impedances from Freq, R1, F0 and Q
        '''
        fr = self.__Freq / self.__F0
        self.__ReZ = self.__R0 + self.__R1 * self.__Q**2 * (
            1 - (1/fr) * (fr - 1 / fr)) / (1 + (self.__Q * (fr - 1 / fr))**2)
        self.__ImZ = - self.__R1 *\
            (self.__Q**3 * (fr - 1 / fr) + self.__Q / fr) /\
            (1 + (self.__Q * (fr - 1 / fr))**2)

    def updateL1C1Values(self):
        ''' Calculation of the antenna's L1 and C1 from
        R1, F0 and Q
        '''
        self.__L1 = self.__Q * self.__R1 / (2 * pi * self.__F0 * 1e6)
        self.__C1 = 1 / (self.__Q * self.__R1 * 2 * pi * self.__F0 * 1e6)

    
    def setFreq(self, Freq):
        ''' Sets Frequency array
        '''
        self.__Freq = Freq
        
    def setR0(self, R0):
        ''' Sets value for resistance (R0) of connection
        between antenna and VNA
        '''
        self.__R0 = R0

    def setR1(self, R1):
        ''' Sets value for antenna resistance R1
        '''
        self.__R1 = R1

    def setF0(self, F0):
        ''' Sets value for antenna resonance frequency F0
        '''
        self.__F0 = F0

    def setQ(self, Q):
        ''' Sets value for antenna quality factor Q
        '''
        self.__Q = Q

    def getFreq(self):
        ''' Returns array of frequencies (in the provided units)
        '''
        return self.__Freq

    def getR0(self):
        ''' Returns resistance of connection between antenna and VNA
        '''
        return self.__R0

    def getR1(self):
        ''' Returns antenna resistance R1
        '''
        return self.__R1

    def getF0(self):
        ''' Returns antenna resonance frequency F0
        '''
        return self.__F0

    def getQ(self):        
        ''' Returns antenna quality factor Q
        '''
        return self.__Q

    def getL1(self):
        ''' Returns antenna impedance L1
        '''
        return self.__L1

    def getC1(self):
        ''' Returns antenna parasitic capacitance C1
        '''
        return self.__C1

    def getReZ(self):
        ''' Returns antenna real impedance
        '''
        return self.__ReZ

    def getImZ(self):
        ''' Returns antenna imaginary impedance
        '''
        return self.__ImZ
