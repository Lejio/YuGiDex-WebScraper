from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, QTimer
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from bs4 import BeautifulSoup

from htmlParser import YuGiParser

class FetchEngine(QWidget):
    
    def __init__(self):
        
        super(FetchEngine, self).__init__()
        
        self.DEFAULT_URL = "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&productName="
        self.GRID_VIEW = "&view=grid"
        
        self.web = QWebEngineView()
        
        self.response = {}
        
        self.parser = YuGiParser()
        
        self.button = QPushButton("Save")
        self.button.clicked.connect(self.performSurgery)
        
        layout = QVBoxLayout()
        layout.addWidget(self.web)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
    
    def __load(self, name: str) -> None:
        
        self.web.load(QUrl(self.DEFAULT_URL + name + self.GRID_VIEW))
        self.currPage = self.web.page()
    
    def findCard(self, card: str) -> None:
        
        cardname = card.replace(" ", "+")
        
        self.__load(cardname)
        
    def performSurgery(self) -> None:
        
        self.currPage.toHtml(self.save_to_html)
        
    def save_to_html(self, html) -> None:
        
        self.html = html
        
        soup = BeautifulSoup(html, 'html.parser')
        
        find_class = soup.find_all(class_="search-result__content")

        if len(find_class) == 0:
            
            print("No tags with this class is found.")
            
        else:
            
            for data in find_class:
                
                self.parser.reset()
                self.parser.feed(str(data))
                
                r = self.parser.getResponse()
                r.append(self.parser.getLink())
                self.response[r[0]] = r[1:]
                self.parser.clean()

        print(self.response)
        self.parser.close()
        
                
        
        