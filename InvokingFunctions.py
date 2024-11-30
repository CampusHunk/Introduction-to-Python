#**Invoking functions**

#Even though invoking functions in Python is not about casting a spell or the like, it does 
# sometimes work wonders. Let's start with the concept. A function is a structured fragment 
# of code we may want to use in more than one place and more than one time. What's more, 
# functions allow us to read both our code and that of someone else way better. Haven't they 
# become your favorite yet?

#Here is a simple function call:
#multiply(2, 3)

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
print("Bye,","then")
print()

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
print()

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
num1 = 3
num2 = 5.4
my_sum = sum((num1, num2))
print(min(num1, num2, my_sum))
print(type( max(num1, num2, my_sum)))

# **New function to sum numbers**

#Create a new function to sum numbers.

#Example
def sum_numbers(a, b):
    return sum((a, b))

x = int(input("\nEnter first number: "))
y = int(input("Enter second number: "))

print("Result:", sum_numbers(x, y))
print()

#Example
w = int(input("Enter first number: "))
v = int(input("Enter second number: "))
my_count = sum((w, v))
print("Result of my count:", my_count)

#Example
c = int(input("\nEnter first number: "))
u = int(input("Enter second number: "))
print(sum((c, u)))
print()

# **Getting to know print() better**

#Suppose we want to read the documentation for the function print.
#We can do this by using the built-in function help().
#help(print)

#Young and beautiful
# Read the input three times. Each one contains the age of a person – Jack's, Alex's, and Lana's. 
# Find the youngest one among them and print this person's age.

jacks_age = int(input("Enter Jack's age: "))
alexs_age = int(input("Enter Alex's age: "))
lanas_age = int(input("Enter Lana's age: "))
print(min(jacks_age, alexs_age, lanas_age))
print()

# **min() and max() revisited**

#Fun fact about min() and max() is that these functions can help you to sort in alphabetical order! If a string is passed as an 
# argument, min() will return the first letter (alphabetically) and max() the last one (somewhat zetabetically). And if you 
# specify more than one value, min() will return the first string in alphabetical order and max(), in contrast, the last one. 
# For example, min("alpha", "omega") gives you "alpha", while max("alpha", "omega") returns "omega".

print(max("gloomy", "grew", "green"))
print(min("gloomy", "grey", "green"))
print(min("green", "grass"))
print(max("gloomy", "grey", "grass"))
print()

#Greeting a user with a function
# In Python, we commonly use functions to execute a block of reusable code. You have a simple function to greet a user whose 
# name is provided as an argument. Your goal is to invoke the function 'greet_user' with the argument 'name' storing a string 
# 'Bob' and assign its return value to a variable 'message'. Later, the 'message' should be printed. 
# Can you fill the blanks in the code to accomplish this task?

def greet_user(name):
    return "Hello, " + name
    
name = "Bob"
message = greet_user(name)
print(message)

#Find the longest word
# Create a program to find the longest of the words given and outputs the length of the longest word. 
# Fill in the gaps with the correct built-in functions.

word1 = "short"
word2 = "long"
word3 = "very long"
def find_longest(word1, word2, word3):
    return max(len(word1), len(word2), len(word3))

print(find_longest(word1, word2, word3))
print()

#String length
# Write a program that takes a string and prints its length.
# The input string whose length you need to find is already stored inside the string variable, use it in your solution.

my_string = input("Enter a name: ")
print(len(my_string))
print()

#Calculating power using base and exponent
# Write a program that takes a base and an exponent as input and prints the result of raising the base to the power of the exponent. 
# The program should read the base and exponent from the user as integers, calculate the result using the pow() function, and print the final value.

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
result = pow(base, exponent)
print(result)
print()

#Showing min and max
# You are building a program to show minimum and maximum numbers.

def show_min(num_1, num_2):
    return min(num_1, num_2), max(num_1, num_2)

def show_max(num_1, num_2):
    return max(num_1, num_2)

print("Min:", show_min(5,10), "Max:", show_max(5, 10))
print()

#Hello, world!
# The classical introductory exercise, slightly modified. Write a program that takes a string, writes it to the variable name
# and then prints "Hello, world! Hello, name". Note that there's a space before the name.
# Tip: Invoke the print() function with two arguments – the output string and the name variable. 
# Don't forget that print() separates each pair of arguments with whitespace.

name = input()
print("Hwllo, world! Hello, " + name)

#Longest word

# Find the longest word in a pair and print its length.

word_one = input()
word_two = input()
print(max(len(word_one), len(word_two)))