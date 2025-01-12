import sys

from PyQt6.QtWidgets import QLineEdit, QWidget, QPushButton, QApplication


class MorseCode(QWidget):
    def __init__(self):
        super().__init__()
        self.alphabet_buttons = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
                                 'h': '....',
                                 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
                                 'p': '.--.',
                                 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--',
                                 'x': '-..-',
                                 'y': '-.--', 'z': '--..'}
        self.alph_buttons = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
                             'h': '....',
                             'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
                             'p': '.--.',
                             'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--',
                             'x': '-..-',
                             'y': '-.--', 'z': '--..'}
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.initUI()

    def initUI(self):
        def create_connect(x):
            return lambda: self.result.setText(f"{self.result.text()}{self.alph_buttons[x]}")

        self.setGeometry(300, 300, 520, 50)
        self.setWindowTitle('Азбука Морзе 2')

        self.result = QLineEdit(self)
        self.result.move(0, 30)
        self.result.resize(520, 20)
        for key in self.alph_buttons:
            self.button = QPushButton(key, self)
            self.button.resize(20, 20)
            self.button.move(20 * self.alphabet.index(key), 0)
            self.button.clicked.connect(create_connect(key))
            self.alphabet_buttons[key] = self.button


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MorseCode()
    wnd.show()
    sys.exit(app.exec())
