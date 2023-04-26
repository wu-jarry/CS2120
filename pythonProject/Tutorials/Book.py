# DEFINE THE BOOK CLASS BELOW

class Book:
    book_identification_number = 10000

    def __init__(self, title="", author="", reviews=[]):
        self._title = title
        self._author = author
        self._reviews = reviews
        self._set_id()

    def _set_id(self):
        self._id = Book.book_identification_number
        Book.book_identification_number += 1

    def get_id(self):
        return self._id

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_reviews(self):
        return self._reviews

    def set_title(self, title):
        self._title = title

    def set_author(self, author):
        self._author = author

    def set_reviews(self, reviews):
        self._reviews = reviews

    def review_scores(self):
        counter = 0
        for element in self._reviews:
            if element == 5:
                counter += 1
        return counter

    def add_review_score(self, other_review):
        return self._reviews.append(other_review)

    def __eq__(self, my_other_book):
        return self.review_scores() == my_other_book.review_scores()

    def __str__(self):
        return f'{self._title}, by {self._author}, has {self.review_scores()} five-star reviews.'

    def __repr__(self):
        return f'Book("{self._title}", "{self._author}", {self.get_reviews()})'
