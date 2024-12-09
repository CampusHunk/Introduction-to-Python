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