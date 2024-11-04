# **Print several lines**

#You have learned how to write simple, single-line Python programs that print text. However, real programs contain many lines.
#You can write such programs using the print() function that you are already familiar with.
print("I")
print('Know')
print('Python')

#Please pay attention to the cases and punctuation marks. They are important.
print("There is a cat on the keyboard, it is true,"
      "Typing messages is not fun, it is important.")

# **Skipping a line in code**
#Skipping a line in the code without a print statement has no effect on the output:
print("How")

print("are you?")

# **We must skip a line**
#By now, you're probably wondering, "How can we print a blank line in Python?" It's super easy! Just use the print() function
#without anything inside the parentheses.
print('How')
print()
print('are')
print()
print('you?')  

#Notice how we successfully left the second and fourth line blank!

print()
print("Line breaks are")
print("small")
print()
print("but important")
print()

# **Let's become economical**
#Want to be more economical and use just one print() function to print several lines? We've got two nifty tricks for you.
#First trick: Use \n to start a new line. How does it work? Check this out:
print("I\nknow\nPython")

#Here, \n inside the string tells Python to jump to a new line and continue printing. Easy and efficient, right?
print('\nThis is the first line.\nThis is the second line.\nUsing single quotes')
print()
print("  Ever wonder why flamingos stand on one leg? \nIt's to conserve body heat!\n  ")

# **Three quotes**

#Here's another cool trick Python has up its sleeve to print several lines at once: using three single (''') or three double (""") quotes.
print('''My name is:
I am learning Python
I am having fun!\n''')

print("""Shopping List:
1. Eggs
2. Milk
3. Bread
4. Cheese""")

# **Print an inspirational quote**

#You may select any ONE method from the list.
#Using multiple print functions
#Using \n
#Using three single or double quotes
#using the three single or double quotes method
##Choose any of the three methods mentioned above to print an inspirational quote.:##
print('''\nThe only limit to our realization of tomorrow
      is our doubts of today.
      Franklin Roosevelt\n''')

# **Print contact card**
#Create a Python program to print a contact card using a single print() function:
print("""Contact Information:
      Name:            John Doe
      Address:         123 Main St
      City:            Johannesburg
      Country:         RSA
      Phone:           (123) 456-7890
      Email:           6s9Rd@example.com""")

# **Comments**
#Comments don't affect the program but are crucial for readability. By explaining what each part of the code does, 
# comments act like helpful notes, guiding developers through the logic and making the code more readable.
#start a line with # and it's a comment.
#The line with # is ignored by the computer.
print()
print('''We have been using comments  
      throughout the course to explain 
      what each code snippet does''')


# print() function will leave an empty line
print()  # empty line

# \n is used to signal Python to start a new line
print("\n")  # empty line

# Three quotation marks can also print multiple lines
print('''This is the first line.
      This is the second line.
      This is the third line.''')