"""
MODULE 1 PRACTICE QUESTIONS
===========================

This file contains practice questions for students to reinforce the concepts
learned in Module 1: Variables, Arithmetic Operations, and String Concatenation.

Instructions:
- Read each question carefully
- Write your code below each question
- Test your solutions by running the file
- Check your answers against the expected output when provided
"""

print("=" * 50)
print("MODULE 1 PRACTICE QUESTIONS")
print("=" * 50)

# =============================================================================
# SECTION 1: VARIABLE ASSIGNMENT
# =============================================================================

print("\n--- SECTION 1: Variable Assignment ---\n")

# Question 1.1
print("Question 1.1:")
print("Create a variable called 'age' and assign it the value 25.")
print("Then create a variable called 'city' and assign it the string 'Boston'.")
print("Print both variables.")
print("Expected output: 25, Boston")
print()

# Write your code here:
age = 25            #assigning the variables in this line and the next
city = 'Boston'     
print(str(age) + ', ' + city)    #printing the output


print("=" * 30)

# Question 1.2
print("Question 1.2:")
print("Create three variables: 'first_name', 'last_name', and 'student_id'.")
print("Assign them appropriate values and print each one on a separate line.")
print()

# Write your code here:
first_name = 'Raissa'     #assigning the variables in this line and the next two
last_name = 'Bakari'
student_id = '002508199'

print(first_name + '\n' + last_name + '\n' + student_id)    #printing the output



print("=" * 30)

# Question 1.3
print("Question 1.3:")
print("Create a variable 'temperature' with the value 72.")
print("Then reassign it to 68 and print the new value.")
print("Expected output: 68")
print()

# Write your code here:
temperature = 72        #initially assigning the variable as 72
temperature = 68        #reassigning the variable's value to 68

print(temperature)      #printing the output



# =============================================================================
# SECTION 2: ARITHMETIC OPERATIONS
# =============================================================================

print("\n--- SECTION 2: Arithmetic Operations ---\n")

# Question 2.1
print("Question 2.1:")
print("Given two numbers 15 and 4, calculate and print:")
print("- Their sum")
print("- Their difference (15 - 4)")
print("- Their product")
print("- Their quotient (15 / 4)")
print("- The remainder when 15 is divided by 4")
print("Expected output: 19, 11, 60, 3.75, 3")
print()

# Write your code here:
x = 15              #assigning the variables on this line and the next
y = 4

add = x + y         #calculating sum
subtract = x - y    #calculating difference
product = x * y     #calculating product
quotient = x / y    #calculating quotient
remainder = x % y   #calculating remainder

print(str(add) + ', ' + str(subtract) + ', ' + str(product) + ', ' + str(quotient) + ', ' + str(remainder))   #printing the output




print("=" * 30)

# Question 2.2
print("Question 2.2:")
print("Calculate the area of a rectangle with length 12 and width 8.")
print("Store the result in a variable called 'area' and print it.")
print("Expected output: 96")
print()

# Write your code here:
length = 12              #assigning variable on this line and the next
width = 8
area = length * width    #calculating area

print(area)              #printing the output



print("=" * 30)

# Question 2.3
print("Question 2.3:")
print("You have $50. You buy 3 items that cost $12.99 each.")
print("Calculate how much money you have left.")
print("Expected output: 11.03")
print()

# Write your code here:
money = 50.00        #assigning variables on this line and the next 
item = 12.99

money = money - (item * 3) #calculating final total of money

print(round(money, 2))            #printing the output



print("=" * 30)

# Question 2.4
print("Question 2.4:")
print("Calculate the average of these five test scores: 85, 92, 78, 96, 89")
print("Store the result in a variable called 'average' and print it.")
print("Expected output: 88.0")
print()

# Write your code here:
average = (85 + 92 + 78 + 96 + 89) / 5   #assigning variable and calculating average of scores

print(average)          #printing the output



# =============================================================================
# SECTION 3: STRING CONCATENATION
# =============================================================================

print("\n--- SECTION 3: String Concatenation ---\n")

# Question 3.1
print("Question 3.1:")
print("Create variables for your first name, middle initial, and last name.")
print("Concatenate them to create your full name and print it.")
print("Example output: John Q. Smith")
print()

# Write your code here:
first_name = 'Raissa '           #assigning variables on this line and the next two
middle_initial = 'A.P.'
last_name = ' Bakari'

print(first_name + middle_initial + last_name) #printing the output



print("=" * 30)

# Question 3.2
print("Question 3.2:")
print("Create a greeting message that includes the user's name and age.")
print("Use variables: name = 'Sarah' and age = 20")
print("Expected output: Hello Sarah, you are 20 years old!")
print()

# Write your code here:
name = 'Sarah'      #assigning variables on this line and the next
age = 20

print('Hello ' + name + ', you are ' + str(age) + ' years old!')    #printing the output



print("=" * 30)

# Question 3.3
print("Question 3.3:")
print("Create variables for a book title and author.")
print("Print a message in the format: 'The book [title] was written by [author].'")
print("Example: 'The book To Kill a Mockingbird was written by Harper Lee.'")
print()

# Write your code here:
book_title = 'The Odyssey'  #assigning variables on this line and the next
book_author = 'Homer'

print('The book ' + book_title + ' was written by ' + book_author + '.')    #printing the output



# =============================================================================
# SECTION 4: COMBINING CONCEPTS
# =============================================================================

