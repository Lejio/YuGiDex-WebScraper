from PySide6.QtWidgets import QMainWindow, QWidget, QApplication, QHBoxLayout
from webEngineScraper import FetchEngine
import sys


class MainWindow(QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()

        bruhWidget = QWidget()
        bruhlayout = QHBoxLayout()

        self.results = FetchEngine()
        self.results.findCard("Triple Tactics Talent")


        bruhlayout.addWidget(self.results)

        bruhWidget.setLayout(bruhlayout)
        self.setCentralWidget(bruhWidget)



if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    app.exec()