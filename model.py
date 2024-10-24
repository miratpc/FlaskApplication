# model.py

class Book:
    def __init__(self, isbn, title, year, price, page, category, coverPhoto, publisher, author):
        self.isbn = isbn
        self.title = title
        self.year = year
        self.price = price
        self.page = page
        self.category = category
        self.coverPhoto = coverPhoto
        self.publisher = publisher
        self.author = author

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "title": self.title,
            "year": self.year,
            "price": self.price,
            "page": self.page,
            "category": self.category,
            "coverPhoto": self.coverPhoto,
            "publisher": self.publisher,
            "author": self.author
        }
