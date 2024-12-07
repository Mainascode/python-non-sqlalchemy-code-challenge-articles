# Represents an Article, with attributes for author, magazine, and title
class Article:
# Stores all instances of Article
    all = []  

    def __init__(self, author, magazine, title): 
    # The author of the article (must be an Author instance)
        self.author = author 
     # The magazine where the article is published (must be a Magazine instance)
        self.magazine = magazine 
        self.title = title 
     # Adds the article instance to the all list
        type(self).all.append(self) 

    # Property for the title with validation for length
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
    # Ensures title is a string of valid length and is set only once
        if isinstance(title, str) and 5 <= len(title) <= 50 and not hasattr(self, '_title'):
            self._title = title

    # Property for the author with validation
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        # Ensures author is an instance of the Author class
        if isinstance(author, Author):
            self._author = author

    # Property for the magazine with validation
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
     # Ensures magazine is an instance of the Magazine class
        if isinstance(magazine, Magazine):
            self._magazine = magazine

# Represents an Author with attributes and behaviors specific to authors
class Author:
# Stores all instances of Author
    all = []  

    # Initializes Author with a name
    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    # Property for name with validation
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        # Ensures name is a non-empty string and is set only once
        if isinstance(name, str) and len(name) >= 1 and not hasattr(self, '_name'):
            self._name = name

    # Returns all articles written by the author
    def articles(self): 
        return [article for article in Article.all if article.author == self]
    
    # Returns all unique magazines the author has written for
    def magazines(self):
        return list({article.magazine for article in self.articles()})
    
    # Creates a new article by the author
    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    # Returns all unique topic areas of magazines the author has written for
    def topic_areas(self):
        if self.articles():
            return list({article.magazine.category for article in self.articles()})
        return None

# Represents a Magazine with attributes for name, category, and related characters
class Magazine: 
 # Stores all instances of Magazine
    all = []

    def __init__(self, name, category):
    # Name of the magazine 
        self.name = name 
     # Category of the magazine
        self.category = category
        type(self).all.append(self)

    # Property for name with validation
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        # Ensures name is a string with valid length
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name

    # Property for category with validation
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        # Ensures category is a non-empty string
        if isinstance(category, str) and len(category) >= 1:
            self._category = category

    # Returns all articles published in the magazine
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    # Returns all unique authors who have written for the magazine
    def contributors(self):
        return list({article.author for article in self.articles()})

    # Returns the titles of all articles in the magazine
    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    # Returns authors who have contributed multiple articles to the magazine
    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            if article.author in author_count:
                author_count[article.author] += 1
            else:
                author_count[article.author] = 1
        return [author for author, count in author_count.items() if count >= 2] or None
