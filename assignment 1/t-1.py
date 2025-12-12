# 1. Create a variable my_age and assign your age to it. Print a message using this variable.
my_age = 21
print(f"My age is {my_age} years old.")

# 2. Ask the user to enter their favorite food and print a message incorporating this input.
favorite_food = input("What is your favorite food? ")
print(f"Wow! eat {favorite_food} daily!")

# Type Conversion:

# 1. Convert the string "42" to an integer and print the result.
number = int("42")
print(number)

# 2. Convert the floating-point number 3.14159 to a string and print the result.
pi_string = str(3.14159)
print(pi_string)

# Strings:
# 1. Concatenate the strings "Hello" and "World!" and print the result.
greeting = "Hello" + " " + "World!"
print(greeting)

# 2. Use string indexing to extract the third character from the string "Python".
third_char = "Python"[2]
print(third_char)

# 3. Take a sentence as input and print only the first five words.
sentence = input("Enter a sentence: ")
first_five = " ".join(sentence.split()[:5])
print(first_five)
