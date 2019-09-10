from numpy import pi, r_, real, imag


def FittingFunctionImpedanceSingleAntenna(R0, R1, F0, Q, f):
    fr = f / F0
    ReZ = R0 + R1 * Q**2 * (1 - (1/fr) * (fr - 1 / fr)) /\
          (1 + (Q * (fr - 1 / fr))**2)
    ImZ = - R1 * (Q**3 * (fr - 1 / fr) + Q / fr) / (1 + (Q * (fr - 1 / fr))**2)
    Zeq = ReZ + 1j * ImZ
    return Zeq


def residualFittingSingleAntenna(params, x, y1, y2):
    resid = r_[functionReZSingleAntenna(
        params['R0'].value, params['R1'].value,
        params['F0'].value, params['Q'].value, x) - y1,
               functionImZSingleAntenna(
                   params['R0'].value, params['R1'].value,
                   params['F0'].value, params['Q'].value, x) - y2]
    return resid

functionReZSingleAntenna = lambda R0, R1, F0, Q, F: R0+R1*Q**2*(1-F0/F)*(F/F0-F0/F)/(1+(Q*(F/F0-F0/F))**2)
functionImZSingleAntenna = lambda R0, R1, F0, Q, F: -R1*(Q**3*(F/F0-F0/F)+Q*F0/F)/(1+(Q*(F/F0-F0/F))**2)


def residualFittingCoupledAntennas(params, f, y1, y2):
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


def FittingFunctionImpedanceCoupledAntennas(R0, R1, L1,
                                            C1, R2, L2, C2,
                                            Rsensor, Csensor, k, f):
    f = f*1e6
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


def CalculateS11(Zeq):
    S11 = (50 - Zeq) / (50 + Zeq)
    return S11
