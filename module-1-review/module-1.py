### MODULE 1 ###

# Variable Assignment
x = 5  # Assigning the value 5 to variable 'x'
name = "Alice"  # Assigning the string "Alice" to variable 'name'

print(x)       # Output: 5
print(name)    # Output: Alice


# Challenge: Create a variable with a value and print it.




# Arithmetic Operations
a = 10
b = 3

sum_value = a + b         # Addition
difference = a - b        # Subtraction
product = a * b           # Multiplication
quotient = a / b          # Division
remainder = a % b         # Modulus (remainder of the division)

print("Sum:", sum_value)               # Output: 13
print("Difference:", difference)       # Output: 7
print("Product:", product)             # Output: 30
print("Quotient:", quotient)           # Output: 3.333...
print("Remainder:", remainder)         # Output: 1

# Challenge: Perform arithmetic operations on two numbers and print the results.



# String Concatenation
greeting = "Hello"
name = "Alice"

full_greeting = greeting + ", " + name + "!"
print(full_greeting)   # Output: Hello, Alice!


# Challenge: Concatenate three strings and print the result.



# Combining variables and expressions
num1 = 8
num2 = 2
result = num1 + num2

message = "The sum of " + str(num1) + " and " + str(num2) + " is " + str(result)
print(message)  # Output: The sum of 8 and 2 is 10

# Challenge: Add two numbers and print the result using string concatenation.



'''
Summary of Key Concepts:
Variables store information and are created using =.

Arithmetic expressions include operations like addition (+), subtraction (-), multiplication (*), and division (/).

String concatenation combines strings using the + operator.

Use str() to convert numbers into strings for concatenation.

Feel free to practice these mini challenges to reinforce your understanding!
'''


# =============================================================================
#  PYTHON FUNDAMENTALS
# =============================================================================

print("\n" + "="*50)
print("EXPANDED MODULE 1 CONTENT")
print("="*50)

# Data Types in Python
print("\n--- DATA TYPES ---")
# Python has several built-in data types

# Integer (whole numbers)
age = 25
students_count = 150
print("Age (integer):", age)
print("Students count (integer):", students_count)

# Float (decimal numbers)
temperature = 98.6
price = 19.99
print("Temperature (float):", temperature)
print("Price (float):", price)

# String (text)
first_name = "John"
last_name = "Smith"
print("First name (string):", first_name)
print("Last name (string):", last_name)

# Boolean (True/False)
is_student = True
is_graduated = False
print("Is student (boolean):", is_student)
print("Is graduated (boolean):", is_graduated)

# Challenge: Create one variable of each data type and print them with labels.




# Variable Naming Conventions
print("\n--- VARIABLE NAMING BEST PRACTICES ---")
# Good variable names are descriptive and follow Python conventions

# Good examples:
student_name = "Alice Johnson"
total_score = 95
is_passing_grade = True
course_code = "CS5001"

print("Student name:", student_name)
print("Total score:", total_score)
print("Passing grade:", is_passing_grade)
print("Course code:", course_code)

# Avoid these naming patterns:
# x = "Alice Johnson"  # Not descriptive
# 2student = "Bob"     # Can't start with number
# student-name = "Bob" # No hyphens allowed
# class = "CS5001"     # 'class' is a reserved word

# Challenge: Create 3 variables with descriptive names for a student record.




# More Arithmetic Operations
print("\n--- ADDITIONAL ARITHMETIC OPERATIONS ---")

base = 2
exponent = 3
result_power = base ** exponent  # Exponentiation (2^3)
print(f"{base} to the power of {exponent} = {result_power}")

# Floor division (integer division)
dividend = 17
divisor = 5
floor_result = dividend // divisor  # Floor division (17 // 5 = 3)
regular_result = dividend / divisor  # Regular division (17 / 5 = 3.4)
print(f"{dividend} // {divisor} = {floor_result}")
print(f"{dividend} / {divisor} = {regular_result}")

# Order of operations (PEMDAS)
calculation = 2 + 3 * 4 ** 2 - 1
print("2 + 3 * 4 ** 2 - 1 =", calculation)  # = 2 + 3 * 16 - 1 = 2 + 48 - 1 = 49

