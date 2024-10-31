import sys
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ボタンを追加') # ウィンドウのタイトル
        self.setGeometry(100,100,200,150) # ウィンドウの位置と大きさ
        button = QPushButton('ボタン',self)
        button.setGeometry(25,25,150,100)
        button.clicked.connect(self.clicked)
        self.show()
    def clicked(self):
        print('ボタンをクリックしました')
        
qAp = QApplication(sys.argv)
win = Window()
qAp.exec()