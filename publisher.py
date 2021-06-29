class publisher:
    def __init__(self):
        self.name='Dhanusha'
    def display(self):
        print("Name : ",self.name)
class Book(publisher):
    def __init__(self):
        self.title='My Book'
        self.author='Dhanusha Nandakumar'
    def display(self):
        super().__init__()
        super().display()
        print("Title : ",self.title,"\n Author : ",self.author)
class Python(Book):
    def __init__(self):
        self.price=300
        self.no_of_pages=100
    def display(self):
        super().__init__()
        super().display()
        print("Price : ",self.price,"\n Number of Pages : ",self.no_of_pages)
b=Python()
print("Book details are : \n")
b.display()  
