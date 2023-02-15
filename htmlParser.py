from html.parser import HTMLParser

class YuGiParser(HTMLParser):
    
    def __init__(self):
        
        super().__init__()

        self.__response = []
        self.__links = ""
        self.data = ""
        
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        
        for i in attrs:
            if len(i) != 0:
                if i[0] == 'href':
                    self.__links = i[1]
        
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
        
        return self.__response[1:]
    
    def getLink(self):
        
        return self.__links
    
    def clean(self):
        
        self.__response = []
        self.__links = []
        self.data = ""
