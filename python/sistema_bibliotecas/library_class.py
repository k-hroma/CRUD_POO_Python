# create the library class and define the aggregate and search methods
class Library():
    def __init__(self, name):
        self._name = name
        self._books = []

    def add_book_library(self, book):
        self._books.append(book)
        print("Successful Discharge")

    def search_autor(self, autor):
        print(f"Results {autor} Search")
        for book in self._books:
            if book.autor.lower() == autor.lower():
                self.show_book(book)

    def show_book(self, book):
        print(f"Book -> Title: {book.title}, Autor: {book.autor}, Gender: {book.gender}")

    def search_gender(self, gender):
        print(f"Results {gender} Search")
        for book in self._books:
            if book.gender.lower() == gender.lower():
                self.show_book(book)

    def show_catalog(self, ):
        print("This is de Library Catalog")
        for book in self._books:
            self.show_book(book)

    @property
    def name(self,):
        return self._name

    @property
    def books(self):
        return self._books