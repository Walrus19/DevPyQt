"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events_form.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""


from PySide6 import QtWidgets, QtCore
from ui.c_signals_events_form import Ui_Form


class Window(QtWidgets.QWidget, Ui_Form):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.w_screen, self.h_screen = QtWidgets.QApplication.primaryScreen().size().toTuple()
        self.setupUi(self)
        self.spinBoxX.setMaximum(self.w_screen-self.size().width())
        self.spinBoxY.setMaximum(self.h_screen - self.size().height())
        self.spinBoxY.setValue(500)
        self.spinBoxX.setValue(500)
        print(self.pos().toTuple())
        # self.spinBoxX.setValue(int(self.x()))
        # self.spinBoxY.setValue(int(self.y()))

        self.initSignals()

        # self.move(0, 0)


    def initSignals(self):
        self.pushButtonGetData.clicked.connect(self.get_state_data)
        self.pushButtonMoveCoords.clicked.connect(lambda: self.move(self.spinBoxX.value(), self.spinBoxY.value()))



    def get_state_data(self):
        # print(QtWidgets.QApplication.screens())
        data = f"""
        Кол-во экранов: {len(QtWidgets.QApplication.screens())}
        Основное окно: {QtWidgets.QApplication.primaryScreen().name()}
        Разрешение экрана: Ширина = {self.w_screen}, Высота = {self.h_screen}
        Размеры окна: {self.size().width()} x {self.size().height()}
        Минимальный размер: {self.minimumSize().toTuple()}
        Максимальный размер: {self.maximumSize().toTuple()}
        Координаты окна: {self.x()}, {self.y()}
        Координаты окна: {self.pos().toTuple()}
        Центр: {self.rect().center().toTuple()}
        Состояние: {self.windowState().name}
        """
        self.plainTextEdit.appendPlainText(data)

    def resizeEvent(self, event, /):
        print(self.size())
        return super().resizeEvent(event)

    # def event(self, event, /):
    #     if type(e
    #     print(event)
    #     return super().event(event)



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
