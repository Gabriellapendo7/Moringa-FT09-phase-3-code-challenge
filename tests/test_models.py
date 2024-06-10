import unittest
from unittest.mock import MagicMock
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def setUp(self):
        #creating a Mocking for database cursor
        self.cursor = MagicMock()

    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")

    def test_create_author(self):
        author = Author(None, "John Doe")
        author.create_author(self.cursor)
        self.cursor.execute.assert_called_once_with("INSERT INTO authors (name) VALUES (?)", ("John Doe",))

    def test_get_all_authors(self):
        # Mocking database response
        self.cursor.fetchall.return_value = [(1, "John Doe"), (2, "John Doe")]
        authors = Author.get_all_authors(self.cursor)
        # Checking if execute method was called with correct argument
        self.cursor.execute.assert_called_once_with("SELECT * FROM authors")
        # Checking if authors were fetched correctly
        self.assertEqual(len(authors), 2)
        self.assertEqual(authors[0].id, 1)
        self.assertEqual(authors[0].name, "John Doe")
        self.assertEqual(authors[1].id, 2)
        self.assertEqual(authors[1].name, "John Doe")

    def test_articles(self):
        # Mocking database response
        self.cursor.fetchall.return_value = [(1, "Test Article", "Test Content", 1, 1)]
        author = Author(1, "John Doe")
        articles = author.articles(self.cursor)
        # Checking if execute method was called with correct argument
        self.cursor.execute.assert_called_once_with("SELECT * FROM articles WHERE author_id = ?", (1,))
        # Checking if articles were fetched correctly
        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0][0], 1) 
        self.assertEqual(articles[0][1], "Test Article") 

    def test_magazines(self):
        # Mocking database response
        self.cursor.fetchall.return_value = [(1, "Tech Magazine", "Technology")]
        author = Author(1, "John Doe")
        magazines = author.magazines(self.cursor)
        # Checking if execute method was called with correct argument
        self.cursor.execute.assert_called_once_with("""
            SELECT magazines.*
            FROM magazines
            JOIN articles ON magazines.id = articles.magazine_id
            WHERE articles.author_id = ?
        """, (1,))
        # Checking if magazines were fetched correctly
        self.assertEqual(len(magazines), 1)
        self.assertEqual(magazines[0][0], 1)  
        self.assertEqual(magazines[0][1], "Tech Magazine") 

if __name__ == "__main__":
    unittest.main()