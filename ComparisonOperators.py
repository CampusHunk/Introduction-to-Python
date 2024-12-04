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

result = 10 < (100 * 100) <= 10000