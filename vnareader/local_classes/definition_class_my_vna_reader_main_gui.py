"""
Definition of class to create the main GUI of the program
from the Qt5 created template from vnaReaderMainWindow_v0
"""
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from matplotlib.backends.backend_qt5agg import (
    NavigationToolbar2QT as NavigationToolbar)
from numpy import loadtxt
from ..qt5_ui_files.vnaReaderMainWindow_v0 import Ui_MainVNAReaderWindow
from .definition_class_my_single_antenna_gui import mySingleAntennaGUI
from .definition_class_my_coupled_antennas_gui import myCoupledAntennasGUI
from .definition_class_vna_spectrum import vnaSpectrum


class vnaReaderMainGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainVNAReaderWindow()
        self.ui.setupUi(self)
        self.RepresentationIndex = ([1, 2])
        self.YLabels = [
            "Re S11", "Im S11", "Mod S11", "Pha S11", "Re Z", "Im Z"]
        self.CurrentFigure = 0
        self.ui.actionOpen.triggered.connect(self.openfiledialog)
        self.ui.actionSingleAntenna.triggered.connect(
            self.openSingleAntennaWindow)
        self.ui.actionCoupledAntennas.triggered.connect(
            self.openCoupledAntennasWindow)
        self.ui.comboBoxCurrentFigure.currentIndexChanged.connect(
            self.changeCurrentFigure)
        self.ui.pushButtonReS11.clicked.connect(self.doReS11)
        self.ui.pushButtonImS11.clicked.connect(self.doImS11)
        self.ui.pushButtonModS11.clicked.connect(self.doModS11)
        self.ui.pushButtonPhaS11.clicked.connect(self.doPhaS11)
        self.ui.pushButtonReZ.clicked.connect(self.doReZ)
        self.ui.pushButtonImZ.clicked.connect(self.doImZ)
        self.ui.pushButtonPreviousFile.clicked.connect(self.doPreviousFile)
        self.ui.pushButtonNextFile.clicked.connect(self.doNextFile)
        self.ui.pushButtonAllFiles.clicked.connect(self.doAllFiles)
        self.addToolBar(NavigationToolbar(
            self.ui.MplWidget_0.canvas, self))
        self.show()

    def openfiledialog(self):
        caption = "Open File"
        directory = "./vnareader/sample_expdata"
        filter_mask = "All Files (*);;Text Files (*.txt)"
        filenames = QFileDialog.getOpenFileNames(
            self, caption, directory, filter_mask)[0]
        self.spectrum = []
        self.numberOfFiles = len(filenames)
        self.currentFileIndex = 0
        for i in range(len(filenames)):
            a = loadtxt(filenames[i], skiprows=2, unpack=True)
            self.spectrum.append(vnaSpectrum(filenames[i], a))
        self.update_graph(
            self.spectrum[self.currentFileIndex].getFreq(),
            self.spectrum[self.currentFileIndex].getData(
                self.RepresentationIndex[0]),
            self.spectrum[self.currentFileIndex].getData(
                self.RepresentationIndex[1]))

    def openSingleAntennaWindow(self):
        self.singleAntennaWindow = mySingleAntennaGUI(
            self.spectrum[self.currentFileIndex])
        self.singleAntennaWindow.show()

    def openCoupledAntennasWindow(self):
        self.coupledAntennasWindow = myCoupledAntennasGUI(
            self.spectrum[self.currentFileIndex])
        self.coupledAntennasWindow.show()

    def changeCurrentFigure(self):
        self.CurrentFigure = self.ui.comboBoxCurrentFigure.currentIndex()

    def doReS11(self):
        self.RepresentationIndex[self.CurrentFigure] = 1
        self.update_graph(
            self.spectrum[self.currentFileIndex].getFreq(),
            self.spectrum[self.currentFileIndex].getData(
                self.RepresentationIndex[0]),
            self.spectrum[self.currentFileIndex].getData(
                self.RepresentationIndex[1]))

    def doImS11(self):
        self.RepresentationIndex[self.CurrentFigure] = 2
        self.update_graph(
            self.spectrum[self.currentFileIndex].getFreq(),
            self.spectrum[self.currentFileIndex].getData(
                self.RepresentationIndex[0]),
            self.spectrum[self.currentFileIndex].getData(
                self.RepresentationIndex[1]))

    def doModS11(self):
        self.RepresentationIndex[self.CurrentFigure] = 3
        self.update_graph(
            self.spectrum[self.currentFileIndex].getFreq(),
            self.spectrum[self.currentFileIndex].getData(
                self.RepresentationIndex[0]),
            self.spectrum[self.currentFileIndex].getData(
                self.RepresentationIndex[1]))

    def doPhaS11(self):
        self.RepresentationIndex[self.CurrentFigure] = 4
        self.update_graph(
            self.spectrum[self.currentFileIndex].getFreq(),
            self.spectrum[self.currentFileIndex].getData(
                self.RepresentationIndex[0]),
            self.spectrum[self.currentFileIndex].getData(
                self.RepresentationIndex[1]))

    def doReZ(self):
        self.RepresentationIndex[self.CurrentFigure] = 5
        self.update_graph(
            self.spectrum[self.currentFileIndex].getFreq(),
            self.spectrum[self.currentFileIndex].getData(
                self.RepresentationIndex[0]),
            self.spectrum[self.currentFileIndex].getData(
                self.RepresentationIndex[1]))

    def doImZ(self):
        self.RepresentationIndex[self.CurrentFigure] = 6
        self.update_graph(
            self.spectrum[self.currentFileIndex].getFreq(),
            self.spectrum[self.currentFileIndex].getData(
                self.RepresentationIndex[0]),
            self.spectrum[self.currentFileIndex].getData(
                self.RepresentationIndex[1]))

    def doPreviousFile(self):
        if self.currentFileIndex > 0:
            self.currentFileIndex -= 1
            self.update_graph(
                self.spectrum[self.currentFileIndex].getFreq(),
                self.spectrum[self.currentFileIndex].getData(
                    self.RepresentationIndex[0]),
                self.spectrum[self.currentFileIndex].getData(
                    self.RepresentationIndex[1]))

    def doNextFile(self):
        if self.currentFileIndex < self.numberOfFiles-1:
            self.currentFileIndex += 1
            self.update_graph(
                self.spectrum[self.currentFileIndex].getFreq(),
                self.spectrum[self.currentFileIndex].getData(
                    self.RepresentationIndex[0]),
                self.spectrum[self.currentFileIndex].getData(
                    self.RepresentationIndex[1]))

    def update_graph(self, x, y1, y2):
        self.ui.MplWidget_0.canvas.axes1.clear()
        self.ui.MplWidget_0.canvas.axes1.plot(x, y1)
        self.ui.MplWidget_0.canvas.axes1.set_ylabel(
            self.YLabels[self.RepresentationIndex[0]-1])
        self.ui.MplWidget_0.canvas.axes1.set_xlabel("f (MHz)")
        self.ui.MplWidget_0.canvas.axes2.clear()
        self.ui.MplWidget_0.canvas.axes2.plot(x, y2)
        self.ui.MplWidget_0.canvas.axes2.set_ylabel(
            self.YLabels[self.RepresentationIndex[1]-1])
        self.ui.MplWidget_0.canvas.axes2.set_xlabel("f (MHz)")
        self.ui.MplWidget_0.canvas.figure.tight_layout()
        self.ui.MplWidget_0.canvas.draw()
        self.ui.labelFileName.setText(
            "File Name: " + self.spectrum[self.currentFileIndex].getFileName())

    def doAllFiles(self):
        self.ui.MplWidget_0.canvas.axes1.clear()
        self.ui.MplWidget_0.canvas.axes2.clear()
        lg = []
        for i in range(len(self.spectrum)):
            self.ui.MplWidget_0.canvas.axes1.plot(
                self.spectrum[i].getFreq(),
                self.spectrum[i].getData(self.RepresentationIndex[0]))
            self.ui.MplWidget_0.canvas.axes2.plot(
                self.spectrum[i].getFreq(),
                self.spectrum[i].getData(self.RepresentationIndex[1]))
            lg.append(str(i))
        self.ui.MplWidget_0.canvas.axes1.set_ylabel(
            self.YLabels[self.RepresentationIndex[0]-1])
        self.ui.MplWidget_0.canvas.axes1.set_xlabel("f (MHz)")
        self.ui.MplWidget_0.canvas.axes1.legend(lg)
        self.ui.MplWidget_0.canvas.axes2.set_ylabel(
            self.YLabels[self.RepresentationIndex[1]-1])
        self.ui.MplWidget_0.canvas.axes2.set_xlabel("f (MHz)")
        self.ui.MplWidget_0.canvas.axes2.legend(lg)
        self.ui.MplWidget_0.canvas.figure.tight_layout()
        self.ui.MplWidget_0.canvas.draw()
        self.ui.labelFileName.setText("All Files")
