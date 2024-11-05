# **What are data types**

#In programming, each piece of data has its own unique type. This type is like a blueprint — it tells us how the data is stored in
#memory, and what kind of operations can be performed on it. Think of it as a playbook for each piece of data!
#As a real-world analogy, think of a dog as a type of biological species. Dogs can bark, right? That’s like an operation specific to that type.

# **Understanding strings**
#Introducing the first data type in Python: the string. Strings are the superheroes of text handling in programming. In Python,
#we shorten it to "str." These data dynamos have some pretty cool tricks up their sleeves.
#One of the coolest? You can wrap strings in either single quotes (' ') or double quotes (" "). Python's doesn't care about whichever one you choose!
#We have been using strings with single and double quotes in our previous lessons.

# **Single vs double quote**
#Let’s say you've got a string loaded with quotation marks, and you're itching to print it out. No worries! Here's the trick: if your string already has one type of quote, wrap it up with the other type. 
# For instance:

print("Yes, I'm learning Python\n")
#See how it works like magic? The part with I'm prints out just fine because we enclosed the whole string in double quotes.

#But beware! Doing it like this: print('Yes, I'm learning Python')

#is a recipe for confusion. Your program will stumble over those quotes, not knowing where the string begins or ends. 
# Always remember the golden rule: mix it up to keep it smooth!
#So, Python does care about which quotation mark you use if your text itself contains quotation marks.
print('Yes, I\'m learning Python')
print('Python is fun!, "I am interested in Data Science"')
print("I want to explore!, \"Sport Analysis\"")
print("I haven't finished reading the book yet.")

# **Introduction to numerical types**
#Guess what? Python's a real pro when it comes to crunching numbers and effortlessly tackling complex mathematical
#calculations. But wait a sec—how can we even do math without numbers? Exactly, we can't! Python's got that covered too.
#Numbers are the bread and butter of programming, and in Python, we've got two main types to play with: int for whole numbers and float for decimals.
# **Integer vs float**
#Integers(int), known as the "whole" numbers, are like the no-nonsense heroes in the numerical world. They keep it simple,
#covering everything from positive and negative integers to zero, without any fuss about decimals.
#Now, onto float! These numbers always come with their trusty decimal point. 
# They're the versatile ones, ready to represent any real numbers you throw at them.
#float decimal consist of a whole number part and a fractional part separated by a decimal point.
print()
print(10) #int whole number
print(3.14) # float decimal number

# *No quote please**
#Quotation marks are only for strings, not numbers.
#Negative numbers always come with a "-" sign before them. It's basic math stuff. Nothing new there!
print(-10)

# **The type() function**
#On your programming adventure, there might come a time when you need to figure out what type your data is. How do you do that with Python?
#Just enter the type() function. It's like your data's own personal ID card — it tells you exactly what type of object you're dealing with.
print()
print(type(10))

#will print <class 'int'> indicating that 10 is an integer type data.

print(type(3.14))

#will print <class 'float'> indicating that 3.14 is a float type data.

# **String inside type()**
print(type("Hello"))
#Just as we expected! 'hello' is indeed a string, or as Python calls it, a 'str'. Case closed!