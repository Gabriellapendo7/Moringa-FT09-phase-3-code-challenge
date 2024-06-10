class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self._id = id
        self.title = title
        self.content = content
        self._author_id = author_id
        self._magazine_id = magazine_id

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value
        else:
            raise ValueError("Title must be a string between 5 and 50 characters")

    @classmethod
       # inserting a new article 
    def create_article(cls, cursor, title, content, author_id, magazine_id):
        cursor.execute("INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)", (title, content, author_id, magazine_id))
        article_id = cursor.lastrowid
        return cls(article_id, title, content, author_id, magazine_id)

    @classmethod
        # getting all article titles
    def get_title(cls, cursor):
        cursor.execute("SELECT title FROM articles")
        titles = cursor.fetchall()
        return [title[0] for title in titles] if titles else None


    def get_author(self, cursor):
        # getting the name of the author associated with the article 
        cursor.execute("SELECT name FROM authors WHERE id = ?", (self._author_id,))
        author_name = cursor.fetchone()
        return author_name[0] if author_name else None


    def get_magazine(self, cursor):
        # getting  the name of the magazine associated with the article
        cursor.execute("SELECT name FROM magazines WHERE id = ?", (self._magazine_id,))
        magazine_name = cursor.fetchone()
        return magazine_name[0] if magazine_name else None
