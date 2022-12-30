class Book:
    #propertites defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    #double-underscore attribute properties are hidden from other classes
    __booklist = None


    #create a class method
    @classmethod
    def getbooktypes (cls):
        return cls.BOOK_TYPES

    #create a static method to access the double under-score
    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist



    #instance method receives a specific object instance as an argument
    #and operate on data specific to that object instance

    def setTitle(self, newTitle):
        self.title = newTitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype


  
print("Book types: ", Book.getbooktypes())
    #create book instances
b1 = Book("Title 1", "HARDCOVER")
b2 = Book("Title 2", "Comic")

    #access the class attirubute
print("Book Types: ", Book.getbooktypes())

#use static method to access a singleton object
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)