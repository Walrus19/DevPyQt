"""
Файл для повторения темы QSettings

Напомнить про работу с QSettings.

Предлагается создать виджет с plainTextEdit на нём, при закрытии приложения,
сохранять введённый в нём текст с помощью QSettings, а при открытии устанавливать
в него сохранённый текст
"""

from PySide6 import QtWidgets
from PySide6.QtCore import QSettings

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUi()

    def __initUi(self):
        self.__plainTextEdit = QtWidgets.QPlainTextEdit()
        self.__plainTextEdit.setPlainText()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.__plainTextEdit)
        self.setLayout(layout)
    def __loadSettings(self):
        self.settings = QSettings()
        return self.settings.value(self.__plainTextEdit)

    def __saveSettings(self):
        self.settings = QSettings()
        return self.settings.setValue(self.__plainTextEdit)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

