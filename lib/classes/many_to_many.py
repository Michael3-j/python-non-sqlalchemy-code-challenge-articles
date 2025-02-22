class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        if not (isinstance(title, str) and 5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")
        
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    def articles(self):
        return [article for article in Article.all if article.author is self]
    
    def magazines(self):
        return list({article.magazine for article in self.articles()})
    
    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    
    def topic_areas(self):
        categories = {mag.category for mag in self.magazines()}
        return categories if categories else None


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not (isinstance(value, str) and 2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Category must be a non-empty string")
        self._category = value
    
    def articles(self):
        return [article for article in Article.all if article.magazine is self]
    
    def contributors(self):
        return list({article.author for article in self.articles()})
    
    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None
    
    def contributing_authors(self):
        author_counts = {article.author: 0 for article in self.articles()}
        for article in self.articles():
            author_counts[article.author] += 1
        
        return [author for author, count in author_counts.items() if count > 2] or None









