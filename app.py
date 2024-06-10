from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine


    # author
def create_author(cursor):
    author_name = input("Enter author name: ")
    author = Author(None, author_name)
    author.create_author(cursor)
    print("Author created Successfully")

def get_all_authors(cursor):
    authors = Author.get_all_authors(cursor)
    if authors:
        print("All Author:")
        for author in authors:
            print(f"ID: {author.id}, Name: {author.name}")
    else:
        print("No author found.")

def get_author_articles(cursor):
    author_id = input("Enter the author ID to display articles: ")
    author = Author(author_id, None)
    articles = author.articles(cursor)
    if articles:
        print(f"Articles associated with Author ID {author_id}:")
        for article in articles:
            print(f"ID: {article[0]}, Title: {article[1]}, Content: {article[2]}")
    else:
        print(f"No articles found for Author ID {author_id}.")

def get_author_magazines(cursor):
    author_id = input("Enter the author ID to display magazines: ")
    author = Author(author_id, None)
    magazines = author.magazines(cursor)
    if magazines:
        print(f"Magazines associated with Author ID {author_id}:")
        for magazine in magazines:
            print(f"ID: {magazine[0]}, Name: {magazine[1]}")
    else:
        print(f"No magazines found for Author ID {author_id}.")



    # magazine
def create_magazine(cursor):
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    magazine = Magazine(None, magazine_name, magazine_category)
    magazine.create_magazine(cursor)
    print("Magazine created Successfully")

def get_all_magazines(cursor):
    magazines = Magazine.get_all_magazines(cursor)
    if magazines:
        print("All Magazines:")
        for magazine in magazines:
            print(f"ID: {magazine.id}, Name: {magazine.name}, Category: {magazine.category}")
    else:
        print("No magazines found.")

def get_magazine_articles(cursor):
    magazine_id = input("Enter the magazine ID to display articles: ")
    magazine = Magazine(magazine_id, None, None)
    articles = magazine.articles(cursor)
    if articles:
        print(f"Articles associated with Magazine ID {magazine_id}:")
        for article in articles:
            print(f"ID: {article[0]}, Title: {article[1]}, Content: {article[2]}")
    else:
        print(f"No articles found for Magazine ID {magazine_id}.")


def get_magazine_contributors(cursor):
    magazine_id = input("Enter the magazine ID to display contributors: ")
    magazine = Magazine(magazine_id, None, None)
    contributors = magazine.contributors(cursor)
    if contributors:
        print(f"Contributors associated with Magazine ID {magazine_id}:")
        for contributor in contributors:
            print(f"ID: {contributor[0]}, Name: {contributor[1]}")
    else:
        print(f"No contributors found for Magazine ID {magazine_id}.")

def get_magazine_article_titles(cursor):
    magazine_id = input("Enter the magazine ID to display article titles: ")
    magazine = Magazine(magazine_id, None, None)
    titles = magazine.article_titles(cursor)
    if titles:
        print(f"Article titles associated with Magazine ID {magazine_id}:")
        for title in titles:
            print(f"Title: {title}")
    else:
        print(f"No article titles found for Magazine ID {magazine_id}.")

def get_magazine_contributing_authors(cursor):
    magazine_id = input("Enter the magazine ID to display contributing authors: ")
    magazine = Magazine(magazine_id, None, None)
    contributing_authors = magazine.contributing_authors(cursor)
    if contributing_authors:
        print(f"Contributing authors associated with Magazine ID {magazine_id}:")
        for author in contributing_authors:
            print(f"ID: {author[0]}, Name: {author[1]}, Article Count: {author[2]}")
    else:
        print(f"No contributing authors found for Magazine ID {magazine_id}.")



    #Article  
def create_article(cursor):
    title = input("Enter article title: ")
    content = input("Enter article content: ")
    author_id = input("Enter author ID: ")
    magazine_id = input("Enter magazine ID: ")
    Article.create_article(cursor, title, content, author_id, magazine_id)
    print("Article created successfully.")

def get_article_title(cursor):
    conn = get_db_connection()
    cursor = conn.cursor()
    titles = Article.get_title(cursor)
    if titles:
        print("Article Titles:")
        for title in titles:
           print(f"Title '{title}'")
    else:
        print("No articles found.")

