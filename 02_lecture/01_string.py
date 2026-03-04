# string
# string is a data type that store a sequence of characters

str1 = "my name is sohaib"
str2 = 'my age is 25'
str3 = """i love python"""

#escape sequence character

# \n user start scentence in next line

str4 = "i am learning python.\n currently on topic string "


print(str1)
print(str2)
print(str3)
print(str4)







# basic operation on strings

# concatination : used to add two string togather

str5 = "sohaib"
str6 = "siddiqui"
finalStr = str5 + str6
print(finalStr)


# length of str : used to find length of str
# len(str)
# also count digit(123) / space(" ") / characthers(abcd)

str7 = "lets find out the length of str"

print(len(str7)) #shoe the length of str : 31 (total no. of chracther)






# indexing

# always start with 0

str8 = "sohaib_siddiqui"

print(str8[3])   # a



# Slicing
# Accessing parts of a sting

str9 = "SohaibSiddiqui"

print(str9[0:6])   # 0,1,2,3,4,5  : Sohaib
print(str9[6:len(str9)])   # Siddiqui


# negative index Slicing


str10 = "Sohaib"

print(str10[-6:len(str10)])    # sohaib
print(str10[-5:-1])   # ohai