class Time:
    def __init__(self,hour=0,minute=0,second=0):
        self.__hour=hour
        self.__minute=minute
        self.__second=second
    def __add__(self,other):
        total_seconds=(self.__hour+other.__hour)*3600+\
                       (self.__minute+other.__minute)*60+\
                       (self.__second+other.__second)
        hours=total_seconds // 3600
        minutes=(total_seconds%3600) // 60
        seconds=total_seconds %60
        return Time(hours,minutes,seconds)
    def display(self):
        print(f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}")
print("Enter first time:")
h1=int(input("Hours: "))
m1=int(input("Minutes: "))
s1=int(input("Seconds: "))
print("Enter second time:")
h2=int(input("Hours: "))
m2=int(input("Minutes: "))
s2=int(input("Seconds: "))
t1 = Time(h1,m1,s1)
t2 = Time(h2,m2,s2)
t3 = t1 + t2
print("\n__Results___")
print("Time 1:",end=" ")
t1.display()
print("Time 2:",end=" ")
t2.display()
print("sum:  ",end=" ")
t3.display()















                
