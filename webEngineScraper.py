from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, QTimer
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from bs4 import BeautifulSoup

from htmlParser import YuGiParser

class FetchEngine(QWidget):
    
    def __init__(self):
        
        super(FetchEngine, self).__init__()
        
        # This is the default search links to TCGPlayer website.
        self.DEFAULT_URL = "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&productName="
        self.GRID_VIEW = "&view=grid"
        
        # Instantiates a web view engine.
        self.web = QWebEngineView()
        
        # Hides the widget so the use sees nothing.
        self.web.hide()
        
        # Instantiates a empty response from page.
        self.response = {}
        
        # Instantiates html parser.
        self.parser = YuGiParser()
        
        # Instantiates a manual save button.
        self.button = QPushButton("Save")
        self.button.clicked.connect(self.__performSurgery)
        
        
        # Creates layout to place all widgets in.
        layout = QVBoxLayout()
        layout.addWidget(self.web)
        layout.addWidget(self.button)
        
        # Sets current layout to the layout we have made, containing all the widgets.
        self.setLayout(layout)
    
    ###############################################################################################
    # Private method that loads the webpage using the given card name.
    ###############################################################################################
    def __load(self, name: str) -> None:
        
        self.web.load(QUrl(self.DEFAULT_URL + name + self.GRID_VIEW))
        self.currPage = self.web.page()
    
    ###############################################################################################
    # Public method. Is used to set the url by giving it the exact card name you want to find info
    # on.
    ###############################################################################################
    def findCard(self, card: str) -> None:
        
        # Formats the link to be used in the QUrl.
        cardname = card.replace(" ", "+")
        
        # Runs private method that actually loads the webpage.
        self.__load(cardname)
        

    ###############################################################################################
    # Private Method. Runs when the 'save' button is clicked. Saves the loaded webpages contents to
    # a callback function.
    ###############################################################################################
    def __performSurgery(self) -> None:
        
        self.currPage.toHtml(self.__save_to_html)
    
    
    ###############################################################################################
    # Private method that enacts as the callback function to receive the html from performSurgery.
    # Uses the bs4 module to convert the html string into something that could be parsed by using
    # html search methods (tags, ids, classes)
    ###############################################################################################
    def __save_to_html(self, html) -> None:
        
        # Instantiates a bs4 object, passing in the html str and parser we want to use.
        soup = BeautifulSoup(html, 'html.parser')
        
        # Gets all the contents that contains the class "search-result__content". Returns str list.
        find_class = soup.find_all(class_="search-result__content")

        # Checks if any results were found.
        if len(find_class) == 0:
            
            print("No tags with this class is found.")
            
        else:
            
            # Goes through each tag with in the results.
            for data in find_class:
                
                # Resets the parser.
                self.parser.reset()
                
                # Feeds the data into parser.
                self.parser.feed(str(data))
                
                # Returns a list in the format of:
                # [Set name, Rariety, Set number, Name of Card, # Listings, 'as low as', Lowest 
                # price, 'Market Price', Market price, Link to card page].
                r = self.parser.getResponse()
                
                # Gets the link. It is processed separately from the others.
                r.append(self.parser.getLink())
                
                # Places them in a dictionary entry in the format:
                # 'Set name': [Rariety, Set number, Name of Card, # Listings, 'as low as', Lowest
                # price, 'Market Price', Market price, Link to card page]
                self.response[r[0]] = r[1:]
                
                # Should reset all the data.
                self.parser.clean()

        print(self.response)
        # Closes the parser when finished.
        self.parser.close()
        
                
        
        