# **Coding style guide**

#When writing longer texts or essays, keeping your writing clear and structured is crucial. Coding is similar. 
# As you progress from simple one-liners to more complex projects, it's important to keep things tidy. 
# That's where PEP 8 comes in — your guide to writing clear, readable Python code. 📝
#Why does this matter? 🤔 As projects grow and more people get involved, your code needs to be easy to understand. 
# PEP 8 ensures everyone can read, follow, and improve your code without confusion.

# **Understanding indentation**

#Let’s dive into something super crucial in Python: indentation! 🤓 Imagine you're writing down instructions for a day's plan. 
# Each main activity starts at the left margin, but if an activity has specific steps, 
# those steps are indented to show they belong to the main activity. Here's a non-coding example:
#Breakfast
 #   - Make coffee
 #   - Cook eggs

#Lunch
#    - Buy groceries
#    - Prepare salad

#This is similar to how Python uses indentation to group lines of code that work together. It’s not just for looks; 
# it actually tells Python that a new block of code is starting, helping both Python and any programmer reading the code to understand it easily.

# **PEP 8 rule on indentation**

#Now that you understand why indentation is important, let’s talk about the specific guidelines PEP 8 provides for indentation. 
# According to PEP 8, we use a 4-space indent to separate different parts of our code.
#Here is an example:

temperature = 30
if temperature > 0:
    print("It's a hot day!")
else:
    print("It's a cold day!\n")

#We know you are confused with the above code with if, else etc. Don't worry - we will teach about them later.
#For now, only observe that we have used exactly four spaces to indent the second and fourth lines following the PEP 8 standard.
#Let's tell you a secret about Python programming:

#   Any line following another that ends with a colon (:) should be indented.

# **Keep it short and sweet**

#Let's move to the next rule. PEP 8 tells us to keep our lines of code short—no more than 79 characters. 
# It’s like not letting a sentence run on for too long in a book; it helps keep things readable. 
# When your code lines are concise, it's easier for others (and future you!) to read and understand 
# what each part of your program is doing without getting lost in a "wall of text."

# **Print long lines**

#At this stage, you might be wondering, "Hey, how can I print a long paragraph in Python if it has more than 79 characters?" 
# That's a totally fair question! Let's tackle this together.
#Check out this not-so-great Python code that ignores the PEP 8 rule about line length:
print()
print("Today was a sunny day, perfect for a picnic. We enjoyed sandwiches and fresh lemonade under the shade of an old oak tree.")
#It's not pretty, but it works! However, according to PEP 8, this code is not recommended.
#Here's a simple tweak to make it neat and compliant with PEP 8:

print("\nToday was a sunny day, perfect for a picnic.We enjoyed sandwiches" 
      " and fresh lemonade under the shade of an old oak tree.\n")

#Although we've split the line to adhere to the rule, Python cleverly prints it as a single seamless line, just like before. 
# This way, your code remains clean and easy to read, all while sticking to the guidelines.
print("The sun set over the horizon, casting a golden glow across the "
      "landscape. Birds chirped their evening songs, while a gentle "
      "breeze rustled through the trees. It was a peaceful end to a "
      "beautiful day.")

# **What’s in a Name?**

#Here comes the next PEP rule: when naming things in Python, like variables, use lowercase and separate words with underscores.
my_name = "John Doe"

# **Avoid extra spaces**

#Let's talk about space management: PEP 8 advises not to put spaces immediately inside parentheses, 
# or between a function name and the parentheses that follow it. 
# It keeps things looking clean and organized.

#Here is an example that doesn't follow the rule:
print(   )
print( 'I have an extra space after opening parenthesis!') #extra spaces after an opening parenthesis.
print('I have an extra space before closing parenthesis!' ) #extra spaces before a closing parenthesis.
print( 'I have two extra spaces inside parentheses!' ) #extra spaces within parentheses.
print  ('I have space after function name') #extra spaces after a function name.

#Here is a good example:
print('I follow the PEP-8 rule!')

# **Naming constants**

#In Python, there's a neat convention for naming constants: they should be written in all capital letters with underscores separating words. 
# This convention helps differentiate constants from variables, making your code clearer and easier to understand.
#What’s a constant, you ask? A constant is a type of variable whose value doesn't change throughout the program. 
# By convention, we use uppercase letters to name them, which signals to other programmers that these values should remain unchanged.
#Example: 
MAX_SIZE = 100
PI = 3.14159
DATABASE_URL = 'https://example.com/data'

#In these examples, MAX_SIZE, PI, and DATABASE_URL are all constants.
#Their names are in all caps with underscores separating words, which immediately tells you, "Hey, these values are constants and should not be modified!"

# **Space around operators**

#PEP 8 has a suggestion for operators also. Use a single space around binary operators 
# (e.g., +, -, *, /, =, ==) to improve readability.
#Proper spacing around operators makes your code easier to read and understand. It helps distinguish between different parts of the expression, reducing the likelihood of errors.
print()
PI = 3.14159
RADIUS = 3
area = PI * RADIUS**2
print("The area of a circle with radius", RADIUS, "is", area)
print()

# **Consistency is the key**

#You already know that in Python, you can wrap your strings in either single (') or double (") quotes. Both ways work perfectly fine. 
# But here’s a pro tip from Python's style guide, PEP 8: pick one style and stick with it across your whole project. 
# Why? Because consistency is key to clean, readable code.
#However, there is an exception:

# If your string has quotes inside it, opt for the opposite type for the string itself. 
# This neat trick lets you skip using backslashes (\), those pesky that can make your code look messy.

#This is good:
print("It's a good string")

#This? Not so much:
print('It\'s a bad string')

#See the difference? In the second example, the backslash before the single quote (\') is necessary to stop the single quote from ending the string too soon. 
# It works, but it's kind of an eyesore, right? PEP 8 tells us that dodging backslashes by smartly choosing our quotation marks can make our code much easier on the eyes.



