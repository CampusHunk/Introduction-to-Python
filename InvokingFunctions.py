#**Invoking functions**

#Even though invoking functions in Python is not about casting a spell or the like, it does 
# sometimes work wonders. Let's start with the concept. A function is a structured fragment 
# of code we may want to use in more than one place and more than one time. What's more, 
# functions allow us to read both our code and that of someone else way better. Haven't they 
# become your favorite yet?

#Here is a simple function call:
multiply(2, 3)

#Here multiply is the name of the function, and numbers in parentheses (1, 7) are its 
# arguments. What is an argument? Well, it's just a value, that will be used inside the function 
# body. Let's go deeper into it!

# **Invoking print()**

#To call, or invoke, a function in your program, simply write its name and add parentheses 
# after it. That's all it takes! Fun fact: if you've ever typed an expression like this 
# print("Hello, world!"), you already know a little about functions. In this tiny example, 
# however, we see the message "Hello, world!" in parentheses after the name of the print 
# function. What does it mean? This string is just an argument. And more often than not, 
# functions do have arguments. As for the print function, we may as well use it with no 
# argument at all or even with multiple arguments:


print("Hello, world!")
print()
print("Bye,","then")

#So, the first call prints one string, and the second call of print without arguments prints, 
# an empty line, and the last call outputs our two messages as one expression. Are you 
# surprised by these results? Then you may learn how the print function works in more 
# detail from its https://docs.python.org/3/library/functions.html#print. 
# The Python documentation contains all sorts of information 
# about the function of your interest, for example, which arguments it expects.

# **Built-in functions**

#Functions can make life easier, provided one is aware of their existence. Many algorithms are 
# already written, so there is no need for reinvention, except perhaps for educational purposes. 
# The Python interpreter has several functions and types built into it, so they are always available. 
# Currently, the number of built-in functions amounts to 71 (in the Python 3.13 version). Some of them 
# are used to convert the object type, for example, str() returns a string, int() returns an integer, and 
# float() returns a floating-point number. Others deal with numbers: you can round() them and sum() them, 
# find the minimum min() or the maximum max(). Still, others give us information about the object:
# its type() or length len().

#In the following example, len() counts the number of characters in the string (the same 
# goes for any sequence, i.e. list, tuple, range, byte sequences, byte arrays).

number = "111"

# finding the leghth of an object
print(len(number))

#Then we declare the variables integer and float_number, convert our string to 
# corresponding types, and write their sum into my_sum. By the way, the sum() function 
# deals with iterable objects, that's why we use double parentheses.

# coverting types
integer = int(number)
float_number = float(number)

# adding numbers
my_sum = sum((integer, float_number))

#The result is a floating-point number, which becomes clear after printing my_sum.

print(my_sum)
print(round(my_sum))

#Furthermore, you can see how to find the minimum and maximum values: in this example, 
# the smallest number equals 3 and the largest number 8.4 (the sum of 3 and 5.4) belongs to floats.

# finding the minimum and maximum.
integer = 3
float_number = 5.4
my_sum = sum((integer, float_number))

print(min(integer, float_number, my_sum))
print(type( max(integer, float_number, my_sum)))

# **New function to sum numbers**

#Create a new function to sum numbers.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def sum_numbers(a, b):
    return sum((a, b))
    print("Result:", sum_numbers(num1, num2))

