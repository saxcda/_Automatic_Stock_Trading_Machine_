  
import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QGroupBox, QGridLayout, QGraphicsScene, QGraphicsView, QVBoxLayout, QPushButton
from PyQt5.QtGui import QColor 

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas

version = "0.0.0"

class MainWidget(QWidget):
    def __init__(self, parent=None):
        super (MainWidget, self).__init__(parent)

        self.setGeometry(0, 0, 1500, 900)

        col=QColor(255, 255, 255)
        self.setStyleSheet('QWidget{background-color:%s}'%col.name())

        self.setWindowTitle("Machine "+version)
        self.ViewTab = ViewTab()
        self.PlotGroup = PlotGroup()
        self.EmptyGroup_1 = EmptyGroup_1()
        self.EmptyGroup_2 = EmptyGroup_2()
        self.mainWindow()
    
    def mainWindow(self):
        mainLayout = QGridLayout()
        mainLayout.addWidget(self.ViewTab, 0, 0, 3, 1)
        mainLayout.addWidget(self.PlotGroup, 0, 1, 1, 1)
        mainLayout.addWidget(self.EmptyGroup_1, 0, 2, 1, 1)
        mainLayout.addWidget(self.EmptyGroup_2, 1, 1, 2, 2)
        self.setLayout(mainLayout)

class ViewTab(QTabWidget):
    def __init__(self, parent=None):
        super(ViewTab, self).__init__(parent)

        self.setGeometry(0, 0, 900, 900)

        self.generateObject()
        
        for tab, name, tab_type in zip(self.tabs, self.tab_names, self.re_sort_list):
            self.addTab(tab, name)
            self.tabInitialize(tab, tab_type)

    def generateObject(self):

        self.tab_0 = QWidget()
        self.tab_1 = QWidget()
        self.tab_2 = QWidget()
        self.tab_3 = QWidget()
        self.tab_4 = QWidget()
        self.tab_5 = QWidget()

        self.plot_1 = MyPlot()
        self.plot_2 = MyPlot()

        self.scene = QGraphicsScene()
        self.main_view = QGraphicsView(self.scene, self.tab_0)
        self.main_view.setGeometry(0, 0, 600, 600)

        self.normal_view_1 = QGraphicsView(self.scene, self.tab_1)
        self.normal_view_1.setGeometry(0, 0, 600, 600)
        self.normal_view_2 = QGraphicsView(self.scene, self.tab_3)
        self.normal_view_2.setGeometry(0, 0, 600, 600)


        self.tabs = [self.tab_0, self.tab_1, self.tab_2, self.tab_3,self.tab_4]
        self.main_view_list = [self.main_view]
        self.plots = [self.plot_1, self.plot_2]
        self.normal_view_list = [self.normal_view_1, self.normal_view_2]

        self.tab_names = ["Main", "empty", "Plot", "empty", "Plot"]
        self.type_list = [0, 1, 2, 1, 2]

        self.re_sort_list = self.listReSort(self.main_view_list, self.normal_view_list, self.plots, self.type_list)


    def listReSort(self, list_1, list_2, list_3, type_list):

        # put all tab types into the list in order
        
        tmp_list = []

        list_1.reverse()
        list_2.reverse()
        list_3.reverse()

        for tp in type_list:
            if tp == 0 :
                n = list_1.pop()
            elif tp == 1 :
                n = list_2.pop()
            elif tp == 2:
                n = list_3.pop()

            tmp_list.append(n)

        return tmp_list

    def tabInitialize(self, tab, tabtype):
        layout = QVBoxLayout()
        layout.addWidget(tabtype)
        tab.setLayout(layout)
    
class PlotGroup(QGroupBox):
    def __init__(self, parent=None):
        super(PlotGroup, self).__init__(parent)
        
        self.view = ViewTab()
        self.setTitle("Plot Options")

        '''
            1. open plot
            2. close plot
            3. low plot
            4. high plot
            5. volume plot
        '''
        self.plotButton_1 = QPushButton("plotButton_1")
        col=QColor(255, 255, 255)
        self.setStyleSheet('QPushButton{background-color:%s}'%col.name())
        self.plotButton_2 = QPushButton("plotButton_2")
        self.plotButton_3 = QPushButton("plotButton_3")
        self.plotButton_4 = QPushButton("plotButton_4")
        self.plotButton_5 = QPushButton("plotButton_5")
        
        
        layout = QGridLayout()
        layout.addWidget(self.plotButton_1, 0, 0, 1, 1)
        layout.addWidget(self.plotButton_2, 1, 0, 1, 1)
        layout.addWidget(self.plotButton_3, 2, 0, 1, 1)
        layout.addWidget(self.plotButton_4, 3, 0, 1, 1)
        layout.addWidget(self.plotButton_5, 4, 0, 1, 1)
        self.setLayout(layout)

class EmptyGroup_1(QGroupBox):
    def __init__(self, parent=None):
        super(EmptyGroup_1, self).__init__(parent)

        self.setTitle("Empty")

        layout = QGridLayout()

        self.setLayout(layout)

class EmptyGroup_2(QGroupBox):
    def __init__(self, parent=None):
        super(EmptyGroup_2, self).__init__(parent)

        self.setTitle("Empty")

        layout = QGridLayout()

        self.setLayout(layout)

class MyPlot(QWidget):
	def __init__(self, fontsize=12, parent=None):
		super(MyPlot, self).__init__(parent)

		self.fig = Figure(figsize=(8,6))
		self.canvas = Canvas(self.fig)
		plt.rcParams.update({'font.size': fontsize})

		layout = QGridLayout()
		layout.addWidget(self.canvas,0,0,1,2)
		self.setLayout(layout)
		self.ax = self.fig.add_subplot(1, 1, 1)

if  __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = MainWidget()
    widget.show()
    
    os._exit(app.exec_())