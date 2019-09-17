"""
Definition of class to create the main GUI of the program
from the Qt5 created template from vnaReaderMainWindow_v0
"""
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from matplotlib.backends.backend_qt5agg import (
    NavigationToolbar2QT as NavigationToolbar)
from numpy import loadtxt
# local imports:
from ..qt5_ui_files.vnaReaderMainWindow_v0 import Ui_MainVNAReaderWindow
from .definition_class_my_single_antenna_gui import mySingleAntennaGUI
from .definition_class_my_coupled_antennas_gui import myCoupledAntennasGUI
from .definition_class_vna_spectrum import vnaSpectrum


class vnaReaderMainGUI(QMainWindow):
    '''
    Class for creating the main GUI of the program

    Attributes:
        ui: handle to the graphical interface
        spectrum: list of objects from class vnaSpectrum, one corresponding to
            each of loaded files
        RepresentationIndex: list of two components indicating the type of
            data to be plotted in figures 0 and 1.
            Representation #1: Real S11
            Representation #2: Imaginary S11
            Representation #3: Module S11
            Representation #4: Phase S11
            Representation #5: Real Z (normalized over 50 Ohm)
            Representation #6: Imaginary Z (normalized over 50 Ohm)
        YLabels: List of strings for each of the 6 possible data types that
            can be plotted in the figures
        CurrentFigure: handle to the figure (0 or 1) on which actions will
            be applied
        numberOfFiles: number of loaded files
        currentFileIndex: index for the current visualized file
        singleAntennaWindow: handle to objects (GUIs) from the class
            mySingleAntennaGUI opened from Analysis menu
        coupledAntennasWindow: handle to objects (GUIs) from the class
            myCoupledAntennasGUI opened from Analysis menu

    Methods:
        __init__(): Initiates the GUI; Initiatiates attributes ui,
            RepresentationIndex, YLabels and CurrentFigure
        openfiledialog(): Opens File Dialogue, stores and plots data from
            loaded files
        openSingleAntennaWindow(): Opens a new GUI for analysis of the
            visualized data in terms of the equivalent circuit for a
            single antenna
        openCoupledAntennasWindow(): Opens a new GUI for analysis of the
            visualized data in terms of the equivalent circuit of two
            magnetically coupled antennas
        changeCurrentFigure(): Changes the handles to the figure (0 or 1)
            on which actions will be applied
        doReS11(): Represents Re(S11) on the selected figure
        doImS11(): Represents Im(S11) on the selected figure
        doModS11(): Represents the module of S11 on the selected figure
        doPhaS11(): Represents the Phase of S11 on the selected figure
        doReZ(): Represents the real part of the normalized impedance
            on the selected figure
        doImZ(): Represents the imaginary part of the normalized impedance
            on the selected figure
        doPreviousFile(): Visualization of data corresponding to previous file
        doNextFile(): Visualization of data corresponding to next file
            update_graph(x, y1, y2): Updates the plot in both figues with
            those provided as arguments
        doAllFiles(): Simultaneous plot in both figures of data from all
            loaded files
    '''
    def __init__(self):
        '''
        Initialization of the main GUI of the VNA Reader Software
        '''
        super().__init__()
        self.ui = Ui_MainVNAReaderWindow()
        self.ui.setupUi(self)
        # Definitions of actions connected to widgets of the GUI
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
        # Initialization of the RepresentationIndex attribute,
        # Figure 0 will show Re(S11) data and Figure 1 will show Im(S11) data)
        self.RepresentationIndex = ([1, 2])
        self.YLabels = [
            "Re S11", "Im S11", "Mod S11", "Pha S11", "Re Z", "Im Z"]
        # Initially actions will be applied on Figure 0
        self.CurrentFigure = 0
        self.show()

    def openfiledialog(self):
        '''
        Opens File Dialogue, stores and plots data from loaded files
        '''
        caption = "Open File"
        directory = "./vnareader/sample_expdata"
        filter_mask = "All Files (*);;Text Files (*.txt)"
        filenames = QFileDialog.getOpenFileNames(
            self, caption, directory, filter_mask)[0]
        # Initially, and empty list (spectrum) is created
        # Below, each component of this list will correspond to an instance
        # of the vnaSpectrum
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
        '''
        Opens a new GUI for analysis of the visualized data
        in terms of the equivalent circuit for a single antenna
        '''
        self.singleAntennaWindow = mySingleAntennaGUI(
            self.spectrum[self.currentFileIndex])
        self.singleAntennaWindow.show()

    def openCoupledAntennasWindow(self):
        '''
        Opens a new GUI for analysis of the visualized data
        in terms of the equivalent circuit of two magnetically coupled
        antennas
        '''
        self.coupledAntennasWindow = myCoupledAntennasGUI(
            self.spectrum[:], self.currentFileIndex, self.numberOfFiles)
        self.coupledAntennasWindow.show()

    def changeCurrentFigure(self):
        '''
        Changes the handles to the figure (0 or 1) on which actions will
        be applied
        '''
        self.CurrentFigure = self.ui.comboBoxCurrentFigure.currentIndex()

    def doReS11(self):
        '''
        Represents Re(S11) on the selected figure
        '''
        self.RepresentationIndex[self.CurrentFigure] = 1
        self.update_graph(
            self.spectrum[self.currentFileIndex].getFreq(),
            self.spectrum[self.currentFileIndex].getData(
                self.RepresentationIndex[0]),
            self.spectrum[self.currentFileIndex].getData(
                self.RepresentationIndex[1]))

    def doImS11(self):
        '''
        Represents Im(S11) on the selected figure
        '''
        self.RepresentationIndex[self.CurrentFigure] = 2
        self.update_graph(
            self.spectrum[self.currentFileIndex].getFreq(),
            self.spectrum[self.currentFileIndex].getData(
                self.RepresentationIndex[0]),
            self.spectrum[self.currentFileIndex].getData(
                self.RepresentationIndex[1]))

    def doModS11(self):
        '''
        Represents Module of S11 on the selected figure
        '''
        self.RepresentationIndex[self.CurrentFigure] = 3
        self.update_graph(
            self.spectrum[self.currentFileIndex].getFreq(),
            self.spectrum[self.currentFileIndex].getData(
                self.RepresentationIndex[0]),
            self.spectrum[self.currentFileIndex].getData(
                self.RepresentationIndex[1]))

    def doPhaS11(self):
        '''
        Represents Phase of S11 on the selected figure
        '''
        self.RepresentationIndex[self.CurrentFigure] = 4
        self.update_graph(
            self.spectrum[self.currentFileIndex].getFreq(),
            self.spectrum[self.currentFileIndex].getData(
                self.RepresentationIndex[0]),
            self.spectrum[self.currentFileIndex].getData(
                self.RepresentationIndex[1]))

    def doReZ(self):
        '''
        Represents the real part of the normalized impedance
        on the selected figure
        '''
        self.RepresentationIndex[self.CurrentFigure] = 5
        self.update_graph(
            self.spectrum[self.currentFileIndex].getFreq(),
            self.spectrum[self.currentFileIndex].getData(
                self.RepresentationIndex[0]),
            self.spectrum[self.currentFileIndex].getData(
                self.RepresentationIndex[1]))

    def doImZ(self):
        '''
        Represents the imaginary part of the normalized impedance
        on the selected figure
        '''
        self.RepresentationIndex[self.CurrentFigure] = 6
        self.update_graph(
            self.spectrum[self.currentFileIndex].getFreq(),
            self.spectrum[self.currentFileIndex].getData(
                self.RepresentationIndex[0]),
            self.spectrum[self.currentFileIndex].getData(
                self.RepresentationIndex[1]))

    def doPreviousFile(self):
        '''
        Visualization of data corresponding to previous file
        '''
        if self.currentFileIndex > 0:
            self.currentFileIndex -= 1
            self.update_graph(
                self.spectrum[self.currentFileIndex].getFreq(),
                self.spectrum[self.currentFileIndex].getData(
                    self.RepresentationIndex[0]),
                self.spectrum[self.currentFileIndex].getData(
                    self.RepresentationIndex[1]))

    def doNextFile(self):
        '''
        Visualization of data corresponding to next file
        '''
        if self.currentFileIndex < self.numberOfFiles-1:
            self.currentFileIndex += 1
            self.update_graph(
                self.spectrum[self.currentFileIndex].getFreq(),
                self.spectrum[self.currentFileIndex].getData(
                    self.RepresentationIndex[0]),
                self.spectrum[self.currentFileIndex].getData(
                    self.RepresentationIndex[1]))

    def update_graph(self, x, y1, y2):
        '''
        Updates plots in both figues with those provided as arguments
        '''
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
        '''
        Simultaneous plot in both figures of data from all loaded files
        '''
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
