"""
Definition of class to create the coupled antennas analysis GUI
from the Qt5 created template from coupledAntennasAnalysisWindow_v0
"""

from PyQt5.QtWidgets import QMainWindow
from matplotlib.backends.backend_qt5agg import (
    NavigationToolbar2QT as NavigationToolbar)
from numpy import abs
from lmfit import minimize, Parameters
# local imports
from ..qt5_ui_files.coupledAntennasAnalysisWindow_v0 import (
        Ui_MainAnalysisCoupledAntennasWindow)
from .definition_class_coupled_antennas_spectrum import (
    calculatedCoupledAntennasSpectrum)
from ..local_functions.definition_local_functions import (
    residualFittingCoupledAntennas, residualFittingCoupledAntennas2)


class myCoupledAntennasGUI(QMainWindow):
    ''' class for coupled antennas analysis GUIs

    Attributes:
        ui
        slidersResolution
        spectrum
        currentFileIndex
        numberOfFiles
        fittedSpectrum

    Methods:
        __init__()
        doFitData()
        R0ToAll()
        R1ToAll()
        L1ToAll()
        C1ToAll()
        kToAll()
        R2ToAll()
        L2ToAll()
        C2ToAll()
        RsensorToAll()
        CsensorToAll()
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
        updateValuesInEditBoxes()
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
        doPreviousFile
        doNextFile

    '''
    def __init__(self, spectrum, current_file_index, number_of_files):

        # Initializes GUI
        super().__init__()
        self.ui = Ui_MainAnalysisCoupledAntennasWindow()
        self.ui.setupUi(self)
        self.addToolBar(NavigationToolbar(self.ui.MplWidget4.canvas, self))

        # set the value of the attribute "slidersResolution" to thei
        # maximum value of ui.horizontalSliderR0, this would need to
        # be improved in newer versions
        self.slidersResolution = self.ui.horizontalSliderR0.maximum()

        ################################
        # set up actions for GUI widgets
        ################################

        # Actions to be taken when moving the slidebars
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

        # Actions to be taken when modifying the values of the
        # "Value, Min and Max Edit Boxes" and pressing Return
        self.ui.lineEditValueR0.returnPressed.connect(
            self.changedLineEditValueR0)
        self.ui.lineEditMaxR0.returnPressed.connect(self.updateSliderBarR0)
        self.ui.lineEditMinR0.returnPressed.connect(self.updateSliderBarR0)
        self.ui.lineEditValueR1.returnPressed.connect(
            self.changedLineEditValueR1)
        self.ui.lineEditMaxR1.returnPressed.connect(self.updateSliderBarR1)
        self.ui.lineEditMinR1.returnPressed.connect(self.updateSliderBarR1)
        self.ui.lineEditValueL1.returnPressed.connect(
            self.changedLineEditValueL1)
        self.ui.lineEditMaxL1.returnPressed.connect(self.updateSliderBarL1)
        self.ui.lineEditMinL1.returnPressed.connect(self.updateSliderBarL1)
        self.ui.lineEditValueC1.returnPressed.connect(
            self.changedLineEditValueC1)
        self.ui.lineEditMaxC1.returnPressed.connect(self.updateSliderBarC1)
        self.ui.lineEditMinC1.returnPressed.connect(self.updateSliderBarC1)
        self.ui.lineEditValuek.returnPressed.connect(
            self.changedLineEditValuek)
        self.ui.lineEditMaxk.returnPressed.connect(self.updateSliderBark)
        self.ui.lineEditMink.returnPressed.connect(self.updateSliderBark)
        self.ui.lineEditValueR2.returnPressed.connect(
            self.changedLineEditValueR2)
        self.ui.lineEditMaxR2.returnPressed.connect(self.updateSliderBarR2)
        self.ui.lineEditMinR2.returnPressed.connect(self.updateSliderBarR2)
        self.ui.lineEditValueL2.returnPressed.connect(
            self.changedLineEditValueL2)
        self.ui.lineEditMaxL2.returnPressed.connect(self.updateSliderBarL2)
        self.ui.lineEditMinL2.returnPressed.connect(self.updateSliderBarL2)
        self.ui.lineEditValueC2.returnPressed.connect(
            self.changedLineEditValueC2)
        self.ui.lineEditMaxC2.returnPressed.connect(self.updateSliderBarC2)
        self.ui.lineEditMinC2.returnPressed.connect(self.updateSliderBarC2)
        self.ui.lineEditValueRsensor.returnPressed.connect(
            self.changedLineEditValueRsensor)
        self.ui.lineEditMaxRsensor.returnPressed.connect(
            self.updateSliderBarRsensor)
        self.ui.lineEditMinRsensor.returnPressed.connect(
            self.updateSliderBarRsensor)
        self.ui.lineEditValueCsensor.returnPressed.connect(
            self.changedLineEditValueCsensor)
        self.ui.lineEditMaxCsensor.returnPressed.connect(
            self.updateSliderBarCsensor)
        self.ui.lineEditMinCsensor.returnPressed.connect(
            self.updateSliderBarCsensor)

        # Actions to be taken when pressing the "Apply to All" Push Buttons
        self.ui.pushButtonR0ToAll.clicked.connect(self.R0ToAll)
        self.ui.pushButtonR1ToAll.clicked.connect(self.R1ToAll)
        self.ui.pushButtonL1ToAll.clicked.connect(self.L1ToAll)
        self.ui.pushButtonC1ToAll.clicked.connect(self.C1ToAll)
        self.ui.pushButtonkToAll.clicked.connect(self.kToAll)
        self.ui.pushButtonR2ToAll.clicked.connect(self.R2ToAll)
        self.ui.pushButtonL2ToAll.clicked.connect(self.L2ToAll)
        self.ui.pushButtonC2ToAll.clicked.connect(self.C2ToAll)
        self.ui.pushButtonRsensorToAll.clicked.connect(self.RsensorToAll)
        self.ui.pushButtonCsensorToAll.clicked.connect(self.CsensorToAll)

        # Action to be taken when pressing the Fit Push Button
        self.ui.pushButtonFit.clicked.connect(self.doFitData)

        # Actions to be taken when pressing the Push Buttons
        # Previous and Next File
        self.ui.pushButtonPreviousFile.clicked.connect(self.doPreviousFile)
        self.ui.pushButtonNextFile.clicked.connect(self.doNextFile)

        # Initialization of class attributes
        self.spectrum = spectrum
        self. currentFileIndex = current_file_index
        self.numberOfFiles = number_of_files
        self.fittedSpectrum = []
        for i in range(self.numberOfFiles):
            self.fittedSpectrum.append(calculatedCoupledAntennasSpectrum(
                self.spectrum[i].getFreq(),
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

    ###########################################################################
    # Actions to be taken when pressing the "Apply to All" Push Buttons
    ###########################################################################

    def R0ToAll(self):
        R0 = self.fittedSpectrum[self.currentFileIndex].getR0()
        for i in range(len(self.fittedSpectrum)):
            self.fittedSpectrum[i].setR0(R0)

    def R1ToAll(self):
        R1 = self.fittedSpectrum[self.currentFileIndex].getR1()
        for i in range(len(self.fittedSpectrum)):
            self.fittedSpectrum[i].setR1(R1)

    def L1ToAll(self):
        L1 = self.fittedSpectrum[self.currentFileIndex].getL1()
        for i in range(len(self.fittedSpectrum)):
            self.fittedSpectrum[i].setL1(L1)

    def C1ToAll(self):
        C1 = self.fittedSpectrum[self.currentFileIndex].getC1()
        for i in range(len(self.fittedSpectrum)):
            self.fittedSpectrum[i].setC1(C1)

    def kToAll(self):
        k = self.fittedSpectrum[self.currentFileIndex].getk()
        for i in range(len(self.fittedSpectrum)):
            self.fittedSpectrum[i].setk(k)

    def R2ToAll(self):
        R2 = self.fittedSpectrum[self.currentFileIndex].getR2()
        for i in range(len(self.fittedSpectrum)):
            self.fittedSpectrum[i].setR2(R2)

    def L2ToAll(self):
        L2 = self.fittedSpectrum[self.currentFileIndex].getL2()
        for i in range(len(self.fittedSpectrum)):
            self.fittedSpectrum[i].setL2(L2)

    def C2ToAll(self):
        C2 = self.fittedSpectrum[self.currentFileIndex].getC2()
        for i in range(len(self.fittedSpectrum)):
            self.fittedSpectrum[i].setC2(C2)

    def RsensorToAll(self):
        Rsensor = self.fittedSpectrum[self.currentFileIndex].getRsensor()
        for i in range(len(self.fittedSpectrum)):
            self.fittedSpectrum[i].setRsensor(Rsensor)

    def CsensorToAll(self):
        Csensor = self.fittedSpectrum[self.currentFileIndex].getCsensor()
        for i in range(len(self.fittedSpectrum)):
            self.fittedSpectrum[i].setCsensor(Csensor)

    ##########################################################################
    #       Methods for visualizing different data files
    ##########################################################################

    def doPreviousFile(self):
        '''
        Visualization of data corresponding to previous file
        '''
        if self.currentFileIndex > 0:
            # if the index for the data file is not the lowest,
            # decrease it by one
            self.currentFileIndex -= 1

            # Updates attribute values in "Value Edit Boxes" with those
            # corresponding to fittedspectrum[New File Index]
            self.updateValuesInEditBoxes()

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

    def doNextFile(self):
        '''
        Visualization of data corresponding to next file
        '''
        if self.currentFileIndex < self.numberOfFiles-1:
            # if the index for the data file is not the highest,
            # increase it by one
            self.currentFileIndex += 1

            # Updates attribute values in "Value Edit Boxes" with those
            # corresponding to fittedspectrum[New File Index]
            self.updateValuesInEditBoxes()

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

            # Plots data corresponding to the new visualized data file
            self.update_graph()

    ###########################################################################
    #       Methods for actions to be taken when the values in the attribute
    #       edit boxes are changed
    ###########################################################################

    def changedLineEditValueR0(self):
        if float(self.ui.lineEditValueR0.text()) > float(
                self.ui.lineEditMaxR0.text()):
            self.ui.lineEditValueR0.setText(
                    self.ui.lineEditMaxR0.text())
        elif float(self.ui.lineEditValueR0.text()) < float(
                self.ui.lineEditMinR0.text()):
            self.ui.lineEditValueR0.setText(self.ui.lineEditMinR0.text())
        self.fittedSpectrum[self.currentFileIndex].setR0(
            float(self.ui.lineEditValueR0.text()))
        # Update and plot Fitted Spectrum with new data
        self.updateFittedSpetrum()

    def changedLineEditValueR1(self):
        if float(self.ui.lineEditValueR1.text()) > float(
                self.ui.lineEditMaxR1.text()):
            self.ui.lineEditValueR1.setText(
                    self.ui.lineEditMaxR1.text())
        elif float(self.ui.lineEditValueR1.text()) < float(
                self.ui.lineEditMinR1.text()):
            self.ui.lineEditValueR1.setText(self.ui.lineEditMinR1.text())
        self.fittedSpectrum[self.currentFileIndex].setR1(
            float(self.ui.lineEditValueR1.text()))
        # Update and plot Fitted Spectrum with new data
        self.updateFittedSpetrum()

    def changedLineEditValueL1(self):
        if float(self.ui.lineEditValueL1.text()) > float(
                self.ui.lineEditMaxL1.text()):
            self.ui.lineEditValueL1.setText(
                    self.ui.lineEditMaxL1.text())
        elif float(self.ui.lineEditValueL1.text()) < float(
                self.ui.lineEditMinL1.text()):
            self.ui.lineEditValueL1.setText(self.ui.lineEditMinL1.text())
        self.fittedSpectrum[self.currentFileIndex].setL1(
            float(self.ui.lineEditValueL1.text()))
        # Update and plot Fitted Spectrum with new data
        self.updateFittedSpetrum()

    def changedLineEditValueC1(self):
        if float(self.ui.lineEditValueC1.text()) > float(
                self.ui.lineEditMaxC1.text()):
            self.ui.lineEditValueC1.setText(
                    self.ui.lineEditMaxC1.text())
        elif float(self.ui.lineEditValueC1.text()) < float(
                self.ui.lineEditMinC1.text()):
            self.ui.lineEditValueC1.setText(self.ui.lineEditMinC1.text())
        self.fittedSpectrum[self.currentFileIndex].setC1(
            float(self.ui.lineEditValueC1.text()))
        # Update and plot Fitted Spectrum with new data
        self.updateFittedSpetrum()

    def changedLineEditValuek(self):
        if float(self.ui.lineEditValuek.text()) > float(
                self.ui.lineEditMaxk.text()):
            self.ui.lineEditValuek.setText(
                    self.ui.lineEditMaxk.text())
        elif float(self.ui.lineEditValuek.text()) < float(
                self.ui.lineEditMink.text()):
            self.ui.lineEditValuek.setText(self.ui.lineEditMink.text())
        self.fittedSpectrum[self.currentFileIndex].setk(
            float(self.ui.lineEditValuek.text()))
        # Update and plot Fitted Spectrum with new data
        self.updateFittedSpetrum()

    def changedLineEditValueR2(self):
        if float(self.ui.lineEditValueR2.text()) > float(
                self.ui.lineEditMaxR2.text()):
            self.ui.lineEditValueR2.setText(
                    self.ui.lineEditMaxR2.text())
        elif float(self.ui.lineEditValueR2.text()) < float(
                self.ui.lineEditMinR2.text()):
            self.ui.lineEditValueR2.setText(self.ui.lineEditMinR2.text())
        self.fittedSpectrum[self.currentFileIndex].setR2(
            float(self.ui.lineEditValueR2.text()))
        # Update and plot Fitted Spectrum with new data
        self.updateFittedSpetrum()

    def changedLineEditValueL2(self):
        if float(self.ui.lineEditValueL2.text()) > float(
                self.ui.lineEditMaxL2.text()):
            self.ui.lineEditValueL2.setText(
                    self.ui.lineEditMaxL2.text())
        elif float(self.ui.lineEditValueL2.text()) < float(
                self.ui.lineEditMinL2.text()):
            self.ui.lineEditValueL2.setText(self.ui.lineEditMinL2.text())
        self.fittedSpectrum[self.currentFileIndex].setL2(
            float(self.ui.lineEditValueL2.text()))
        # Update and plot Fitted Spectrum with new data
        self.updateFittedSpetrum()

    def changedLineEditValueC2(self):
        if float(self.ui.lineEditValueC2.text()) > float(
                self.ui.lineEditMaxC2.text()):
            self.ui.lineEditValueC2.setText(
                    self.ui.lineEditMaxC2.text())
        elif float(self.ui.lineEditValueC2.text()) < float(
                self.ui.lineEditMinC2.text()):
            self.ui.lineEditValueC2.setText(
                self.ui.lineEditMinC2.text())
        self.fittedSpectrum[self.currentFileIndex].setC2(
            float(self.ui.lineEditValueC2.text()))
        # Update and plot Fitted Spectrum with new data
        self.updateFittedSpetrum()

    def changedLineEditValueRsensor(self):
        if float(self.ui.lineEditValueRsensor.text()) > float(
                self.ui.lineEditMaxRsensor.text()):
            self.ui.lineEditValueRsensor.setText(
                    self.ui.lineEditMaxRsensor.text())
        elif float(self.ui.lineEditValueRsensor.text()) < float(
                self.ui.lineEditMinRsensor.text()):
            self.ui.lineEditValueRsensor.setText(
                self.ui.lineEditMinRsensor.text())
        self.fittedSpectrum[self.currentFileIndex].setRsensor(
            float(self.ui.lineEditValueRsensor.text()))
        # Update and plot Fitted Spectrum with new data
        self.updateFittedSpetrum()

    def changedLineEditValueCsensor(self):
        if float(self.ui.lineEditValueCsensor.text()) > float(
                self.ui.lineEditMaxCsensor.text()):
            self.ui.lineEditValueCsensor.setText(
                self.ui.lineEditMaxCsensor.text())
        elif float(self.ui.lineEditValueCsensor.text()) < float(
                self.ui.lineEditMinCsensor.text()):
            self.ui.lineEditValueCsensor.setText(
                self.ui.lineEditMinCsensor.text())
        self.fittedSpectrum[self.currentFileIndex].setCsensor(
            float(self.ui.lineEditValueCsensor.text()))
        # Update and plot Fitted Spectrum with new data
        self.updateFittedSpetrum()

    ###########################################################################
    #       Methods for updating slide bar positions
    ###########################################################################

    def updateSliderBarR0(self):
        '''
        Updates position of R0 slide bar
        '''
        self.ui.horizontalSliderR0.setValue(
            (float(self.ui.lineEditValueR0.text()) -
             float(self.ui.lineEditMinR0.text())) *
            self.slidersResolution /
            (float(self.ui.lineEditMaxR0.text()) -
             float(self.ui.lineEditMinR0.text())))

    def updateSliderBarR1(self):
        '''
        Updates position of R1 slide bar
        '''
        self.ui.horizontalSliderR1.setValue(
            (float(self.ui.lineEditValueR1.text()) -
             float(self.ui.lineEditMinR1.text())) *
            self.slidersResolution /
            (float(self.ui.lineEditMaxR1.text()) -
             float(self.ui.lineEditMinR1.text())))

    def updateSliderBarL1(self):
        '''
        Updates position of L1 slide bar
        '''
        self.ui.horizontalSliderL1.setValue(
            (float(self.ui.lineEditValueL1.text()) -
             float(self.ui.lineEditMinL1.text())) *
            self.slidersResolution /
            (float(self.ui.lineEditMaxL1.text()) -
             float(self.ui.lineEditMinL1.text())))

    def updateSliderBarC1(self):
        '''
        Updates position of C1 slide bar
        '''
        self.ui.horizontalSliderC1.setValue(
            (float(self.ui.lineEditValueC1.text()) -
             float(self.ui.lineEditMinC1.text())) *
            self.slidersResolution /
            (float(self.ui.lineEditMaxC1.text()) -
             float(self.ui.lineEditMinC1.text())))

    def updateSliderBark(self):
        '''
        Updates position of k slide bar
        '''
        self.ui.horizontalSliderk.setValue(
            (float(self.ui.lineEditValuek.text()) -
             float(self.ui.lineEditMink.text())) *
            self.slidersResolution /
            (float(self.ui.lineEditMaxk.text()) -
             float(self.ui.lineEditMink.text())))

    def updateSliderBarR2(self):
        '''
        Updates position of R2 slide bar
        '''
        self.ui.horizontalSliderR2.setValue(
            (float(self.ui.lineEditValueR2.text()) -
             float(self.ui.lineEditMinR2.text())) *
            self.slidersResolution /
            (float(self.ui.lineEditMaxR2.text()) -
             float(self.ui.lineEditMinR2.text())))

    def updateSliderBarL2(self):
        '''
        Updates position of L2 slide bar
        '''
        self.ui.horizontalSliderL2.setValue(
            (float(self.ui.lineEditValueL2.text()) -
             float(self.ui.lineEditMinL2.text())) *
            self.slidersResolution /
            (float(self.ui.lineEditMaxL2.text()) -
             float(self.ui.lineEditMinL2.text())))

    def updateSliderBarC2(self):
        '''
        Updates position of C2 slide bar
        '''
        self.ui.horizontalSliderC2.setValue(
            (float(self.ui.lineEditValueC2.text()) -
             float(self.ui.lineEditMinC2.text())) *
            self.slidersResolution /
            (float(self.ui.lineEditMaxC2.text()) -
             float(self.ui.lineEditMinC2.text())))

    def updateSliderBarRsensor(self):
        '''
        Updates position of Rsensor slide bar
        '''
        self.ui.horizontalSliderRsensor.setValue(
            (float(self.ui.lineEditValueRsensor.text()) -
             float(self.ui.lineEditMinRsensor.text())) *
            self.slidersResolution /
            (float(self.ui.lineEditMaxRsensor.text()) -
             float(self.ui.lineEditMinRsensor.text())))

    def updateSliderBarCsensor(self):
        '''
        Updates position of Csensor slide bar
        '''
        self.ui.horizontalSliderCsensor.setValue(
            (float(self.ui.lineEditValueCsensor.text()) -
             float(self.ui.lineEditMinCsensor.text())) *
            self.slidersResolution /
            (float(self.ui.lineEditMaxCsensor.text()) -
             float(self.ui.lineEditMinCsensor.text())))

    ###########################################################################
    #      Data Fitting
    ###########################################################################

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
        if self.ui.checkBoxFitR0.isChecked():
            params['R0'].vary = True
        else:
            params['R0'].vary = False
        if self.ui.checkBoxFitR1.isChecked():
            params['R1'].vary = True
        else:
            params['R1'].vary = False
        if self.ui.checkBoxFitL1.isChecked():
            params['L1'].vary = True
        else:
            params['L1'].vary = False
        if self.ui.checkBoxFitC1.isChecked():
            params['C1'].vary = True
        else:
            params['C1'].vary = False
        if self.ui.checkBoxFitk.isChecked():
            params['k'].vary = True
        else:
            params['k'].vary = False
        if self.ui.checkBoxFitR2.isChecked():
            params['R2'].vary = True
        else:
            params['R2'].vary = False
        if self.ui.checkBoxFitL2.isChecked():
            params['L2'].vary = True
        else:
            params['L2'].vary = False
        if self.ui.checkBoxFitC2.isChecked():
            params['C2'].vary = True
        else:
            params['C2'].vary = False
        if self.ui.checkBoxFitRsensor.isChecked():
            params['Rsensor'].vary = True
        else:
            params['Rsensor'].vary = False
        if self.ui.checkBoxFitCsensor.isChecked():
            params['Csensor'].vary = True
        else:
            params['Csensor'].vary = False

        # perform the actual fit
        if self.ui.checkBox2RegionsFit.isChecked():
            # If the 2 regions fit radio button is checked:
            # Read the vaues of the initial and final frequencies
            # for the 2 regions provided in the corresponding
            # line edit widgets
            f1min = float(self.ui.lineEditF1Min.text())
            f1max = float(self.ui.lineEditF1Max.text())
            f2min = float(self.ui.lineEditF2Min.text())
            f2max = float(self.ui.lineEditF2Max.text())
            # Find the indexes of the frequency array of the components
            # with closer values to those provided
            index_f1min = (abs(self.spectrum[self.currentFileIndex].getFreq() -
                               f1min)).argmin()
            index_f1max = (abs(self.spectrum[self.currentFileIndex].getFreq() -
                               f1max)).argmin()
            index_f2min = (abs(self.spectrum[self.currentFileIndex].getFreq() -
                               f2min)).argmin()
            index_f2max = (abs(self.spectrum[self.currentFileIndex].getFreq() -
                               f2max)).argmin()
            # create arrays corresponding to the two selected regions
            f1 = self.spectrum[self.currentFileIndex].getFreq()[
                index_f1min:index_f1max
            ]
            ReZ1 = self.spectrum[self.currentFileIndex].getReZ()[
                index_f1min: index_f1max
            ]*50
            ImZ1 = self.spectrum[self.currentFileIndex].getImZ()[
                index_f1min: index_f1max
            ]*50
            f2 = self.spectrum[self.currentFileIndex].getFreq()[
                index_f2min: index_f2max
            ]
            ReZ2 = self.spectrum[self.currentFileIndex].getReZ()[
                index_f2min: index_f2max
            ]*50
            ImZ2 = self.spectrum[self.currentFileIndex].getImZ()[
                index_f2min: index_f2max
            ]*50
            # call the minimize lmfit method
            result = minimize(residualFittingCoupledAntennas2, params,
                              method='leastsq',
                              args=(f1, ReZ1, ImZ1, f2, ReZ2, ImZ2))
        else:
            # If the 2 regions fit radio button is NOT checked:
            result = minimize(
                residualFittingCoupledAntennas, params,
                method='leastsq',
                args=(self.spectrum[self.currentFileIndex].getFreq(),
                      self.spectrum[self.currentFileIndex].getReZ()*50,
                      self.spectrum[self.currentFileIndex].getImZ()*50
                      )
            )

        # Update fittedSpectrum attributes with those found in the fit
        self.fittedSpectrum[self.currentFileIndex].setR0(
            result.params['R0'].value)
        self.fittedSpectrum[self.currentFileIndex].setR1(
            result.params['R1'].value)
        self.fittedSpectrum[self.currentFileIndex].setL1(
            result.params['L1'].value)
        self.fittedSpectrum[self.currentFileIndex].setC1(
            result.params['C1'].value)
        self.fittedSpectrum[self.currentFileIndex].setR2(
            result.params['R2'].value)
        self.fittedSpectrum[self.currentFileIndex].setL2(
            result.params['L2'].value)
        self.fittedSpectrum[self.currentFileIndex].setRsensor(
            result.params['Rsensor'].value)
        self.fittedSpectrum[self.currentFileIndex].setCsensor(
            result.params['Csensor'].value)
        self.fittedSpectrum[self.currentFileIndex].setk(
            result.params['k'].value)

        # Recalculate impedance and S11 values from parameters found in the fit
        self.fittedSpectrum[
            self.currentFileIndex].calculateImpedanceCoupledAntennas()
        self.fittedSpectrum[self.currentFileIndex].calculateS11()

        # Updates attribute values in "Value Edit Boxes" with those
        # corresponding to fittedspectrum[currentFileIndex], in this
        # case those found in the fit
        self.updateValuesInEditBoxes()

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

    ###########################################################################
    #      Function for updating class attribute values in edit boxes
    ###########################################################################

    def updateValuesInEditBoxes(self):
        '''
        Update class attribute values in edit boxes either with those found
        from fits or with those stored when changing the visualized data file
        '''
        self.ui.lineEditValueR0.setText(
            "{0:0.2e}".format(
                self.fittedSpectrum[self.currentFileIndex].getR0()
            )
        )
        self.ui.lineEditValueR1.setText(
            "{0:0.2e}".format(
                self.fittedSpectrum[self.currentFileIndex].getR1()
            )
        )
        self.ui.lineEditValueL1.setText(
            "{0:0.2e}".format(
                self.fittedSpectrum[self.currentFileIndex].getL1()
            )
        )
        self.ui.lineEditValueC1.setText(
            "{0:0.2e}".format(
                self.fittedSpectrum[self.currentFileIndex].getC1()
            )
        )
        self.ui.lineEditValueR2.setText(
            "{0:0.2e}".format(
                self.fittedSpectrum[self.currentFileIndex].getR2()
            )
        )
        self.ui.lineEditValueL2.setText(
            "{0:0.2e}".format(
                self.fittedSpectrum[self.currentFileIndex].getL2()
            )
        )
        self.ui.lineEditValueC2.setText(
            "{0:0.2e}".format(
                self.fittedSpectrum[self.currentFileIndex].getC2()
            )
        )
        self.ui.lineEditValueRsensor.setText(
            "{0:0.2e}".format(
                self.fittedSpectrum[self.currentFileIndex].getRsensor()
            )
        )
        self.ui.lineEditValueCsensor.setText(
            "{0:0.2e}".format(
                self.fittedSpectrum[self.currentFileIndex].getCsensor()
            )
        )
        self.ui.lineEditValuek.setText(
            "{0:0.2e}".format(
                self.fittedSpectrum[self.currentFileIndex].getk()
            )
        )

    ###########################################################################
    #      Functions for updating class attributes when slide bars are changed
    ###########################################################################

    def updateValueR0(self, value):
        '''
        Defines actions to be undertaken when R1 slide bar is changed:
        1) Updates R0 attribute as well as 2) the value displayed in
        the "R0 Value Edit Box". It also updated the 3) impedance and
        4) S11 for the displayed data file. Finally, it 5) updates the plots.
        '''
        # Updates R0 attribute of the object fittedSpectrum[currentFileIndex]
        # from values read from "R0 edit boxes" (ie "Value", "Min"
        # and "Max" edit boxes)
        self.fittedSpectrum[self.currentFileIndex].setR0(float(
            self.ui.lineEditMinR0.text()) + value * (
                float(self.ui.lineEditMaxR0.text()) - float(
                    self.ui.lineEditMinR0.text())) / self.slidersResolution)
        # Updates R0 attribute in the "R0 Value Edit Box"
        self.ui.lineEditValueR0.setText(
            "{0:0.2e}".format(
                self.fittedSpectrum[self.currentFileIndex].getR0()
            )
        )
        # Update and plot Fitted Spectrum with new data
        self.updateFittedSpetrum()

    def updateValueR1(self, value):
        '''
        Defines actions to be undertaken when R1 slide bar is changed:
        1) Updates R1 attribute as well as 2) the value displayed in
        the "R1 Value Edit Box". It also updated the 3) impedance and
        4) S11 for the displayed data file. Finally, it 5) updates the plots.
        '''
        # Updates R1 attribute of the object fittedSpectrum[currentFileIndex]
        # from values read from "R1 edit boxes" (ie "Value", "Min"
        # and "Max" edit boxes)
        self.fittedSpectrum[self.currentFileIndex].setR1(float(
            self.ui.lineEditMinR1.text()) + value * (
                float(self.ui.lineEditMaxR1.text()) - float(
                    self.ui.lineEditMinR1.text())) / self.slidersResolution)
        # Updates R1 attribute in the "R1 Value Edit Box"
        self.ui.lineEditValueR1.setText(
            "{0:0.2e}".format(
                self.fittedSpectrum[self.currentFileIndex].getR1()
            )
        )
        # Update and plot Fitted Spectrum with new data
        self.updateFittedSpetrum()

    def updateValueL1(self, value):
        '''
        Defines actions to be undertaken when L1 slide baar is changed:
        1) Updates L1 attribute as well as 2) the value displayed in
        the "L1 Value Edit Box". It also updated the 3) impedance and
        4) S11 for the displayed data file. Finally, it 5) updates the plots.
        '''
        # Updates L1 attribute of the object fittedSpectrum[currentFileIndex]
        # from values read from "L1 edit boxes" (ie "Value", "Min"
        # and "Max" edit boxes)
        self.fittedSpectrum[self.currentFileIndex].setL1(float(
            self.ui.lineEditMinL1.text()) + value * (
                float(self.ui.lineEditMaxL1.text()) - float(
                    self.ui.lineEditMinL1.text())) / self.slidersResolution)
        # Updates L1 attribute in the "L1 Value Edit Box"
        self.ui.lineEditValueL1.setText(
            "{0:0.2e}".format(
                self.fittedSpectrum[self.currentFileIndex].getL1()
            )
        )
        # Update and plot Fitted Spectrum with new data
        self.updateFittedSpetrum()

    def updateValueC1(self, value):
        '''
        Defines actions to be undertaken when C1 slide bar is changed:
        1) Updates C1 attribute as well as 2) the value displayed in
        the "C1 Value Edit Box". It also updated the 3) impedance and
        4) S11 for the displayed data file. Finally, it 5) updates the plots.
        '''
        # Updates C1 attribute of the object fittedSpectrum[currentFileIndex]
        # from values read from "C1 edit boxes" (ie "Value", "Min"
        # and "Max" edit boxes)
        self.fittedSpectrum[self.currentFileIndex].setC1(float(
            self.ui.lineEditMinC1.text()) + value * (
                float(self.ui.lineEditMaxC1.text()) - float(
                    self.ui.lineEditMinC1.text())) / self.slidersResolution)
        # Updates C1 attribute in the "C1 Value Edit Box"
        self.ui.lineEditValueC1.setText(
            "{0:0.2e}".format(
                self.fittedSpectrum[self.currentFileIndex].getC1()
            )
        )
        # Update and plot Fitted Spectrum with new data
        self.updateFittedSpetrum()

    def updateValueR2(self, value):
        '''
        Defines actions to be undertaken when R2 slide bar is changed:
        1) Updates R2 attribute as well as 2) the value displayed in
        the "R2 Value Edit Box". It also updated the 3) impedance and
        4) S11 for the displayed data file. Finally, it 5) updates the plots.
        '''
        # Updates R2 attribute of the object fittedSpectrum[currentFileIndex]
        # from values read from "R2 edit boxes" (ie "Value", "Min"
        # and "Max" edit boxes)
        self.fittedSpectrum[self.currentFileIndex].setR2(float(
            self.ui.lineEditMinR2.text()) + value * (
                float(self.ui.lineEditMaxR2.text()) - float(
                    self.ui.lineEditMinR2.text())) / self.slidersResolution)
        # Updates R2 attribute in the "R2 Value Edit Box"
        self.ui.lineEditValueR2.setText(
            "{0:0.2e}".format(
                self.fittedSpectrum[self.currentFileIndex].getR2()
            )
        )
        # Update and plot Fitted Spectrum with new data
        self.updateFittedSpetrum()

    def updateValueL2(self, value):
        '''
        Defines actions to be undertaken when L2 slide bar is changed:
        1) Updates L2 attribute as well as 2) the value displayed in
        the "L2 Value Edit Box". It also updated the 3) impedance and
        4) S11 for the displayed data file. Finally, it 5) updates the plots.
        '''
        # Updates L2 attribute of the object fittedSpectrum[currentFileIndex]
        # from values read from "L2 edit boxes" (ie "Value", "Min"
        # and "Max" edit boxes)
        self.fittedSpectrum[self.currentFileIndex].setL2(float(
            self.ui.lineEditMinL2.text()) + value * (float(
                self.ui.lineEditMaxL2.text()) - float(
                    self.ui.lineEditMinL2.text()
                )) / self.slidersResolution)
        # Updates L2 attribute in the "L2 Value Edit Box"
        self.ui.lineEditValueL2.setText("{0:0.2e}".format(
            self.fittedSpectrum[self.currentFileIndex].getL2()
            )
        )
        # Update and plot Fitted Spectrum with new data
        self.updateFittedSpetrum()

    def updateValueC2(self, value):
        '''
        Defines actions to be undertaken when C2 slide bar is changed:
        1) Updates C2 attribute as well as 2) the value displayed in
        the "C2 Value Edit Box". It also updated the 3) impedance and
        4) S11 for the displayed data file. Finally, it 5) updates the plots.
        '''
        # Updates C2 attribute of the object fittedSpectrum[currentFileIndex]
        # from values read from "C2 edit boxes" (ie "Value", "Min"
        # and "Max" edit boxes)
        self.fittedSpectrum[self.currentFileIndex].setC2(float(
            self.ui.lineEditMinC2.text()) + value * (
                float(self.ui.lineEditMaxC2.text()) - float(
                    self.ui.lineEditMinC2.text())) / self.slidersResolution)
        # Updates C2 attribute in the "C2 Value Edit Box"
        self.ui.lineEditValueC2.setText("{0:0.2e}".format(
            self.fittedSpectrum[self.currentFileIndex].getC2()
            )
        )
        # Update and plot Fitted Spectrum with new data
        self.updateFittedSpetrum()

    def updateValueRsensor(self, value):
        '''
        Defines actions to be undertaken when Rsensor slide bar is changed:
        1) Updates Rsensor attribute as well as 2) the value displayed in
        the "Rsensor Value Edit Box". It also updated the 3) impedance and
        4) S11 for the displayed data file. Finally, it 5) updates the plots.
        '''
        # Updates Rsensor attribute of the object
        # fittedSpectrum[currentFileIndex] from values read from
        # "Rsensor edit boxes" (ie "Value", "Min" and "Max" edit boxes)
        self.fittedSpectrum[self.currentFileIndex].setRsensor(float(
            self.ui.lineEditMinRsensor.text()) + value * (
                float(self.ui.lineEditMaxRsensor.text()) - float(
                    self.ui.lineEditMinRsensor.text())
            ) / self.slidersResolution)
        # Updates Rsensor attribute in the "Rsensor Value Edit Box"
        self.ui.lineEditValueRsensor.setText("{0:0.2e}".format(
            self.fittedSpectrum[self.currentFileIndex].getRsensor()
            )
        )
        # Update and plot Fitted Spectrum with new data
        self.updateFittedSpetrum()

    def updateValueCsensor(self, value):
        '''
        Defines actions to be undertaken when Csensor slide bar is changed:
        1) Updates Csensor attribute as well as 2) the value displayed in
        the "Csensor Value Edit Box". It also updated the 3) impedance and
        4) S11 for the displayed data file. Finally, it 5) updates the plots.
        '''
        # Updates Csensor attribute of the object
        # fittedSpectrum[currentFileIndex] from values read from
        # "Csensor edit boxes" (ie "Value", "Min" and "Max" edit boxes)
        self.fittedSpectrum[self.currentFileIndex].setCsensor(float(
            self.ui.lineEditMinCsensor.text()) + value * (float(
                self.ui.lineEditMaxCsensor.text()) - float(
                    self.ui.lineEditMinCsensor.text())
                ) / self.slidersResolution
        )
        # Updates Csensor attribute in the "Csensor Value Edit Box"
        self.ui.lineEditValueCsensor.setText("{0:0.2e}".format(
            self.fittedSpectrum[self.currentFileIndex].getCsensor()
            )
        )
        # Update and plot Fitted Spectrum with new data
        self.updateFittedSpetrum()

    def updateValuek(self, value):
        '''
        Defines actions to be undertaken when k (coupling factor)
        slide bar is changed: 1) Updates k attribute as well as
        2) the value displayed in the "k Value Edit Box". It also
        updates the 3) impedance and 4) S11 for the displayed data file.
        Finally, it 5) updates the plots.
        '''
        # Updates k attribute of the object fittedSpectrum[currentFileIndex]
        # from values read from "k edit boxes" (ie "Value", "Min"
        # and "Max" edit boxes)
        self.fittedSpectrum[self.currentFileIndex].setk(float(
            self.ui.lineEditMink.text()) + value * (
                float(self.ui.lineEditMaxk.text()) - float(
                    self.ui.lineEditMink.text())) / self.slidersResolution)
        # Updates k attribute in the "k Value Edit Box"
        self.ui.lineEditValuek.setText("{0:0.2e}".format(
            self.fittedSpectrum[self.currentFileIndex].getk()
            )
        )
        # Update and plot Fitted Spectrum with new data
        self.updateFittedSpetrum()

    ###########################################################################
    #      Update and plot Fitted Spectrum when data is changed
    ###########################################################################

    def updateFittedSpetrum(self):
        # Updates impedance (both Re and Im) for
        # fittedSpectrum[currentFileIndex]
        self.fittedSpectrum[
            self.currentFileIndex].calculateImpedanceCoupledAntennas()
        # Updates S11 for fittedSpectrum[currentFileIndex]
        self.fittedSpectrum[self.currentFileIndex].calculateS11()
        # Updates graphs
        self.update_graph()

    ###########################################################################
    #      Function for plotting data
    ###########################################################################

    def update_graph(self):
        '''
        Updates all 4 different subplots in the GUIs
        '''
        # Plot the not-normalized real impedances in axes1
        self.ui.MplWidget4.canvas.axes1.clear()
        self.ui.MplWidget4.canvas.axes1.plot(
            self.spectrum[self.currentFileIndex].getFreq(),
            self.spectrum[self.currentFileIndex].getReZ()*50
        )
        self.ui.MplWidget4.canvas.axes1.plot(
            self.fittedSpectrum[self.currentFileIndex].getFreq(),
            self.fittedSpectrum[self.currentFileIndex].getReZ(),
            'r--'
        )
        self.ui.MplWidget4.canvas.axes1.set_ylabel("Re Z")
        self.ui.MplWidget4.canvas.axes1.set_xlabel("f (MHz)")
        self.ui.MplWidget4.canvas.axes1.set_xlim(
            float(self.ui.lineEditValueFmin.text()),
            float(self.ui.lineEditValueFmax.text()))

        # Plot the not-normalized imaginary impedances in axes2
        self.ui.MplWidget4.canvas.axes2.clear()
        self.ui.MplWidget4.canvas.axes2.plot(
            self.spectrum[self.currentFileIndex].getFreq(),
            self.spectrum[self.currentFileIndex].getImZ()*50
        )
        self.ui.MplWidget4.canvas.axes2.plot(
            self.fittedSpectrum[self.currentFileIndex].getFreq(),
            self.fittedSpectrum[self.currentFileIndex].getImZ(),
            'r--'
        )
        self.ui.MplWidget4.canvas.axes2.set_ylabel("Im Z")
        self.ui.MplWidget4.canvas.axes2.set_xlabel("f (MHz)")
        self.ui.MplWidget4.canvas.axes2.set_xlim(
            float(self.ui.lineEditValueFmin.text()),
            float(self.ui.lineEditValueFmax.text()))

        # Plot module of S11 in axes3
        self.ui.MplWidget4.canvas.axes3.clear()
        self.ui.MplWidget4.canvas.axes3.plot(
            self.spectrum[self.currentFileIndex].getFreq(),
            self.spectrum[self.currentFileIndex].getModS11()
        )
        self.ui.MplWidget4.canvas.axes3.plot(
            self.fittedSpectrum[self.currentFileIndex].getFreq(),
            self.fittedSpectrum[self.currentFileIndex].getModS11(),
            'r--'
        )
        self.ui.MplWidget4.canvas.axes3.set_ylabel("Mod S11")
        self.ui.MplWidget4.canvas.axes3.set_xlabel("f (MHz)")
        self.ui.MplWidget4.canvas.axes3.set_xlim(
            float(self.ui.lineEditValueFmin.text()),
            float(self.ui.lineEditValueFmax.text()))

        # Plot the not-normalized real vs imaginary impedances in axes4
        self.ui.MplWidget4.canvas.axes4.clear()
        self.ui.MplWidget4.canvas.axes4.plot(
            self.spectrum[self.currentFileIndex].getReZ()*50,
            self.spectrum[self.currentFileIndex].getImZ()*50
        )
        self.ui.MplWidget4.canvas.axes4.plot(
            self.fittedSpectrum[self.currentFileIndex].getReZ(),
            self.fittedSpectrum[self.currentFileIndex].getImZ(),
            'r--'
        )
        self.ui.MplWidget4.canvas.axes4.set_ylabel("Im Z")
        self.ui.MplWidget4.canvas.axes4.set_xlabel("ReZ")
        self.ui.MplWidget4.canvas.figure.tight_layout()
        self.ui.MplWidget4.canvas.draw()
