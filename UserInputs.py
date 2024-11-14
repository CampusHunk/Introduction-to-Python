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



