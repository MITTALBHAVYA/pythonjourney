class Library:
    def __init__(self):
        self.noBooks=0
        self.books=[]
    def addBooks(self,book):
        self.books.append(book)
        self.noBooks=len(self.books)
    def showInfo(self):
        print(f"the number of books in the library are {self.noBooks} which are")
        for book in self.books:
            print(book)
l1=Library()
l1.addBooks("HARRY PORTER")
l1.addBooks("JAI SHREE RAM")
l1.showInfo()