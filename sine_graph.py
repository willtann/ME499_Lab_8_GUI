#!/usr/bin/env python3
from counter import Interface
from slider import SliderDisplay
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import math
from random import random


class Grapher(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('Grapher')

        # Control buttons for the interface
        quit_button = QPushButton('Quit')
        quit_button.clicked.connect(app.exit)

        graph_button = QPushButton('Graph')
        graph_button.clicked.connect(self.graph)

        # The display for the graph
        self.figure = Figure()
        self.display = FigureCanvas(self.figure)
        self.figure.clear()

        # The layout of the interface
        widget = QWidget()
        self.setCentralWidget(widget)

        """ Add Graph Button"""
        top_level_layout = QHBoxLayout()
        widget.setLayout(top_level_layout)
        left_side_layout = QVBoxLayout()
        left_side_layout.addWidget(graph_button)

        """ Add Value Sliders """
        amplitude = SliderDisplay('Amplitude', 0, 5)
        self.amp_in = amplitude.curr_val
        left_side_layout.addWidget(amplitude)

        frequency = SliderDisplay('Frequency', 0, 5, units='Hz')
        self.freq_in = frequency.curr_val
        left_side_layout.addWidget(frequency)

        phase = SliderDisplay('Phase Shift', 0, 1, units="rad")
        self.phase_in = phase.curr_val
        left_side_layout.addWidget(phase)

        """ Add Quit Button"""
        left_side_layout.addStretch()
        left_side_layout.addWidget(quit_button)

        """ Add Plot window """
        top_level_layout.addLayout(left_side_layout)
        top_level_layout.addWidget(self.display)

    def graph(self):
        self.draw([random() for i in range(25)])
        return self.draw

    def draw(self, data):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(data)
        ax.set_xlim([0, 5])
        ax.set_ylim([-5, 5])
        ax.set_title('title')
        ax.set_xlabel('sin(x)')
        ax.set_ylabel('x[rad')
        self.display.draw()


if __name__ == '__main__':
    app = QApplication([])

    gui = Grapher()
    print(gui.draw)
    gui.show()

    app.exec_()
