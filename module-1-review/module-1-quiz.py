"""
MODULE 1 QUIZ
=============

This quiz tests understanding of Module 1 concepts: Variables, Arithmetic Operations, and String Concatenation.
Students should answer all questions and submit their responses.

Instructions:
- Answer multiple choice questions by writing the letter (A, B, C, or D)
- For coding questions, write the Python code
- For short answer questions, write 1-2 sentences

"""

print("=" * 40)
print("MODULE 1 QUIZ")
print("Name: Raissa Bakari")
print("Date: 9/17/2025")
print("=" * 40)

# =============================================================================
# MULTIPLE CHOICE QUESTIONS 
# =============================================================================

print("\nMULTIPLE CHOICE: Choose the best answer")
print("-" * 40)

print("\n1. Which of the following is the correct way to assign the value 10 to a variable named 'count'?")
print("   A) count == 10")
print("   B) count = 10")
print("   C) 10 = count")
print("   D) count := 10")
print("   Answer: B")

print("\n2. What is the output of: print(15 % 4)")
print("   A) 3.75")
print("   B) 3")
print("   C) 4")
print("   D) 15")
print("   Answer: B")

print("\n3. Which operator is used for string concatenation in Python?")
print("   A) *")
print("   B) &")
print("   C) +")
print("   D) |")
print("   Answer: C")

print("\n4. What does the following code output?")
print("   x = 5")
print("   y = 3")
print("   print(x + y * 2)")
print("   A) 16")
print("   B) 11")
print("   C) 13")
print("   D) 10")
print("   Answer: B")

print("\n5. To include a number in a string concatenation, you must:")
print("   A) Use the int() function")
print("   B) Use the str() function")
print("   C) Use the float() function")
print("   D) Nothing special is needed")
print("   Answer: B")

# =============================================================================
# SHORT ANSWER QUESTIONS 
# =============================================================================

print("\n\nSHORT ANSWER: Answer in 1-2 complete sentences")
print("-" * 50)

print("\n6. Explain the difference between the = operator and the == operator in Python.")
print("   Answer: The = operator is used to assign variables (like x = 1), and the == operator is used as an equal sign (like in an if statement you'd have if x == 1).")
print("   _____________________________________________________")

print("\n7. What is the modulus operator (%) used for? Give an example.")
print("   Answer: The % operator is used to calculate the remainder. For example, 21 % 4 would be equal to 1.")
print("   _____________________________________________________")

print("\n8. Why do we need to use str() when concatenating numbers with strings?")
print("   Answer: To convert the number into a string.")
print("   _____________________________________________________")

# =============================================================================
# CODING QUESTIONS 
# =============================================================================

print("\n\nCODING QUESTIONS: Write Python code for each problem")
print("-" * 50)

print("\n9. Write code to calculate the area of a circle with radius 7.")
print("   Use the formula: area = 3.14159 * radius * radius")
print("   Store the result in a variable called 'area' and print it.")
print()
print("   Code:")
print("   radius = 7")
print("   area = 3.14159 * radius * radius")
print("   print(area)")

print("\n10. Create variables for your favorite movie title and the year it was released.")
print("    Then create a message that says: 'My favorite movie is [title] from [year].'")
print("    Print the message.")
print()
print("    Code:")
print("    movie_title = 'Inception'")
print("    movie_year = 2010")
print("    print('My favorite movie is ' + movie_title + ' from ' + str(movie_year) + '.')")

print("\n11. Write code that calculates how many weeks and days are in 100 days.")
print("    Print the result in the format: '100 days = X weeks and Y days'")
print("    (Hint: Use integer division // and modulus %)")
print()
print("    Code:")
print("    days = 100")
print("    weeks = days // 7")
print("    days = days % 7")
print("    print('100 days =', weeks, 'weeks and', days, 'days.')")

# =============================================================================
# BONUS QUESTION 
# =============================================================================


print("-" * 45)

print("\n12. Create a program that calculates the total cost of buying textbooks.")
print("    - Math book: $89.99")
print("    - Science book: $76.50")
print("    - History book: $65.25")
print("    - Student discount: 15% off the total")
print("    Calculate and print the original total, discount amount, and final total.")
print()
print("    Code:")
print("    math = 89.99")
print("    science = 76.50")
print("    history = 65.25")
print("    discount = 0.15")
print("    total = math + science + history")
print("    discount = total * discount")
print("    final_total = total - discount")
print("    print('Original Total: $' + str(round(total, 2)))")
print("    print('Student Discount: $' + str(round(discount, 2)))")
print("    print('Final Total With Discount: $' + str(round(final_total, 2)))")

print("\n" + "=" * 40)
print("END OF QUIZ")


print("=" * 40)
