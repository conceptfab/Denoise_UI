import os
import subprocess
import sys
from datetime import datetime
from sys import platform as _platform

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QFileDialog

# skalowanie interfejsu
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
appver = '0.4.6'


class UiMainWindow:

    def __init__(self):

        # definicje
        self.file_name = None
        self.file_vrimg = None
        self.load_settings = False

        self.log_file_def = 'app.log'
        self.log_file = r'./' + self.log_file_def
        self.logfile = (os.path.exists(self.log_file))

        self.separator = '\n \n#############################################' \
                         '#############################################\n'

        self.consoletext = ''
        self.pathexe = ''
        self.plik = ''
        self.sciezka = []
        self.file_n = False

        self.starttime = datetime.now()
        self.starttimestr = str(datetime.now().strftime("[ %d/%m/%Y  %H:%M:%S ]"))
        self.startstamp = (self.starttimestr + ' Uruchamiam Vdenoise UI '
                           + appver + '\n' + 'Python version: ' + str(sys.version))
        self.logtext = self.separator + self.startstamp

        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.label_3.setFont(QtGui.QFont('Monospaced', 7))
        self.label_3.setText("Plik Vrimg")
        self.label_3.setObjectName("label_3")

        self.layout_widget = QtWidgets.QWidget(self.centralwidget)
        self.layout_widget.setGeometry(QtCore.QRect(20, 40, 601, 22))
        self.layout_widget.setObjectName("layout_widget")
        self.horizontal_layout = QtWidgets.QHBoxLayout(self.layout_widget)
        self.horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout.setObjectName("horizontal_layout")

        self.line_edit_2 = QtWidgets.QLineEdit(self.layout_widget)
        self.line_edit_2.setInputMask("")
        self.line_edit_2.setObjectName("line_edit_2")

        self.horizontal_layout.addWidget(self.line_edit_2)

        self.tool_button_2 = QtWidgets.QToolButton(self.layout_widget)
        self.tool_button_2.setObjectName("tool_button_2")
        self.tool_button_2.setStatusTip('Open Vrimg')
        self.tool_button_2.clicked.connect(self.open_vrimg)

        self.horizontal_layout.addWidget(self.tool_button_2)

        self.layout_widget1 = QtWidgets.QWidget(self.centralwidget)
        self.layout_widget1.setGeometry(QtCore.QRect(20, 170, 601, 41))
        self.layout_widget1.setObjectName("layout_widget1")

        self.horizontal_layout_7 = QtWidgets.QHBoxLayout(self.layout_widget1)
        self.horizontal_layout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_7.setObjectName("horizontal_layout_7")

        self.line_edit = QtWidgets.QLineEdit(self.layout_widget1)
        self.line_edit.setObjectName("line_edit")

        self.horizontal_layout_7.addWidget(self.line_edit)

        self.tool_button = QtWidgets.QToolButton(self.layout_widget1)
        self.tool_button.setText("...")
        self.tool_button.setObjectName("tool_button")

        self.tool_button.clicked.connect(self.open_denoise)
        self.horizontal_layout_7.addWidget(self.tool_button)

        self.push_button = QtWidgets.QPushButton(self.layout_widget1)
        self.push_button.setText("Denoise!")
        self.push_button.setObjectName("push_button")
        self.push_button.setStatusTip('Denoise!')
        self.push_button.clicked.connect(self.start_exe)
        self.horizontal_layout_7.addWidget(self.push_button)

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 160, 131, 16))
        self.label_6.setText("vdenoise.exe")
        self.label_6.setFont(QtGui.QFont('Monospaced', 7))
        self.label_6.setObjectName("label_6")

        self.textwindow = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textwindow.setGeometry(QtCore.QRect(20, 220, 601, 211))
        self.textwindow.setFont(QtGui.QFont('Monospaced', 7))
        self.textwindow.insertPlainText(self.startstamp)

        self.layout_widget2 = QtWidgets.QWidget(self.centralwidget)
        self.layout_widget2.setGeometry(QtCore.QRect(20, 80, 601, 61))
        self.layout_widget2.setObjectName("layout_widget2")
        self.grid_layout = QtWidgets.QGridLayout(self.layout_widget2)

        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.setObjectName("grid_layout")
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacer_item, 1, 3, 1, 1)
        # Check Display
        self.check_box_2 = QtWidgets.QCheckBox(self.layout_widget2)
        self.check_box_2.setObjectName("check_box_2")
        self.grid_layout.addWidget(self.check_box_2, 0, 4, 1, 1)

        self.combo_box = QtWidgets.QComboBox(self.layout_widget2)
        self.combo_box.setObjectName("combo_box")
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.setCurrentIndex(1)
        self.grid_layout.addWidget(self.combo_box, 0, 1, 1, 1)

        self.label_5 = QtWidgets.QLabel(self.layout_widget2)
        self.label_5.setText("mode")
        self.label_5.setObjectName("label_5")
        self.grid_layout.addWidget(self.label_5, 0, 0, 1, 1)

        self.combo_box_1 = QtWidgets.QComboBox(self.layout_widget2)
        self.combo_box_1.setObjectName("combo_box_1")
        self.combo_box_1.addItem("")
        self.combo_box_1.addItem("")
        self.combo_box_1.addItem("")
        self.combo_box_1.setCurrentIndex(1)
        self.grid_layout.addWidget(self.combo_box_1, 0, 3, 1, 1)

        self.label_4 = QtWidgets.QLabel(self.layout_widget2)
        self.label_4.setText("threshold")
        self.label_4.setObjectName("label_4")
        self.grid_layout.addWidget(self.label_4, 1, 0, 1, 1)

        self.check_box = QtWidgets.QCheckBox(self.layout_widget2)
        self.check_box.setObjectName("check_box")
        self.grid_layout.addWidget(self.check_box, 1, 4, 1, 1)

        self.check_box_3 = QtWidgets.QCheckBox(self.layout_widget2)
        self.check_box_3.setObjectName("check_box_3")
        self.check_box_3.setChecked(True)

        self.grid_layout.addWidget(self.check_box_3, 1, 9, 1, 1)

        self.check_box_4 = QtWidgets.QCheckBox(self.layout_widget2)
        self.check_box_4.setObjectName("check_box_4")
        self.check_box_4.setChecked(True)

        self.grid_layout.addWidget(self.check_box_4, 0, 9, 1, 1)

        self.double_spin_box = QtWidgets.QDoubleSpinBox(self.layout_widget2)
        self.double_spin_box.setObjectName("double_spin_box")
        self.double_spin_box.setRange(0., 2.)
        self.double_spin_box.setDecimals(3)
        self.double_spin_box.setValue(0.001)
        self.double_spin_box.setSingleStep(0.001)

        self.grid_layout.addWidget(self.double_spin_box, 1, 1, 1, 1)

        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")

        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage('DeNoiseUI ' + appver)

        # menu Open
        self.action_open = QtWidgets.QAction(main_window)
        self.action_open.setObjectName("action_open")

        self.open_icon = QIcon('icons/open.png')  # create icon
        self.action_open = QAction(self.open_icon, '')
        self.action_open.setStatusTip('Open')
        self.action_open.setShortcut('Ctrl+O')
        self.action_open.triggered.connect(self.open_file_dialog)

        # menu Save
        self.action_save = QtWidgets.QAction(main_window)
        self.action_save.setObjectName("action_save")

        self.save_icon = QIcon('icons/save.png')  # create icon
        self.action_save = QAction(self.save_icon, '')
        self.action_save.setStatusTip('Save')
        self.action_save.setShortcut('Ctrl+S')
        self.action_save.triggered.connect(self.save_dialog)

        # menu Exit
        self.exit_icon = QIcon('icons/exit.png')  # create icon
        self.action_exit = QAction(self.exit_icon, '')
        self.action_exit.setObjectName("action_exit")

        self.action_exit.setStatusTip('Click to exit the application')
        self.action_exit.setShortcut('Ctrl+Q')
        self.action_exit.triggered.connect(self.koniec)

        # menu
        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.action_save)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_exit)

        # self.menubar.addAction(self.menuHelp.menuAction())
        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)
        # self.load_autosafe()

    def setup_ui(self, main_window):
        self.scriptDir = os.path.dirname(os.path.realpath(__file__))

        main_window.setObjectName("MAIN_WINDOW")
        main_window.resize(640, 480)
        main_window.setMinimumSize(QtCore.QSize(640, 480))
        main_window.setMaximumSize(QtCore.QSize(640, 480))
        main_window.setWindowIcon(QtGui.QIcon(self.scriptDir + os.path.sep + 'icons' + os.path.sep + 'cfab.png'))

        main_window.setCentralWidget(self.centralwidget)

        # self.menuHelp = QtWidgets.QMenu(self.menubar)
        # self.menuHelp.setObjectName("menuHelp")

        main_window.setMenuBar(self.menubar)

        main_window.setStatusBar(self.statusbar)

        self.writelog()
        if self.check_box_4.isChecked():
            self.load_autosafe()
        else:
            return None

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MAIN_WINDOW", "V-ray Denoise UI"))
        self.line_edit_2.setText(_translate("MAIN_WINDOW", "wskaż plik VRIMG"))
        self.tool_button_2.setText(_translate("MAIN_WINDOW", "..."))
        self.line_edit.setText(_translate("MAIN_WINDOW", "wskaż plik vdenoise.exe"))
        self.check_box_2.setText(_translate("MAIN_WINDOW", "Display Preview"))
        self.combo_box.setItemText(0, _translate("MAIN_WINDOW", "mild"))
        self.combo_box.setItemText(1, _translate("MAIN_WINDOW", "default"))
        self.combo_box.setItemText(2, _translate("MAIN_WINDOW", "strong"))
        self.combo_box_1.setItemText(0, _translate("MAIN_WINDOW", "CPU"))
        self.combo_box_1.setItemText(1, _translate("MAIN_WINDOW", "GPU"))
        self.combo_box_1.setItemText(2, _translate("MAIN_WINDOW", "OpenCL Experimental"))

        self.check_box.setText(_translate("MAIN_WINDOW", "Auto Radius"))
        self.check_box_3.setText(_translate("MAIN_WINDOW", "Save Log"))
        self.check_box_4.setText(_translate("MAIN_WINDOW", "Auto Save"))

        # menu - add text
        self.menu_file.setTitle(_translate("MAIN_WINDOW", "File"))
        self.action_open.setText(_translate("MAIN_WINDOW", "Open"))
        self.action_save.setText(_translate("MAIN_WINDOW", "Save"))
        self.action_exit.setText(_translate("MAIN_WINDOW", "Exit"))

        self.menubar.addAction(self.menu_file.menuAction())

    def open_denoise(self):
        """
        Uruchamiam aplikację
        """
        if self.load_settings is True:
            self.load_settings = False

        if _platform == 'win32' or _platform == 'win64':
            file_name = QFileDialog.getOpenFileName(None, 'Znajdź plik vdenoise.exe',
                                                    '', 'vdenoise.exe')

            if str(file_name[0]) == '':
                filenull = ('\n' + str(datetime.now().strftime("[ %H:%M:%S ]" + ' Nie dodano '
                                                                                'pliku Vdenoise')))
                self.textwindow.insertPlainText(filenull)
                self.logtext = filenull
                self.writelog()
                return

            elif str(file_name[0]) != '':
                file_name = str(file_name[0])
                zlyukosnik = '/'
                dobryukosnik = '\\'
                zamiana = str.maketrans(zlyukosnik, dobryukosnik)
                self.file_name = file_name.translate(zamiana)
                filenull = ('\n' + str(datetime.now().strftime("[ %H:%M:%S ]")
                                       + ' Dodano plik Vdenoise: '
                                       + (str(self.file_name))))
                self.line_edit.setText(self.file_name)
                self.textwindow.insertPlainText(filenull)
                self.logtext = filenull
                self.writelog()
                return

        if _platform == 'darwin':
            self.textwindow.insertPlainText('mac os nie jest obsługiwany')
            return

    def open_vrimg(self):

        if _platform == 'win32' or _platform == 'win64':

            file_vrimg = QFileDialog.getOpenFileName(None, 'Dodaj plik Vrimg', '', '*.vrimg *.exr')

            if str(file_vrimg[0]) == '':
                vrimgnull = ('\n' + str(datetime.now().strftime("[ %H:%M:%S ]"
                                                                + ' Nie dodano pliku *.vrimg *.exr')))
                self.textwindow.insertPlainText(vrimgnull)
                self.logtext = vrimgnull
                self.writelog()
                return

            elif str(file_vrimg[0]) != '':
                file_vrimg = str(file_vrimg[0])
                self.load_vrimg = True
                zlyukosnik = '/'
                dobryukosnik = '\\'
                zamiana = str.maketrans(zlyukosnik, dobryukosnik)
                self.file_vrimg = file_vrimg.translate(zamiana)
                self.new_vrimg = (str(self.file_vrimg))
                self.line_edit_2.setText(self.file_vrimg)
                vrimgnull = ('\n' + str(datetime.now().strftime("[ %H:%M:%S ]")
                                        + ' Dodano plik: ' + (str(self.file_vrimg))))
                self.textwindow.insertPlainText(vrimgnull)
                self.logtext = vrimgnull
                self.super_file = str(self.file_vrimg)
                self.writelog()
            else:
                return

        if _platform == 'darwin':
            self.textwindow.insertPlainText('mac os nie jest obsługiwany')
            return

    def parametry(self):
        self.sciezka = []
        if self.load_settings is True:
            self.sciezka.append(self.par_zero)
        else:
            self.sciezka.append(self.file_name)

        if self.load_vrimg is True:

            self.sciezka.append(' -inputFile=' + self.super_file)
            super_xtra = (' -inputFile=' + self.super_file)

        else:
            self.sciezka.append(' -inputFile=' + self.file_vrimg)

        self.sciezka.append(' -mode=' + str(self.combo_box.currentText()))
        self.sciezka.append(' -threshold=' + '{0:.3f}'.format(self.double_spin_box.value()))
        if self.check_box.isChecked():
            self.sciezka.append(' -autoRadius=1')
        else:
            self.sciezka.append(' -autoRadius=0')

        if self.check_box_2.isChecked():
            self.sciezka.append(' -display=1')
        else:
            self.sciezka.append(' -display=0')

        if str(self.combo_box_1.currentText()) == 'CPU':
            self.sciezka.append(' -useGpu=0')

        elif str(self.combo_box_1.currentText()) == 'GPU':
            self.sciezka.append(' -useGpu=1')

        elif str(self.combo_box_1.currentText()) == 'OpenCL Experimental':
            self.sciezka.append(' -useGpu=2')

        self.gotowa_sciezka = (self.sciezka[0] + super_xtra + self.sciezka[2]
                               + self.sciezka[3] + self.sciezka[4]
                               + self.sciezka[5] + self.sciezka[6])

        self.consoletext = ('\n' + str(datetime.now().strftime("[ %H:%M:%S ]")) + ' Uruchamiam '
                                                                                  'Vdenoise z parametrami: \n' +
                            self.sciezka[0]
                            + '\n' + super_xtra + '\n' + self.sciezka[2] + '\n' + self.sciezka[3]
                            + '\n' + self.sciezka[4] + '\n' + self.sciezka[5] + '\n' + self.sciezka[6])

        self.textwindow.insertPlainText(self.consoletext)

        self.logtext = self.consoletext
        self.pathexe = self.gotowa_sciezka

    def save_dialog(self):
        file = QFileDialog.getSaveFileName(None, 'Zapisz plik ustawień',
                                           '', '*.sav')

        if str(file[0]) == '':
            return
        else:
            self.save_file(file[0])

    def save_autosave(self):
        plik_save = (os.path.dirname(os.path.realpath(__file__))) + '\\' + 'autosave.sav'
        self.save_file(plik_save)

    def load_autosafe(self):
        plik_save = (os.path.dirname(os.path.realpath(__file__))) + '\\' + 'autosave.sav'
        if os.path.exists(plik_save) is True:
            self.open_file(plik_save)
            self.load_settings = True
            self.logtext = ('\n' + str(datetime.now().strftime("[ %H:%M:%S ]"))
                            + ' Plik autosave.sav został wczytany' + '\n')
            self.writelog()
        else:
            self.logtext = ('\n' + str(datetime.now().strftime("[ %H:%M:%S ]"))
                            + ' Brak pliku autosave.sav' + '\n')
            self.writelog()

    def save_file(self, file_name):
        print(file_name)
        """ zapisuje plik parametrów"""
        file_name = file_name.replace('/', '\\')

        if os.path.exists(file_name) is True:
            self.logtext = ('\n' + str(datetime.now().strftime("[ %H:%M:%S ]"))
                            + ' Usuwam plik ' + file_name + '\n')
            self.writelog()
            os.remove(file_name)

        if str(file_name) == '':

            savenull = ('\n' + str(datetime.now().strftime("[ %H:%M:%S ]"
                                                           + ' Nie zapisano pliku *.sav')))
            self.textwindow.insertPlainText(savenull)
            self.logtext = savenull
            self.writelog()
            return

        elif str(file_name) != '':
            save = []
            if self.file_name is None:
                save.append(r'None')
            else:
                save.append(self.file_name)

            save.append(' -mode=' + str(self.combo_box.currentText()))
            save.append(' -threshold=' + '{0:.3f}'.format(self.double_spin_box.value()))
            if self.check_box.isChecked():
                save.append(' -autoRadius=1')
            else:
                save.append(' -autoRadius=0')

            if self.check_box_2.isChecked():
                save.append(' -display=1')
            else:
                save.append(' -display=0')

            if str(self.combo_box_1.currentText()) == 'CPU':
                save.append(' -useGpu=0')

            elif str(self.combo_box_1.currentText()) == 'GPU':
                save.append(' -useGpu=1')

            elif str(self.combo_box_1.currentText()) == 'OpenCL Experimental':
                save.append(' -useGpu=2')

            if self.check_box_4.isChecked():
                save.append(' -autosave=1')
            else:
                save.append(' -autosave=0')

            if self.check_box_3.isChecked():
                save.append(' -autolog=1')
            else:
                save.append(' -autolog=0')

            for parametr in save:
                file = open(file_name, 'a')
                file.write(parametr + '\n')
                file.close()
            self.logtext = ('\n' + str(datetime.now().strftime("[ %H:%M:%S ]") + ' Plik z ustawieniami został '
                                                                                 'zapisany: ' + str(file_name)
                                       + '\n' + str(save) + '\n'))
            self.writelog()

    def open_file_dialog(self):
        open_name = QFileDialog.getOpenFileName(None, 'Otwórz plik ustawień', '', '*.sav')
        open_name = open_name[0]
        print(open_name)
        self.open_file(open_name)

    def open_file(self, open_name):

        print(open_name)
        parametrs = []

        try:
            with open(open_name) as f:
                lines = f.readlines()
        except:
            return None

        for parametr in lines:
            parametr = parametr.strip(' \t\n\r')
            parametrs.append(parametr)

        self.par_zero = parametrs[0]
        if self.par_zero == 'None':
            self.line_edit.setText('wskaż plik vdenoise')
        else:
            self.line_edit.setText(self.par_zero)

        par_one = parametrs[1]
        print(par_one)
        if par_one == '-mode=mild':
            self.combo_box.setCurrentIndex(0)

        elif par_one == '-mode=default':
            self.combo_box.setCurrentIndex(1)

        elif par_one == '-mode=strong':
            self.combo_box.setCurrentIndex(2)

        par_two = parametrs[2]
        print(par_two)
        par_two = par_two.replace('-threshold=', '')
        par_two = float(par_two)
        self.double_spin_box.setValue(par_two)

        par_three = parametrs[3]
        print(par_three)
        par_three = par_three.replace('-autoRadius=', '')
        if par_three == '0':
            self.check_box.setChecked(False)
        elif par_three == '1':
            self.check_box.setChecked(True)

        par_four = parametrs[4]
        print(par_four)
        par_four = par_four.replace('-display=', '')
        if par_four == '0':
            self.check_box_2.setChecked(False)
        elif par_four == '1':
            self.check_box_2.setChecked(True)

        par_five = parametrs[5]
        print(par_five)
        par_five = par_five.replace('-useGpu=', '')

        if par_five == '0':
            self.combo_box_1.setCurrentIndex(0)

        elif par_five == '1':
            self.combo_box_1.setCurrentIndex(1)

        elif par_five == '2':
            self.combo_box_1.setCurrentIndex(2)

        par_six = parametrs[6]
        print(par_six)
        par_six = par_six.replace('-autosave=', '')
        par_six = str(par_six)
        if par_six == '0':
            self.check_box_4.setChecked(False)

        if par_six == '1':
            self.check_box_4.setChecked(True)

        par_seven = parametrs[7]
        print(par_seven)
        par_seven = par_seven.replace('-autolog=', '')
        par_seven = str(par_seven)
        if par_seven == '0':
            self.check_box_3.setChecked(False)

        if par_six == '1':
            self.check_box_3.setChecked(True)

        log_open = ('\n' + str(datetime.now().strftime("[ %H:%M:%S ]") + 'Plik z ustawieniami został wczytany'))
        self.logtext = log_open

        self.load_settings = True

    def writelog(self):
        if self.check_box_3.isChecked():
            self.plik = open(self.log_file_def, 'a', encoding="utf -8")
            self.plik.write(self.logtext)
            self.plik.close()
        else:
            return

    def start_exe(self):

        if self.file_name is not None and self.file_vrimg is not None:
            self.denoise()

        elif self.load_settings is True and self.file_vrimg is None:
            self.open_vrimg()
            self.denoise()

        elif self.file_name is None and self.file_vrimg is None:
            self.open_denoise()
            self.open_vrimg()
            self.denoise()

        elif self.file_name is None:
            if self.load_settings is True:
                self.denoise()
            else:
                self.open_denoise()
                self.denoise()

        elif self.file_vrimg is None:
            self.open_vrimg()
            self.denoise()

        else:
            return

    def denoise(self):
        """ Uruchamiam plik vdenoise.exe"""
        if self.file_name is not None and self.file_vrimg is not None:
            for p in self.sciezka:
                print('X ->' + p)
            self.parametry()
            self.logtext = ('\n' + str(datetime.now().strftime("[ %H:%M:%S ]"))
                            + ' Denoise start!' + '\n')
            self.writelog()
            subprocess.Popen(self.pathexe)

        elif self.load_settings is True and self.file_vrimg is not None:
            for p in self.sciezka:
                print('X ->' + p)
            self.parametry()
            self.logtext = ('\n' + str(datetime.now().strftime("[ %H:%M:%S ]"))
                            + ' Denoise start!' + '\n')
            self.writelog()
            print(self.pathexe)
            subprocess.Popen(self.pathexe)

        else:
            self.logtext = ('\n' + str(datetime.now().strftime("[ %H:%M:%S ]"))
                            + ' Brak danych' + '\n')
            self.writelog()
            return

    def koniec(self):
        self.save_autosave()
        self.logtext = ('\n' + str(datetime.now().strftime("[ %H:%M:%S ]"))
                        + ' Koniec sesji' + '\n')
        self.writelog()
        quit()


if __name__ == "__main__":
    APP = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    UI = UiMainWindow()
    UI.setup_ui(main_window)
    main_window.show()
    sys.exit(APP.exec_())
