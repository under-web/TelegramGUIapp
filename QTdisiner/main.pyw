# https://www.youtube.com/watch?v=kWBwcWNV4Dc
# https://gist.github.com/rbonvall/9982648 редирект из консоли в виджет

# from PyQt5 import uic
# from PyQt5.QtWidgets import QApplication
#
# Form, Window = uic.loadUiType("GShell.ui")
#
# app = QApplication([])
# window = Window()
# form = Form()
# form.setupUi(window)
# window.show()
# app.exec()
from QTdisiner.GShell import *

import sys

def on_click_send_message():
    print('Отправил сообщение!')

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
ui.pushButton.clicked.connect(on_click_send_message)

sys.exit(app.exec_())