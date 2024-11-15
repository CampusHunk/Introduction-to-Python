# **Input: a new built-in function**

#Interaction with the others is essential, and computers make no exception.
#Sometimes programs need to interact with users, either to receive some data or to deliver some sort of result. 
# And that's when the input() function steals the show.

# n Python, the input() function is used to take input from the user.

# **Inputting through code**

#The input data we want to get is simply the value the user enters. The input() function captures this value and returns it as a string
#For example, the program below reads the user's name and prints a greeting.

user_name = input("Enter your name: ")
print("Hello", user_name)

#In the first line, the program waits for the user to enter something and saves this input in a variable for later use.

# **Age counter**
age = input("Enter your age: ")
print("You are", age,"years old")
print()
# **Coding from scratch**

#Write a Python program that takes the user's nickname as input and outputs a sign-in message like this: Welcome back nick!. 
# Clearly, the inputted nickname should appear instead of nick.
nick_name = input("Enter your name: ")
print("Welcome back",nick_name +"!")
print(f"Welcome back {nick_name}!")

# **Stating your purpose**

#What if the user doesn't know what kind of input the computer expects? Imagine standing in front of someone who expects something from you, 
# but you have no idea what to give because they haven't told you what they want.
#That's why we highly recommend clearly stating the expected type of input from our users. To do this, the input() function can take an optional message:

name = input("Enter your name: ")
#The program starts, the user sees the message, enters their name (say, Hyperskill), and gets the result as follows... Ah, you can guess it yourself:

# **Another method**

#Another way to do this is to print the message separately:
print("Enter your name:")
name = input()
print("Hello", name)

#There's no big difference actually: in the previous example, the input will be printed in the same line as the message, 
# while in this case it will be entered on the next line. So, how many lines will be printed when executing the program above?
#3 lines.

age = input("Enter your age: ")
print("You are", age, "years old")

# **Learn from mistakes**

#Now let's try a different task: fixing errors.

#Bugs and errors are inevitable in programming. A good programmer is not one who never makes mistakes, 
# but one who knows how to resolve them when they happen.

# **Submitting an input**

#First of all, how long can the user's input be, and how does the program understand that the person entered everything they wanted?

# Here's a thing about the input()function: as soon as the program has started executing this function, 
# it stops and waits for the user to enter some value and press Enter.
#That also means that if there's no input from the user, the program will not execute any further.
#Based on what we just said, will the warning be displayed before the user inputs a value?

dummy_variable = input("Enter some dummy value: ")
print("Warning: Oh, cmon, you are taking too long") #prints after the user inputs a value

# **Taking several inputs**

#What if you need to read several inputs? In that case, you should call the function more than once:

day = input("Enter the day: ")
month = input("Enter the month: ")
year = input("Enter the year: ")

#How about three inputs? Can you fill in the blanks below to input the city name, country, and ZIP code?
city = input("Insert the city you currently live in: ")
country = input("Insert the country you currently live in: ")
print("You live in " + city + ", " + country)
zip_code = input("Insert your ZIP code: ")

# **Type of input**

#Any value you enter, the function sees as a string.
#It doesn’t matter if you enter digits or letters; the input will be converted to a string. 
# So, how do we convert them to other types? You must be patient and wait until the next topic.
#For now, since you know all about data types, what would be the type of the year variable in the piece of code below?
year = type(input("Enter an integer representing your birth year: "))

# **Final boss**

#Now, for your final challenge: write a program that asks for the user's name and profession and then prints an introductory sentence, just like in the example below.
#While printing messages for users during asking for input is generally recommended, please omit them in this challenge, 
# or your code might not pass the tests. Use only input() function without any message inside.

user_name = input("Enter your name: ")
user_profession = input("Enter your profession: ")
print("Hello", user_name, "you are a", user_profession)