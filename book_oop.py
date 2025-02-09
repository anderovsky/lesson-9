class Book:
    def __init__(self, name, author, ISBN, year):
        self.name = name
        self.author = author
        self.ISBN = ISBN
        self.year = year
        self.available = True

    def __str__(self):
        return f"{self.name} / autor {self.author} / vydanie z roku {self.year}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def available_books(self):
        return [str(k) for k in self.books if k.available]

kniznica = Library()
kniha1 = Book(name="Harry Potter", author="Rowling", ISBN="123", year=1998)
kniha2 = Book(name="Pan prstenov", author="Tolkien", ISBN="345", year=1990)
kniha3 = Book(name="Dejiny", author="Zamarovský", ISBN="678", year=1980)

kniznica.add_book(kniha1)

print(kniznica)