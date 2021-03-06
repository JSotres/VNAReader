# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vnaReaderMainWindow_v0.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from .mplwidget import MplWidget

class Ui_MainVNAReaderWindow(object):
    def setupUi(self, MainVNAReaderWindow):
        MainVNAReaderWindow.setObjectName("MainVNAReaderWindow")
        MainVNAReaderWindow.resize(702, 553)
        MainVNAReaderWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainVNAReaderWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.pushButtonAllFiles = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAllFiles.sizePolicy().hasHeightForWidth())
        self.pushButtonAllFiles.setSizePolicy(sizePolicy)
        self.pushButtonAllFiles.setObjectName("pushButtonAllFiles")
        self.gridLayout.addWidget(self.pushButtonAllFiles, 0, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 3, 1, 1)
        self.pushButtonNextFile = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonNextFile.sizePolicy().hasHeightForWidth())
        self.pushButtonNextFile.setSizePolicy(sizePolicy)
        self.pushButtonNextFile.setObjectName("pushButtonNextFile")
        self.gridLayout.addWidget(self.pushButtonNextFile, 0, 2, 1, 1)
        self.pushButtonPreviousFile = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonPreviousFile.sizePolicy().hasHeightForWidth())
        self.pushButtonPreviousFile.setSizePolicy(sizePolicy)
        self.pushButtonPreviousFile.setObjectName("pushButtonPreviousFile")
        self.gridLayout.addWidget(self.pushButtonPreviousFile, 0, 0, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelCurrentFigure = QtWidgets.QLabel(self.centralwidget)
        self.labelCurrentFigure.setObjectName("labelCurrentFigure")
        self.horizontalLayout_3.addWidget(self.labelCurrentFigure)
        spacerItem4 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.comboBoxCurrentFigure = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxCurrentFigure.setObjectName("comboBoxCurrentFigure")
        self.comboBoxCurrentFigure.addItem("")
        self.comboBoxCurrentFigure.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBoxCurrentFigure)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.labelFileName = QtWidgets.QLabel(self.centralwidget)
        self.labelFileName.setMinimumSize(QtCore.QSize(500, 20))
        self.labelFileName.setAlignment(QtCore.Qt.AlignCenter)
        self.labelFileName.setObjectName("labelFileName")
        self.horizontalLayout_6.addWidget(self.labelFileName)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem9 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.MplWidget_0 = MplWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MplWidget_0.sizePolicy().hasHeightForWidth())
        self.MplWidget_0.setSizePolicy(sizePolicy)
        self.MplWidget_0.setMinimumSize(QtCore.QSize(600, 300))
        self.MplWidget_0.setObjectName("MplWidget_0")
        self.horizontalLayout_2.addWidget(self.MplWidget_0)
        spacerItem10 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem11 = QtWidgets.QSpacerItem(17, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem11)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonReS11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonReS11.setObjectName("pushButtonReS11")
        self.horizontalLayout.addWidget(self.pushButtonReS11)
        self.pushButtonImS11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonImS11.sizePolicy().hasHeightForWidth())
        self.pushButtonImS11.setSizePolicy(sizePolicy)
        self.pushButtonImS11.setObjectName("pushButtonImS11")
        self.horizontalLayout.addWidget(self.pushButtonImS11)
        self.pushButtonModS11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonModS11.setObjectName("pushButtonModS11")
        self.horizontalLayout.addWidget(self.pushButtonModS11)
        self.pushButtonPhaS11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonPhaS11.sizePolicy().hasHeightForWidth())
        self.pushButtonPhaS11.setSizePolicy(sizePolicy)
        self.pushButtonPhaS11.setObjectName("pushButtonPhaS11")
        self.horizontalLayout.addWidget(self.pushButtonPhaS11)
        self.pushButtonReZ = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonReZ.sizePolicy().hasHeightForWidth())
        self.pushButtonReZ.setSizePolicy(sizePolicy)
        self.pushButtonReZ.setObjectName("pushButtonReZ")
        self.horizontalLayout.addWidget(self.pushButtonReZ)
        self.pushButtonImZ = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonImZ.sizePolicy().hasHeightForWidth())
        self.pushButtonImZ.setSizePolicy(sizePolicy)
        self.pushButtonImZ.setObjectName("pushButtonImZ")
        self.horizontalLayout.addWidget(self.pushButtonImZ)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem13)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainVNAReaderWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainVNAReaderWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 702, 22))
        self.menubar.setObjectName("menubar")
        self.menuOpen = QtWidgets.QMenu(self.menubar)
        self.menuOpen.setObjectName("menuOpen")
        self.menuAnalysis = QtWidgets.QMenu(self.menubar)
        self.menuAnalysis.setObjectName("menuAnalysis")
        MainVNAReaderWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainVNAReaderWindow)
        self.statusbar.setObjectName("statusbar")
        MainVNAReaderWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainVNAReaderWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSingleAntenna = QtWidgets.QAction(MainVNAReaderWindow)
        self.actionSingleAntenna.setObjectName("actionSingleAntenna")
        self.actionCoupledAntennas = QtWidgets.QAction(MainVNAReaderWindow)
        self.actionCoupledAntennas.setObjectName("actionCoupledAntennas")
        self.menuOpen.addAction(self.actionOpen)
        self.menuAnalysis.addAction(self.actionSingleAntenna)
        self.menuAnalysis.addAction(self.actionCoupledAntennas)
        self.menubar.addAction(self.menuOpen.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())

        self.retranslateUi(MainVNAReaderWindow)
        QtCore.QMetaObject.connectSlotsByName(MainVNAReaderWindow)

    def retranslateUi(self, MainVNAReaderWindow):
        _translate = QtCore.QCoreApplication.translate
        MainVNAReaderWindow.setWindowTitle(_translate("MainVNAReaderWindow", "VNA Reader"))
        self.pushButtonAllFiles.setText(_translate("MainVNAReaderWindow", "All"))
        self.pushButtonNextFile.setText(_translate("MainVNAReaderWindow", ">"))
        self.pushButtonPreviousFile.setText(_translate("MainVNAReaderWindow", "<"))
        self.labelCurrentFigure.setText(_translate("MainVNAReaderWindow", "Figure:"))
        self.comboBoxCurrentFigure.setItemText(0, _translate("MainVNAReaderWindow", "Figure 1"))
        self.comboBoxCurrentFigure.setItemText(1, _translate("MainVNAReaderWindow", "Figure 2"))
        self.labelFileName.setText(_translate("MainVNAReaderWindow", "-"))
        self.pushButtonReS11.setText(_translate("MainVNAReaderWindow", "Re S11"))
        self.pushButtonImS11.setText(_translate("MainVNAReaderWindow", "Im S11"))
        self.pushButtonModS11.setText(_translate("MainVNAReaderWindow", "Mod S11"))
        self.pushButtonPhaS11.setText(_translate("MainVNAReaderWindow", "Pha S11"))
        self.pushButtonReZ.setText(_translate("MainVNAReaderWindow", "Re Z"))
        self.pushButtonImZ.setText(_translate("MainVNAReaderWindow", "Im Z"))
        self.menuOpen.setTitle(_translate("MainVNAReaderWindow", "File"))
        self.menuAnalysis.setTitle(_translate("MainVNAReaderWindow", "Analysis"))
        self.actionOpen.setText(_translate("MainVNAReaderWindow", "Open"))
        self.actionSingleAntenna.setText(_translate("MainVNAReaderWindow", "Single Antenna"))
        self.actionCoupledAntennas.setText(_translate("MainVNAReaderWindow", "Coupled Antennas"))


