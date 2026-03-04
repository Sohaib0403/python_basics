# nesting

# condition in another condition

str1 = int(input("enter your age : "))

if(str1 >= 18 and str1 != 0) :
    if(str1 >= 40) :
       print("to old to drive")
    else :
       print("good age to drive to drive") 
elif ( str1 < 18 and str1 != 0)  :
    print("your are a kid")
else  :
    print("enter your age")
