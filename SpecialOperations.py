# **Integer arithmetic: special operations**

#In Python, we have a few special operations that are not part of the basic arithmetic operations.
#Exponentiation, or raising a number a to the power of b,  is a super useful operation in mathematics. 
#In Python, we don't use the ^ symbol for exponentiation. Instead, we use
print(2**3)
print()
a = 2
b = 3
print("2 to the power of 3 is:", a**b) #Pretty cool, right?


# **Volume of a cube**

#Assume you're a student tackling a geometry problem: finding the volume of a cube.
#the volume of a cube can be calculated using a simple formula: Volume=(side length)**3
#Armed with a ruler, you measure one side, finding it to be 4 units long. find the volume of the cube and print it to the screen by writing a Python program.

volume = 4**3
print("Volume is 4 to the power of 3 is:", volume)
print()

# **The remainder**

#Before moving into the next special operator in Python, let's discuss a little about the remainder.
#The remainder of a division, also known as the modulus, is the integer left over after dividing one integer by another. In other words,
# when you divide one integer by another, the remainder is what's left when the division is not exact.
#For example, if you divide 10 by 3, the remainder is 1.
#Or 7 by 3, the quotient is 2 and the remainder is 1 because 3  goes into 7 twice with a remainder of 1.
#You've mastered multiplication, subtraction, and integer division in Python. But did you know you can use just these three
#operations to calculate the remainder of a division? For example, the remainder when dividing 15 by 6 is 3 which can be calculated as follows:
remainder_15 = 15 - (15 // 6) * 6
print(remainder_15)
remainder_53 = 53 - (53 // 7) * 7
print(remainder_53)
remainder_7 = 7 - (7 // 3) * 3
print(remainder_7)
print()

# **Modulo operator**

#The modulo operator (%) is a special operator in Python that returns the remainder of a division.
#One of its handy uses is checking whether a number is even or odd. For instance:
print(62 % 12)
print(23 % 4)

# **Calculating the leftover**
# Lets say you have 15 chocolates and you want to distribute them equally among 4 students. How many chocolates will be left after the equal distribution?
print(15 % 4)
print(14 - (14 // 2) * 2)
print()

# **Time format converter**

#We've stored a time value in the 24-hour format in a variable named hour. Your task is to convert this value to a 12-hour format and print the result.
#For example, if the value of hour is 14, the output should be 2.
#If hour is 12, the output should be 0. 
hour = 14
hour_24 = 12
hour_123 = 13
time_converter = 4
print(hour % time_converter)
print(hour_24 % time_converter)
print(hour_123 % time_converter)
print()

# **Complex expressions**
#You can blend together the arithmetic operations we've covered to craft more complex expressions.
#Keep in mind the order of precedence for these operators. Here's the hierarchy:
#Parentheses > Exponentiation > Multiplication/Division/Integer Division/Modulo > Addition/Subtraction
#While not an operation itself, parentheses serve to clarify the order of execution. 
# Anything within parentheses gets calculated before any operations outside. They're like the directors calling the shots on which operations to execute first. Pretty dominating, huh?
print((5 + 3) - 6**2 / 3) 
print((5 + 3) - (6**2 / 3))
print(6**3)

# **Investment planning**
# **Integer arithmetic: special operations**

# In Python, we have a few special operations that are not part of the basic arithmetic operations.
# Exponentiation, or raising a number a to the power of b,  is a super useful operation in mathematics. 
# In Python, we don't use the ^ symbol for exponentiation. Instead, we use
print(2**3)
print()

# Define variables for better readability
a = 2
b = 3
print(f"{a} to the power of {b} is: {a**b}") 

# **Volume of a cube**

# Assume you're a student tackling a geometry problem: finding the volume of a cube.
# The volume of a cube can be calculated using a simple formula: Volume=(side length)**3
# Armed with a ruler, you measure one side, finding it to be 4 units long. Find the volume of the cube and print it to the screen by writing a Python program.

side_length = 4
volume = side_length**3
print(f"Volume of a cube with side length {side_length} is: {volume}")
print()

# **The remainder**

# Before moving into the next special operator in Python, let's discuss a little about the remainder.
# The remainder of a division, also known as the modulus, is the integer left over after dividing one integer by another. In other words,
# when you divide one integer by another, the remainder is what's left when the division is not exact.
# For example, if you divide 10 by 3, the remainder is 1.
# Or 7 by 3, the quotient is 2 and the remainder is 1 because 3  goes into 7 twice with a remainder of 1.
# You've mastered multiplication, subtraction, and integer division in Python. But did you know you can use just these three
# operations to calculate the remainder of a division? For example, the remainder when dividing 15 by 6 is 3 which can be calculated as follows:
def calculate_remainder(dividend, divisor):
    return dividend - (dividend // divisor) * divisor

remainder_15 = calculate_remainder(15, 6)
print(remainder_15)
remainder_53 = calculate_remainder(53, 7)
print(remainder_53)
remainder_7 = calculate_remainder(7, 3)
print(remainder_7)
print()

# **Modulo operator**

# The modulo operator (%) is a special operator in Python that returns the remainder of a division.
# One of its handy uses is checking whether a number is even or odd. For instance:
print(62 % 12)
print(23 % 4)

# **Calculating the leftover**
# Let's say you have 15 chocolates and you want to distribute them equally among 4 students. How many chocolates will be left after the equal distribution?
print(15 % 4)
print(14 - (14 // 2) * 2)
print()

# **Time format converter**

# We've stored a time value in the 24-hour format in a variable named hour. Your task is to convert this value to a 12-hour format and print the result.
# For example, if the value of hour is 14, the output should be 2.
# If hour is 12, the output should be 0. 
def convert_to_12_hour_format(hour):
    return hour % 12

hour = 14
hour_24 = 12
hour_123 = 13
print(convert_to_12_hour_format(hour))
print(convert_to_12_hour_format(hour_24))
print(convert_to_12_hour_format(hour_123))
print()

# **Complex expressions**
# You can blend together the arithmetic operations we've covered to craft more complex expressions.
# Keep in mind the order of precedence for these operators. Here's the hierarchy:
# Parentheses > Exponentiation > Multiplication/Division/Integer Division/Modulo > Addition/Subtraction
# While not an operation itself, parentheses serve to clarify the order of execution. 
# Anything within parentheses gets calculated before any operations outside. They're like the directors calling the shots on which operations to execute first. Pretty dominating, huh?
print((5 + 3) - 6**2 / 3) 
print((5 + 3) - (6**2 / 3))
print(6**3)

# **Investment planning**

#Who doesn't want to be rich? So, let's invest some money.
#If you invest $x at an annual interest rate of r%, compounded yearly, the value of the investment a after y years will be:
# a = x * (1 + r/100) ** y
#Let's say you have invested $1000 at the yearly compound interest rate of 5% What will be the value of the investment after 10 years?

x = 1000
r = 5
y = 10

print(x * (1 + r/100) ** y, 'n')

# **Hours and minutes**

#For an upcoming programming competition, the event's website displays a countdown of 856 minutes until it starts. 
# Write a Python program to convert this value into hours and remaining minutes. Store the hour value in the variable hours and the minute value in the variable remaining_minutes

minutes = 856
hours = minutes // 60
remaining_minutes = minutes % 60
print(hours)
print(remaining_minutes)