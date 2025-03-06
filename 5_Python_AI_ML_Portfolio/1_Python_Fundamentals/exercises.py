
# -------------------------------------------------------
# DATA TYPES & VARIABLES
# -------------------------------------------------------

# This section introduces fundamental data types in Python. A string is used
# for text, an integer for whole numbers, a float for decimal values, and
# a boolean for True/False logic. We also use an f-string to format and
# print these variables in a structured way.
print("\n📌 Data Types & Variables")

# String: A sequence of characters enclosed in quotes
name = "John Doe"

# Integer: Whole numbers without decimals
age = 25

# Float: Numbers with decimal points
height = 5.9

# Boolean: Represents True or False values
is_student = False

# Using an f-string to format and print variables
print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")



# -------------------------------------------------------
# LISTS, TUPLES, AND DICTIONARIES
# -------------------------------------------------------

# This section covers three fundamental data structures in Python. Lists
# are ordered and mutable, allowing modification. Tuples are similar but
# immutable, meaning their values cannot be changed after creation.
# Dictionaries store key-value pairs, making data retrieval efficient.

print("\n📌 Lists, Tuples, and Dictionaries")

# List: An ordered, mutable collection (can be changed)
fruits = ["Apple", "Banana", "Cherry"]

# Tuple: An ordered, immutable collection (cannot be changed)
numbers = (1, 2, 3, 4, 5)

# Dictionary: A collection of key-value pairs
student = {
    "name": "Alice",
    "age": 22,
    "major": "Computer Science"
}

# Print values from each data structure
print("Fruits List:", fruits)  # Lists allow modification
print("Numbers Tuple:", numbers)  # Tuples are immutable
print("Student Dictionary:", student)  # Dictionaries use key-value storage

# -------------------------------------------------------
# LOOPS & CONDITIONALS
# -------------------------------------------------------

# This section introduces loops and conditionals, two fundamental
# control structures in Python. Loops allow us to execute code 
# multiple times, while conditionals help us make decisions based
# on specific conditions. These structures are essential for AI/ML
# as they enable automation, data processing, and decision-making.

print("\n📌 Loops & Conditionals")

# FOR LOOP: Iterating through a list
fruits = ["Apple", "Banana", "Cherry"]

# This loop iterates through each item in the fruits list.
# If the item is "Banana", it prints a special message.
for fruit in fruits:
    if fruit == "Banana":
        print(f"{fruit} is my favorite!")  # Conditional statement
    else:
        print(f"I like {fruit}")


# IF-ELSE CONDITIONALS: Making decisions
age = 20

# This conditional checks if the person is eligible to vote.
# If age is 18 or more, it prints an eligible message.
# Otherwise, it prints a not eligible message.
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# WHILE LOOP: Repeating until a condition is met
count = 0

# This loop runs while count is less than 5. It increments
# count by 1 in each iteration to prevent an infinite loop.
while count < 5:
    print(f"Count is: {count}")
    count += 1

# -------------------------------------------------------
# FUNCTIONS & MODULES
# -------------------------------------------------------

# This section introduces functions and modules, essential components
# of writing clean and reusable code. Functions allow us to encapsulate
# logic into callable blocks, reducing repetition and improving
# readability. Modules help in organizing code by allowing us to import
# predefined or custom functionalities.

print("\n📌 Functions & Modules")


# FUNCTION DEFINITION: Creating a reusable block of code
# This function takes a name as input and returns a greeting message.
def greet(name):
    """Returns a greeting message with the given name."""
    return f"Hello, {name}!"

# Calling the function and displaying the result
print(greet("David"))


# IMPORTING MODULES: Using built-in functionalities
import math  # Importing the math module to use mathematical functions

# Using the sqrt function from the math module to calculate square root
number = 16
sqrt_value = math.sqrt(number)
print(f"The square root of {number} is {sqrt_value}")

# -------------------------------------------------------
# FILE HANDLING
# -------------------------------------------------------

# This section introduces file handling, which allows Python to
# read from and write to files. File handling is crucial for
# working with datasets, logging outputs, and saving model results
# in AI/ML applications. Python uses built-in functions to open,
# read, write, and close files efficiently.

print("\n📌 File Handling")


# WRITING TO A FILE: Creating and storing data
filename = "sample_text.txt"

# Opening a file in write mode ('w')
# This creates a new file or overwrites an existing file
with open(filename, "w") as file:
    file.write("Hello, this is a sample file!\nPython is fun!")


# READING FROM A FILE: Retrieving stored data
# Open the file in read mode ('r')
with open(filename, "r") as file:
    content = file.read()
    
# Displaying the file content
print("\nFile Content:")
print(content)