from UI_prototype import *
from Busines_logiс import *
import sys


try:
    application = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.pushButton_run.clicked.connect(ui.on_click_button)

    # see_watcher()
    MainWindow.show()
    sys.exit(application.exec_())
except Exception as err:
    print(err)
    input()