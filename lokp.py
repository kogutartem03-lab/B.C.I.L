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
from holp import MoilScreen


class KolirScreen(QWidget):
    def __init__(self, name):
        super().__init__()

        self.name = name
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
        
    def set_appear(self):
        self.resize(1280,720)
        self.setWindowTitle("Початок")
        
    def initUI(self):
        self.text_2 = QLabel("вітаємо вас у нрограмі")
        self.text_3 = QLabel(self.name)
        
        self.lb_login = QLabel("Веди свій І.П.Д.")
        self.le_name = QLineEdit()
        self.le_name.setPlaceholderText("І.П.Д.")
        self.le_name.setFixedSize(250, 35)
        self.le_name.setStyleSheet("font-size: 14px;")
        self.btn_start = QPushButton("Почати!")
        
        self.main_layout = QVBoxLayout()
        self.center_layout = QVBoxLayout()
        self.center_layout.addWidget(self.text_2, alignment=Qt.AlignmentFlag.AlignCenter)
        self.center_layout.addWidget(self.text_3, alignment=Qt.AlignmentFlag.AlignCenter) 
        self.center_layout.addStretch(30)
        self.center_layout.addWidget(self.le_name, alignment=Qt.AlignmentFlag.AlignCenter)
        self.center_layout.addWidget(self.btn_start, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addStretch()
        self.main_layout.addLayout(self.center_layout)
        self.main_layout.addStretch()
        
        self.setLayout(self.main_layout)
  
        self.main_layout.addLayout(self.center_layout)
        self.main_layout.addStretch()
       
        
        
        
        
        
    def connects(self):
        self.btn_start.clicked.connect(self.nex_click)


    def nex_click(self):
        name = self.le_name.text()
        self.hide()
        self.holp_screen = MoilScreen(name)   
        self.holp_screen.show()
        
   
            
        
            