print("\n--- SECTION 4: Combining All Concepts ---\n")

# Question 4.1
print("Question 4.1:")
print("Create a simple calculator program:")
print("- Create two number variables: num1 = 24, num2 = 6")
print("- Calculate all four basic operations")
print("- Print each result with a descriptive message")
print("Example: '24 + 6 = 30'")
print()

# Write your code here:
num1 = 24       #assigning variables on this line and the next
num2 = 6

add = num1 + num2       #calculating addition
subtract = num1 - num2  #calculating subtraction
multiply = num1 * num2  #calculating multiplication
divide = num1 / num2    #calculating division

print(num1, '+', num2, '=', add)    #printing the output on this line and the next 3
print(num1, '-', num2, '=', subtract)
print(num1, '*', num2, '=', multiply)
print(num1, '/', num2, '=', divide)




print("=" * 30)

# Question 4.2
print("Question 4.2:")
print("Create a program that calculates the tip for a restaurant bill:")
print("- Bill amount: $45.50")
print("- Tip percentage: 18%")
print("- Calculate the tip amount and total bill")
print("- Print both values with descriptive messages")
print("Expected: Tip: $8.19, Total: $53.69")
print()

# Write your code here:
bill = 45.50        #assigning variables on this line and the next
tip = 0.18

tip_total = bill * tip          #calculating tip
final_bill = tip_total + bill   #calculating final bill


print('Tip: $' + str(tip_total) + ', Total: $' + str(final_bill))    #printing the output




print("=" * 30)

# Question 4.3
print("Question 4.3:")
print("Create a student report card:")
print("- Student name: 'Alex Johnson'")
print("- Three test scores: 87, 92, 85")
print("- Calculate the average")
print("- Print a report showing the name, all scores, and average")
print("Format: 'Student: Alex Johnson | Scores: 87, 92, 85 | Average: 88.0'")
print()

# Write your code here:
name = 'Alex Johnson'   #assigning variables on this line and the next two
test1 = 87
test2 = 92
test3 = 85

average = (test1 + test2 + test3) / 3   #calculating average of tests

print('Student: ' + name +' | Scores: ' + str(test1) + ', ' + str(test2) + ', ' + str(test3) + ' | Average: ' + str(average))  #printing the output




print("=" * 30)

# Question 4.4
print("Question 4.4:")
print("Create a shopping receipt:")
print("- Item 1: 'Apples' - $3.99")
print("- Item 2: 'Bread' - $2.50")
print("- Item 3: 'Milk' - $4.25")
print("- Calculate subtotal, tax (8.5%), and total")
print("- Print a formatted receipt")
print()

# Write your code here:
apples = 3.99       #assigning variables on this line and the next three
bread = 2.50
milk = 4.25
tax = 0.085

total = apples + bread + milk   #calculating subtotal
tax = total * tax               #calculating tax
total = total + tax             #calculating final total

print('Apples: $' + str(apples))     #printing the output on this line and the next three
print('Bread: $' + str(bread))
print('Milk: $' + str(milk))
print('Your total with tax is $' + str(round(total, 2)))




# =============================================================================
# SECTION 5: CHALLENGE QUESTIONS - NOT GRADED (OPTIONAL)
# =============================================================================

print("\n--- SECTION 5: Challenge Questions ---\n")

# Challenge 5.1
print("Challenge 5.1:")
print("Temperature Converter:")
print("Convert 75 degrees Fahrenheit to Celsius using the formula:")
print("Celsius = (Fahrenheit - 32) * 5/9")
print("Print the result with a descriptive message.")
print("Expected: 75°F is equal to 23.89°C")
print()

# Write your code here:
farenheit = 75             #assigning variable
celcius = (farenheit - 32) * (5/9)  #calculating conversion from farenheit to celcius

print(str(farenheit) + '°F is equal to ' + str(round(celcius,2)), '°C')   #printing the output




print("=" * 30)

# Challenge 5.2
print("Challenge 5.2:")
print("Time Calculator:")
print("You have 3847 seconds. Convert this to hours, minutes, and seconds.")
print("Print the result in the format: 'X hours, Y minutes, Z seconds'")
print("Hint: Use integer division (//) and modulus (%) operators")
print("Expected: 1 hours, 4 minutes, 7 seconds")
print()

# Write your code here:
time = 3847                     #assigning initial variable value
hours = time // 3600            #calculating hours
time = time - (hours * 3600)    #updating variable value
minutes = time // 60            #calculating minutes
time = time - (minutes * 60)    #updating variable value
seconds = time % 60             #calculating seconds

print(hours, 'hours,', minutes, 'minutes,', seconds, 'seconds')     #printing the output




print("=" * 30)

# Challenge 5.3
print("Challenge 5.3:")
print("Create a mad lib story:")
print("Create variables for: adjective, noun, verb, place, number")
print("Use them to create a funny story and print it.")
print("Be creative with your story structure!")
print()

# Write your code here:
adjective = 'crazy'     #assigning variables on this line and the next 4
noun = 'microwave'
verb = 'run'
place = 'Northeastern University'
number = 17

print('One', adjective, 'day, I decided to take my', noun, 'and', verb, 'all the way to', place, '. I couldn’t believe it when I saw', number, 'people doing the same thing!') #printing the output




print("\n" + "=" * 50)
print("END OF PRACTICE QUESTIONS")
print("Great job practicing! Keep coding!")
print("=" * 50)
