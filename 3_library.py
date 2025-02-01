# You are building a Library Management System. Create a `Book` class with properties like `title`, 
# `author`, and `isbn`. Write a method to display book details.


class Library:
    def Details(self,title,author,isbn):
        self.titlename=title
        self.author=author
        self.isbn=isbn
    def get_library_info(self):
        print (f'Title: {self.titlename} \nAuthor: {self.author} \nISBN: {self.isbn}')
        print() 
a=input("Enter the Title of Book ")
b=input("Enter name of the Author is ")
c=input("Enter Books ISBN  ")

L=Library()
L.Details(a,b,c)
L.get_library_info()

