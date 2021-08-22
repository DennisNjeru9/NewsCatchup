class Source:
    '''
    News Source class to define News Source objects.
    '''
    
    def __init__(self,id,name,description,url,category,language,country):
        '''
        Create an init method to allow the passing of parameters needed inside the movie objects.

        Args:
            id = The news source id.
            name = The news source's name
            description = brief description of the news source
            urlr = link to the news source
            category = type of news source
            language = language of news source
            country = origin or nationality of news source
        '''
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country

        