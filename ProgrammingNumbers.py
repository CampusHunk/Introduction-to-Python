# **Programming with numbers**

#Programs that don't calculate at least something are quite rare. Thus, learning to program with numbers is always a good idea.
#An even more valuable skill we're about to learn is processing user data. With this skill, you can create interactive and much 
# more flexible applications. But first, let's make sure you remember all about integer arithmetic. What should be the output of 
# the mini-program below?
a = 5
b = 3
my_sum = a + b
my_product = a * b
print("My product - my sum is:", my_product - my_sum)
print()

# **Reading numbers from user input**

#Since you have become familiar with the input() function in Python, it's hardly new to you that any data passed to this 
# function is treated as a string.
#But how should we deal with numerical values? As a general rule, they are explicitly converted to corresponding numerical types. 
# To do it, we add data type before input:
Integer = int(input("Enter your first number: "))
Float = float(input("Enter your second number: "))
print("Integer + Float is:",Integer + Float)
print()

# **Common errors**

#We should consider user mistakes: if a user types an incorrect input, like the string 'two' instead of the number 2, an error 
# (ValueError, to be precise) will occur. We'll learn how to handle such scenarios in the future.
num_1 = int(input("Enter first number: "))
num_2 = int(input("ENter second number: "))
print("First number + second number is:", num_1 + num_2)
print()

# **Free air points**

#Imagine you have a credit card with a free air points bonus program. As a user, you are expected to input the amount of money 
# you spend on average from this card per month. Let's assume that the bonus program gives you 2 free air points for every dollar you spend. 
# Here's a simple program to figure out when you can travel somewhere for free. Fill the blanks to complete it!

#The average amount of money per month 
money = int(input("How much money you spend per month: "))

#The number of points per unit of money
n_points = 2

#Earned points
points_per_month = money * n_points

#The distance between Paris and London
distance = 215

#How many months do you need to get
# a free trip?
print("Months required to get a free trip:", distance * 2 // points_per_month, "months")
print()

# **Advanced forms of assignment**

#Whenever you use an equal sign =, you actually assign some value to a variable. For that reason, = is typically referred to as 
# an assignment operator.
#Meanwhile, there are other assignment operators you can use in Python. They are also called compound assignment operators, 
# for they carry out an arithmetic operation and assignment in one step. Have a look at the code snippet below:

# simple assignment
number = 2
number = number + 5 #7

#This code is equivalent to the following one:

# compound assignment
number = 2
number += 5 #7

#One can clearly see from the example that the second piece of code is more concise (for it doesn't repeat the variable's name). 
# Naturally, similar assignment forms exist for the rest of arithmetic operations.
#If you’re coming from a language like C++, you might expect that ++ or -- operators will increase or decrease a value in Python. 
# However, Python does not support these operators, so be mindful and use += or -= for incrementing or decrementing values. 
# And, == is a comparison operator, which we’ll cover later, not a compound assignment operator.

# **Compound assignment operators**

#Suppose you have this abstract piece of code:
capital = int(input("Enter your capital: "))
capital = capital * 0.8
additional_income = 1000
capital = capital + additional_income
print()

#As we learned, it can be shortened and become more readable, without changing its functionality. Let's do it:
capital = int(input("Enter your capital contribution: "))
capital *= 0.8
additional_income = 1000
capital += additional_income
print("Your capital after the year:", capital)
print()

# **Calculating income**
#Imagine making all the calculations in banks by hand, like we used to do years ago. A nightmare, right?

#Well, calculate the income from a savings account with a 5% interest rate after one year, given the amount of money. Use the 
# simple interest formula to calculate the income:
amount = 1000
interest_rate = 5
years = 1
income = amount * interest_rate * years
income /= 100
print("Your income for the year after interest:", income)
print()

# **Calculating an expression**

#Write a program that inputs variable n as integer and prints the result of the expression:

#Take input
n = int(input("Enter the value of n: "))
#Calculate the expression
n = ((n + 1) * n + 2) * n + 3 
print("The value of n is:", n)
print()

# **Calculating 3D perimeter**

#Now, brace yourself for some classical math tasks.

#In this task, the program should ask the user about parameters of a rectangular parallelepiped (3 integers representing the 
# length, width, and height) and print the sum of edge lengths.

# Sum of lengths of all edges: s= 4(a + b + c)
a = int(input("Enter length: "))
b = int(input("Enter width: "))
c = int(input("Enter height: "))
perimeter = 4 * (a + b + c)
print("the sum of edge lengths is:", perimeter)
print()

#In this task, the program should ask the user about parameters of a rectangular parallelepiped (3 integers representing the 
# length, width, and height) and print its surface instead.

# Surface area: s = 2 (ab + bc + ca)

a = int(input("Enter length: "))
b = int(input("Enter width: "))
c = int(input("Enter height: "))
surface = 2 * (a * b + b * c + c * a)
print("The total surface area is:", surface)
print()

# **Calculating volume**
#Ask the user about parameters of a rectangular parallelepiped (3 integers representing the length, width, and height) and print its volume.

# Volume: v = abc
a = int(input("Enter length: "))
b = int(input("Enter width: "))
c = int(input("Enter height: "))
volume = a * b * c
print("Total volume is:", volume)
print()
