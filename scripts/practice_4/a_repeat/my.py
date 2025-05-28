"""
Демонстрация 'зависания' приложения при долгом выполнении слота
"""

import time

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        self.setFixedSize(200, 100)

        layout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel("Отсчёт идёт: ")
        self.button = QtWidgets.QPushButton("Начать")

        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.button.pressed.connect(self.startCounter)

    def startCounter(self) -> None:
        """
        Функция отсчёта до 10 (имитация длительного выполнения функции)

        :return: None
        """

        for i in range(1, 11):
            time.sleep(1)
            self.label.setText(f"Отсчёт идёт: {i} сек.")
            QtWidgets.QApplication.processEvents()  # Добавляем нужную строчку


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = Window()
    window.show()
    app.exec()
Просто? Но НЕПРАВИЛЬНО!

Теперь, при нажатии на кнопку "Начать", ваш код работает без зависаний.

Теперь QApplication.processEvents() периодически передает управление обратно основному циклу событий Qt и позволяет ему реагировать на события как обычно.

Qt принимает события и обработывает их, перед тем как вернется к выполнению оставшейся части долгого кода.

Это работает, но это НЕПРАВИЛЬНО по нескольким причинам.

Во-первых:

когда управление передается обратно в Qt, ваш код больше не выполняется. Это означает, что любая длительная работа, которую вы пытаетесь выполнить, займет больше времени. Это определенно не то, что необходимо.

Во-вторых:

обработка событий вне основного цикла событий (app.exec()) приводит к тому, что ваше приложение переходит к обработке кода (например, для запущенных слотов или событий) внутри вашего цикла. Это может привести к неопределенному поведению.

Приведенный ниже код демонстрирует это в действии:

"""
Демонстрация коллизии в приложении при использовании processEvents()
"""

import time

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        self.setFixedSize(200, 100)

        layout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel("Отсчёт идёт: ")
        self.button = QtWidgets.QPushButton("Начать")
        self.buttonCollision = QtWidgets.QPushButton("Помешать")

        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addWidget(self.buttonCollision)

        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.button.clicked.connect(self.startCounter)
        self.buttonCollision.clicked.connect(lambda: self.label.setText("Я вклинилась в основной поток"))

    def startCounter(self) -> None:
        """
        Функция отсчёта до 10 (имитация длительного выполнения функции)

        :return: None
        """

        for i in range(1, 11):
            time.sleep(1)
            self.label.setText(f"Отсчёт идёт: {i} сек.")
            QtWidgets.QApplication.processEvents()


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = Window()
    window.show()
    app.exec()