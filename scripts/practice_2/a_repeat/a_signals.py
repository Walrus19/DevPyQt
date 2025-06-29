"""
Файл для повторения темы сигналов

Напомнить про работу с сигналами и изменением Ui.

Предлагается создать приложение, которое принимает в lineEditInput строку от пользователя,
и при нажатии на pushButtonMirror отображает в lineEditMirror введённую строку в обратном
порядке (задом наперед).
"""

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.count = 0

        self.__initUi()
        self.__initSignals()

    def __initUi(self):
        self.layout_h1 = QtWidgets.QHBoxLayout()
        self.layout_h2 = QtWidgets.QHBoxLayout()

        self.lineEditInput = QtWidgets.QLineEdit()
        self.lineEditMirror = QtWidgets.QLineEdit()

        self.pushButtonMirror = QtWidgets.QPushButton('Mirror')
        self.pushButtonClear = QtWidgets.QPushButton('Clear')

        self.layout_h1.addWidget(self.lineEditInput)
        self.layout_h1.addWidget(self.lineEditMirror)

        self.layout_h2.addWidget(self.pushButtonMirror)
        self.layout_h2.addWidget(self.pushButtonClear)

        self.layout_main = QtWidgets.QVBoxLayout()
        self.layout_main.addLayout(self.layout_h1)
        self.layout_main.addLayout(self.layout_h2)

        self.setLayout(self.layout_main)


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

    def keyPressEvent(self, event, /):
        print(event)

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
