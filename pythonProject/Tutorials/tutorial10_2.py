from Novel import *

# instantiate a Novel object
favourite_book = Novel("Station Eleven", "Emily St. John Mandel")
print(favourite_book)

# instantiate another Novel object
another_fave = Novel("Ready Player One", "Ernest Cline", "Science Fiction")
print(another_fave)

# check for equality
if favourite_book == another_fave:
    print(f'{favourite_book.get_title()} and {another_fave.get_title()} have the same number of five-star reviews.')
print()

# get the id and genre of the second Novel object
print(f'{another_fave.get_title()} has the following id: {another_fave.get_id()}')
print(f"Its genre is: {another_fave.get_genre()}")
