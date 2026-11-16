from PyQt5.QtWidgets import (
    QLabel, 
    QApplication,                   
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout
)
from PyQt5.QtCore import Qt



class HolirScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
        
    def set_appear(self):
        self.resize(1280,720)
        self.setWindowTitle("Початок")