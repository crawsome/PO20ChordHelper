from PyQt5 import QtGui
from PyQt5 import QtWidgets, QtCore

from window import Ui_MainWindow
from sys import argv, exit
from chord_data import *

from PyQt5.QtWidgets import QApplication, QFrame


class PO20Chords(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(PO20Chords, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.w = self.window()

        self.chordfields = [self.w.chord1, self.w.chord2, self.w.chord3, self.w.chord4,
                            self.w.chord5, self.w.chord6, self.w.chord7, self.w.chord8,
                            self.w.chord9, self.w.chord10, self.w.chord11, self.w.chord12,
                            self.w.chord13, self.w.chord14, self.w.chord15, self.w.chord16, ]

        self.symbolfields = [self.w.symbol1, self.w.symbol2, self.w.symbol3, self.w.symbol4,
                             self.w.symbol5, self.w.symbol6, self.w.symbol7, self.w.symbol8,
                             self.w.symbol9, self.w.symbol10, self.w.symbol11, self.w.symbol12,
                             self.w.symbol13, self.w.symbol14, self.w.symbol15, self.w.symbol16]

        chord_radio_buttons = [self.w.amrb, self.w.emrb, self.w.dmrb,
                               self.w.crb, self.w.grb, self.w.frb,
                               self.w.erb, self.w.drb, self.w.arb]
        # Directory where piano chord images are stored
        self.picdir = 'img/'

        # var for storing our permutation of chords / blanks
        self.ourkey = ''
        self.oursymbols = []
        self.ourchords = []

        self.background_active = False
        self.background_pixmap = QtGui.QPixmap(self.picdir + 'PO20face.png')
        self.w.backgroundimage.lower()

        self.chord_pixmap: QtGui.QPixmap

        self.w.amrb.clicked.connect(lambda: self.get_buttonstate(self.w.amrb))
        self.w.emrb.clicked.connect(lambda: self.get_buttonstate(self.w.emrb))
        self.w.dmrb.clicked.connect(lambda: self.get_buttonstate(self.w.dmrb))
        self.w.crb.clicked.connect(lambda: self.get_buttonstate(self.w.crb))
        self.w.grb.clicked.connect(lambda: self.get_buttonstate(self.w.grb))
        self.w.frb.clicked.connect(lambda: self.get_buttonstate(self.w.frb))
        self.w.erb.clicked.connect(lambda: self.get_buttonstate(self.w.erb))
        self.w.drb.clicked.connect(lambda: self.get_buttonstate(self.w.drb))
        self.w.arb.clicked.connect(lambda: self.get_buttonstate(self.w.arb))

        self.w.chord1.clicked.connect(lambda: self.apply_chordimage(self.w.chord1))
        self.w.chord2.clicked.connect(lambda: self.apply_chordimage(self.w.chord2))
        self.w.chord3.clicked.connect(lambda: self.apply_chordimage(self.w.chord3))
        self.w.chord4.clicked.connect(lambda: self.apply_chordimage(self.w.chord4))
        self.w.chord5.clicked.connect(lambda: self.apply_chordimage(self.w.chord5))
        self.w.chord6.clicked.connect(lambda: self.apply_chordimage(self.w.chord6))
        self.w.chord7.clicked.connect(lambda: self.apply_chordimage(self.w.chord7))
        self.w.chord8.clicked.connect(lambda: self.apply_chordimage(self.w.chord8))
        self.w.chord9.clicked.connect(lambda: self.apply_chordimage(self.w.chord9))
        self.w.chord10.clicked.connect(lambda: self.apply_chordimage(self.w.chord10))
        self.w.chord11.clicked.connect(lambda: self.apply_chordimage(self.w.chord11))
        self.w.chord12.clicked.connect(lambda: self.apply_chordimage(self.w.chord12))
        self.w.chord13.clicked.connect(lambda: self.apply_chordimage(self.w.chord13))
        self.w.chord14.clicked.connect(lambda: self.apply_chordimage(self.w.chord14))
        self.w.chord15.clicked.connect(lambda: self.apply_chordimage(self.w.chord15))
        self.w.chord16.clicked.connect(lambda: self.apply_chordimage(self.w.chord16))

        self.w.actionAbout_2.triggered.connect(self.about_menu_window)
        self.actionbackground.triggered.connect(self.toggle_background)
        self.w.actionQuit.triggered.connect(self.quit)
        self.actionShow_all_chords.triggered.connect(self.show_all_chords)

    # Quit the program
    def quit(self):
        exit(self)

    # Generic popup info window
    def popup_window(self, msg='You didn\'t provide a message!', title='INFO'):
        qm = QtWidgets.QMessageBox()
        qm.setFixedSize(500, 200)
        qm.setWindowTitle(title)
        qm.setText(msg)
        qm.exec()
        return

    # set the chord image based on chords current string in the box
    def apply_chordimage(self, b):
        if not b.text() or b.text() == '...':
            self.window().imagelabel.hide()
            return
        self.window().imagelabel.show()
        imagename = str(sym_master_simp[b.text()])
        self.chord_pixmap = QtGui.QPixmap(self.picdir + f'{imagename}.png')
        self.window().imagelabel.setPixmap(self.chord_pixmap)

    # toggle ON/OFF the pocket Operator background. Did my best :P
    def toggle_background(self):
        # Tip: you can copy a stylesheet like this
        # ss = self.w.chord1.styleSheet()
        # I feel like looping the stylesheet application below was a really cool thing

        if self.background_active:
            self.w.backgroundimage.hide()
            for chordfield in self.chordfields:
                chordfield.setStyleSheet("QPushButton{color: Black;background: normal;}")
            for symbolfield in self.symbolfields:
                symbolfield.setStyleSheet("QLabel{color: Black}")
            self.background_active = False
        else:
            self.w.backgroundimage.show()
            for chordfield in self.chordfields:
                chordfield.setStyleSheet("QPushButton{color: Yellow;background: Transparent;}")
            for index, symbolfield in enumerate(self.symbolfields):
                symbolfield.setStyleSheet("QLabel{color: Yellow;background:black;}")

            self.w.backgroundimage.setPixmap(self.background_pixmap)
            self.w.backgroundimage.lower()
            self.background_active = True

    def get_buttonstate(self, b):
        self.ourkey = b.objectName()

        chart_mappings = {'amrb': sym_am, 'crb': sym_c, 'erb': sym_e,
                          'emrb': sym_em, 'grb': sym_g, 'drb': sym_d,
                          'dmrb': sym_dm, 'frb': sym_f, 'arb': sym_a}

        self.keylabel.setText(b.text())
        self.oursymbols = chart_mappings[self.ourkey]
        self.ourchords = []
        try:
            for index, sym in enumerate(self.oursymbols):
                if sym:
                    self.ourchords.append(sym_master[index])
                else:
                    self.ourchords.append('')
            self.apply_key()
        except Exception as e:
            print(e)

    # this maps to View -> Show All. Shows all chords.
    def show_all_chords(self):
        self.ourchords = []
        self.oursymbols = []
        self.ourchords = sym_master
        for index, i in enumerate(self.ourchords):
            self.oursymbols.append(str(index + 1))
        self.apply_key()

    # writes each cel to each property
    def apply_key(self):
        # this step writes the chord symbols above the boxes
        for index, field in enumerate(self.symbolfields):
            field.setText('')
            field.setText(self.oursymbols[index])

        # this writes the chord names in the boxes
        for index, field in enumerate(self.chordfields):
            field.setText('')
            field.setText(self.ourchords[index])

    # Menu popup for the About menu. I wanted it to be portable and dynamic.
    def about_menu_window(self):
        dm = QtWidgets.QDialog()
        dm.setWindowTitle('About PO-20 Chord Helper')
        dm.setFixedSize(400, 280)
        dm.setObjectName("aboutwindow")
        dm.resize(400, 300)
        dm.setWindowIcon(QtGui.QIcon('icon.png'))
        okbutton = QtWidgets.QPushButton(dm)
        okbutton.setGeometry(QtCore.QRect(255, 210, 80, 25))
        okbutton.setObjectName("okbutton")
        okbutton.clicked.connect(dm.close)
        frame = QtWidgets.QFrame(dm)
        frame.setGeometry(QtCore.QRect(10, 70, 180, 180))
        frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame.setFrameShadow(QtWidgets.QFrame.Raised)
        frame.setObjectName("frame")
        imagelabel = QtWidgets.QLabel(frame)
        imagelabel.setGeometry(QtCore.QRect(10, 10, 160, 160))
        font = QtGui.QFont()
        font.setPointSize(36)
        imagelabel.setScaledContents(True)
        imagelabel.setAlignment(QtCore.Qt.AlignCenter)
        imagelabel.setObjectName("imagelabel")
        qr_pixmap = QtGui.QPixmap(self.picdir + 'venmo.png')
        qr_pixmap.scaled(130, 110)
        imagelabel.setPixmap(qr_pixmap)
        imagelabel.update()

        font = QtGui.QFont()
        label = QtWidgets.QLabel(dm)
        label_2 = QtWidgets.QLabel(dm)
        label_3 = QtWidgets.QLabel(dm)
        label_4 = QtWidgets.QLabel(dm)
        label_5 = QtWidgets.QLabel(dm)

        label.setAlignment(QtCore.Qt.AlignLeft)
        label_2.setAlignment(QtCore.Qt.AlignLeft)
        label_3.setAlignment(QtCore.Qt.AlignLeft)
        label_4.setAlignment(QtCore.Qt.AlignHCenter)
        label_5.setAlignment(QtCore.Qt.AlignLeft)

        label.setObjectName("label")
        label_2.setObjectName("label_2")
        label_3.setObjectName("label_3")
        label_4.setObjectName("label_4")
        label_5.setObjectName("label_5")

        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        label_2.setFont(font)

        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        label_3.setFont(font)

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        label_4.setFont(font)

        font = QtGui.QFont()
        font.setUnderline(True)
        label_5.setFont(font)

        label.setGeometry(QtCore.QRect(240, 150, 110, 50))
        label_2.setGeometry(QtCore.QRect(40, 10, 70, 50))
        label_3.setGeometry(QtCore.QRect(40, 30, 320, 50))
        label_4.setGeometry(QtCore.QRect(30, 240, 140, 50))
        label_5.setGeometry(QtCore.QRect(240, 100, 140, 50))

        _translate = QtCore.QCoreApplication.translate

        dm.setWindowTitle(_translate("aboutwindow", "Unofficial PO-20 Chord Navigator"))
        okbutton.setText(_translate("aboutwindow", "OK"))
        # imagelabel.setText(_translate("aboutwindow", "..."))
        # C:\Users\crawsome\PycharmProjects\po20chords\pochords.py

        label.setText(_translate(
            "aboutwindow", '<b>Website:</b><p><a href="https://colinburke.com">Visit my website!</a></p>'))
        label_2.setText(_translate("aboutwindow", "About"))
        label_3.setText(_translate("aboutwindow",
                                   "Dedicated to hackers and musicians everywhere free-of-cost.<br>Please contribute if this app helped you!"))
        label_4.setText(_translate("aboutwindow", "Venmo QR"))
        label_5.setText(_translate("aboutwindow",
                                   '<b>Github:</b><p><a href="https://github.com/crawsome/PO20ChordHelper">This project on Github</a></p>'))

        label.setOpenExternalLinks(True)
        label_5.setOpenExternalLinks(True)

        try:
            dm.exec()
            imagelabel.update()
            imagelabel.show()
            label.openExternalLinks()
        except Exception as e:
            print(e)


def main():
    app = QApplication(argv)
    form = PO20Chords()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
