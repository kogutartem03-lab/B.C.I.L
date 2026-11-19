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
from melor import *



class MoilScreen(QWidget):
    def __init__(self, name):
        super().__init__()

        self.name = name
        self.set_appear()
        self.initUI()
        #self.connects()
        self.btn_start.clicked.connect(self.check_text)
        self.show()
        
    def set_appear(self):
        self.resize(1280,720)
        self.setWindowTitle("Початок")
        
    def initUI(self):
        self.text_4 = QLabel("місце де спогади")
        self.text_5 = QLabel()
                        
        self.btn_start = QPushButton("кінец?")
        self.main_layout = QVBoxLayout()
        self.center_layout = QVBoxLayout()
        
        self.center_layout.addWidget(self.text_4, alignment=Qt.AlignmentFlag.AlignCenter)            
        self.center_layout.addWidget(self.text_5, alignment=Qt.AlignmentFlag.AlignCenter) 
        self.center_layout.addWidget(self.btn_start, alignment=Qt.AlignmentFlag.AlignCenter)               
        self.main_layout.addLayout(self.center_layout)
        self.setLayout(self.main_layout)
                
        
          
    def check_text(self):
        user_input = self.name
        if user_input == "Word lend":
            self.text_5.setText(TEXT_NERTY_1)
        elif user_input == "197 - A":
            self.text_5.setText(TEXT_NERTY_2)
        elif user_input == "D.Endru":
            self.text_5.setText(TEXT_NERTY_3)
        elif user_input == "gelum album":
            self.text_5.setText(TEXT_NERTY_4)
        else:
            self.text_5.setText("Перепрошуємо ваш запрос може бути не дійсним чи неправдивим будласка перевірте те що ви написали")
        
                               
        
    