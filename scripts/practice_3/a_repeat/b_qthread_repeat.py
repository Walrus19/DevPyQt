"""
Файл для повторения темы QThread

Напомнить про работу с QThread.

Предлагается создать небольшое приложение, которое будет с помощью модуля request
получать доступность того или иного сайта (возвращать из потока status_code сайта).

Поработать с сигналами, которые возникают при запуске/остановке потока,
передать данные в поток (в данном случае url),
получить данные из потока (статус код сайта),
попробовать управлять потоком (запуск, остановка).

Опционально поработать с валидацией url
"""

from PySide6 import QtWidgets, QtCore
import requests
from site1 import Ui_Form
import time


class CheckerUrl(QtCore.QThread):
    result = QtCore.Signal(int)

    def __init__(self):
        super().__init__()
        self.url = None

    def setUrl(self, url: str):
        self.url = url

    def run(self):
        self.started.emit()

        try:
            response = requests.get(self.url)
            time.sleep(3)
            status_code = response.status_code
            self.result.emit(status_code)
        except requests.RequestException:
            self.result.emit(-1)
        self.finished.emit()


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.thread_check = CheckerUrl()
        self.initSignals()

    def startedThread(self):
        self.thread_check.setUrl(self.ui.lineEdit.text())
        self.thread_check.start()
        self.ui.pushButton.setDisabled(True)


    def set_data(self, data):
        if data == -1:
            self.ui.label.setText('Ошибка доступа к сайту')
        else:
            self.ui.label.setText(str(data))

    def initSignals(self):
        self.ui.pushButton.clicked.connect(self.startedThread)
        self.thread_check.started.connect(lambda: self.ui.label.setText('Запуск потока'))
        self.thread_check.result.connect(self.set_data)
        self.thread_check.finished.connect(lambda: self.ui.pushButton.setDisabled(False))


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

