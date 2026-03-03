# Type conversion

a = 2
b = 5.6

c = a + b

print(c)  # int + float = float
print(type(c))



# type cansting
# forcly converted one type to another type
# only work for numbers not alphabets or letters



# e = 10
# f = "20" 

# g = e + f           will show error 
# print(g)     

e = 10
f = int("20") # forcly converted string to int

g = e + f
print(g)      # int 