# Using parentheses to change order
calculation_with_parens = (2 + 3) * (4 ** 2 - 1)
print("(2 + 3) * (4 ** 2 - 1) =", calculation_with_parens)  # = 5 * 15 = 75

# Challenge: Calculate the area of a triangle: (base * height) / 2




# Modern String Formatting with f-strings
print("\n--- F-STRING FORMATTING (MODERN APPROACH) ---")
# f-strings are the modern, preferred way to format strings in Python

name = "Emma"
age = 22
gpa = 3.85

# Old way (concatenation)
old_message = "Hello, my name is " + name + " and I am " + str(age) + " years old."
print("Old way:", old_message)

# New way (f-strings) - much cleaner!
new_message = f"Hello, my name is {name} and I am {age} years old."
print("New way:", new_message)

# f-strings can include expressions
detailed_message = f"{name} is {age} years old and has a GPA of {gpa:.2f}"
print("Detailed:", detailed_message)

# f-strings with calculations
width = 10
height = 15
area_message = f"A rectangle with width {width} and height {height} has area {width * height}"
print("Calculation:", area_message)

# Challenge: Use f-strings to create a message about a book with title, author, and page count.




# Getting Input from Users
print("\n--- USER INPUT ---")
# The input() function lets users type information

print("Let's get some information about you!")

# Note: In practice files, we'll comment out input() to avoid interrupting the flow
# Uncomment these lines when you want to try interactive input:

# user_name = input("What's your name? ")
# user_age = input("What's your age? ")
# print(f"Nice to meet you, {user_name}! You are {user_age} years old.")

# For demonstration, we'll use preset values:
user_name = "Alex"  # Simulating user input
user_age = "20"     # Note: input() always returns a string!

print(f"Demo: Nice to meet you, {user_name}! You are {user_age} years old.")

# Converting user input to numbers
age_as_number = int(user_age)  # Convert string to integer
birth_year = 2025 - age_as_number
print(f"You were probably born in {birth_year}")

# Challenge: Create a program that calculates someone's birth year from their age.




# Real-World Example: Restaurant Bill Calculator
print("\n--- REAL-WORLD EXAMPLE: RESTAURANT BILL ---")

# Bill details
appetizer = 8.99
main_course = 24.50
dessert = 6.75
drink = 3.25

# Calculate subtotal
subtotal = appetizer + main_course + dessert + drink
print(f"Subtotal: ${subtotal:.2f}")

# Calculate tax (8.5%)
tax_rate = 0.085
tax_amount = subtotal * tax_rate
print(f"Tax (8.5%): ${tax_amount:.2f}")

# Calculate tip (18%)
tip_rate = 0.18
tip_amount = subtotal * tip_rate
print(f"Tip (18%): ${tip_amount:.2f}")

# Calculate total
total = subtotal + tax_amount + tip_amount
print(f"Total: ${total:.2f}")

# Using f-strings for a nice receipt
print("\n--- RECEIPT ---")
print(f"Appetizer:    ${appetizer:>6.2f}")
print(f"Main Course:  ${main_course:>6.2f}")
print(f"Dessert:      ${dessert:>6.2f}")
print(f"Drink:        ${drink:>6.2f}")
print("-" * 20)
print(f"Subtotal:     ${subtotal:>6.2f}")
print(f"Tax:          ${tax_amount:>6.2f}")
print(f"Tip:          ${tip_amount:>6.2f}")
print("-" * 20)
print(f"TOTAL:        ${total:>6.2f}")

# Challenge: Create a shopping receipt for 4 items with tax and discount.




# Working with Multiple Variables
print("\n--- WORKING WITH MULTIPLE VARIABLES ---")

# Student grade calculation
homework1 = 85
homework2 = 92
homework3 = 78
midterm = 88
final_exam = 91

# Calculate average
total_points = homework1 + homework2 + homework3 + midterm + final_exam
num_assignments = 5
average = total_points / num_assignments

print(f"Homework 1: {homework1}")
print(f"Homework 2: {homework2}")
print(f"Homework 3: {homework3}")
print(f"Midterm: {midterm}")
print(f"Final Exam: {final_exam}")
print(f"Average: {average:.1f}")

