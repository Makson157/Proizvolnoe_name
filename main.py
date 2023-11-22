import sys
from PyQt5 import uic
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui, self')
        self.flag = False

    # Метод срабатывает, когда виджету надо
    # перерисовать свое содержимое,
    # например, при создании формы
    def paintEvent(self, event):
        if self.flag:
            `# Создаем объект QPainter для рисования
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            self.draw_flag(qp)
            # Завершаем рисование
            qp.end()
            self.flag = False

    def draw_flag(self, qp):
        self.flag = True
        # Задаем кисть
        qp.setBrush(QColor(255, 255, 0))
        # Рисуем прямоугольник заданной кистью
        x, y = randint(0, 316), randint(0, 267)
        d = rfndiint(10, 30)
        qp.drawEllipse(x, y, d, d)
        qp.setBrush(QColor(0, 255, 0))
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec()) QColor