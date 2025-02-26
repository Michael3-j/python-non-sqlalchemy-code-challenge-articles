class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,title):
        if hasattr(self,"_title"):
            raise Exception("can not change the name of the title")
        elif isinstance(title,str) and 5< len(title) <50:
            self._title = title
        else:
            raise Exception (f"The {title} must be a string with  characters betwwen 5 and 50")
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author (self, author):
        if not isinstance(author,Author):
            raise Exception(f"{author} is not an instance in Author class")
        else:
            self._author = author

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self,magazine):
        if not isinstance(magazine,Magazine):
            raise Exception (f"{magazine} is not an instance in Magazine class")
        else:
            self._magazine = magazine






class Author:
    def __init__(self, name):
        
        self.name = name
        self._magazine = []
        self._title = []
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if hasattr(self,"_name"):
            raise Exception("Can not change name of the Author")
        elif isinstance(name,str) and len(name)>0:
            self._name = name
        else:
            raise Exception("The name must be a string with more than 0 characters")




    def articles(self):

        article_list = [article for article in Article.all if article.author == self]
        return article_list
        
        

    def magazines(self):
        magazine_list = {article.magazine for article in Article.all if article.author == self if isinstance(article.magazine,Magazine)}
        return list(magazine_list)

    def add_article(self, magazine, title):
        if isinstance(magazine, Magazine):
            new = Article(self, magazine, title)
        return new
        
        

        
    def topic_areas(self):
        magazines_list = self.magazines()
        category_list =[magazine.category for magazine in magazines_list if isinstance(magazine,Magazine)]

        if len(category_list) == 0:
            return None
        
        return category_list

        

class Magazine:
    def __init__(self, name, category):
        
        self.name = name
        self.category = category
        self._author = []
        self._article = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if isinstance(name,str) and (2<= len(name) <= 16):
            self._name = name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self,category):
        if isinstance(category,str) and len(category) >0:
            self._category =category
     


    def articles(self):
       articles_list =[article for article in Article.all if article.magazine == self]
       return articles_list

    def contributors(self):
        contributors_list ={article.author for article in Article.all if article.magazine == self if isinstance(article.author,Author)}
        return list(contributors_list)

        #Returns a unique list of authors who have written for this magazineS
         #Must be of type Author

    def article_titles(self):
        article_list = self.articles()
        title_list = [articles.title for articles in article_list]

        if len(title_list) == 0:
            return None
        return title_list




    def contributing_authors(self):
        contributor_count = {}

        for article in Article.all:
            if article.magazine is self:
                if article.author in contributor_count:
                    contributor_count[article.author] += 1
                else:
                    contributor_count[article.author]   =1

        contributing_authors = [author for author,count in contributor_count.items() if count >2]

        if contributing_authors:
            return contributing_authors
        else:
            return None

        









