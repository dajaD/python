#basic class

class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        #add more propertites
        self.author = author
        self.pages =  pages
        self.price = price
        self.__secret = "this is a secret attribute"


    #method to get price
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount

#instance of class
b1 = Book("Brave new World", "Random Name", 1225, 39.95)
b2 = Book("War and Peace", "Another Name", 234, 29.95)


#print class and property
print(b1)
print(b1.title)

#get price of b1
print(b1.getprice())

#try discount
print(b2.getprice())
b2.setdiscount(.5)
print(b2.getprice())

#access secret attribute
#print(b2.__secret)
#gives an error, can't be seen outside the class
#can be accessed using the by name-mangling
print(b2._Book__secret)

