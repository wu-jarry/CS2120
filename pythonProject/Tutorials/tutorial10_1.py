from Book import *

# instantiate the first book
my_book = Book()
print(my_book)
print()

# add attributes
my_book.set_title("Think Python, 2nd Edition")
my_book.set_author('Allen B. Downey')
my_book.set_reviews([5, 4, 5, 5, 1, 3, 5, 5, 2, 3, 1, 5, 4, 5])

# instantiate the second book
my_other_book = Book("Thinking in Systems", "Donella H. Meadows")
list_of_reviews = [5, 5, 5, 5, 5, 2, 3, 5, 1, 4, 5]
my_other_book.set_reviews(list_of_reviews)

# output information about the books
print(f'The first book: {Book(my_book)}')
print(f"The first book's id: {Book.get_id(my_book)}")
print(f'The second book: {my_other_book}')
print(f"The second book's id: {my_other_book.get_id()}")
print()

# output the object repr
print(f'The reprs:')
print(f'First: {repr(my_book)}')
print(f'Second: {repr(my_other_book)}')
print()

# check for equality
if my_book == my_other_book:
    print(f'{my_book.get_title()} and {my_other_book.get_title()} have the same number of five-star reviews.')

# alter the reviews
my_book.add_review_score(5)
print(f"The first book's review scores: {my_book.get_reviews()}")
print(f'Number of five-star reviews for the first book: {my_book.review_scores()}')
print(f'Number of five-star reviews for the second book: {my_other_book.review_scores()}')

# check again for equality
if my_book == my_other_book:
    print(f'{my_book.get_title()} and {my_other_book.get_title()} have the same number of five-star reviews.')