def get_article_author(cursor):
    article_id = input("Enter the article ID to display the author: ")
    cursor.execute("SELECT title, content, author_id, magazine_id FROM articles WHERE id = ?", (article_id,))
    article_details = cursor.fetchone()

    if article_details:
        title, content, author_id, magazine_id = article_details
        article = Article(article_id, title, content, author_id, magazine_id)
        author = article.get_author(cursor)
        if author:
            print(f"Author of Article ID {article_id}: , Authors Name :{author}")
        else:
            print(f"No author found for Article ID {article_id}.")
    else:
        print(f"No article found with ID {article_id}.")


def get_magazine(cursor):
    article_id = input("Enter the article ID to display the magazine: ")
    cursor.execute("SELECT title, content, author_id, magazine_id FROM articles WHERE id = ?", (article_id,))
    article_details = cursor.fetchone()

    if article_details:
        title, content, author_id, magazine_id = article_details
        article = Article(article_id, title, content, author_id, magazine_id)
        magazine = article.get_magazine(cursor)
        if magazine:
            print(f"Magazine of Article ID {article_id}: , Magazine Name {magazine}")
        else:
            print(f"No magazine found for Article ID {article_id}.")
    else:
        print(f"No article found with ID {article_id}.")




def main():
        # Initialize the database and create tables
    create_tables()


    while True:
        print("\nChoose:")
        print("1.  Create Author")
        print("2.  Create Magazine")
        print("3.  Create Article")
        print("4.  get All Authors")
        print("5.  get Author Articles")
        print("6.  get Author Magazines")
        print("7.  get All Magazines")
        print("8.  get Magazine Articles")
        print("9.  get Magazine Contributors")
        print("11. get Magazine Article Titles")
        print("11. get Magazine Contributing Authors")
        print("12. Get Article title")
        print("13. Get the name of the author of an article")
        print("14. Get the magazine of an article")
        print("15. Exit")

        choice = input("Enter A Number: ")

        if choice == "1":
            conn = get_db_connection()
            cursor = conn.cursor()
            create_author(cursor)
            conn.commit()
            conn.close()
        elif choice == "2":
            conn = get_db_connection()
            cursor = conn.cursor()
            create_magazine(cursor)
            conn.commit()
            conn.close()
        elif choice == "3":
            conn = get_db_connection()
            cursor = conn.cursor()
            create_article(cursor)
            conn.commit()
            conn.close()
        elif choice == "4":
            conn = get_db_connection()
            cursor = conn.cursor()
            get_all_authors(cursor)
            conn.close()
        elif choice == "5":
            conn = get_db_connection()
            cursor = conn.cursor()
            get_author_articles(cursor)
            conn.close()
        elif choice == "6":
            conn = get_db_connection()
            cursor = conn.cursor()
            get_author_magazines(cursor)
            conn.close()
        elif choice == "7":
            conn = get_db_connection()
            cursor = conn.cursor()
            get_all_magazines(cursor)
            conn.close()
        elif choice == "8":
            conn = get_db_connection()
            cursor = conn.cursor()
            get_magazine_articles(cursor)
            conn.close()
        elif choice == "9":
            conn = get_db_connection()
            cursor = conn.cursor()
            get_magazine_contributors(cursor)
            conn.close()
        elif choice == "10":
            conn = get_db_connection()
            cursor = conn.cursor()
            get_magazine_article_titles(cursor)
            conn.close()
        elif choice == "11":
            conn = get_db_connection()
            cursor = conn.cursor()
            get_magazine_contributing_authors(cursor)
            conn.close()
        elif choice == "12":
            conn = get_db_connection()
            cursor = conn.cursor()
            get_article_title(cursor)
            conn.close()
        elif choice == "13":
            conn = get_db_connection()
            cursor = conn.cursor()
            get_article_author(cursor)
            conn.close()
        elif choice == "14":
            conn = get_db_connection()
            cursor = conn.cursor()
            get_magazine(cursor)
            conn.close()
        elif choice == "15":
            print("Exiting")
            break
        else:
            print("Invalid option. Please enter a valid option.")


if __name__ == "__main__":
    main()