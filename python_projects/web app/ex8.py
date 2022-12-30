#composition

class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price

        self.author = author

        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append((chapter))

    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount
        return result


class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount

   
auth = Author("first", "last")
b1 = Book("book name", 49.95, auth)

b1.addchapter(Chapter("chapter 1", 300))
b1.addchapter(Chapter("chapter 2", 50))
b1.addchapter(Chapter("chpater 3", 60))


print(b1.author)
print(b1.title)
print(b1.getbookpagecount())
