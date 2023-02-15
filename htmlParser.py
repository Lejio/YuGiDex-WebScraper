from html.parser import HTMLParser

class YuGiParser(HTMLParser):
    
    def __init__(self):
        
        super().__init__()

        self.__response = []
        self.__links = []
        self.data = ""
        
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        
        if tag == 'a':
            self.__links.append(attrs[0][1])
        
        return super().handle_starttag(tag, attrs)

    def handle_data(self, data):
        
        self.data = data
        if (data.replace(' ', '').replace('\n', '') == ''):
            return
            
        data = data.replace('\n', '').split()
        data = " ".join(data)
        self.__response.append(data)
        
    def getResponse(self):
        
        self.__response.remove("·")
        
        return self.__response
    
    def getLink(self):
        
        return self.__links
    
    def finish(self):
        
        self.close()
        
