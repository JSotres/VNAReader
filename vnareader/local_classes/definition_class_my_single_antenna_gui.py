"""
Definition of class to create the single antenna analysis GUI
from the Qt5 created template from singleAntennaAnalysisGUI
"""

from PyQt5.QtWidgets import QMainWindow, QFileDialog
import os
import pandas as pd
from matplotlib.backends.backend_qt5agg import (
    NavigationToolbar2QT as NavigationToolbar)
from lmfit import minimize, Parameters
from ..qt5_ui_files.singleAntennaAnalysisWindow_v0 import (
        Ui_MainAnalysisSingleAntennaWindow)
from .definition_class_single_antenna_spectrum import (
        calculatedSingleVNASpectrum)
from ..local_functions.definition_local_functions import (
        residualFittingSingleAntenna)


class mySingleAntennaGUI(QMainWindow):
    def __init__(self, spectrum):
        super().__init__()
        self.ui = Ui_MainAnalysisSingleAntennaWindow()
        self.ui.setupUi(self)
        self.addToolBar(NavigationToolbar(self.ui.MplWidget_0.canvas, self))

        # Declaration of magnitude by which value of sliders should be scaled
        # in methods where the position of the slider is actualized
        # Assumes min value = 0, and that it is the same magnitude
        # for all sliders
        # Needs to be improved!
        self.slidersResolution = self.ui.verticalSliderR0.maximum()

        # Declaration of objects
        self.spectrum = spectrum
        self.fittedSpectrum = calculatedSingleVNASpectrum(
            self.spectrum.getFreq(),
            float(self.ui.lineEditValueR0.text()),
            float(self.ui.lineEditValueR1.text()),
            float(self.ui.lineEditValueF0.text()),
            float(self.ui.lineEditValueQ.text())
        )
        # Declaration of methods for widgets in the GUI
        self.ui.action_Export_as_csv.triggered.connect(self.exportCSV)
        self.ui.action_Export_as_xlsx.triggered.connect(self.exportXLSX)
        self.ui.verticalSliderR0.valueChanged.connect(self.updateValueR0)
        self.ui.verticalSliderR1.valueChanged.connect(self.updateValueR1)
        self.ui.verticalSliderF0.valueChanged.connect(self.updateValueF0)
        self.ui.verticalSliderQ.valueChanged.connect(self.updateValueQ)
        self.ui.lineEditValueR0.returnPressed.connect(self.updateSlideBarR0)
        self.ui.lineEditMaxR0.returnPressed.connect(self.updateSlideBarR0)
        self.ui.lineEditMinR0.returnPressed.connect(self.updateSlideBarR0)
        self.ui.lineEditValueR1.returnPressed.connect(self.updateSlideBarR1)
        self.ui.lineEditMaxR1.returnPressed.connect(self.updateSlideBarR1)
        self.ui.lineEditMinR1.returnPressed.connect(self.updateSlideBarR1)
        self.ui.lineEditValueF0.returnPressed.connect(self.updateSlideBarF0)
        self.ui.lineEditMaxF0.returnPressed.connect(self.updateSlideBarF0)
        self.ui.lineEditMinF0.returnPressed.connect(self.updateSlideBarF0)
        self.ui.lineEditValueQ.returnPressed.connect(self.updateSlideBarQ)
        self.ui.lineEditMaxQ.returnPressed.connect(self.updateSlideBarQ)
        self.ui.lineEditMinQ.returnPressed.connect(self.updateSlideBarQ)
        self.ui.pushButtonFitData.clicked.connect(self.doFitData)
        # Update values of slide bars
        self.updateSlideBarR0()
        self.updateSlideBarR1()
        self.updateSlideBarF0()
        self.updateSlideBarQ()
        # Plot experimental and fitted data
        self.update_graph()

    # --------- Method for exporting fitted parameters --------

    def exportCSV(self):
        
        data = {"R0":[self.fittedSpectrum.getR0()],
                "R1":[self.fittedSpectrum.getR1()],
                "F0":[self.fittedSpectrum.getF0()],
                "Q":[self.fittedSpectrum.getQ()],
                "L1":[self.fittedSpectrum.getL1()],
                "C1":[self.fittedSpectrum.getC1()]
                }
        df = pd.DataFrame(data)
        caption = "Save File"
        directory = os.getcwd()
        name = QFileDialog.getSaveFileName(self, caption, directory, "*.csv")
        df.to_csv(name[0], index=False)
        

    def exportXLSX(self):
        
        data = {"R0":[self.fittedSpectrum.getR0()],
                "R1":[self.fittedSpectrum.getR1()],
                "F0":[self.fittedSpectrum.getF0()],
                "Q":[self.fittedSpectrum.getQ()],
                "L1":[self.fittedSpectrum.getL1()],
                "C1":[self.fittedSpectrum.getC1()]
                }
        df = pd.DataFrame(data)
        caption = "Save File"
        directory = os.getcwd()
        name = QFileDialog.getSaveFileName(self, caption, directory, "*.xlsx")
        df.to_excel(name[0], index=False)
    
        

    # --------- Methods for updating slide bar positions --------
    def updateSlideBarR0(self):
        self.ui.verticalSliderR0.setValue(
            (float(self.ui.lineEditValueR0.text()) -
             float(self.ui.lineEditMinR0.text())) *
            self.slidersResolution /
            (float(self.ui.lineEditMaxR0.text()) -
             float(self.ui.lineEditMinR0.text())))

    def updateSlideBarR1(self):
        self.ui.verticalSliderR1.setValue(
            (float(self.ui.lineEditValueR1.text()) -
             float(self.ui.lineEditMinR1.text())) *
            self.slidersResolution /
            (float(self.ui.lineEditMaxR1.text()) -
             float(self.ui.lineEditMinR1.text())))

    def updateSlideBarF0(self):
        self.ui.verticalSliderF0.setValue(
            (float(self.ui.lineEditValueF0.text()) -
             float(self.ui.lineEditMinF0.text())) *
            self.slidersResolution /
            (float(self.ui.lineEditMaxF0.text()) -
             float(self.ui.lineEditMinF0.text())))

    def updateSlideBarQ(self):
        self.ui.verticalSliderQ.setValue(
            (float(self.ui.lineEditValueQ.text()) -
             float(self.ui.lineEditMinQ.text())) *
            self.slidersResolution /
            (float(self.ui.lineEditMaxQ.text()) -
             float(self.ui.lineEditMinQ.text())))

    def doFitData(self):
        params = Parameters()
        params.add('R0', value=float(self.ui.lineEditValueR0.text()))
        params.add('R1', value=float(self.ui.lineEditValueR1.text()))
        params.add('Q', value=float(self.ui.lineEditValueQ.text()))
        params.add('F0', value=float(self.ui.lineEditValueF0.text()))
        params['R0'].vary = False

        result = minimize(
            residualFittingSingleAntenna, params,
            args=(self.spectrum.getFreq(),
                  self.spectrum.getReZ()*50, self.spectrum.getImZ()*50
                  )
        )

        self.fittedSpectrum.setR0(result.params['R0'].value)
        self.fittedSpectrum.setR1(result.params['R1'].value)
        self.fittedSpectrum.setQ(result.params['Q'].value)
        self.fittedSpectrum.setF0(result.params['F0'].value)
        self.fittedSpectrum.calculateImpedanceSingleAntenna()
        self.fittedSpectrum.updateL1C1Values()
        self.update_graph()
        self.ui.lineEditValueR0.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getR0()))
        self.ui.lineEditValueR1.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getR1()))
        self.ui.lineEditValueQ.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getQ()))
        self.ui.lineEditValueF0.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getF0()))
        self.ui.lineEditValueL1.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getL1()))
        self.ui.lineEditValueC1.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getC1()))

    def updateValueR0(self, value):
        self.fittedSpectrum.setR0(float(
            self.ui.lineEditMinR0.text())+value*(
                float(self.ui.lineEditMaxR0.text())-float(
                    self.ui.lineEditMinR0.text()))/self.slidersResolution)
        self.ui.lineEditValueR0.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getR0()))
        self.fittedSpectrum.calculateImpedanceSingleAntenna()
        self.fittedSpectrum.updateL1C1Values()
        self.update_graph()
        self.ui.lineEditValueC1.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getC1()))
        self.ui.lineEditValueL1.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getL1()))

    def updateValueR1(self, value):
        self.fittedSpectrum.setR1(float(
            self.ui.lineEditMinR1.text())+value*(
                float(self.ui.lineEditMaxR1.text())-float(
                    self.ui.lineEditMinR1.text()))/self.slidersResolution)
        self.ui.lineEditValueR1.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getR1()))
        self.fittedSpectrum.calculateImpedanceSingleAntenna()
        self.fittedSpectrum.updateL1C1Values()
        self.update_graph()
        self.ui.lineEditValueC1.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getC1()))
        self.ui.lineEditValueL1.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getL1()))

    def updateValueF0(self, value):
        self.fittedSpectrum.setF0(float(
            self.ui.lineEditMinF0.text())+value*(
                float(self.ui.lineEditMaxF0.text())-float(
                    self.ui.lineEditMinF0.text()))/self.slidersResolution)
        self.ui.lineEditValueF0.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getF0()))
        self.fittedSpectrum.calculateImpedanceSingleAntenna()
        self.fittedSpectrum.updateL1C1Values()
        self.update_graph()
        self.ui.lineEditValueC1.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getC1()))
        self.ui.lineEditValueL1.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getL1()))

    def updateValueQ(self, value):
        self.fittedSpectrum.setQ(float(self.ui.lineEditMinQ.text())+value*(
            float(self.ui.lineEditMaxQ.text()) -
            float(self.ui.lineEditMinQ.text()))/self.slidersResolution)
        self.ui.lineEditValueQ.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getQ()))
        self.fittedSpectrum.calculateImpedanceSingleAntenna()
        self.fittedSpectrum.updateL1C1Values()
        self.update_graph()
        self.ui.lineEditValueC1.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getC1()))
        self.ui.lineEditValueL1.setText(
            "{0:0.2e}".format(self.fittedSpectrum.getL1()))

    def update_graph(self):
        self.ui.MplWidget_0.canvas.axes1.clear()
        self.ui.MplWidget_0.canvas.axes1.plot(
            self.spectrum.getFreq(), self.spectrum.getReZ()*50)
        self.ui.MplWidget_0.canvas.axes1.plot(
            self.fittedSpectrum.getFreq(), self.fittedSpectrum.getReZ(), 'r--')
        self.ui.MplWidget_0.canvas.axes1.set_ylabel("Re Z")
        self.ui.MplWidget_0.canvas.axes1.set_xlabel("f (MHz)")
        self.ui.MplWidget_0.canvas.axes1.set_xlim(
            float(self.ui.lineEditValueFmin.text()),
            float(self.ui.lineEditValueFmax.text()))
        self.ui.MplWidget_0.canvas.axes2.clear()
        self.ui.MplWidget_0.canvas.axes2.plot(
            self.spectrum.getFreq(), self.spectrum.getImZ()*50)
        self.ui.MplWidget_0.canvas.axes2.plot(
            self.fittedSpectrum.getFreq(), self.fittedSpectrum.getImZ(), 'r--')
        self.ui.MplWidget_0.canvas.axes2.set_ylabel("Im Z")
        self.ui.MplWidget_0.canvas.axes2.set_xlabel("f (MHz)")
        self.ui.MplWidget_0.canvas.axes2.set_xlim(
            float(self.ui.lineEditValueFmin.text()),
            float(self.ui.lineEditValueFmax.text()))
        self.ui.MplWidget_0.canvas.figure.tight_layout()
        self.ui.MplWidget_0.canvas.draw()
