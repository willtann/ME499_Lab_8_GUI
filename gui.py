#! /Users/tannerwilliams/.conda/envs/untitled/bin/python
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QSlider, QLabel


""" References:
    [1] https://zetcode.com/pyqt/qslider/
    [2] 
    [3]
"""

class Interface(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('This is my fancy window for stuff')

        # A widget to hold everything
        widget = QWidget()
        self.setCentralWidget(widget)
        self.setFixedSize(400, 300)

        # A layout
        layout = QVBoxLayout()
        widget.setLayout(layout)

        # A button
        quit_button = QPushButton('Quit')
        quit_button.clicked.connect(app.exit)

        # You probably want to add in other interface elements here

        """ Value label """
        self.label = QLabel('0', self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        """ Adding slider """
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setRange(0, 10)
        self.slider.valueChanged.connect(self.current_label)
        layout.addWidget(self.slider)

        """ Quit Button """
        layout.addWidget(quit_button)

    # convert slider value to string for label
    def current_label(self, value):
        self.label.setText(str(value))


if __name__ == '__main__':
    app = QApplication([])

    interface = Interface()

    interface.show()

    app.exec_()

