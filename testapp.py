from PySide6.QtWidgets import QMainWindow, QWidget, QApplication, QHBoxLayout
from webEngineScraper import FetchEngine
import sys


class MainWindow(QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()

        bruhWidget = QWidget()
        bruhlayout = QHBoxLayout()

        # Instantiates a fetch engine. It is a QWidget so you have to add it to the 
        self.results = FetchEngine()
        self.results.findCard("Dark Magician")
        self.results.finished.connect(self.getResponse)
        bruhlayout.addWidget(self.results)

        # self.hide()
        
        bruhWidget.setLayout(bruhlayout)
        self.setCentralWidget(bruhWidget)
        
    def getResponse(self):
        
        self.response = self.results.getResponse()
        print(self.response)
        



if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    app.exec()