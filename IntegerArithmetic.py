# **Introduction to integer arithmetic**

#Arithmetic operations aren't just for math class — they're super important in programming too! Whether you're calculating
# change at the store or figuring out the area of a room, arithmetic operations help you process numbers in programs.

#Multiplication = *Finding the area of a rectangle from its length and width.
#Addition = *Calculating the total expenses after shopping.
#Subtraction = *Determining the remaining amount of milk after making a cup of coffee.
#Division = *Calculating the average monthly revenue from the total yearly revenue.

# **Basic arithmetic operations**

#In the magical world of Python, you've got the power of basic arithmetic operations right at your fingertips! Think of it like
# having a fully functional calculator built into your code. Need to add, subtract, multiply, or divide? Python's got your back!

# **Addition and subtraction**

#Alright, let's dive into addition and subtraction in Python! With the "+" symbol, you can add values effortlessly, while the "-"
# symbol gracefully subtracts them. Some exaples:
a = 5
b = 3
print(a + b)
print(a - b, '\n')

# **Checking balance**

#Let's apply our new Python skill into practice. In the following code, we already defined two variables for you: total_money,
# and cost. Please calculate the current balance by subtracting the cost from the total money and print the result.
total_money = 100
cost = 50
print("The current balance is:",total_money - cost, 'Rands\n')

# **Monthly savings**

#Write a Python program that calculates your total savings over three months if you save 200 in the first month 150 in the 
# second month, and 250 in the third month. Print the total savings.
month_one = 150
month_two = 200
month_three = 250
print(month_one + month_two + month_three, 'Rands\n')

# **Multiplication and division**

#Let's move forward to the next set of operations. We know you may have guessed the symbols for multiplication and division.
# to be thorough, here are examples to illustrate multiplication and division:
length = 12
width = 6
print(length * width)
print(length / width, '\n')

# **Splitting the bill

#Let's engage in more practice to strengthen our understanding.
#You and your friends had an amazing dinner at a fancy restaurant, enjoying delicious food and great conversation. When the 
# bill arrives, it totals 128 Since you are a group of 5 friends, you decide to split the bill evenly. Write a Python program to 
# calculate how much each friend needs to contribute to pay the bill.
print(128 / 5, 'Rands\n')
cash = 128
friends = 5
print(cash / friends, 'Rands\n')

# **Playing with data types**

#In Python, when you multiply, add, or subtract two integer numbers, 
# the result remains an integer. However, when you divide an integer by another integer, 
# the result is always a floating-point number. Consider this example:
print(10 / 3)
print(10 - 3)
print(10 * 3)
print(10 + 3)
print()
print(type (10 / 3))
print(type(10 - 3))
print(type(10 * 3))
print(type(10 + 3))

# **Integer division**

#Let's tackle this question now: how can we obtain an integer by dividing two numbers?
#The answer is the integer division (also known as floor division and denoted by (//) in Python. 
# While regular division (/) yields
#a floating-point number, integer division produces an integer value by discarding the decimal part. 
# Here's a quick example to illustrate the contrast:
print('\n', 36 / 5)
print(36 // 5)
print()

# **Equal distribution**

#Write a line of code to print the number of books each student should receive if we distribute them equally among the students.
number_of_students = 17
number_of_books = 70
print("Each student should receive: ", number_of_books // number_of_students, "books" '\n')

# **Number of full weeks**

#Imagine you are planning a project and need to convert a total number of days into the number of full weeks. This can help in
# understanding how many full weeks you have left for project planning.
#Let's assume you have 45 days left to complete your project. Write a line of code to print the number of full weeks remaining.
days_left = 45
number_of_weeks = days_left // 7
print(number_of_weeks, "Weeks_left", '\n')

# **Trip planning**

#You are planning a road trip and need to calculate the budget. You have a total of R1500 for the trip. You expect to spend R600
# on fuel, R300 on food, and R200 on accommodation. 
#You also want to buy souvenirs and each souvenir costs R25 Please write a program to calculate how many souvenirs you can buy after the trip.
total_cash = 1500
fuel_expense = 600
food_expense = 300
accommodation_expense = 200
cash_balance = total_cash - fuel_expense - food_expense - accommodation_expense
print("Cash balance: ", cash_balance, '\n')
souvenir_cost_price = 25
print("You will be able to buy ", cash_balance // souvenir_cost_price, "souvenirs",'\n')