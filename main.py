import sys
import random as rd
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from Yandex_rep_3.interface import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()


        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()


    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        r = rd.randint(0, 255)
        g = rd.randint(0, 255)
        b = rd.randint(0, 255)

        a = rd.randint(50, 500)
        c = rd.randint(50, 500)
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(a, a, c, c)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())