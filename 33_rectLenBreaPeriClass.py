class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    
length1=float(input("Enter the length of Rectangle1: "))
breadth1=float(input("Enter the breadth of Rectangle1: "))
r1=rectangle(length1,breadth1)
length2=float(input("Enter the length of Rectangle2: "))
breadth2=float(input("Enter the breadth of Rectangle2: "))
r2=rectangle(length2,breadth2)
print("Area of Rectangle1 :",r1.area())
print("Perimeter of Rectangle1 :",r1.perimeter())
print("Area of Rectangle1 :",r2.area())
print("Perimeter of Rectangle1 :",r2.area())

if r1.area()>r2.area():
    print("Rectangle 1 has more area")
elif r1.area()<r2.area():
    print("Rectangle 2 has more area")
else:
    print("Both Rectangle has same area")
