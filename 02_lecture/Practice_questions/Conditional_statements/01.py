# grade students based on marks

# 90+ = A
# 90 > marks >80 = B
# 80> marks >= 70  = C 
# 70 > marks = D


name = input("enter student name : ")
marks = int(input("enter the student marks : "))

if(marks >= 90) :
    print(name + " A grade")
elif(marks < 90 and marks >= 80) :
    print(name + " B grade")
elif(marks < 80 and marks >= 70) :
    print(name + " C grade")
else :
    print(name + " D grade")