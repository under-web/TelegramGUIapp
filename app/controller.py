
import sys
from View.UI_prototype import *
from Busines_logiс import *


application = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

ui.pushButton_run.clicked.connect(ui.on_click_button)

see_watcher()
MainWindow.show()
sys.exit(application.exec_())