class Source:
    '''
    News Source class to define News Source objects.
    '''
    
    def __init__(self,id,name,description,url,language):
        '''
        Create an init method to allow the passing of parameters needed inside the news source objects.

        Args:
            id = The news source id
            name = The news source's name
            description = brief description of the news source
            url = link to the news source
            language = language of news source
            country = origin or nationality of news source
        '''
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.language = language

class Article:
    '''
    News Article to define News Article object.
    '''
    def __init__(self,author,title,description,url,urlToImage,publishedAt):
        '''
        
        '''
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        
