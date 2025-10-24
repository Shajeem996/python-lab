string = input("ENTER STRING") 
n = len(string) 
if n >= 2:
    first = string[0] 
    last = string[n-1] 
    mod_str = last + string[1:n-1] + first 
else:
    mod_str = string
print("Modified String:", mod_str)
