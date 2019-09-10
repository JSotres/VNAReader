# In this file, a class for handling Vector Network
# Analyzer experimental is defined

from numpy import vstack, arctan


class vnaSpectrum:
    """Definition of the class vnaSpectrum
    Used to handle instances created
    from VNA raw data. It provides methods
    for initiating the instance, setting values for
    its variables and methods for reading and changing
    their values"""

    def __init__(self, filename, expdata):
        # Initialization of (private) variables
        # filename: name of the file from where experimental data was read
        # column #0: frequency (MHz)
        # column #1: real part of the S11 scattering parameter
        # column #2: imaginary part of the S11 scattering parameter
        # Q: quality factor for the antenna
        # Both filename and expdata are stored as private variables
        self.__filename = filename
        self.__expdata = expdata
        # More columns added to expdata
        # column #3: module of the S11 scattering parameter
        # column #4: phase of the S11 scattering parameter
        # column #5: real part of the normalized equivalent impedance
        # column #6: imaginary part of the normalized equivalent impedance
        self.__expdata = vstack([
            self.__expdata,
            (self.__expdata[1, :]**2 + self.__expdata[2, :]**2)**0.5
        ])
        self.__expdata = vstack([
            self.__expdata,
            arctan(self.__expdata[2, :]/self.__expdata[1, :])
        ])
        self.__expdata = vstack([
            self.__expdata,
            (1-self.__expdata[1, :]**2-self.__expdata[2, :]**2) / (
                (1-self.__expdata[1, :])**2+self.__expdata[2, :]**2)
        ])
        self.__expdata = vstack([
            self.__expdata,
            2 * self.__expdata[2, :] / (
                (1-self.__expdata[1, :])**2 + self.__expdata[2, :]**2)
        ])

    # Methods for reading and setting values of class vnaSpectrum variables
    def setReS11(self, realS11):
        self.__expdata[1, :] = realS11

    def setImS11(self, imaginaryS11):
        self.__expdata[2, :] = imaginaryS11

    def setModS11(self, ModS11):
        self.__expdata[3, :] = ModS11

    def setPhaS11(self, PhaS11):
        self.__expdata[4, :] = PhaS11

    def setReZ(self, realZ):
        self.__expdata[5, :] = realZ

    def setImZ(self, imaginaryZ):
        self.__expdata[6, :] = imaginaryZ

    def getFileName(self):
        return self.__filename

    def getFreq(self):
        return self.__expdata[0, :]

    def getReS11(self):
        return self.__expdata[1, :]

    def getImS11(self):
        return self.__expdata[2, :]

    def getModS11(self):
        return self.__expdata[3, :]

    def getPhaS11(self):
        return self.__expdata[4, :]

    def getReZ(self):
        return self.__expdata[5, :]

    def getImZ(self):
        return self.__expdata[6, :]

    def getData(self, index):
        return self.__expdata[index, :]
