books = [
    {"title":"Little Red Riding Hood", "author":"Who Knows", "genre":"Comedy", "releaseYear":2025, "publisher":"no publisher"},
    {"title":"Hood Riding Red Little", "author":"Nobody Knows", "genre":"Tragedy", "releaseYear":2024, "publisher":"me"},
    {"title":"Brata musis posluchat!", "author":"Gabriela Futova", "genre":"Reality", "releaseYear":2023, "publisher":"i dont think there is one"},
]

def add_book(books,title,author,genre,releaseYear,publisher):
    books.append({"title":title, "author":author, "genre":genre, "releaseYear":releaseYear, "publisher":publisher})

def delete_book(books, title):
    for book in books:
        if book["title"] == title:
            books.remove(book)

def search_book(books, title):
    for book in books:
        if book["title"] == title:
            return book
    return {}

def replace_book(books, searchTitle, newTitle, newAuthor, newGenre, newReleaseYear, newPublisher):
    for book in books:
        if book["title"] == searchTitle:
            book["title"] = newTitle
            book["author"] = newAuthor
            book["genre"] = newGenre
            book["releaseYear"] = newReleaseYear
            book["publisher"] = newPublisher


def show_all_books():
    print(books)


def show_menu():
    print("1. Add a book")
    print("2. Delete a book")
    print("3. Search for a book")
    print("4. Replace a book")
    print("5. Show all books")
    print("6. Exit")

print("Vitaj v nasej kniznici")
while True:
    show_menu()
    choice = int(input("Choose your option: "))
    if choice == 1:
        title = input("Enter title: ")
        author = input("Enter author: ")
        genre = input("Enter genre: ")
        releaseYear = int(input("Enter release year: "))
        publisher = input("Enter publisher: ")
        add_book(books, title, author, genre, releaseYear, publisher)
    elif choice == 5:
        show_all_books()
    else:
        break

print("Dakujem za pouzitie nasej kniznice")