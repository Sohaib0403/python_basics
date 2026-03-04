# WAP to find the greater of 3 numbers entered by the user 

a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

if(a > b):
    if(a > c):
        print("a is greater number")
    else :
        print("c is greater number")
elif(b > a) :
    if(b > c):
        print("a is greater number")
    else :
        print("c is greater number")