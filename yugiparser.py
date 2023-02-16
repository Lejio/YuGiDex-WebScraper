from html.parser import HTMLParser


class YuGiParser(HTMLParser):
    
    def __init__(self):
        
        super().__init__()

        self.__response = []
        self.__links = ""
            
    
    ###############################################################################################
    # Public override method. The tag is passed along with it's attributes. Gets href.
    ###############################################################################################
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        
        for i in attrs:
            
            # Checks if the tag has any attributes at all.
            if len(i) != 0:
                
                # If the attribute is 'href', then it is the link to that listing page.
                if i[0] == 'href':
                    self.__links = i[1]
        
        return super().handle_starttag(tag, attrs)
    

    ###############################################################################################
    # Public override method. Parses and formats the code.
    ###############################################################################################
    def handle_data(self, data):
                
        # If after removing the spaces and escape characters, if the data is empty, do nothing.
        if (data.replace(' ', '').replace('\n', '') == ''):
            return
        
        # If the data is not empty, .split() - (changes string into a list, removing all spaces).
        data = data.replace('\n', '').split()
        data = " ".join(data)
        self.__response.append(data)


    ###############################################################################################
    # Public getter method. Returns the response in a list.
    ###############################################################################################
    def getResponse(self):
        
        # Remove the interpunct that is contaminating the data.
        self.__response.remove("·")
        
        return self.__response[1:]

    ###############################################################################################
    # Public getter method. Returns the link to that specific listing on TCGPlayer.
    ###############################################################################################
    def getLink(self):
        
        return self.__links
    

    ###############################################################################################
    # Public method that resets all parsed information.
    ###############################################################################################
    def clean(self):
        
        self.__response = []
        self.__links = []