"""
Definition of class to create the coupled antennas analysis GUI
from the Qt5 created template from coupledAntennasAnalysisWindow_v0
"""

from PyQt5.QtWidgets import QMainWindow
from matplotlib.backends.backend_qt5agg import (
    NavigationToolbar2QT as NavigationToolbar)
from lmfit import minimize, Parameters
# local imports
from ..qt5_ui_files.coupledAntennasAnalysisWindow_v0 import (
        Ui_MainAnalysisCoupledAntennasWindow)
from .definition_class_coupled_antennas_spectrum import calculatedCoupledAntennasSpectrum
from ..local_functions.definition_local_functions import residualFittingCoupledAntennas


class myCoupledAntennasGUI(QMainWindow):
    ''' class for coupled antennas analysis GUIs
    
    Attributes:
        ui
        slidersResolution
        spectrum
        fittedSpectrum
    
    Methods:
        __init__()
        doFitData()
        updateSliderBarR0()
        updateSliderBarR1()
        updateSliderBarL1()
        updateSliderBarC1()
        updateSliderBark()
        updateSliderBarL2()
        updateSliderBarC2()
        updateSliderBarR2()
        updateSliderBarRsensor()
        updateSliderBarCsensor()
        updateValueR0()
        updateValueR1()
        updateValueL1()
        updateValueC1()
        updateValuek()
        updateValueR2()
        updateValueL2()
        updateValueC2()
        updateValueRsensor()
        updateValueCsensor()
        update_graph()

    '''
    def __init__(self, spectrum):
        # Initializes GUI
        super().__init__()
        self.ui = Ui_MainAnalysisCoupledAntennasWindow()
        self.ui.setupUi(self)
        self.addToolBar(NavigationToolbar(self.ui.MplWidget4.canvas, self))
        # set up actions for GUI widgets
        self.slidersResolution = self.ui.horizontalSliderR0.maximum()
        self.ui.horizontalSliderR0.sliderMoved.connect(self.updateValueR0)
        self.ui.horizontalSliderR1.sliderMoved.connect(self.updateValueR1)
        self.ui.horizontalSliderL1.sliderMoved.connect(self.updateValueL1)
        self.ui.horizontalSliderC1.sliderMoved.connect(self.updateValueC1)
        self.ui.horizontalSliderk.sliderMoved.connect(self.updateValuek)
        self.ui.horizontalSliderR2.sliderMoved.connect(self.updateValueR2)
        self.ui.horizontalSliderL2.sliderMoved.connect(self.updateValueL2)
        self.ui.horizontalSliderC2.sliderMoved.connect(self.updateValueC2)
        self.ui.horizontalSliderRsensor.sliderMoved.connect(
            self.updateValueRsensor)
        self.ui.horizontalSliderCsensor.sliderMoved.connect(
            self.updateValueCsensor)
        self.ui.lineEditValueR0.returnPressed.connect(self.updateSliderBarR0)
        self.ui.lineEditMaxR0.returnPressed.connect(self.updateSliderBarR0)
        self.ui.lineEditMinR0.returnPressed.connect(self.updateSliderBarR0)
        self.ui.lineEditValueR1.returnPressed.connect(self.updateSliderBarR1)
        self.ui.lineEditMaxR1.returnPressed.connect(self.updateSliderBarR1)
        self.ui.lineEditMinR1.returnPressed.connect(self.updateSliderBarR1)
        self.ui.lineEditValueL1.returnPressed.connect(self.updateSliderBarL1)
        self.ui.lineEditMaxL1.returnPressed.connect(self.updateSliderBarL1)
        self.ui.lineEditMinL1.returnPressed.connect(self.updateSliderBarL1)
        self.ui.lineEditValueC1.returnPressed.connect(self.updateSliderBarC1)
        self.ui.lineEditMaxC1.returnPressed.connect(self.updateSliderBarC1)
        self.ui.lineEditMinC1.returnPressed.connect(self.updateSliderBarC1)
        self.ui.lineEditValuek.returnPressed.connect(self.updateSliderBark)
        self.ui.lineEditMaxk.returnPressed.connect(self.updateSliderBark)
        self.ui.lineEditMink.returnPressed.connect(self.updateSliderBark)
        self.ui.lineEditValueR2.returnPressed.connect(self.updateSliderBarR2)
        self.ui.lineEditMaxR2.returnPressed.connect(self.updateSliderBarR2)
        self.ui.lineEditMinR2.returnPressed.connect(self.updateSliderBarR2)
        self.ui.lineEditValueL2.returnPressed.connect(self.updateSliderBarL2)
        self.ui.lineEditMaxL2.returnPressed.connect(self.updateSliderBarL2)
        self.ui.lineEditMinL2.returnPressed.connect(self.updateSliderBarL2)
        self.ui.lineEditValueC2.returnPressed.connect(self.updateSliderBarC2)
        self.ui.lineEditMaxC2.returnPressed.connect(self.updateSliderBarC2)
        self.ui.lineEditMinC2.returnPressed.connect(self.updateSliderBarC2)
        self.ui.lineEditValueRsensor.returnPressed.connect(
            self.updateSliderBarRsensor)
        self.ui.lineEditMaxRsensor.returnPressed.connect(
            self.updateSliderBarRsensor)
        self.ui.lineEditMinRsensor.returnPressed.connect(
            self.updateSliderBarRsensor)
        self.ui.lineEditValueCsensor.returnPressed.connect(
            self.updateSliderBarCsensor)
        self.ui.lineEditMaxCsensor.returnPressed.connect(
            self.updateSliderBarCsensor)
        self.ui.lineEditMinCsensor.returnPressed.connect(
            self.updateSliderBarCsensor)
        self.ui.pushButtonFit.clicked.connect(self.doFitData)
        # Initializes attributes
        self.spectrum = spectrum
        self.fittedSpectrum = calculatedCoupledAntennasSpectrum(
            self.spectrum.getFreq(),
            float(self.ui.lineEditValueR0.text()),
            float(self.ui.lineEditValueR1.text()),
            float(self.ui.lineEditValueL1.text()),
            float(self.ui.lineEditValueC1.text()),
            float(self.ui.lineEditValueR2.text()),
            float(self.ui.lineEditValueL2.text()),
            float(self.ui.lineEditValueC2.text()),
            float(self.ui.lineEditValueRsensor.text()),
            float(self.ui.lineEditValueCsensor.text()),
            float(self.ui.lineEditValuek.text())
        )
        # Update values of slide bars
        self.updateSliderBarR0()
        self.updateSliderBarR1()
        self.updateSliderBarL1()
        self.updateSliderBarC1()
        self.updateSliderBark()
        self.updateSliderBarL2()
        self.updateSliderBarC2()
        self.updateSliderBarR2()
        self.updateSliderBarRsensor()
        self.updateSliderBarCsensor()
        # Plot experimental and fitted data
        self.update_graph()

    # --------- Methods for updating slide bar positions --------
    def updateSliderBarR0(self):
        self.ui.horizontalSliderR0.setValue(
            (float(self.ui.lineEditValueR0.text()) -
             float(self.ui.lineEditMinR0.text())) *
            self.slidersResolution /
            (float(self.ui.lineEditMaxR0.text()) -
             float(self.ui.lineEditMinR0.text())))

    def updateSliderBarR1(self):
        self.ui.horizontalSliderR1.setValue(
            (float(self.ui.lineEditValueR1.text()) -
             float(self.ui.lineEditMinR1.text())) *
            self.slidersResolution /
            (float(self.ui.lineEditMaxR1.text()) -
             float(self.ui.lineEditMinR1.text())))

    def updateSliderBarL1(self):
        self.ui.horizontalSliderL1.setValue(
            (float(self.ui.lineEditValueL1.text()) -
             float(self.ui.lineEditMinL1.text())) *
            self.slidersResolution /
            (float(self.ui.lineEditMaxL1.text()) -
             float(self.ui.lineEditMinL1.text())))

    def updateSliderBarC1(self):
        self.ui.horizontalSliderC1.setValue(
            (float(self.ui.lineEditValueC1.text()) -
             float(self.ui.lineEditMinC1.text())) *
            self.slidersResolution /
            (float(self.ui.lineEditMaxC1.text()) -
             float(self.ui.lineEditMinC1.text())))

    def updateSliderBark(self):
        self.ui.horizontalSliderk.setValue(
            (float(self.ui.lineEditValuek.text()) -
             float(self.ui.lineEditMink.text())) *
            self.slidersResolution /
            (float(self.ui.lineEditMaxk.text()) -
             float(self.ui.lineEditMink.text())))

    def updateSliderBarR2(self):
        self.ui.horizontalSliderR2.setValue(
            (float(self.ui.lineEditValueR2.text()) -
             float(self.ui.lineEditMinR2.text())) *
            self.slidersResolution /
            (float(self.ui.lineEditMaxR2.text()) -
             float(self.ui.lineEditMinR2.text())))

    def updateSliderBarL2(self):
        self.ui.horizontalSliderL2.setValue(
            (float(self.ui.lineEditValueL2.text()) -
             float(self.ui.lineEditMinL2.text())) *
            self.slidersResolution /
            (float(self.ui.lineEditMaxL2.text()) -
             float(self.ui.lineEditMinL2.text())))

    def updateSliderBarC2(self):
        self.ui.horizontalSliderC2.setValue(
            (float(self.ui.lineEditValueC2.text()) -
             float(self.ui.lineEditMinC2.text())) *
            self.slidersResolution /
            (float(self.ui.lineEditMaxC2.text()) -
             float(self.ui.lineEditMinC2.text())))

    def updateSliderBarRsensor(self):
        self.ui.horizontalSliderRsensor.setValue(
            (float(self.ui.lineEditValueRsensor.text()) -
             float(self.ui.lineEditMinRsensor.text())) *
            self.slidersResolution /
            (float(self.ui.lineEditMaxRsensor.text()) -
             float(self.ui.lineEditMinRsensor.text())))

    def updateSliderBarCsensor(self):
        self.ui.horizontalSliderCsensor.setValue(
            (float(self.ui.lineEditValueCsensor.text()) -
             float(self.ui.lineEditMinCsensor.text())) *
            self.slidersResolution /
            (float(self.ui.lineEditMaxCsensor.text()) -
             float(self.ui.lineEditMinCsensor.text())))

    def doFitData(self):
        '''Fitting of experimental impedance data to
        theoretical expression'''
        # Parameters are created for the fit as required by lmfit
        params = Parameters()
        params.add('R0', value=float(self.ui.lineEditValueR0.text()),
                   min=float(self.ui.lineEditMinR0.text()),
                   max=float(self.ui.lineEditMaxR0.text()))
        params.add('R1', value=float(self.ui.lineEditValueR1.text()),
                   min=float(self.ui.lineEditMinR1.text()),
                   max=float(self.ui.lineEditMaxR1.text()))
        params.add('L1', value=float(self.ui.lineEditValueL1.text()),
                   min=float(self.ui.lineEditMinL1.text()),
                   max=float(self.ui.lineEditMaxL1.text()))
        params.add('C1', value=float(self.ui.lineEditValueC1.text()),
                   min=float(self.ui.lineEditMinC1.text()),
                   max=float(self.ui.lineEditMaxC1.text()))
        params.add('k', value=float(self.ui.lineEditValuek.text()),
                   min=float(self.ui.lineEditMink.text()),
                   max=float(self.ui.lineEditMaxk.text()))
        params.add('R2', value=float(self.ui.lineEditValueR2.text()),
                   min=float(self.ui.lineEditMinR2.text()),
                   max=float(self.ui.lineEditMaxR2.text()))
        params.add('L2', value=float(self.ui.lineEditValueL2.text()),
                   min=float(self.ui.lineEditMinL2.text()),
                   max=float(self.ui.lineEditMaxL2.text()))
        params.add('C2', value=float(self.ui.lineEditValueC2.text()),
                   min=float(self.ui.lineEditMinC2.text()),
                   max=float(self.ui.lineEditMaxC2.text()))
        params.add('Rsensor', value=float(self.ui.lineEditValueRsensor.text()),
                   min=float(self.ui.lineEditMinRsensor.text()),
                   max=float(self.ui.lineEditMaxRsensor.text()))
        params.add('Csensor', value=float(self.ui.lineEditValueCsensor.text()),
                   min=float(self.ui.lineEditMinCsensor.text()),
                   max=float(self.ui.lineEditMaxCsensor.text()))

        # Checkboxes for fitting parameters in the GUI are checked,
        # and their fittability established accordingly
        if self.ui.radioButtonFitR0.isChecked():
            params['R0'].vary = True
        else:
            params['R0'].vary = False
        if self.ui.radioButtonFitR1.isChecked():
            params['R1'].vary = True
        else:
            params['R1'].vary = False
        if self.ui.radioButtonFitL1.isChecked():
            params['L1'].vary = True
        else:
            params['L1'].vary = False
        if self.ui.radioButtonFitC1.isChecked():
            params['C1'].vary = True
        else:
            params['C1'].vary = False
        if self.ui.radioButtonFitk.isChecked():
            params['k'].vary = True
        else:
            params['k'].vary = False
        if self.ui.radioButtonFitR2.isChecked():
            params['R2'].vary = True
        else:
            params['R2'].vary = False
        if self.ui.radioButtonFitL2.isChecked():
            params['L2'].vary = True
        else:
            params['L2'].vary = False
        if self.ui.radioButtonFitC2.isChecked():
            params['C2'].vary = True
        else:
            params['C2'].vary = False
        if self.ui.radioButtonFitRsensor.isChecked():
            params['Rsensor'].vary = True
        else:
            params['Rsensor'].vary = False
        if self.ui.radioButtonFitCsensor.isChecked():
            params['Csensor'].vary = True
        else:
            params['Csensor'].vary = False

        # perform the actual fit
        result = minimize(
            residualFittingCoupledAntennas, params,
            method='powell',
            args=(self.spectrum.getFreq(), self.spectrum.getReZ()*50,
                  self.spectrum.getImZ()*50
            )
        )

        # Update parameters with those found in the fit
        self.fittedSpectrum.setR0(result.params['R0'].value)
        self.fittedSpectrum.setR1(result.params['R1'].value)
        self.fittedSpectrum.setL1(result.params['L1'].value)
        self.fittedSpectrum.setC1(result.params['C1'].value)
        self.fittedSpectrum.setR2(result.params['R2'].value)
        self.fittedSpectrum.setL2(result.params['L2'].value)
        self.fittedSpectrum.setRsensor(result.params['Rsensor'].value)
        self.fittedSpectrum.setCsensor(result.params['Csensor'].value)
        self.fittedSpectrum.setk(result.params['k'].value)

        # Recalculate impedance and S11 values from parameters foun in the fit
        self.fittedSpectrum.calculateImpedanceCoupledAntennas()
        self.fittedSpectrum.calculateS11()

        # Update values of slide bars
        self.updateSliderBarR0()
        self.updateSliderBarR1()
        self.updateSliderBarL1()
        self.updateSliderBarC1()
        self.updateSliderBark()
        self.updateSliderBarL2()
        self.updateSliderBarC2()
        self.updateSliderBarR2()
        self.updateSliderBarRsensor()
        self.updateSliderBarCsensor()

        # Update graph
        self.update_graph()

        # Update fit parameter values in the GUI with those found in the fit
        self.ui.lineEditValueR0.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getR0()))
        self.ui.lineEditValueR1.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getR1()))
        self.ui.lineEditValueL1.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getL1()))
        self.ui.lineEditValueC1.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getC1()))
        self.ui.lineEditValueR2.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getR2()))
        self.ui.lineEditValueL2.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getL2()))
        self.ui.lineEditValueC2.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getC2()))
        self.ui.lineEditValueRsensor.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getRsensor()))
        self.ui.lineEditValueCsensor.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getCsensor()))
        self.ui.lineEditValuek.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getk()))

    def updateValueR0(self, value):
        self.fittedSpectrum.setR0(float(
            self.ui.lineEditMinR0.text()) + value * (
                float(self.ui.lineEditMaxR0.text()) - float(
                    self.ui.lineEditMinR0.text())) / self.slidersResolution)
        self.ui.lineEditValueR0.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getR0()))
        self.fittedSpectrum.calculateImpedanceCoupledAntennas()
        self.fittedSpectrum.calculateS11()
        self.update_graph()

    def updateValueR1(self, value):
        self.fittedSpectrum.setR1(float(
            self.ui.lineEditMinR1.text()) + value * (
                float(self.ui.lineEditMaxR1.text()) - float(
                    self.ui.lineEditMinR1.text())) / self.slidersResolution)
        self.ui.lineEditValueR1.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getR1()))
        self.fittedSpectrum.calculateImpedanceCoupledAntennas()
        self.fittedSpectrum.calculateS11()
        self.update_graph()

    def updateValueL1(self, value):
        self.fittedSpectrum.setL1(float(
            self.ui.lineEditMinL1.text()) + value * (
                float(self.ui.lineEditMaxL1.text()) - float(
                    self.ui.lineEditMinL1.text())) / self.slidersResolution)
        self.ui.lineEditValueL1.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getL1()))
        self.fittedSpectrum.calculateImpedanceCoupledAntennas()
        self.fittedSpectrum.calculateS11()
        self.update_graph()

    def updateValueC1(self, value):
        self.fittedSpectrum.setC1(float(
            self.ui.lineEditMinC1.text()) + value * (
                float(self.ui.lineEditMaxC1.text()) - float(
                    self.ui.lineEditMinC1.text())) / self.slidersResolution)
        self.ui.lineEditValueC1.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getC1()))
        self.fittedSpectrum.calculateImpedanceCoupledAntennas()
        self.fittedSpectrum.calculateS11()
        self.update_graph()

    def updateValueR2(self, value):
        self.fittedSpectrum.setR2(float(
            self.ui.lineEditMinR2.text()) + value * (
                float(self.ui.lineEditMaxR2.text()) - float(
                    self.ui.lineEditMinR2.text())) / self.slidersResolution)
        self.ui.lineEditValueR2.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getR2()))
        self.fittedSpectrum.calculateImpedanceCoupledAntennas()
        self.fittedSpectrum.calculateS11()
        self.update_graph()

    def updateValueL2(self, value):
        self.fittedSpectrum.setL2(float(self.ui.lineEditMinL2.text()) + value * (
            float(self.ui.lineEditMaxL2.text()) - float(
                self.ui.lineEditMinL2.text())) / self.slidersResolution)
        self.ui.lineEditValueL2.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getL2()))
        self.fittedSpectrum.calculateImpedanceCoupledAntennas()
        self.fittedSpectrum.calculateS11()
        self.update_graph()

    def updateValueC2(self, value):
        self.fittedSpectrum.setC2(float(
            self.ui.lineEditMinC2.text()) + value * (
                float(self.ui.lineEditMaxC2.text()) - float(
                    self.ui.lineEditMinC2.text())) / self.slidersResolution)
        self.ui.lineEditValueC2.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getC2()))
        self.fittedSpectrum.calculateImpedanceCoupledAntennas()
        self.fittedSpectrum.calculateS11()
        self.update_graph()

    def updateValueRsensor(self, value):
        self.fittedSpectrum.setRsensor(float(
            self.ui.lineEditMinRsensor.text()) + value * (
                float(self.ui.lineEditMaxRsensor.text()) - float(
                    self.ui.lineEditMinRsensor.text())) / self.slidersResolution)
        self.ui.lineEditValueRsensor.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getRsensor()))
        self.fittedSpectrum.calculateImpedanceCoupledAntennas()
        self.fittedSpectrum.calculateS11()
        self.update_graph()

    def updateValueCsensor(self, value):
        self.fittedSpectrum.setCsensor(float(
            self.ui.lineEditMinCsensor.text()) + value * (float(
                self.ui.lineEditMaxCsensor.text()) - float(
                    self.ui.lineEditMinCsensor.text())) / self.slidersResolution)
        self.ui.lineEditValueCsensor.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getCsensor()))
        self.fittedSpectrum.calculateImpedanceCoupledAntennas()
        self.fittedSpectrum.calculateS11()
        self.update_graph()

    def updateValuek(self, value):
        self.fittedSpectrum.setk(float(
            self.ui.lineEditMink.text()) + value * (
                float(self.ui.lineEditMaxk.text()) - float(
                    self.ui.lineEditMink.text())) / self.slidersResolution)
        self.ui.lineEditValuek.setText("{0:0.2e}".format(self.fittedSpectrum.getk()))
        self.fittedSpectrum.calculateImpedanceCoupledAntennas()
        self.fittedSpectrum.calculateS11()
        self.update_graph()

    def update_graph(self):
        self.ui.MplWidget4.canvas.axes1.clear()
        self.ui.MplWidget4.canvas.axes1.plot(
            self.spectrum.getFreq(), self.spectrum.getReZ()*50)
        self.ui.MplWidget4.canvas.axes1.plot(
            self.fittedSpectrum.getFreq(), self.fittedSpectrum.getReZ(), 'r--')
        self.ui.MplWidget4.canvas.axes1.set_ylabel("Re Z")
        self.ui.MplWidget4.canvas.axes1.set_xlabel("f (MHz)")
        self.ui.MplWidget4.canvas.axes1.set_xlim(
            float(self.ui.lineEditValueFmin.text()),
            float(self.ui.lineEditValueFmax.text()))
        self.ui.MplWidget4.canvas.axes2.clear()
        self.ui.MplWidget4.canvas.axes2.plot(
            self.spectrum.getFreq(), self.spectrum.getImZ()*50)
        self.ui.MplWidget4.canvas.axes2.plot(
            self.fittedSpectrum.getFreq(), self.fittedSpectrum.getImZ(), 'r--')
        self.ui.MplWidget4.canvas.axes2.set_ylabel("Im Z")
        self.ui.MplWidget4.canvas.axes2.set_xlabel("f (MHz)")
        self.ui.MplWidget4.canvas.axes2.set_xlim(
            float(self.ui.lineEditValueFmin.text()),
            float(self.ui.lineEditValueFmax.text()))
        self.ui.MplWidget4.canvas.axes3.clear()
        self.ui.MplWidget4.canvas.axes3.plot(
            self.spectrum.getFreq(), self.spectrum.getModS11())
        self.ui.MplWidget4.canvas.axes3.plot(
            self.fittedSpectrum.getFreq(), self.fittedSpectrum.getModS11(), 'r--')
        self.ui.MplWidget4.canvas.axes3.set_ylabel("Mod S11")
        self.ui.MplWidget4.canvas.axes3.set_xlabel("f (MHz)")
        self.ui.MplWidget4.canvas.axes3.set_xlim(
            float(self.ui.lineEditValueFmin.text()),
            float(self.ui.lineEditValueFmax.text()))
        self.ui.MplWidget4.canvas.axes4.clear()
        self.ui.MplWidget4.canvas.axes4.plot(
            self.spectrum.getReZ()*50, self.spectrum.getImZ()*50)
        self.ui.MplWidget4.canvas.axes4.plot(
            self.fittedSpectrum.getReZ(), self.fittedSpectrum.getImZ(), 'r--')
        self.ui.MplWidget4.canvas.axes4.set_ylabel("Im Z")
        self.ui.MplWidget4.canvas.axes4.set_xlabel("ReZ")
        self.ui.MplWidget4.canvas.figure.tight_layout()
        self.ui.MplWidget4.canvas.draw()

