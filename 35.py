class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def __lt__(self,other):
        return self.area()<other.area()
length1=float(input("Enter the length of Rectangle1: "))
width1=float(input("Enter the breadth of Rectangle1: "))
r1=Rectangle(length1,width1)
length2=float(input("Enter the length of Rectangle2: "))
width2=float(input("Enter the breadth of Rectangle2: "))
r2=Rectangle(length2,width2)
if r1<r2:
    print("r1 has smaller Area")
else:
    print("r2  has smaller Area")
