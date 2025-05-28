"""
Файл для повторения темы сигналов

Напомнить про работу с сигналами и изменением Ui.

Предлагается создать приложение, которое принимает в lineEditInput строку от пользователя,
и при нажатии на pushButtonMirror отображает в lineEditMirror введённую строку в обратном
порядке (задом наперед).
"""

from PySide6 import QtWidgets
from a import Ui_Form


class Window(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.count = 0

        self.setupUi(self)
        self.__initSignals()

    def __initUi(self):
        pass


    def __initSignals(self):
        self.pushButtonMirror.clicked.connect(self.__onPushButtonMirrorClicked)
        self.pushButtonClear.clicked.connect(self.lineEditMirror.clear)
        self.lineEditInput.textChanged.connect(self.__onLineEditMirrorTextChanged)


    def __onPushButtonMirrorClicked(self):
        self.count += 1
        text = self.lineEditInput.text()
        self.lineEditMirror.setText(text[::-1])
        print(f'Нажали на кнопку {self.count} раз')

    def __onPushButtonClearClicked(self):
        pass

    def __onLineEditMirrorTextChanged(self, text):
        self.lineEditMirror.setText(text[::-1])
        print(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
