from PyQt5.QtWidgets import (
    QLabel, 
    QApplication,                   
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QLineEdit
)
from PyQt5.QtCore import Qt



class HolirScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.set_appear()
        self.initUI()
        #self.connects()
        self.show()
        
    def set_appear(self):
        self.resize(1280,720)
        self.setWindowTitle("Початок")
        
    def initUI(self):
        self.text_1 = QLabel("Ласково просимо у програмі Безпека Захисту Індівідуальних Данів і Логічне розвязання")
        
        
        self.lb_login = QLabel("Веди свій І.П.Д.")
        self.le_name = QLineEdit()
        self.le_name.setPlaceholderText("І.П.Д.")
        
        
        self.k_main = QVBoxLayout()
        self.k_main.addWidget(self.text_1, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v_main = QVBoxLayout()
        
        
       
       
        self.h_row1 = QHBoxLayout()
        
        
        self.h_row1.addWidget(self.lb_login)
        self.h_row1.addWidget(self.le_name)
        self.v_main.addLayout(self.h_row1)
        
        self.setLayout(self.v_main)