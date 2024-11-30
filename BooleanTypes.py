# **Boolean type and operations. True and false**

#In programming languages, the boolean, or logical, type is a common way to represent 
# something that has only two opposite states like on or off, yes or no, etc. It's a very useful 
# type which you will quickly see for yourself when you start working on your projects or even 
# write small programs. In this topic, we'll look at the boolean type in Python and learn how to use it.

# **Boolean type**

#The Boolean type, or simply bool, is a special data type that has only two possible values: 
# True and False. In Python, the names of boolean values start with a capital letter.
#If you are writing an application that keeps track of door openings, you'll find it natural to 
# use bool to store the current door state.

is_open = True
is_closed = False

# **Boolean operations**

#There are three built-in boolean operators in Python: and, or and not. The first two are 
# binary operators which means that they expect two operands. not is a unary operator, it is 
# always applied to a single operand. First, let's look at these operators applied to the boolean values.

# and is a binary operator, it takes two arguments and returns True if both arguments are true, otherwise, it returns False.
a = True and True # True
b = True and False # False
c = False and False # False
d = False and True # False

# or is a binary operator, it returns True if at least one argument is true, otherwise, it returns False.

e = True or True # True
f = True or False # True
g = False or False # False
h = False or True # True

# not is a unary operator, it reverses the boolean value of its argument.

to_be = True
not_to_be = not to_be # False

# **The precedence of boolean operations**

#Logical operators have a different priority and it affects the order of evaluation. Here are the 
# operators in order of their priorities:
# not > and > or
#So, not is considered first, then and, finally or. Having this in mind, consider the following expression:

print(False or not False)  # True

#First, the part not False gets evaluated, and after evaluation, we are left with False or True. 
# This results in True, if you recall the previous section.
#While dealing solely with the boolean values may seem obvious, the precedence of logical 
# operations will be quite important to remember when you start working with so-called truthy and falsy values.

# **The truthy and falsy values**

#Though Python has the boolean data type, we often want to use non-boolean values in a logical context. 
# And Python lets you test almost any object for truthfulness. When used with logical operators, values of non-boolean types, 
# such as integers or strings, are called truthy or falsy. It depends on whether they are interpreted as True or False.

# The following values are evaluated to False in Python:
# constants defined to be false: None and False,
# zero of any numeric type: 0, 0.0,
# empty sequences and containers: "", [], {}.

# Anything else generally evaluates to True. Here is a couple of examples:
print(0.0 or False) # False
print("True" and True) # True
print("" or False) # False

# Generally speaking, and and or could take any arguments that can be tested for a boolean value.
# Now we can demonstrate more clearly the difference in operator precedence:

# `and` has a higher priority than `or`
truthy_integer = False or 5 and 100 #100

#Again, let's break the above expression into parts. Since the operator and has a higher 
# priority than or, we should look at the 5 and 100 part. Both 100 and 5 happen to be 
# truthy values, so this operation will return 100. You have never seen this before, so it's 
# natural to wonder why we have a number instead of the True value here. 
#The explanation is as follows: 
# The operators or and and return one of their operands, not necessarily of the boolean type (see details below). 
# Nonetheless, not always returns a boolean value.

# and returns the first value if it evaluates to False, otherwise it returns the second value.
# or returns the first value if it evaluates to True, otherwise it returns the second value.

# Another tricky example is below:
tricky = not (False or '') #True

#A pair of parentheses is a way to specify the order in which the operations are performed. 
# Thus, we evaluate this part of the expression first: False or ''. This operand '' 
# evaluates to False and or returns this empty string. Since the result of the enclosed 
# expression is negated, we get True in the end: not '' is the same as True. Why didn't we get, say, 
# a non-empty string? The not operator creates a new value, which by default has the boolean type. 
# So, as stated earlier, the unary operator always returns a logical value.

# **Short-circuit evaluation**

#The last thing to mention is that logical operators in Python are short-circuited. That's why 
# they are also called lazy. That means that the second operand in such an expression is 
# evaluated only if the first one is not sufficient to evaluate the whole expression.

# x and y returns x if x is falsy; otherwise, it evaluates and returns y.
# x or y returns x if x is truthy; otherwise, it evaluates and returns y.

#For instance:
#lazy_or = True (1/0) # division is never evaluated, because the first argument is True

#lazy_and = False (1/0) # division is never evaluated, because the first argument is False

# Boolean values
# Assuming that variables have the following boolean values:
a = True
b = not a
print(not (a and b)) # True

# When Sunny Meets Rainy: A Logic Twist
is_raining = True
is_sunny = False
print(not is_raining and is_sunny) # False

# Truthy and falsy values
# When do you get truthy or falsy values? When using logical operators with non-boolean values;

5 and 0 and 12 # 0
True or False # True
not (False or True) # False
5 or '' # 5

# Evaluating a loan application
# Use your knowledge of boolean operations to determine whether a bank should give a loan to its client. Using this program, 
# you can evaluate the conditions for any applicant and make an informed decision about whether to proceed with the loan or not.
# The program takes into account three criteria: credit score, income criterion, and the existence of another loan.

# Example of an applicant's characteristics
credit_score = 750
annual_income = 60000
has_collateral = True
has_existing_loan = False

# This criterion should be True if the applicant's annual income is at least 50,000 or they have collateral.
annual_income = (annual_income >= 50000) or has_collateral
print(annual_income) # True

## Decision: check if all of the criteria are satisfied
is_appoved = ((credit_score >= 700) and (annual_income >= 50000) and not has_existing_loan) # True

# **Computing and displaying boolean operation result**

#Given two variables x and y set to 'True' and 'False' respectively. The code computes a third variable, z, 
# as a Boolean operation between x and y. It then concatenates the result of the Boolean 
# operation to the string 'The result of 'True and False' is ' and stores this in a variable called 'result'. 
# Your task is to make sure the print statement outputs the correct computation of the Boolean operation.

x = True
y = False
z = x and y
result = 'The result of ' + str(x) + ' and ' + str(y) + ' is ' + str(z)
print(result)

# **Decision making with rain and umbrella status**

#Suppose it's raining outside and you wonder if you should stay home or not. Your decision is based on whether you have an umbrella or not. 
# You decide to write a Python program that makes this decision for you. Remember, you should only stay home if it's raining and you do not have an umbrella.

is_raining = True
has_umbrella = False
should_stay_home = is_raining and not has_umbrella
message = 'Should I stay home? ' + str(should_stay_home)
print(message)

# **Check if a number is divisible by 2**

#Using logical operators write a Python program that takes an integer as input. If the integer is divisible by 2, print True; otherwise, print False. 
# For input, you will scan a single integer. The output should be either True or False based on the condition.

