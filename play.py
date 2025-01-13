import sys
from PyQt6 import QtCore, QtWidgets, QtMultimedia
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt


class AntiPlagiarism(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.resize(400, 323)
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.do = QtWidgets.QPushButton(parent=self.centralwidget)
        self.do.setGeometry(QtCore.QRect(0, 0, 40, 270))
        self.do.setObjectName("pushButton")
        self.re = QtWidgets.QPushButton(parent=self.centralwidget)
        self.re.setGeometry(QtCore.QRect(50, 0, 40, 270))
        self.re.setObjectName("pushButton_2")
        self.mi = QtWidgets.QPushButton(parent=self.centralwidget)
        self.mi.setGeometry(QtCore.QRect(100, 0, 40, 270))
        self.mi.setObjectName("pushButton_3")
        self.fa = QtWidgets.QPushButton(parent=self.centralwidget)
        self.fa.setGeometry(QtCore.QRect(150, 0, 40, 270))
        self.fa.setObjectName("pushButton_4")
        self.doo = QtWidgets.QPushButton(parent=self.centralwidget)
        self.doo.setGeometry(QtCore.QRect(350, 0, 40, 270))
        self.doo.setObjectName("pushButton_5")
        self.si = QtWidgets.QPushButton(parent=self.centralwidget)
        self.si.setGeometry(QtCore.QRect(300, 0, 40, 270))
        self.si.setObjectName("pushButton_6")
        self.sol = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sol.setGeometry(QtCore.QRect(200, 0, 40, 270))
        self.sol.setObjectName("pushButton_7")
        self.lya = QtWidgets.QPushButton(parent=self.centralwidget)
        self.lya.setGeometry(QtCore.QRect(250, 0, 40, 270))
        self.lya.setObjectName("pushButton_8")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.do.setText(_translate("MainWindow", "До"))
        self.re.setText(_translate("MainWindow", "Ре"))
        self.mi.setText(_translate("MainWindow", "Ми"))
        self.fa.setText(_translate("MainWindow", "Фа"))
        self.doo.setText(_translate("MainWindow", "До"))
        self.si.setText(_translate("MainWindow", "Си"))
        self.sol.setText(_translate("MainWindow", "Соль"))
        self.lya.setText(_translate("MainWindow", "Ля"))

        self.do.clicked.connect(lambda: self.action_play('notes/до.mp3'))
        self.re.clicked.connect(lambda: self.action_play('notes/ре.mp3'))
        self.mi.clicked.connect(lambda: self.action_play('notes/ми.mp3'))
        self.fa.clicked.connect(lambda: self.action_play('notes/фа.mp3'))
        self.sol.clicked.connect(lambda: self.action_play('notes/соль.mp3'))
        self.lya.clicked.connect(lambda: self.action_play('notes/ля.mp3'))
        self.si.clicked.connect(lambda: self.action_play('notes/си.mp3'))
        self.doo.clicked.connect(lambda: self.action_play('notes/до.mp3'))

    def action_play(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        self._audio_output = QtMultimedia.QAudioOutput()
        self._player = QtMultimedia.QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)
        self._audio_output.setVolume(50)
        self._player.setSource(media)
        self._player.play()

    def keyPressEvent(self, event):
        buttons = {
            'C': 'notes/ми.mp3',
            'D': 'notes/фа.mp3',
            'E': 'notes/соль.mp3',
            'F': 'notes/ля.mp3',
            'G': 'notes/си.mp3',
            'A': 'notes/до.mp3',
            'B': 'notes/ре.mp3'
        }
        key = event.key()
        if key in [Qt.Key.Key_C, Qt.Key.Key_D, Qt.Key.Key_E, Qt.Key.Key_F,
                   Qt.Key.Key_G, Qt.Key.Key_A, Qt.Key.Key_B]:
            self.action_play(buttons[chr(key)])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = AntiPlagiarism()
    wnd.show()
    sys.exit(app.exec())
