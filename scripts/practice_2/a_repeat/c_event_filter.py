"""
Файл для повторения темы фильтр событий

Напомнить про работу с фильтром событий.

Предлагается создать кликабельный QLabel с текстом "Красивая кнопка",
используя html - теги, покрасить разные части текста на нём в разные цвета
(красивая - красным, кнопка - синим)
"""

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__initUi()

    def __initUi(self):
        self.setFixedSize(300, 100)
        # self.setMouseTracking(True)
        html_code = """
        <html>
        <head>
        <style>
        .blue-text {
          color: blue;
        }
        .red-text {
          color: red;
        }
        </style>
        </head>
        <body>
        <p>
         <span class="red-text">Красивая</span> <span class="blue-text">кнопка</span>
        </p>
        </body>
        </html>
        """
        self.__label = QtWidgets.QLabel(html_code)
        self.__label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.__label.installEventFilter(self)  # Установка фильтра событий на конкретный виджет

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.__label)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
