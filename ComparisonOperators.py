# **Comparison operators**

# Comparison or relation operations let you compare two values and determine the relation
# between them. There are ten comparison operators in Python:

#* < strictly less than
#* > strictly greater than
#* <= less than or equal to
#* >= greater than or equal to
#* == equal to
#* != not equal to
#* is object identity
#* is not negated object identity
#* in membership 
#* not in negated membership

# The result of applying these operators is always bool. The following sections focus on the
# first six operators (<, <=, >, >=, ==, !=), but you can find more details about identity
# and membership testing in the next topics. Also, pay attention to the greater/less than or 
# qual operators, they are supposed to be written in the same order their names are pronounced: 
# <= less than or equal, >= greater than or equal.

# **Comparing integers**

#In this topic, we will cover only integer comparison.
a = 5
b = -10
c = 15

result_one = a < b
result_two = a == a
result_three = a != b
result_four = b >= c

# Any expression that returns an integer is a valid comparison operand too:

calculated_result = a == b + c

# Given the defined variables a, b and c, we basically check if 5 is equal to -10 + 15, 
# which is true.

# **Comparison chaining**

# Since comparison operations return boolean values, you can join them using logical operators. 
# In this case, it is important to know their priority, i.e. which one is executed first. 
# All comparison operations have the same priority, and it is lower than that of any arithmetic, 
# shifting, or bitwise operation (the last two are used for operations with bytes).

x = -5
y = 10
z = 12

result = x < y and y <= z

# n Python, there is a fancier way to write complex comparisons. It is called chaining. For 
# example, x < y <= z is almost equivalent to the expression you saw in the last example. 
# The difference is that y is evaluated only once.

result = 10 < (100 * 100) <= 10000  # True, the multiplication is evaluated once

#Please pay attention to the fact that tools for code quality often recommend chaining comparisons instead of joining them.

#Comparison chaining, however, should be used carefully because sometimes expressions 
# might get tricky, so the result would depend on the operators' order and how the parentheses are put. 
# Consider this example:

a = 1
b = 2
c = 3
d = 4
e = 5
f = 6

print(b + c <= d or e + f >= d == e == 5)
print((b + c <= d or e + f >= d == e) == (e == 5))

# The first expression is False because it is evaluated the following way: or operator has the 
# lowest priority, so it will be evaluated last. The first argument (b + c <= e) is False. 
# The second argument is the long one: f + g >= e == f == 5, it is going to be evaluated 
# consequently, so let's break it down: this expression is equivalent to (f + g >= e) and (e == f) and (f == 5), 
# which evaluates to False. Finally calculate the value of the whole expression: False or False is False. 
# In the second case, we have False in the left parenthesis and False in the right parenthesis, 
# so False equals False.

# **Logic & arithmetics**

# Let's look at another interesting case. At the beginning of the topic, we learned that the 
# result of applying comparison operators is always bool. However, if there is a logical and 
# arithmetic part in an expression, we might see unusual behavior due to logical operators in 
# Python being short-circuited, or lazy:

a1 = 1
b1 = 2
c1 = 3
e1 = 4
f1 = 5
g1 = 6

# True and-expressions return the result of the last operation:
print(b1 + c1 * f1 >= e1 and (f1 + g1) * c1) ## (17 >= 4 is True) and 33 -> 33
print((f1 + g1) * c1 and b1 + c1 * f1 >= e1) ## 33 and (17 >= 4 is True) -> 33

# False and-expressions return a boolean False value:
print(b1 + c1 * f1 <= e1 and (f1 + g1) * c)  # (17 <= 4 is False) and 33 --> False
print((f1 + g1) * c1 and b1 + c1 * f1 <= e1)  # 33 and (17 <= 4 is False) --> False

# True or-expressions return the result of the first operation:
print(b1 + c1 * f1 >= e1 or (f1 + g1) * c)  # (17 >= 4 is True) or 33 --> True
print((f1 + g1) * c1 or b1 + c1 * f1 >= e1)  # 33 or (17 >= 4 is True) --> 33

# True-False or-expressions return the True part:
print((f1 + g1) * c1 or b1 + c1 * f1 <= e1)  # 33 or (17 <= 4 is False) --> 33
print(b1 + c1 * f1 <= e1 or (f1 + g1) * c1)  # (17 <= 4 is False) or 33 --> 33

# True test
# Select all the values of variable a such that test_result is True.
# -100
# 0
# 100
# 200
# 500

a = ...
a = -100  # Can also use 0 or 500 to get True result

test_result = a <= 0 or a > 200
print("Test result:",test_result)

#Let's check each value from the given options:

#-100: Since -100 ≤ 0, this will make test_result True
#0: Since 0 ≤ 0, this will make test_result True
#100: Since 100 > 0 AND 100 ≤ 200, this will make test_result False
#200: Since 200 > 0 AND 200 ≤ 200, this will make test_result False
#500: Since 500 > 200, this will make test_result True

# **Comparing two integers and reporting the result**

# Consider you have two integers, num1 set to 100 and num2 set to 200. You need to compare these two numbers and store the 
# result of the comparison (whether num1 is less than num2) in a variable named comparison_result. Then, use a pre-formatted 
# string to report the comparison result in the form: 'The comparison result of num1 being less than num2 is: comparison_result.

num1 = 100
num2 = 200
comparison_result = num1 < num2
print("The comparison result of num1 being less than num2 is:", comparison_result)

# **Carry on!**

# If you've ever traveled by plane, you know that there are strict rules when it comes to carry-on luggage. A handbag has three 
# dimensions: width, length and height. Some company set the following rule for the carry-on:

height = 10
width = 35
length = 25

allowed = (height <= 10 and width < 35 and length <= 40) or (height + width + length <= 80)
print(allowed)

