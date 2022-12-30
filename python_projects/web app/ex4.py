#inhertance pratice

class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher

class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages

        

class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)


class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)


b1 = Book("Book 1", "Author name 1", 300, 49.95)
m1 = Magazine("Magazine 1", "Author name 2", 6.0, "Daily") 
n1 = Newspaper("Newspaper 1", "Author name 3", 5.99, "Daily")

print(b1.author)
print(m1.price, b1.price, n1.price)
print(n1.period)