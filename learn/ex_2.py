# https://ru.stackoverflow.com/questions/790877/%D0%BF%D0%BE%D0%B4%D1%81%D0%BA%D0%B0%D0%B6%D0%B8%D1%82%D0%B5-%D0%BA%D0%B0%D0%BA-%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4-%D0%BA%D0%BE%D0%BD%D1%81%D0%BE%D0%BB%D0%B8-python-%D0%BF%D0%B5%D1%80%D0%B5%D0%B4%D0%B0%D0%B2%D0%B0%D1%82%D1%8C-%D0%B2-%D0%B2%D0%B8%D0%B4%D0%B6%D0%B5%D1%82-pyqt5

import sys

from PyQt5.QtWidgets import QMainWindow, QTextEdit, QMenuBar, QApplication
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal as Signal


class OutputLogger(QObject):
    emit_write = Signal(str, int)

    class Severity:
        DEBUG = 0
        ERROR = 1

    def __init__(self, io_stream, severity):
        super().__init__()

        self.io_stream = io_stream
        self.severity = severity

    def write(self, text):
        self.io_stream.write(text)
        self.emit_write.emit(text, self.severity)

    def flush(self):
        self.io_stream.flush()


OUTPUT_LOGGER_STDOUT = OutputLogger(sys.stdout, OutputLogger.Severity.DEBUG)
OUTPUT_LOGGER_STDERR = OutputLogger(sys.stderr, OutputLogger.Severity.ERROR)

sys.stdout = OUTPUT_LOGGER_STDOUT
sys.stderr = OUTPUT_LOGGER_STDERR


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.text_edit = QTextEdit()

        OUTPUT_LOGGER_STDOUT.emit_write.connect(self.append_log)
        OUTPUT_LOGGER_STDERR.emit_write.connect(self.append_log)

        menu_bar = QMenuBar()
        menu = menu_bar.addMenu('Say')
        menu.addAction('hello', lambda: print('Hello!'))
        menu.addAction('fail', lambda: print('Fail!', file=sys.stderr))
        self.setMenuBar(menu_bar)

        self.setCentralWidget(self.text_edit)

    def append_log(self, text, severity):
        text = repr(text)

        if severity == OutputLogger.Severity.ERROR:
            text = '<b>{}</b>'.format(text)

        self.text_edit.append(text)


if __name__ == '__main__':
    app = QApplication([])

    mw = MainWindow()
    mw.show()

    print('"Go" in console!')

    app.exec()