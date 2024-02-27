class Book:

    def __init__(self, name, author, pages):
        self.names = name
        self.author = author
        self.pages = pages


book = Book("My Book", "Me", 200)
print(book.names)
print(book.author)
print(book.pages)