# Determine letter grade (simple version)
if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print(f"Letter Grade: {letter_grade}")

# Challenge: Calculate GPA for 4 courses with different credit hours.




# Constants and Mathematical Calculations
print("\n--- CONSTANTS AND MATH ---")

# Constants (variables that shouldn't change - use UPPERCASE)
PI = 3.14159
GRAVITY = 9.81
SPEED_OF_LIGHT = 299792458  # meters per second

# Circle calculations
radius = 7
circumference = 2 * PI * radius
area = PI * radius ** 2

print(f"Circle with radius {radius}:")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.2f}")

# Physics calculation - distance fallen
time = 5  # seconds
distance = 0.5 * GRAVITY * time ** 2
print(f"Object falls {distance:.1f} meters in {time} seconds")

# Challenge: Calculate the volume of a cylinder (π * r² * h).




# Comments and Documentation
print("\n--- COMMENTS AND DOCUMENTATION ---")

# Single-line comments start with #
# They explain what the code does

"""
Multi-line comments (docstrings) use triple quotes.
They're great for longer explanations or documentation.
This type of comment can span multiple lines.
"""

# Good commenting practices:
price = 29.99        # Price per item in dollars
quantity = 3         # Number of items purchased
total = price * quantity  # Calculate total cost

# Avoid obvious comments:
# x = 5  # This sets x to 5 (too obvious!)

# Use descriptive variable names to reduce need for comments:
items_in_cart = 5    # Better than: x = 5  # number of items

print(f"Total cost: ${total:.2f}")

# Challenge: Write a well-commented program that converts temperature.




# Type Hints for Code Readability
print("\n--- TYPE HINTS FOR CODE READABILITY ---")

# Type hints help make your code more readable and catch errors early
# They tell other programmers (and yourself!) what type of data to expect

# Basic type hints
student_name: str = "Alice Johnson"
student_age: int = 20
student_gpa: float = 3.85
is_enrolled: bool = True

print(f"Student: {student_name}")
print(f"Age: {student_age}")
print(f"GPA: {student_gpa}")
print(f"Enrolled: {is_enrolled}")

# Type hints with calculations
width: int = 10
height: int = 15
area: int = width * height  # Type hint shows this will be an integer

print(f"Rectangle area: {area}")

# Mixed types in calculations
price_per_item: float = 12.99
quantity: int = 3
total_cost: float = price_per_item * quantity  # Result will be float

print(f"Total cost: ${total_cost:.2f}")

# Why type hints are helpful:
# 1. Makes code self-documenting
# 2. Helps catch errors before running
# 3. Makes code easier to understand for other programmers
# 4. IDEs can provide better suggestions

# Without type hints (harder to understand):
x = 25
y = "John"
z = 3.14

# With type hints (much clearer!):
temperature: int = 25
name: str = "John"
pi_value: float = 3.14

print(f"Temperature: {temperature}°F")
print(f"Name: {name}")
print(f"Pi: {pi_value}")

# Type hints for user input conversions
print("\nType hints with input conversion:")
# Simulating user input with type hints
user_input_age: str = "22"  # input() always returns string
actual_age: int = int(user_input_age)  # Convert to integer
birth_year: int = 2025 - actual_age

print(f"If you're {actual_age}, you were born around {birth_year}")

# Complex example: Student report with type hints
print("\nStudent Report with Type Hints:")
first_name: str = "Emma"
last_name: str = "Wilson"
student_id: int = 12345
math_score: float = 87.5
science_score: float = 92.0
english_score: float = 89.5

# Calculate average with type hint
average_score: float = (math_score + science_score + english_score) / 3

# Create formatted report
full_name: str = f"{first_name} {last_name}"
report: str = f"Student: {full_name} (ID: {student_id})\nAverage Score: {average_score:.1f}"

print(report)

# Challenge: Create variables with type hints for a book record (title, author, pages, price, in_stock).




print("\n" + "="*50)
print("END OF EXPANDED MODULE 1")
print("Great job learning Python fundamentals!")
print("="*50)





