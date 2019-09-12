'''
List of functions used in the program VNA Reader
'''

from numpy import pi, r_, real, imag


def functionReZSingleAntenna(R0, R1, F0, Q, F):
    '''
    Calculates the Real (normalized over 50 Ohm) impedance
    of a single (R1+L1)||C1 antenna
    '''
    FN = F / F0
    return R0 + R1 * Q**2 * (1 - 1 / FN) * (FN - 1 / FN) / (
            1 + (Q * (FN - 1 / FN))**2)


def functionImZSingleAntenna(R0, R1, F0, Q, F):
    '''
    Calculates the Imaginary (normalized over 50 Ohm) impedance
    of a single (R1+L1)||C1 antenna
    '''
    FN = F / F0
    return -R1 * (Q**3 * (FN - 1 / FN) + Q / FN) / (
            1 + (Q * (FN - 1 / FN))**2)


def residualFittingSingleAntenna(params, x, y1, y2):
    '''
    Calculates residues between experimental real (y1) and imaginary (y2)
    impedance (not normalized) over a range of frequencies (x) and
    theoretical data calculated with the functions functionReZSingleAntenna
    and functionImZSingleAntenna assuming the parameters provided in params
    '''
    resid = r_[functionReZSingleAntenna(
        params['R0'].value, params['R1'].value,
        params['F0'].value, params['Q'].value, x) - y1,
               functionImZSingleAntenna(
                   params['R0'].value, params['R1'].value,
                   params['F0'].value, params['Q'].value, x) - y2]
    return resid


def FittingFunctionImpedanceCoupledAntennas(R0, R1, L1,
                                            C1, R2, L2, C2,
                                            Rsensor, Csensor, k, f):
    '''
    Calculates the (not normalized) impedance of two magnetically
    coupled antennas, that of the transponder copled with a resistor
    and a capacitor in parallel
    '''
    # Assumig the frequency is provided in MHZ, transofrm into Hz
    f = f*1e6
    # frequency is from here transformed into angularfrequency
    ZC1 = -1j/(2*pi*f*C1)
    ZL1 = 1j*2*pi*f*L1
    ZR1 = R1
    ZRtag = R2
    ZLtag = 1j*2*pi*f*L2
    ZCtag = -1j/(2*pi*f*(C2+Csensor))
    ZRsensor = Rsensor
    Zsensor = (ZCtag * ZRsensor) / (ZCtag + ZRsensor)
    Ztag = ZRtag + ZLtag + Zsensor
    Zreflected = ZL1 + (k**2 * L1 * L2 * (2*pi*f)**2) / Ztag
    Zeq = ZC1 * (Zreflected + ZR1) / (ZC1 + Zreflected + ZR1)
    return Zeq


def residualFittingCoupledAntennas(params, f, y1, y2):
    '''
    Calculates residues between  experimental real (y1) and
    imaginary (y2) impedance (not normalized) over a range of
    frequencies (f) and theoretical data calculated with the
    function FittingFunctionImpedanceCoupledAntennas assuming
    the parameters provided in params
    '''
    resid = r_[real(FittingFunctionImpedanceCoupledAntennas(
                   params['R0'].value, params['R1'].value,
                   params['L1'].value, params['C1'].value,
                   params['R2'].value, params['L2'].value,
                   params['C2'].value, params['Rsensor'].value,
                   params['Csensor'].value, params['k'].value, f)) - y1,
               imag(FittingFunctionImpedanceCoupledAntennas(
                   params['R0'].value, params['R1'].value,
                   params['L1'].value, params['C1'].value,
                   params['R2'].value, params['L2'].value,
                   params['C2'].value, params['Rsensor'].value,
                   params['Csensor'].value, params['k'].value, f)) - y2
               ]
    return resid


def residualFittingCoupledAntennas2(params, f1, rez1, imz1, f2, rez2, imz2):
    '''
    Calculates residues between  experimental real (y1) and
    imaginary (y2) impedance (not normalized) over a range of
    frequencies (f) and theoretical data calculated with the
    function FittingFunctionImpedanceCoupledAntennas assuming
    the parameters provided in params
    '''
    resid = r_[real(FittingFunctionImpedanceCoupledAntennas(
                   params['R0'].value, params['R1'].value,
                   params['L1'].value, params['C1'].value,
                   params['R2'].value, params['L2'].value,
                   params['C2'].value, params['Rsensor'].value,
                   params['Csensor'].value, params['k'].value, f1)) - rez1,
               imag(FittingFunctionImpedanceCoupledAntennas(
                   params['R0'].value, params['R1'].value,
                   params['L1'].value, params['C1'].value,
                   params['R2'].value, params['L2'].value,
                   params['C2'].value, params['Rsensor'].value,
                   params['Csensor'].value, params['k'].value, f1)) - imz1,
               real(FittingFunctionImpedanceCoupledAntennas(
                   params['R0'].value, params['R1'].value,
                   params['L1'].value, params['C1'].value,
                   params['R2'].value, params['L2'].value,
                   params['C2'].value, params['Rsensor'].value,
                   params['Csensor'].value, params['k'].value, f2)) - rez2,
               real(FittingFunctionImpedanceCoupledAntennas(
                   params['R0'].value, params['R1'].value,
                   params['L1'].value, params['C1'].value,
                   params['R2'].value, params['L2'].value,
                   params['C2'].value, params['Rsensor'].value,
                   params['Csensor'].value, params['k'].value, f2)) - imz2
               ]
    return resid


def CalculateS11VNAReaderv1(Zeq):
    S11 = (50 - Zeq) / (50 + Zeq)
    return S11
