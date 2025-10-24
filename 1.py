curr = int(input("Enter the current year:")) 
fut = int(input("Enter the future year:")) 
print("Leap Years:") 
for year in range(curr, fut+1): 
    if ((year % 4 == 0) and year % 100 != 0) or (year % 400 == 0): 
        print(year)
