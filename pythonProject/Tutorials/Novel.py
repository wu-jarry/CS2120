# DEFINE THE NOVEL CLASS BELOW
from Book import *


class Novel(Book):
    def __init__(self, title, author, genre=""):
        super().__init__(title, author, reviews=[5, 5, 2, 3])
        self._genre = genre

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_genre(self):
        return self._genre

    def review_scores(self):
        one_star = 0
        two_star = 0
        three_star = 0
        four_star = 0
        five_star = 0
        for element in self._reviews:
            if element == 1:
                one_star += 1
            elif element == 2:
                two_star += 1
            elif element == 3:
                three_star += 1
            elif element == 4:
                four_star += 1
            elif element == 5:
                five_star += 1
        star_counter = [one_star, two_star, three_star, four_star, five_star]
        return star_counter

    def __repr__(self):
        return f'Book("{self._title}", "{self._author}", "{self._genre}", {self._reviews})'

    def __str__(self):
        return f'{self._title} has:\n' \
               f'{self.review_scores()[0]} one-star review(s)\n' \
               f'{self.review_scores()[1]} two-star review(s)\n' \
               f'{self.review_scores()[2]} three-star review(s)\n' \
               f'{self.review_scores()[3]} four-star review(s)\n' \
               f'{self.review_scores()[4]} five-star review(s)\n'

