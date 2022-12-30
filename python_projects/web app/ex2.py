class Book:
    def __init__(self, title):
        self.title = title

class Newspaper:
    def __init__(self, name):
        self.name = name

b1 = Book("The catcher and the rye")
b2 = Book("The help")

n1 = Newspaper("Chicago suntime")
n2 = Newspaper("The Washington post")

#use type() to inspect the object type
print(type(b1))
print(type(n1))

#compare two type together
print(type(b1) == type(b2))
print(type(b1) == type(n1))
print()

#use isinstances to compare a specific instance to a known type
print(isinstance(b1, Book))
print(isinstance(n1, Newspaper))
print(isinstance(n2, Book))
print(isinstance(n2, object))