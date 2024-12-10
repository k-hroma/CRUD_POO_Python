from book_class import Book
from library_class import Library


# create the firs library type object
national_library = Library("National Library")
print(f"Welcome to {national_library.name}")

# create the book type objects
book1 = Book("Esferas de la insureccion", "Suely Rolnik", "Ensayo")
book2 = Book("Como imponer un limite absoluto al capitalismo", "Jun Fujita Hirose", "Ensayo")
book3 = Book('Cien años de soledad', 'Gabriel García Márquez', 'Ficción')
book4 = Book('Don Quijote de la Mancha', 'Miguel de Cervantes', 'Comedia')
book5 = Book('El amor en los tiempos del cólera', 'Gabriel García Márquez', 'Ficción')
book6 = Book('Pedro Páramo', 'Juan Rulfo', 'Ficción')
book7 = Book('Pantaleón y las visitadores', 'Mario Vargas Llosa', 'Comedia')

# add the books to de list books
national_library.add_book_library(book1)
national_library.add_book_library(book2)
national_library.add_book_library(book3)
national_library.add_book_library(book4)
national_library.add_book_library(book5)
national_library.add_book_library(book6)
national_library.add_book_library(book7)

# search books by autor
national_library.search_autor("Suely Rolnik")
national_library.search_autor("Mario Vargas Llosa")

# search books by gender
national_library.search_gender("Ensayo")
national_library.search_gender("Ficción")

# show all catalog
national_library.show_catalog()
