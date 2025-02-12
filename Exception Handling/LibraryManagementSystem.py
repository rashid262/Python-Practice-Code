class BookNotAvailableError(Exception):
    pass

class Library:
    def __init__(self):
        self.books = {"Harry Potter": True, "The Hobbit": True, "The Great Gatsby": True}  # Predefined books

    def rent_book(self, title):
        if title not in self.books:
            raise BookNotAvailableError("Unavailable")
        elif not self.books[title]:  # Already rented
            raise BookNotAvailableError(f"{title} is already rented.")
        else:
            self.books[title] = False
            print(f"{title} rented successfully")

    def return_book(self, title):
        if title not in self.books:
            raise BookNotAvailableError(f"Cannot return {title}. It was never in the library.")
        elif self.books[title]:  # Already returned
            raise BookNotAvailableError(f"Return failed. Book {title} was not rented.")
        else:
            self.books[title] = True
            print(f"{title} returned successfully.")

title1 = input()
title2 = input()

lib1 = Library()

try:
    lib1.rent_book(title1)
except BookNotAvailableError as e:
    print(e)

try:
    lib1.return_book(title2)
except BookNotAvailableError as e:
    print(e)
