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


 
