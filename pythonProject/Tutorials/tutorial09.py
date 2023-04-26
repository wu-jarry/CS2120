# YOUR NAME

######################### ADD YOUR CODE BELOW #########################

# create your class definitions
class Library:
    def __init__(self, name="Taylor", librarians=[], books=[]):
        self.name = name
        self.librarians = librarians
        self.books = books


class Librarian:
    def __init__(self, name="", favourite_genre="", position=""):
        self.name = name
        self.favourite_genre = favourite_genre
        self.position = position


class Book:
    author = ''

    def __init__(self, name="", genre=""):
        self.name = name
        self.genre = genre


# create your main function
def main():

    # 1. create the Book objects with the provided attributes (using dot notation)
    book1 = Book()
    book2 = Book()
    book1.name = "Kafka on the Shore"
    book1.genre = "literary fiction"
    book2.name = "The Handmaid's Tale"
    book2.genre = "science fiction"
    # book1 = Book(name="Kafka on the Shore", genre="literary Fiction")
    # book2 = Book(name="The Handmaid's Tale", genre="science fiction")
    book3 = Book(name="The Lord of the Rings", genre="fantasy")
    book4 = Book(name="It", genre="horror")

# 2. create the Librarian objects with the provided attributes (using dot notation)
    librarian1 = Librarian(name="Rupert Giles", favourite_genre="horror", position="Head of Rare Books")
    librarian2 = Librarian(name="Miss Saeki", favourite_genre="literary fiction", position="Head Librarian")

# 3. create the Library object with the provided attributes (using dot notation)
    library1 = Library()
    library1.librarians = [librarian1, librarian2]
    library1.books = [book1, book2, book3]

# 4. programmatically add the fourth Book object to the library's collection
    library1.books.append(book4)

# 5. print out the names of the library's books (use a loop)
    print(f'The following is a list of the books available at {library1.name}:')
    for element in library1.books:
        print(element.name)

# 6. print the librarians' names (including the asterisk for the Head Librarian)
    print(f'\nThe librarians at {library1.name} are:')
    for element in library1.librarians:
        if element.position == "Head Librarian":
            element.name = "*" + element.name
    for element in library1.librarians:
        print(element.name)

# 7. build a list of each librarian's favourite books from the list of Book objects in the Library's collection
#    if a book is in the librarian's favourite genre, it should be added to their list of favourite books
    librarian1_favourite_books = []
    librarian2_favourite_books = []
    for element in library1.books:
        if element.genre == librarian1.favourite_genre:
            librarian1_favourite_books.append(element)
        if element.genre == librarian2.favourite_genre:
            librarian2_favourite_books.append(element)

# 8. for each book in the first librarian's book list, if the object has an author
    for element in librarian1_favourite_books:
        if element.author:
            print(f'{element.author} and {library1.librarians.libarian1.name}')
    for element in librarian2_favourite_books:
        if element.name:
            print(f"\n{element.name} is one of {librarian2.name.strip('*')}'s favourite books.")

######################### ADD YOUR CODE ABOVE #########################
main()