# **Matchmaker**

# Here are the values of some variables:
x = 1
y = 1
z = 1000
q = 1000
m = 37

contestant_1 = z < y
contestant_2 = x == y
contestant_3 = m > q

print("Matchmaker:",contestant_1)
print("Matchmaker:",contestant_2)
print("Matchmaker:", contestant_3)

# **In the middle**

# Write a program that reads an integer value from input and checks if it is less than 10 or greater than 250.
a = int(input().strip())
checker = a < 10 or a > 250
print(checker)

# **Hot or not? Weather station's dilemma**

# A weather station needs to report if the temperature is above or below a certain threshold. Can you fill the blanks in the code 
# to convert Celsius to Fahrenheit and check if it's above the threshold?

celsius = 25
threshold = 80
fahrenheit = (celsius * 9/5) + 32
above_threshold = fahrenheit > threshold
result = "above" if above_threshold else "below"
print(f"The temperature is {fahrenheit}°F, which is {result} the threshold.\n")

# **Goldilocks' thermostat challenge**

# Write a program to check if the current temperature is within a safe range? The program should print "Safe" if 
# the temperature is between the minimum and maximum values, and "Alert!" otherwise.

current_temp = 22
safe_min = 18
safe_max = 24
if current_temp >= safe_min and current_temp <= safe_max:
    print("Safe\n") 
else:
    print("Alert!")

# **Discount**

# The museum gives discounts to people according to the following rule:
# This condition determines if a person is eligible for a museum discount based on their age
# The condition (age < 21) or (age >= 65) will return True in two cases:
# 1. If the person is under 21 years old (age < 21)
# 2. If the person is 65 years or older (age >= 65)
# This creates two age groups that get discounts:
# - Youth discount: Ages 0-20 
# - Senior discount: Ages 65 and up
# Anyone between 21-64 years old (inclusive) will not get a discount
age = 15
discount = (age < 21) or (age >= 65)
print(discount)

# Based on the discount rule (age < 21) or (age >= 65):
# Mary (49) - No discount (49 >= 21 and 49 < 65)
# Andrew (50) - No discount (50 >= 21 and 50 < 65) 
# Dora (21) - No discount (21 >= 21 and 21 < 65)
# John (15) - Gets discount (15 < 21)
# Ann (75) - Gets discount (75 >= 65)
# So John and Ann will get discounts

# **Guessing game**

# You are playing a guessing game with a user. Imagine that you came up with an integer stored in a variable set_number.
# Check if set_number is equal to the product of two integers entered by the user.

# The input format:
# Two lines containing integer numbers for you to multiply.

set_number = 6557
num_1 = int(input("Enter first number:"))   
num_2 = int(input("Enter second number:"))
print(set_number == num_1 * num_2)

# *Comparing heights: Andy and Ben**

# Write a Python program that reads two integer numbers from the input. The first integer is the height of Andy, and the second 
# one is the height of his best friend Ben. Your program should print 'True' if Andy is taller than Ben or 'False' otherwise.

andy_height = int(input("Enter Andy's height: "))
ben_height = int(input("Enter Ben's height:"))
print(andy_height > ben_height)

# **Focus on the positive**

# Write a program that reads an integer value from the input and checks if it is positive.
# Hints:
# 0 is not a positive number.
# A comparison already returns a boolean, so if you need the result of the comparison, you can print it, like this print(5 > 9)#False

num = int(input("Enter a number:"))
negative_num = 0
print(num > negative_num)

# **Movie theater**

# The movie theater has cinema halls that can accommodate a certain number of viewers each day. Figure out if a movie theater 
# can hold a given number of viewers that plan to visit it on a particular day.
# The input format:
# The first line contains the number of cinema halls.
# The second line contains the number of cinema visitors.
# The third line contains the number of cinema visitors on a particular day.

num_halls = int(input("Enter the number of cinema halls:"))
num_visitors = int(input("Enter the number of cinema visitors:"))
num_visitors_per_day = int(input("Enter the number of cinema visitors on a particular day:"))
print(num_halls * num_visitors_per_day >= num_visitors)

# or 

num_halls = int(input("Enter the number of cinema halls:"))
capacity = int(input("Enter the number of cinema visitors:"))
planned_viewers = int(input("Enter the number of cinema visitors on a particular day:"))
total_capacity = num_halls * capacity
print(total_capacity >= planned_viewers)

# **Very odd**

# Find out if the result of dividing A by B is an odd number.

# The input format:
# The first line is the dividend (A) and the second line is the divisor (B). 
# It is guaranteed that the numbers are divided without remainder.

A = int(input("Enter a dividend:"))
B = int(input("Enter a divisor:"))
result = A // B
print(result % 2 != 0)

# or

A = int(input("Enter a dividend:"))
B = int(input("Enter a divisor:"))
result = A / B
is_odd = result % 2 != 0
print(is_odd)

# **Enrolling**

# Imagine, you are developing a rule in terms of logical and comparison operations to determine whether you should enroll a 
# student in your course or not. The rule itself looks like this:

average_grade = int(input("Enter the average grade:"))
recommended_by_tutor = bool(input("Enter if recommended by tutor:"))
finished_introductory_course = bool(input("Enter if finished introductory course:"))
introductory_course_grade = int(input("Enter introductory course grade:"))

enroll_student = ((average_grade >= 40 and recommended_by_tutor) 
or (finished_introductory_course and introductory_course_grade > 85))
print(enroll_student)

# Parameters meaning:

# average_grade is an integer variable that shows the student's average grade.
# recommended_by_tutor is a bool variable that shows whether the student has a recommendation from the tutor.
# finished_introductory_course is a bool variable that shows whether the student finished the introductory course.
# introductory_course_grade is an integer variable that shows the student's introductory course grade.
