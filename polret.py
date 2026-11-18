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
from lokp import KolirScreen


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
        
    def initUI(self):
        self.text_1 = QLabel("Ласково просимо у програмі Безпека Захисту Індівідуальних Данів і Логічне розвязання. Ця програма пивина вам допомогти до знаходень роботи і до фаілів.")
        
        
        self.lb_login = QLabel("Веди свій І.П.Д.")
        self.le_name = QLineEdit()
        self.le_name.setPlaceholderText("І.П.Д.")
        self.le_name.setFixedSize(250, 35)
        self.le_name.setStyleSheet("font-size: 14px;")
        self.btn_start = QPushButton("Почати!")
        
        
        self.k_main = QVBoxLayout()
        self.k_main.addWidget(self.text_1, alignment=Qt.AlignmentFlag.AlignCenter)
        self.k_main.setContentsMargins(0, 60, 0, 0)
        self.v_main = QVBoxLayout()
        self.v_main = QVBoxLayout()
        

        self.v_main.addLayout(self.k_main)
        self.v_main.addStretch()
       
        self.h_row1 = QHBoxLayout()
        self.h_row1.addStretch()
        
        self.h_row1.addWidget(self.lb_login)
        self.h_row1.addWidget(self.le_name)
        self.h_row1.addStretch()
        self.v_main.addLayout(self.h_row1)
        self.v_main.addWidget(self.btn_start, alignment=Qt.AlignmentFlag.AlignBottom)
        self.v_main.addStretch()
        
        self.setLayout(self.v_main)
        
        
        
    def connects(self):
        self.btn_start.clicked.connect(self.nex_click)

 
    def nex_click(self):
        name = self.le_name.text()
        self.hide()
        self.lokp_screen = KolirScreen(name)
        self.lokp_screen.show()    