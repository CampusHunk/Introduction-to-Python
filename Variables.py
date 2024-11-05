# **Introduction to variables**

#In programming, think of variables as labeled boxes where you can store values to use later. They're super handy for keeping
# track of data while your program runs and does its magic.
#When writing programs to solve real-life problems, it's essential to store necessary data in memory and access it when
#needed. In this lesson, you'll learn how variables can help us accomplish this.

# **Defining variables**
#Defining a variable is pretty simple! Just use the equal sign (=) to give a name to a value. For example, when you write:

message = "Good Morning"
#you're storing the string Good Morning! in a variable called message. It's like putting a label on a box so you know what's inside!

#Now can you store the string Johannesburg! in a variable city?
city = "Johannesburg"

# **Retrieving values**

#Your friend might take forever to pay you back, but Python is way more reliable. 
# You can grab the data from a variable whenever you need it. How? Just call the variable by its name!
print(message)
print(city)

# **Variable reassignment**

#It might be nighttime where you are, so "Good Morning!" might not be quite right. No worries, you can easily change the 
# message to "Good Evening!" by assigning a new value to the variable.

message = "Good Evening!"
print(message)
print(city)

# **Print the correct fruit**
print()
fruit_a = "apple"
fruit_b = "banana"
print(fruit_a)
print(fruit_b)

# **Reassigning a different type of data**
#Imagine you're a secret agent for the government, and you only use numeric codes to communicate with your colleagues. 
# Can you switch the message from "Good Evening!" to the numeric code 5009

#Of course, you can! In Python, you can assign different types of values to the same variable. 
# You might start with a string and later store a number in the same variable. This flexibility is what makes Python a dynamically typed language.

message = 5009
print(message)
#There you go! Your message is now the secret numeric code. Stay stealthy!

# **Naming rules**

#You can name a variable pretty much anything you want, but there are a few Python rules to keep in mind.
#Variable names are case-sensitive.
#They must start with a letter or an underscore.
#They can also include letters, digits, and underscores.

# **Digit rule**

#Heads up for an important rule!
#Imagine you have two cars a Mercedes and a Porsche, and you want to store their names in a variable. You can do it like this:
two_cars = "Mercedes, Porsche"

#But you can't do it like this: 2_cars = "Mercedes, Porsche"
#Python doesn't allow variable names to start with a number.
print(two_cars)

# **Code docto**
cost_1 = 100
cost_2 = 200
total_cost = cost_1 + cost_2
print()
print(total_cost)

# **Avoiding confusion**

#Python won't let you confuse it by using variable names that match its built-in keywords. 
# So, you can't name your variable with any of these reserved words.
#You can check out the full list of reserved names here: https://docs.python.org/3/reference/lexical_analysis.html#keywords. 
# We are also providing the screenshot of the list for your convenience:
#Avoid naming your variable using any words from the list above. 

# **Descriptive names**

#Python won't stop you from choosing any variable name that follows the rules we've discussed. But here's a valuable tip:
#Avoid using cryptic variable names that don't convey their purpose.
#For example, if you want to store your friend Mike's age in a variable, you could write:
x = 33
#But that's not recommended. Instead, use something more descriptive but concise, and remember to use underscores to separate the words, like this:

persons_age = 33
print(persons_age)
persons_name = "Mike is:"
age_suffix = "years old"

print(persons_name, persons_age, age_suffix)

