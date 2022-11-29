# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Busines_logiс import *
class Modal(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setWindowModality(Qt.WindowModal)
        # self.setModal(True)
        self.resize(200, 200)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(843, 720)

        self.process = QtCore.QProcess()
        self.process.readyReadStandardOutput.connect(self.stdoutReady)
        self.process.readyReadStandardError.connect(self.stderrReady)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton_parsing = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_parsing.setGeometry(QtCore.QRect(50, 130, 571, 17))
        self.radioButton_parsing.setObjectName("radioButton_parsing")
        self.radioButton_2_pars_sendm = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2_pars_sendm.setGeometry(QtCore.QRect(50, 160, 571, 20))
        self.radioButton_2_pars_sendm.setObjectName("radioButton_2_pars_sendm")
        self.radioButton_3_send_messages = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3_send_messages.setGeometry(QtCore.QRect(50, 190, 571, 20))
        self.radioButton_3_send_messages.setObjectName("radioButton_3_send_messages")
        self.radioButton_4_join_group = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4_join_group.setGeometry(QtCore.QRect(50, 220, 571, 20))
        self.radioButton_4_join_group.setObjectName("radioButton_4_join_group")
        self.radioButton_5_invite = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5_invite.setGeometry(QtCore.QRect(50, 250, 501, 17))
        self.radioButton_5_invite.setObjectName("radioButton_5_invite")
        self.radioButton_6_send_file = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6_send_file.setGeometry(QtCore.QRect(50, 280, 481, 17))
        self.radioButton_6_send_file.setObjectName("radioButton_6_send_file")
        self.radioButton_7_send_filemes = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_7_send_filemes.setGeometry(QtCore.QRect(50, 310, 501, 17))
        self.radioButton_7_send_filemes.setObjectName("radioButton_7_send_filemes")
        self.radioButton_8_parsing_admin = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_8_parsing_admin.setGeometry(QtCore.QRect(50, 340, 501, 17))
        self.radioButton_8_parsing_admin.setObjectName("radioButton_8_parsing_admin")
        self.radioButton_9_chek_phone = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_9_chek_phone.setGeometry(QtCore.QRect(50, 400, 501, 17))
        self.radioButton_9_chek_phone.setObjectName("radioButton_9_chek_phone")
        self.radioButton_10_get_phone = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_10_get_phone.setGeometry(QtCore.QRect(50, 370, 501, 17))
        self.radioButton_10_get_phone.setObjectName("radioButton_10_get_phone")
        self.pushButton_run = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_run.setGeometry(QtCore.QRect(720, 520, 75, 51))
        self.pushButton_run.setObjectName("pushButton_run")
        self.label_telegram_combain = QtWidgets.QLabel(self.centralwidget)
        self.label_telegram_combain.setGeometry(QtCore.QRect(50, 70, 521, 51))
        font = QtGui.QFont()
        font.setFamily("Niagara Engraved")
        font.setPointSize(28)
        self.label_telegram_combain.setFont(font)
        self.label_telegram_combain.setObjectName("label_telegram_combain")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 450, 611, 191))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(660, 40, 141, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../Desktop/Снимок.PNG"))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 843, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton_parsing.setText(_translate("MainWindow", "[1] Извлечениe (id / nickname) пользователей групп или чатов"))
        self.radioButton_2_pars_sendm.setText(_translate("MainWindow", "[2] Извлечение пользователей (id/nickname) , с последующей отправкой сообщений."))
        self.radioButton_3_send_messages.setText(_translate("MainWindow", "[3] Рассылка. Только отправка сообщений"))
        self.radioButton_4_join_group.setText(_translate("MainWindow", "[4] Присоединяться к группам."))
        self.radioButton_5_invite.setText(_translate("MainWindow", "[5] Добавлять пользователей в канал - INVITE (работает только по USERNAME)."))
        self.radioButton_6_send_file.setText(_translate("MainWindow", "[6] Отправить только  файл  (из папки dir/), пользователям."))
        self.radioButton_7_send_filemes.setText(_translate("MainWindow", "[7] Отправить  файл  (из папки dir/) и текст-сообщение пользователям."))
        self.radioButton_8_parsing_admin.setText(_translate("MainWindow", "[8] Извлечь Администраторов группы (из file_channel --> all_user.txt)."))
        self.radioButton_9_chek_phone.setText(_translate("MainWindow", "[10] Чекер номеров телефонов на наличие аккаунта телеграм (из phones.txt --> all_user.txt)."))
        self.radioButton_10_get_phone.setText(_translate("MainWindow", "[9]Извлечь номера телефонов участников групп (из file_channel --> all_user.txt).\'"))
        self.pushButton_run.setText(_translate("MainWindow", "Пуск"))
        self.label_telegram_combain.setText(_translate("MainWindow", "TelegramCombain"))

    def open(self):
        self.app2 = Modal()
        self.app2.show()
    def on_click_button(self):
        print("Мы нажали кнопку")
        if self.radioButton_parsing.isChecked():
            func_1_parsing()
            self.textEdit.append('Мы нажали кнопку парсинга')
            self.pushButton_run.setEnabled(False)
        elif self.radioButton_3_send_messages.isChecked():
            func_3_send_mesg()
            self.textEdit.append('Мы нажали кнопку рассылки')
            self.pushButton_run.setEnabled(False)
        else:

            print('Еще не реализован Radio')
            self.pushButton_run.setEnabled(True)
            self.open()
    def append(self, text):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(text)

    def stdoutReady(self):
        text = str(self.process.readAllStandardOutput())
        print(text.strip())
        self.append(text)

    def stderrReady(self):
        text = str(self.process.readAllStandardError())
        print(text.strip())
        self.append(text)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
