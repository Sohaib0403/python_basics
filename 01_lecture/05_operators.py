# arithmetic operators
# + - * / % ** //


# sum of two numbers


a = 6
b = 7

sum = a + b
print(sum)

# find the diffrence of two numbers

diffrence = a - b
print(diffrence)


#find the product of two numbers

product = a*b
print(product)

#find division of two numbers

division = a/b
print(division)

#find remainder of two numbers

remainder = a%b
print(remainder)

#find power of two numbers

power = a**b
print(power)

#find floor division of two numbers

floor_division = a//b
print(floor_division)


# relational operators
# used to compare two values
# show output in boolean (true or false)
# == != < > <= >=

print(a == b) # is equals to
print(a != b) # is not equals to
print(a>b) # is a is greater than b
print(a<b) # a is smaller than b
print(a>=b) # is a is greater than or equals to b
print(a<=b) # is a is smaller than or equals to b



#assignment operators
# = += -= *= /= %= **= //=

# used to assign values to variables
# = is used to assign values to variables
# += is used to add values to variables
# -= is used to subtract values from variables
# *= is used to multiply values to variables
# /= is used to divide values to variables
# %= is used to find remainder of values to variables
# **= is used to find power of values to variables
# //= is used to find floor division of values to variables


# example
c=b
print(c)

d = 0
d += b
print(d)

d -= b
print(d)

d *= b
print(d)

d /= b
print(d)

d %= b
print(d)

d **= b
print(d)

d //= b
print(d)




#logical operators
# and or not
# used to combine two or more conditions
# show output in boolean (true or false)
# and is used to check if both conditions are true
# or is used to check if at least one condition is true
# not is used to check if the condition is false

print(a and b)
print(a or b)
print(not a)


#identity operators
# is is not
# used to check if two values are same
# show output in boolean (true or false)
# is is used to check if two values are same
# is not is used to check if two values are not same

print(a is b)
print(a is not b)


#membership operators
# in not in
# used to check if a value is present in a sequence
# show output in boolean (true or false)
# in is used to check if a value is present in a sequence
# not in is used to check if a value is not present in a sequence

letter = "a"
word1 = "apple"
word2 = "cherry"

print(letter in word1)
print(letter not in word2)




# Bitwise Operators Example 2

# Define two integers
a = 12     # Binary of 12 = 1100
b = 10     # Binary of 10 = 1010


# &  (Bitwise AND)
# Returns 1 only if both bits are 1
#   1100
# & 1010
# -------
#   1000  → 8
print(a & b)   # Output: 8


# |  (Bitwise OR)
# Returns 1 if at least one bit is 1
#   1100
# | 1010
# -------
#   1110  → 14
print(a | b)   # Output: 14


# ^  (Bitwise XOR)
# Returns 1 if bits are different
#   1100
# ^ 1010
# -------
#   0110  → 6
print(a ^ b)   # Output: 6


# ~  (Bitwise NOT)
# Formula: ~a = -(a + 1)
# ~12 = -(12 + 1) = -13
print(~a)      # Output: -13


# <<  (Left Shift)
# Multiply by 2^b
# 12 << 2 means shift 2 times
# 1100 → 110000  → 48
print(a << 2)  # Output: 48


# >>  (Right Shift)
# Divide by 2^b
# 12 >> 2
# 1100 → 0011  → 3
print(a >> 2)  # Output: 3


