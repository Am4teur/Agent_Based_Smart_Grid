# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

import map
from matplotlib import pyplot as plt
import matplotlib.backends.backend_agg as agg
import simulation
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1113, 847)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(30, 30, 151, 31))
        self.label_time.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_time.setFont(font)
        self.label_time.setTextFormat(QtCore.Qt.AutoText)
        self.label_time.setObjectName("label_time")
        self.label_vehicles = QtWidgets.QLabel(self.centralwidget)
        self.label_vehicles.setGeometry(QtCore.QRect(30, 100, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_vehicles.setFont(font)
        self.label_vehicles.setObjectName("label_vehicles")
        self.label_priority = QtWidgets.QLabel(self.centralwidget)
        self.label_priority.setGeometry(QtCore.QRect(30, 180, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_priority.setFont(font)
        self.label_priority.setObjectName("label_priority")
        self.label_stations = QtWidgets.QLabel(self.centralwidget)
        self.label_stations.setGeometry(QtCore.QRect(30, 140, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_stations.setFont(font)
        self.label_stations.setObjectName("label_stations")
        self.label_outages = QtWidgets.QLabel(self.centralwidget)
        self.label_outages.setGeometry(QtCore.QRect(30, 220, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_outages.setFont(font)
        self.label_outages.setObjectName("label_outages")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(420, 20, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_start.setFont(font)
        self.btn_start.setObjectName("btn_start")
        self.disp_time = QtWidgets.QLabel(self.centralwidget)
        self.disp_time.setGeometry(QtCore.QRect(240, 30, 111, 31))
        self.disp_time.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.disp_time.setFont(font)
        self.disp_time.setTextFormat(QtCore.Qt.AutoText)
        self.disp_time.setObjectName("disp_time")
        self.disp_vehicles = QtWidgets.QLabel(self.centralwidget)
        self.disp_vehicles.setGeometry(QtCore.QRect(240, 100, 111, 31))
        self.disp_vehicles.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.disp_vehicles.setFont(font)
        self.disp_vehicles.setTextFormat(QtCore.Qt.AutoText)
        self.disp_vehicles.setObjectName("disp_vehicles")
        self.disp_stations = QtWidgets.QLabel(self.centralwidget)
        self.disp_stations.setGeometry(QtCore.QRect(240, 140, 111, 31))
        self.disp_stations.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.disp_stations.setFont(font)
        self.disp_stations.setTextFormat(QtCore.Qt.AutoText)
        self.disp_stations.setObjectName("disp_stations")
        self.disp_priority = QtWidgets.QLabel(self.centralwidget)
        self.disp_priority.setGeometry(QtCore.QRect(240, 180, 111, 31))
        self.disp_priority.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.disp_priority.setFont(font)
        self.disp_priority.setTextFormat(QtCore.Qt.AutoText)
        self.disp_priority.setObjectName("disp_priority")
        self.disp_outages = QtWidgets.QLabel(self.centralwidget)
        self.disp_outages.setGeometry(QtCore.QRect(240, 220, 111, 31))
        self.disp_outages.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.disp_outages.setFont(font)
        self.disp_outages.setTextFormat(QtCore.Qt.AutoText)
        self.disp_outages.setObjectName("disp_outages")
        self.btn_step = QtWidgets.QPushButton(self.centralwidget)
        self.btn_step.setGeometry(QtCore.QRect(560, 20, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_step.setFont(font)
        self.btn_step.setObjectName("btn_step")
        self.btn_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop.setGeometry(QtCore.QRect(700, 20, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_stop.setFont(font)
        self.btn_stop.setObjectName("btn_stop")
        self.label_map = QtWidgets.QLabel(self.centralwidget)
        self.label_map.setGeometry(QtCore.QRect(410, 100, 701, 651))
        self.label_map.setText("")
        self.label_map.setObjectName("label_map")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(350, 10, 20, 781))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_simulation = QtWidgets.QLabel(self.centralwidget)
        self.label_simulation.setGeometry(QtCore.QRect(30, 300, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_simulation.setFont(font)
        self.label_simulation.setObjectName("label_simulation")
        self.btn_1_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1_1.setGeometry(QtCore.QRect(30, 370, 231, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1_1.setFont(font)
        self.btn_1_1.setObjectName("btn_1_1")
        self.btn_1_N = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1_N.setGeometry(QtCore.QRect(30, 440, 231, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1_N.setFont(font)
        self.btn_1_N.setObjectName("btn_1_N")
        self.btn_N_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_N_1.setGeometry(QtCore.QRect(30, 510, 231, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_N_1.setFont(font)
        self.btn_N_1.setObjectName("btn_N_1")
        self.btn_N_N = QtWidgets.QPushButton(self.centralwidget)
        self.btn_N_N.setGeometry(QtCore.QRect(30, 580, 231, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_N_N.setFont(font)
        self.btn_N_N.setObjectName("btn_N_N")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1113, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.extra()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simulation"))
        self.label_time.setText(_translate("MainWindow", "Time to end:"))
        self.label_vehicles.setText(_translate("MainWindow", "Vehicles:"))
        self.label_priority.setText(_translate("MainWindow", "Priority Vehicles:"))
        self.label_stations.setText(_translate("MainWindow", "Stations:"))
        self.label_outages.setText(_translate("MainWindow", "Power outages:"))
        self.btn_start.setText(_translate("MainWindow", "Start"))
        self.disp_time.setText(_translate("MainWindow", "0"))
        self.disp_vehicles.setText(_translate("MainWindow", "0"))
        self.disp_stations.setText(_translate("MainWindow", "0"))
        self.disp_priority.setText(_translate("MainWindow", "0"))
        self.disp_outages.setText(_translate("MainWindow", "0"))
        self.btn_step.setText(_translate("MainWindow", "Step"))
        self.btn_stop.setText(_translate("MainWindow", "Stop"))
        self.label_simulation.setText(_translate("MainWindow", "Simulation"))
        self.btn_1_1.setText(_translate("MainWindow", "1 DA | 1 CH"))
        self.btn_1_N.setText(_translate("MainWindow", "N DA | 1 CH"))
        self.btn_N_1.setText(_translate("MainWindow", "1 DA | N CH"))
        self.btn_N_N.setText(_translate("MainWindow", "N DA | 1 CH"))


    def extra(self):
        self.disp_time.setText("0")
        self.disp_vehicles.setText("0")
        self.disp_stations.setText("0")
        self.disp_priority.setText("0")
        self.disp_outages.setText("0")
        self.btn_start.setStyleSheet("background-color: green")
        self.btn_start.clicked.connect(self.click_start)
        self.btn_step.setStyleSheet("background-color: #1aa3ff")
        self.btn_step.clicked.connect(self.click_step)
        self.btn_stop.setStyleSheet("background-color: red")
        self.btn_stop.clicked.connect(self.click_stop)

        self.btn_1_1.clicked.connect(self.click_1_1)
        self.btn_1_N.clicked.connect(self.click_1_N)
        self.btn_N_1.clicked.connect(self.click_N_1)
        self.btn_N_N.clicked.connect(self.click_N_N)

        self.map = map.map()
        self.reload_map()


    def click_start(self):
        self.default_map()
        self.disp_time.setText("0")
        print("start")
        self.sim = simulation.simulation()
        self.sim.test( self.map, self)

        

    def click_step(self):
        self.reload_map()
        self.disp_time.setText("1")
        print("step")
        
    def click_stop(self):
        self.empty_map()
        self.disp_time.setText("2")
        self.sim.stop()
        print("stop")
    
    def click_1_1(self):
        print("click_1_1")

    def click_1_N(self):
        print("click_1_N")

    def click_N_1(self):
        print("click_N_1")

    def click_N_N(self):
        print("click_N_N")


    def default_map(self):
        #self.map
        self.label_map.setPixmap(QtGui.QPixmap("images/Alameda_buildings.png"))

    def empty_map(self):
        self.label_map.setText(" ")

    def reload_map(self):
        reload_result = self.map.reload_frame()

        ax = reload_result[1]

        qimage = self.canvasToQImage(ax.figure.canvas)

        # how to get the image of a map
        #mapImg = pygame.image.fromstring(new_map[0], new_map[1], "RGB")

        self.label_map.setPixmap(QtGui.QPixmap(qimage))


    def canvasToQImage(self, canvas):
        data = canvas.buffer_rgba()
        ch = 4
        w, h = canvas.get_width_height()
        bytesPerLine = ch * w
        img = QtGui.QImage(data, w, h, bytesPerLine, QtGui.QImage.Format_ARGB32)
        return img.rgbSwapped()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
